#!/usr/bin/env python3
"""Fail-closed safe-point evidence resolver and compare-and-swap writer.

This tool is deliberately offline: it verifies a supplied evidence manifest but
cannot authenticate GitHub, owner approval, workflow runs, or repository state.
Those facts must be independently obtained and bound to the exact candidate SHA.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
REQUIRED_CHECKS = ("unit-tests", "architecture-audit", "security-negative-tests")


class EvidenceError(ValueError):
    pass


def _sha(value: Any, field: str) -> str:
    if not isinstance(value, str) or not SHA_RE.fullmatch(value):
        raise EvidenceError(f"{field}: requires a full lowercase 40-character commit SHA")
    return value


def _required_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EvidenceError(f"{field}: missing/empty")
    return value.strip()


def validate_manifest(manifest: dict[str, Any], current_safe_sha: str) -> str:
    """Return candidate SHA only when every required evidence field is bound.

    No booleans alone count as proof: run IDs and their tested SHA are required.
    """
    current_safe_sha = _sha(current_safe_sha, "current_safe_sha")
    if not isinstance(manifest, dict):
        raise EvidenceError("manifest must be a JSON object")

    safe = _sha(manifest.get("safe_base_sha"), "safe_base_sha")
    if safe != current_safe_sha:
        raise EvidenceError("safe-base mismatch: stale candidate; preserve current safe point")

    candidate = _sha(manifest.get("candidate_sha"), "candidate_sha")
    tree = _sha(manifest.get("candidate_tree_sha"), "candidate_tree_sha")
    tested = _sha(manifest.get("tested_sha"), "tested_sha")
    if tested != candidate:
        raise EvidenceError("test evidence is stale or bound to a different candidate SHA")
    approved = _sha(manifest.get("owner_approved_sha"), "owner_approved_sha")
    if approved != candidate:
        raise EvidenceError("owner approval is not bound to the exact candidate SHA")

    _sha(manifest.get("candidate_base_sha"), "candidate_base_sha")
    if manifest["candidate_base_sha"] != safe:
        if manifest.get("accepted_dependency_chain") is not True:
            raise EvidenceError("stacked candidate base differs; accepted dependency chain required")
        chain = manifest.get("dependency_shas")
        if not isinstance(chain, list) or not chain:
            raise EvidenceError("dependency chain missing")
        for idx, value in enumerate(chain):
            _sha(value, f"dependency_shas[{idx}]")

    _required_text(manifest.get("point0_golden_id"), "point0_golden_id")
    _required_text(manifest.get("current_id"), "current_id")
    _required_text(manifest.get("sole_next_id"), "sole_next_id")
    _required_text(manifest.get("source_ref"), "source_ref")
    _required_text(manifest.get("readback_receipt"), "readback_receipt")
    _required_text(manifest.get("security_review_receipt"), "security_review_receipt")
    _required_text(manifest.get("owner_approval_receipt"), "owner_approval_receipt")

    checks = manifest.get("checks")
    if not isinstance(checks, list):
        raise EvidenceError("checks must be a list")
    seen: set[str] = set()
    for i, check in enumerate(checks):
        if not isinstance(check, dict):
            raise EvidenceError(f"checks[{i}] must be an object")
        name = _required_text(check.get("name"), f"checks[{i}].name")
        if name in seen:
            raise EvidenceError(f"duplicate check: {name}")
        seen.add(name)
        run_id = _required_text(check.get("run_id"), f"checks[{i}].run_id")
        if not run_id.isdigit():
            raise EvidenceError(f"checks[{i}].run_id must be a numeric run identifier")
        check_sha = _sha(check.get("tested_sha"), f"checks[{i}].tested_sha")
        if check_sha != candidate:
            raise EvidenceError(f"check {name} is not bound to candidate SHA")
        if check.get("conclusion") != "success":
            raise EvidenceError(f"check {name} is not successful")
    missing = sorted(set(REQUIRED_CHECKS) - seen)
    if missing:
        raise EvidenceError("required checks missing: " + ", ".join(missing))

    # Require a unique, complete source identity; no inferred values.
    source = manifest.get("source_identity")
    if not isinstance(source, dict):
        raise EvidenceError("source_identity missing")
    _sha(source.get("commit_sha"), "source_identity.commit_sha")
    _sha(source.get("tree_sha"), "source_identity.tree_sha")
    if source.get("commit_sha") != safe:
        raise EvidenceError("source snapshot commit does not match safe base")
    _required_text(manifest.get("validation_profile"), "validation_profile")
    _required_text(manifest.get("time_binding_utc"), "time_binding_utc")
    return candidate


def resolve(manifest: dict[str, Any], current_safe_sha: str) -> dict[str, str]:
    candidate = validate_manifest(manifest, current_safe_sha)
    return {
        "status": "VALIDATED_CANDIDATE",
        "previous_safe_sha": current_safe_sha,
        "candidate_sha": candidate,
        "candidate_tree_sha": manifest["candidate_tree_sha"],
        "tested_sha": manifest["tested_sha"],
    }


def advance_safe_point(state_path: Path, expected_old_sha: str, manifest: dict[str, Any]) -> dict[str, str]:
    """Atomically CAS-update a local safe-point state file; refuses stale writers."""
    expected_old_sha = _sha(expected_old_sha, "expected_old_sha")
    if not state_path.exists():
        raise EvidenceError("safe-point state file does not exist; refusing to initialize implicitly")
    current = json.loads(state_path.read_text(encoding="utf-8"))
    if not isinstance(current, dict):
        raise EvidenceError("safe-point state must be a JSON object")
    current_sha = _sha(current.get("safe_sha"), "state.safe_sha")
    if current_sha != expected_old_sha:
        raise EvidenceError("compare-and-swap failed: state changed since expected old SHA")
    result = resolve(manifest, current_sha)
    payload = {"safe_sha": result["candidate_sha"], "tree_sha": result["candidate_tree_sha"],
               "previous_safe_sha": current_sha, "receipt": manifest["readback_receipt"]}
    state_path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=".safe-point-", dir=str(state_path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(payload, stream, sort_keys=True, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_name, state_path)
        # fsync directory entry where supported
        dir_fd = os.open(str(state_path.parent), os.O_RDONLY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
    result["status"] = "SAFE_POINT_ADVANCED"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="JSON evidence manifest")
    parser.add_argument("--current-safe-sha", required=True)
    parser.add_argument("--state-file", type=Path, help="Optional CAS state file; omit for validation-only")
    parser.add_argument("--expected-old-sha", help="Required when --state-file is used")
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    try:
        if args.state_file:
            if not args.expected_old_sha:
                raise EvidenceError("--expected-old-sha is required with --state-file")
            result = advance_safe_point(args.state_file, args.expected_old_sha, manifest)
        else:
            result = resolve(manifest, args.current_safe_sha)
    except (EvidenceError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "REJECTED", "reason": str(exc)}, indent=2))
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
