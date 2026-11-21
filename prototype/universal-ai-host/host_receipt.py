#!/usr/bin/env python3
"""Validate HAIF universal AI-host receipts using only the Python standard library."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

CAPABILITIES = {
    "github_repository_read", "github_oauth_or_connector_authorization",
    "isolated_workspace", "command_execution", "branch_scoped_write",
    "pull_request_creation", "artifact_download_upload",
    "durable_session_or_workspace_persistence",
}
STAGES = {"authorization", "source_recovery", "workspace", "execution", "write", "read_back", "restart_test"}
SECRET_KEY = re.compile(
    r"(password|passwd|token|secret|credential|cookie|private[_-]?key|otp|recovery[_-]?code)",
    re.IGNORECASE,
)
SECRET_VALUE = re.compile(
    r"(?i)(gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|Bearer\s+[A-Za-z0-9._~+/-]{12,})"
)
ACCEPTANCE = {
    "NOT_ACCEPTED": 0, "SOURCE_RECOVERED": 1, "PACKAGE_VERIFIED": 2,
    "WORKSPACE_RECOVERED": 3, "EXECUTION_VERIFIED": 4, "HOST_RECOVERED": 5,
}


class ReceiptError(ValueError):
    pass


def _walk(value: Any, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if SECRET_KEY.search(str(key)):
                raise ReceiptError(f"secret-like field is forbidden at {path}.{key}")
            _walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _walk(child, f"{path}[{index}]")
    elif isinstance(value, str) and SECRET_VALUE.search(value):
        raise ReceiptError(f"secret-like value is forbidden at {path}")


def validate_receipt(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["receipt root must be an object"]
    try:
        _walk(data)
    except ReceiptError as exc:
        errors.append(str(exc))

    required = {
        "schema_version", "receipt_id", "host", "repository", "capabilities",
        "stages", "acceptance_level", "secrets_present", "created_at", "evidence",
    }
    missing = required - data.keys()
    if missing:
        errors.append("missing top-level fields: " + ", ".join(sorted(missing)))
        return errors

    if data["schema_version"] != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    if data["secrets_present"] is not False:
        errors.append("secrets_present must be false")
    level = data["acceptance_level"]
    if level not in ACCEPTANCE:
        errors.append("unknown acceptance_level")

    host = data["host"]
    if not isinstance(host, dict) or any(
        not isinstance(host.get(k), str) or not host[k].strip()
        for k in ("provider", "model_or_host", "session_id")
    ):
        errors.append("host must include non-empty provider, model_or_host, and session_id")

    repository = data["repository"]
    if not isinstance(repository, dict):
        errors.append("repository must be an object")
    else:
        if repository.get("full_name") != "ahmadnezhadhosseini64-cloud/future-ai-palang-footprint":
            errors.append("repository.full_name must identify the canonical HAIF repository")
        sha = repository.get("observed_head_sha")
        if sha is not None and (not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha)):
            errors.append("observed_head_sha must be a 40-character lowercase Git SHA or null")

    capabilities = data["capabilities"]
    if not isinstance(capabilities, dict) or set(capabilities) != CAPABILITIES:
        errors.append("capabilities must contain exactly the eight defined capability keys")
    else:
        for key, item in capabilities.items():
            if not isinstance(item, dict) or item.get("status") not in {"AVAILABLE", "UNAVAILABLE", "NOT_CHECKED"}:
                errors.append(f"invalid capability status: {key}")
                continue
            if "evidence_reference" not in item or (
                item["status"] == "AVAILABLE" and not item["evidence_reference"]
            ):
                errors.append(f"AVAILABLE capability requires evidence_reference: {key}")

    stages = data["stages"]
    if not isinstance(stages, dict) or set(stages) != STAGES:
        errors.append("stages must contain exactly the seven defined stage keys")
    else:
        for key, item in stages.items():
            if not isinstance(item, dict) or item.get("status") not in {
                "PASS", "FAIL", "OPEN", "NOT_RUN", "UNAVAILABLE"
            }:
                errors.append(f"invalid stage status: {key}")
                continue
            if "evidence_reference" not in item:
                errors.append(f"stage requires evidence_reference: {key}")

    if not isinstance(data["evidence"], list):
        errors.append("evidence must be an array")

    requirements = {
        "SOURCE_RECOVERED": ("source_recovery",),
        "PACKAGE_VERIFIED": ("source_recovery", "execution"),
        "WORKSPACE_RECOVERED": ("source_recovery", "workspace"),
        "EXECUTION_VERIFIED": ("source_recovery", "workspace", "execution"),
        "HOST_RECOVERED": ("source_recovery", "workspace", "execution", "read_back", "restart_test"),
    }
    if level in requirements and isinstance(stages, dict):
        for stage in requirements[level]:
            if not isinstance(stages.get(stage), dict) or stages[stage].get("status") != "PASS":
                errors.append(f"{level} requires {stage}.status=PASS")
    if level == "HOST_RECOVERED":
        if not isinstance(repository, dict) or not repository.get("observed_head_sha"):
            errors.append("HOST_RECOVERED requires observed repository HEAD")
        if not isinstance(stages, dict) or not isinstance(stages.get("authorization"), dict) or stages["authorization"].get("status") != "PASS":
            errors.append("HOST_RECOVERED requires authorization evidence")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="validate one JSON receipt")
    validate.add_argument("receipt", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.receipt.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2
    errors = validate_receipt(data)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: receipt structure and safety checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
