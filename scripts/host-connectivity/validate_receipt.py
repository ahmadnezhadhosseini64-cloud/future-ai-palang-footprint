#!/usr/bin/env python3
"""Dependency-free structural and security checks for HAIF host receipts."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

STATUSES = {"PASS", "FAIL", "NOT_CONNECTED", "NOT_AVAILABLE", "NOT_RUN", "BLOCKED"}
HEX_SHA = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")


def validate(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["receipt must be a JSON object"]
    required = {"receipt_version", "host", "repository", "capabilities", "recovery", "acceptance", "open_gates"}
    missing = sorted(required - data.keys())
    if missing:
        errors.append("missing top-level fields: " + ", ".join(missing))
    if data.get("receipt_version") != "1.0.0":
        errors.append("receipt_version must be 1.0.0")
    host = data.get("host")
    if not isinstance(host, dict) or not all(k in host for k in ("provider", "model", "session_fresh")):
        errors.append("host must include provider, model and session_fresh")
    repo = data.get("repository")
    if not isinstance(repo, dict):
        errors.append("repository must be an object")
    else:
        if repo.get("owner") != "ahmadnezhadhosseini64-cloud" or repo.get("name") != "future-ai-palang-footprint":
            errors.append("repository identity does not match the canonical repository")
        if not isinstance(repo.get("default_branch"), str) or not repo["default_branch"]:
            errors.append("repository.default_branch is required")
        sha = repo.get("head_sha")
        if sha is not None and (not isinstance(sha, str) or not HEX_SHA.fullmatch(sha)):
            errors.append("repository.head_sha must be a 40/64-character lowercase hex SHA or null")
    caps = data.get("capabilities")
    expected_caps = {"read", "execute", "workspace", "write", "persistence"}
    if not isinstance(caps, dict) or not expected_caps.issubset(caps):
        errors.append("capabilities must separately declare read, execute, workspace, write and persistence")
    else:
        for key in ("read", "execute", "workspace", "persistence"):
            if caps[key] not in STATUSES:
                errors.append(f"capabilities.{key} has an unsupported status")
        if caps["write"] not in {"BRANCH_ONLY", "NONE", "NOT_VERIFIED", "BLOCKED"}:
            errors.append("capabilities.write must be NONE, BRANCH_ONLY, NOT_VERIFIED or BLOCKED")
    recovery = data.get("recovery")
    if not isinstance(recovery, dict) or not all(k in recovery for k in ("source_recovered", "reference_index", "mother_version", "current_checkpoint", "sole_queue")):
        errors.append("recovery must declare source_recovered, reference_index, mother_version, current_checkpoint and sole_queue")
    elif recovery.get("source_recovered") and (recovery.get("reference_index") != "FOUND" or not recovery.get("current_checkpoint") or not recovery.get("sole_queue")):
        errors.append("source_recovered requires a found index, current checkpoint and sole queue")
    if data.get("acceptance") not in {"SOURCE_RECOVERED", "PACKAGE_VERIFIED", "HOST_RECOVERED", "PARTIAL", "BLOCKED"}:
        errors.append("acceptance has an unsupported value")
    if not isinstance(data.get("open_gates"), list):
        errors.append("open_gates must be an array")
    if data.get("acceptance") == "HOST_RECOVERED":
        if not isinstance(caps, dict) or any(caps.get(k) != "PASS" for k in ("read", "execute", "workspace", "persistence")):
            errors.append("HOST_RECOVERED requires PASS for read, execute, workspace and persistence")
        if not isinstance(recovery, dict) or recovery.get("source_recovered") is not True:
            errors.append("HOST_RECOVERED requires source_recovered=true")
    security = data.get("security_attestation")
    if not isinstance(security, dict):
        errors.append("security_attestation is required")
    else:
        if security.get("no_credentials_stored") is not True:
            errors.append("credentials/tokens must never be stored in a receipt")
        if security.get("handshake_is_not_authentication") is not True:
            errors.append("the textual handshake must not be treated as authentication")
    # Reject likely credential-bearing keys at any depth.
    forbidden = {"token", "access_token", "refresh_token", "password", "secret", "cookie", "authorization", "pat", "otp"}
    def walk(value: object, path: str = "$") -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if str(key).lower() in forbidden:
                    errors.append(f"forbidden credential field at {path}.{key}")
                walk(child, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{path}[{index}]")
    walk(data)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path, help="path to a JSON acceptance receipt")
    args = parser.parse_args()
    try:
        payload = json.loads(args.receipt.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2
    errors = validate(payload)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"INVALID ({len(errors)} error(s))", file=sys.stderr)
        return 1
    print("VALID: HAIF host acceptance receipt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
