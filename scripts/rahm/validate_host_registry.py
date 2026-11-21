#!/usr/bin/env python3
"""Validate HAIF Host Registry invariants beyond JSON Schema shape."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

HOST_ID = re.compile(r"^HAIF-HOST-[0-9]{8}-[0-9]{3}$")
WORKSPACE_ID = re.compile(r"^HAIF-WORKSPACE-[0-9]{8}-[0-9]{3}$")


def validate_registry(registry: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(registry, dict) or not isinstance(registry.get("hosts"), list):
        return ["REGISTRY_OR_HOSTS_INVALID"]
    seen_hosts: set[str] = set()
    seen_workspaces: set[str] = set()
    seen_repositories: set[str] = set()
    for index, host in enumerate(registry["hosts"]):
        label = f"hosts[{index}]"
        if not isinstance(host, dict):
            errors.append(f"{label}:NOT_AN_OBJECT")
            continue
        host_id = host.get("host_id")
        workspace_id = host.get("workspace_id")
        private_repo = host.get("private_repository")
        if not isinstance(host_id, str) or not HOST_ID.fullmatch(host_id):
            errors.append(f"{label}:INVALID_HOST_ID")
        elif host_id in seen_hosts:
            errors.append(f"{label}:DUPLICATE_HOST_ID")
        else:
            seen_hosts.add(host_id)
        if not isinstance(workspace_id, str) or not WORKSPACE_ID.fullmatch(workspace_id):
            errors.append(f"{label}:INVALID_WORKSPACE_ID")
        elif workspace_id in seen_workspaces:
            errors.append(f"{label}:DUPLICATE_WORKSPACE_ID")
        else:
            seen_workspaces.add(workspace_id)
        if private_repo is not None:
            if not isinstance(private_repo, str) or not private_repo.startswith("ahmadnezhadhosseini64-cloud/haif-host-"):
                errors.append(f"{label}:INVALID_PRIVATE_REPOSITORY_OWNER_OR_NAME")
            elif private_repo in seen_repositories:
                errors.append(f"{label}:DUPLICATE_PRIVATE_REPOSITORY")
            else:
                seen_repositories.add(private_repo)
        if private_repo is None and host.get("private_repository_visibility") != "NOT_CREATED":
            errors.append(f"{label}:PRIVATE_REPOSITORY_VISIBILITY_CONFLICT")
        if private_repo is not None and host.get("private_repository_visibility") != "PRIVATE":
            errors.append(f"{label}:HOST_REPOSITORY_MUST_BE_PRIVATE")
        if host.get("master_access") != "PUBLIC_READ_ONLY":
            errors.append(f"{label}:MASTER_ACCESS_MUST_BE_PUBLIC_READ_ONLY")
        if host.get("master_write_access") is not False:
            errors.append(f"{label}:MASTER_WRITE_MUST_BE_FALSE")
        if host.get("rahm_access") != "NONE":
            errors.append(f"{label}:RAHM_ACCESS_MUST_BE_NONE")
        if host.get("host_direct_write_access") is not False:
            errors.append(f"{label}:HOST_DIRECT_WRITE_MUST_BE_FALSE")
        if host.get("owner_id_issuer") != "CHATGPT_CONTROL_PLANE_ON_OWNER_COMMAND":
            errors.append(f"{label}:INVALID_HOST_ID_ISSUER")
        if host.get("monitoring_mode") == "LIVE_READ_VERIFIED":
            if host.get("connector_read_access") != "VERIFIED" or private_repo is None:
                errors.append(f"{label}:LIVE_MONITORING_WITHOUT_VERIFIED_REPOSITORY_READ")
        if host.get("monitoring_mode") == "OWNER_EXPORT_SNAPSHOT" and not host.get("owner_export_receipt_ref"):
            errors.append(f"{label}:SNAPSHOT_MONITORING_WITHOUT_EXPORT_RECEIPT")
        if host.get("permission_scope") == "L4_OWNER_BROKERED_PRIVATE_HOST_REPO":
            if host.get("broker_write_access") != "OWNER_BROKER_ONLY" or private_repo is None:
                errors.append(f"{label}:L4_REQUIRES_OWNER_BROKER_AND_PRIVATE_REPOSITORY")
        if host.get("status") == "ACTIVE":
            for key in ("owner_approval_ref", "acceptance_receipt_ref", "host_id_issue_receipt_ref", "registered_at_utc", "workspace_isolation_ref"):
                if not host.get(key):
                    errors.append(f"{label}:ACTIVE_REQUIRES_{key.upper()}")
            if private_repo is None or host.get("private_repository_visibility") != "PRIVATE":
                errors.append(f"{label}:ACTIVE_REQUIRES_PRIVATE_HOST_REPOSITORY")
        if host.get("status") == "REVOKED" and not host.get("revocation_ref"):
            errors.append(f"{label}:REVOKED_REQUIRES_REVOCATION_REF")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, required=True)
    args = parser.parse_args()
    try:
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"HOST_REGISTRY_INVALID={exc}")
        return 2
    errors = validate_registry(registry)
    if errors:
        print("HOST_REGISTRY_INVARIANTS=FAIL")
        for error in errors:
            print(error)
        return 1
    print(f"HOST_REGISTRY_INVARIANTS=PASS records={len(registry['hosts'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
