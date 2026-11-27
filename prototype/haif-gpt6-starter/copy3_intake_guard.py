"""Fail-closed structural intake checks for proposals arriving from isolated Copy 3.

This validates freshness and protected paths only. It does NOT authenticate a host,
verify a signature, or replace the independent external verifier.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SHA40 = re.compile(r"^[0-9a-f]{40}$")
REQUIRED = (
    "copy2_source_sha",
    "copy3_head_sha",
    "pr_base_sha",
    "pr_head_sha",
    "changed_paths",
)
PROTECTED_EXACT = {
    "CODEOWNERS",
    ".github/CODEOWNERS",
    "prototype/haif-gpt6-starter/safe_copy_audit.py",
    "prototype/haif-gpt6-starter/safe_points_guard.py",
    "prototype/haif-gpt6-starter/copy3_intake_guard.py",
    "prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md",
    "prototype/haif-gpt6-starter/UNIVERSAL_AI_HOST_ENTRY_FA.md",
    "prototype/universal-host/UNIVERSAL_AI_HOST_ENTRY_FA.md",
    "prototype/haif-gpt6-starter/test_host_entry_sync.py",
    "prototype/haif-gpt6-starter/manifest.json",
    "prototype/haif-gpt6-starter/LIVING_MASTER_REFERENCE.md",
    "prototype/haif-gpt6-starter/GPT6_HOST_INSTRUCTIONS.md",
    "prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md",
    "prototype/haif-gpt6-starter/HOST_REGISTRY_SCHEMA.json",
    "prototype/haif-gpt6-starter/HOST_REGISTRY_TEMPLATE.json",
    "docs/REFERENCE_INDEX.md",
}
PROTECTED_PREFIXES = (
    ".github/",
    "docs/architecture/SAFE-COPY/",
    "docs/architecture/HOST-SECURITY/",
    "docs/architecture/HOST-IDENTITY/",
    "docs/architecture/HOST-REGISTRY/",
    "docs/architecture/HOST-WORKSPACES/",
    "docs/architecture/RAHM/",
    "MASTER/",
    "RAHM/",
    "POINT-0/",
)


def validate_copy3_receipt(receipt: dict[str, Any], expected_copy2_sha: str) -> list[str]:
    errors: list[str] = []
    if not SHA40.fullmatch(expected_copy2_sha or ""):
        return ["expected Copy 2 SHA must be a full 40-character lowercase commit SHA"]

    for key in REQUIRED:
        if key not in receipt:
            errors.append(f"missing receipt field: {key}")

    # Host/model/session claims are intentionally not authentication inputs.
    for key in ("copy2_source_sha", "copy3_head_sha", "pr_base_sha", "pr_head_sha"):
        value = receipt.get(key)
        if not isinstance(value, str) or not SHA40.fullmatch(value):
            errors.append(f"{key} must be a full 40-character lowercase commit SHA")
        value = receipt.get(key)
        if not isinstance(value, str) or not SHA40.fullmatch(value):
            errors.append(f"{key} must be a full 40-character lowercase commit SHA")

    if receipt.get("copy2_source_sha") != expected_copy2_sha:
        errors.append("Copy 3 was not created from the current expected Copy 2 SHA")
    if receipt.get("pr_base_sha") != expected_copy2_sha:
        errors.append("PR base SHA is stale or does not equal the current Copy 2 SHA")
    if receipt.get("pr_head_sha") != receipt.get("copy3_head_sha"):
        errors.append("PR head SHA does not match the recorded Copy 3 head SHA")

    paths = receipt.get("changed_paths")
    if not isinstance(paths, list) or not paths or any(not isinstance(p, str) or not p.strip() for p in paths):
        errors.append("changed_paths must be a non-empty list of non-empty repository paths")
    else:
        normalized = []
        for raw_path in paths:
            normalized_path = raw_path.replace("\\", "/")
            while normalized_path.startswith("./"):
                normalized_path = normalized_path[2:]
            normalized.append(normalized_path)
        if len(set(normalized)) != len(normalized):
            errors.append("changed_paths contains duplicates")
        for path in normalized:
            if path.startswith("/") or ".." in Path(path).parts:
                errors.append(f"unsafe repository path: {path}")
                continue
            if (path in PROTECTED_EXACT
                    or path.startswith("prototype/haif-gpt6-starter/test_safe_")
                    or any(path.startswith(prefix) for prefix in PROTECTED_PREFIXES)):
                errors.append(f"Copy 3 proposal touches owner-protected path: {path}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--expected-copy2-sha", required=True)
    args = parser.parse_args()
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"COPY3_INTAKE=FAIL: invalid receipt: {exc}")
        return 1
    if not isinstance(receipt, dict):
        print("COPY3_INTAKE=FAIL: receipt root must be a JSON object")
        return 1
    errors = validate_copy3_receipt(receipt, args.expected_copy2_sha)
    if errors:
        print("COPY3_INTAKE=FAIL")
        for error in errors:
            print(" -", error)
        return 1
    print("COPY3_INTAKE=STRUCTURALLY_VALID_ONLY")
    print("HOST_IDENTITY=NOT_AUTHENTICATED")
    print("EXTERNAL_VERIFIER=REQUIRED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
