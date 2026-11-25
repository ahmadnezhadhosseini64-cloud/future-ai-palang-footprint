"""Negative tests for host enrollment gates; they do not provision accounts."""
import unittest
from host_intake_gate import HostGateError, stage1_read_only_receipt, stage2_workspace_gate


def stage1():
    return {"host_claimed_id":"host-abc","repo":"owner/canonical","ref":"main",
            "commit_sha":"a"*40,"tree_sha":"b"*40,"readback_utc":"2026-11-25T15:00:00Z",
            "read_only_proof":"receipt-r1","write_attempted":False,
            "canonical_write_access":False,"identity_verified_by_owner":False}


def stage2():
    return {"owner_review_approved":True,"stage1_host_id":"host-abc","workspace_id":"ws-1",
            "workspace_repo":"host/private-workspace","workspace_commit_sha":"c"*40,
            "permission_readback_receipt":"perm-r1","isolation_test_receipt":"iso-r1",
            "workspace_visibility":"private","canonical_repo_write_permission":False,
            "main_master_access":False,"shared_credentials":False,
            "workspace_isolation_verified":True,"workspace_access_subjects":["host-abc","owner"],
            "owner_subject":"owner","host_write_scope":"workspace-only"}


class HostIntakeGateTests(unittest.TestCase):
    def test_stage1_only_receipt_not_active(self):
        self.assertIn("OWNER_REVIEW_REQUIRED",stage1_read_only_receipt(stage1())["status"])

    def test_stage1_rejects_write_or_unknown(self):
        r=stage1(); r["write_attempted"]=True
        with self.assertRaisesRegex(HostGateError,"read-only"):
            stage1_read_only_receipt(r)
        r=stage1(); r["canonical_write_access"]=None
        with self.assertRaisesRegex(HostGateError,"explicitly absent"):
            stage1_read_only_receipt(r)

    def test_stage1_rejects_self_issued_identity_approval(self):
        r=stage1(); r["identity_verified_by_owner"]=True
        with self.assertRaisesRegex(HostGateError,"cannot self-assert"):
            stage1_read_only_receipt(r)

    def test_stage2_requires_owner_gate(self):
        r=stage2(); r["owner_review_approved"]=False
        with self.assertRaisesRegex(HostGateError,"owner review"):
            stage2_workspace_gate(r,stage1())

    def test_stage2_requires_same_host(self):
        r=stage2(); r["stage1_host_id"]="other"
        with self.assertRaisesRegex(HostGateError,"does not match"):
            stage2_workspace_gate(r,stage1())

    def test_stage2_rejects_public_or_canonical_workspace(self):
        r=stage2(); r["workspace_visibility"]="public"
        with self.assertRaisesRegex(HostGateError,"private"):
            stage2_workspace_gate(r,stage1())
        r=stage2(); r["workspace_repo"]="owner/canonical"
        with self.assertRaisesRegex(HostGateError,"separate repository"):
            stage2_workspace_gate(r,stage1())

    def test_stage2_rejects_canonical_write_main_access_or_shared_secrets(self):
        for field in ("canonical_repo_write_permission","main_master_access","shared_credentials"):
            r=stage2(); r[field]=True
            with self.subTest(field=field), self.assertRaises(HostGateError):
                stage2_workspace_gate(r,stage1())

    def test_stage2_requires_verified_isolation_and_workspace_only_scope(self):
        r=stage2(); r["workspace_isolation_verified"]=False
        with self.assertRaisesRegex(HostGateError,"isolation test"):
            stage2_workspace_gate(r,stage1())
        r=stage2(); r["host_write_scope"]="canonical"
        with self.assertRaisesRegex(HostGateError,"workspace-only"):
            stage2_workspace_gate(r,stage1())

    def test_stage2_acl_must_be_explicit_unique_and_include_host_owner(self):
        for acl in ([],["owner"],["host-abc","owner","owner"]):
            r=stage2(); r["workspace_access_subjects"]=acl
            with self.assertRaises(HostGateError):
                stage2_workspace_gate(r,stage1())

    def test_valid_receipts_do_not_claim_provisioning(self):
        out=stage2_workspace_gate(stage2(),stage1())
        self.assertEqual(out["status"],"STAGE2_ISOLATION_RECEIPT_VALIDATED_NOT_PROVISIONED_BY_THIS_TOOL")


if __name__ == "__main__":
    unittest.main()
