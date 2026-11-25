"""Fail-closed validation for the two-stage AI-host intake contract.

This validates receipts, not account-level permissions. Actual isolation requires
independent owner provisioning and live permission read-back; this module cannot
grant access or authenticate a host.
"""
from __future__ import annotations

from typing import Any


class HostGateError(ValueError):
    pass


def stage1_read_only_receipt(receipt: dict[str, Any]) -> dict[str, str]:
    if not isinstance(receipt, dict):
        raise HostGateError("Stage-1 receipt must be a JSON object")
    for key in ("host_claimed_id", "repo", "ref", "commit_sha", "tree_sha", "readback_utc", "read_only_proof"):
        value = receipt.get(key)
        if not isinstance(value, str) or not value.strip():
            raise HostGateError(f"Stage-1 receipt missing {key}")
    if receipt.get("write_attempted") is not False:
        raise HostGateError("Stage 1 must be read-only; write attempt or unknown status rejected")
    if receipt.get("canonical_write_access") is not False:
        raise HostGateError("Stage 1 canonical write access must be explicitly absent")
    if receipt.get("identity_verified_by_owner") is not False:
        raise HostGateError("Stage-1 receipt cannot self-assert owner identity verification")
    return {"status": "STAGE1_RECEIPT_COMPLETE_OWNER_REVIEW_REQUIRED", "host_claimed_id": receipt["host_claimed_id"]}


def stage2_workspace_gate(receipt: dict[str, Any], stage1: dict[str, Any]) -> dict[str, str]:
    stage1_read_only_receipt(stage1)
    if not isinstance(receipt, dict):
        raise HostGateError("Stage-2 workspace receipt must be an object")
    if receipt.get("owner_review_approved") is not True:
        raise HostGateError("explicit owner review approval is required")
    if receipt.get("stage1_host_id") != stage1.get("host_claimed_id"):
        raise HostGateError("Stage-2 host does not match reviewed Stage-1 host")
    for key in ("workspace_id", "workspace_repo", "workspace_commit_sha", "permission_readback_receipt", "isolation_test_receipt"):
        value = receipt.get(key)
        if not isinstance(value, str) or not value.strip():
            raise HostGateError(f"Stage-2 receipt missing {key}")
    if receipt.get("workspace_visibility") != "private":
        raise HostGateError("workspace must be verified private")
    if receipt.get("workspace_repo") == stage1.get("repo"):
        raise HostGateError("workspace must be a separate repository from canonical source")
    if receipt.get("canonical_repo_write_permission") is not False:
        raise HostGateError("host must have no canonical repository write permission")
    if receipt.get("main_master_access") is not False:
        raise HostGateError("main/MASTER access must be explicitly denied")
    if receipt.get("shared_credentials") is not False:
        raise HostGateError("owner/shared credentials are prohibited")
    if receipt.get("workspace_isolation_verified") is not True:
        raise HostGateError("independent workspace isolation test must pass")
    allowed = receipt.get("workspace_access_subjects")
    if not isinstance(allowed, list) or not allowed or any(not isinstance(x, str) or not x for x in allowed):
        raise HostGateError("workspace access list must be explicit")
    if len(set(allowed)) != len(allowed):
        raise HostGateError("duplicate workspace access subjects")
    if receipt["stage1_host_id"] not in allowed:
        raise HostGateError("reviewed host is not present in workspace ACL")
    if receipt.get("owner_subject") not in allowed:
        raise HostGateError("owner must be present in workspace ACL")
    if receipt.get("host_write_scope") != "workspace-only":
        raise HostGateError("write scope must be exactly workspace-only")
    return {"status": "STAGE2_ISOLATION_RECEIPT_VALIDATED_NOT_PROVISIONED_BY_THIS_TOOL",
            "host_id": receipt["stage1_host_id"], "workspace_id": receipt["workspace_id"]}
