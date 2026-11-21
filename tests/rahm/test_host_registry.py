import unittest

from scripts.rahm.validate_host_registry import validate_registry


def host_record():
    return {
        "host_id": "HAIF-HOST-20261122-001",
        "workspace_id": "HAIF-WORKSPACE-20261122-001",
        "host_type": "GPT",
        "model_version": "GPT-6",
        "adapter_version": "1.0.0",
        "permission_scope": "L3_OWNER_EXPORT_PROPOSAL_ONLY",
        "status": "ACTIVE",
        "registered_at_utc": "2026-11-22T00:00:00Z",
        "last_seen_at_utc": "2026-11-22T00:00:00Z",
        "master_version_seen": "1.7.94",
        "master_commit_seen": "a" * 40,
        "private_repository": "ahmadnezhadhosseini64-cloud/haif-host-haif-host-20261122-001",
        "private_repository_visibility": "PRIVATE",
        "master_access": "PUBLIC_READ_ONLY",
        "master_write_access": False,
        "rahm_access": "NONE",
        "host_direct_write_access": False,
        "broker_write_access": "NOT_CONFIGURED",
        "connector_read_access": "VERIFIED",
        "monitoring_mode": "LIVE_READ_VERIFIED",
        "owner_approval_ref": "OWNER-APPROVAL-001",
        "credential_reference": None,
        "acceptance_receipt_ref": "HOST-ACCEPTANCE-001",
        "host_id_issue_receipt_ref": "HOST-ID-ISSUANCE-001",
        "owner_id_issuer": "CHATGPT_CONTROL_PLANE_ON_OWNER_COMMAND",
        "owner_export_receipt_ref": None,
        "last_export_at_utc": None,
        "workspace_isolation_ref": "WORKSPACE-ISOLATION-001",
        "revocation_ref": None,
    }


class HostRegistryInvariantTests(unittest.TestCase):
    def test_empty_registry_is_valid(self):
        self.assertEqual(validate_registry({"hosts": []}), [])

    def test_valid_active_private_host_is_valid(self):
        self.assertEqual(validate_registry({"hosts": [host_record()]}), [])

    def test_rejects_master_write(self):
        record = host_record()
        record["master_write_access"] = True
        self.assertIn("hosts[0]:MASTER_WRITE_MUST_BE_FALSE", validate_registry({"hosts": [record]}))

    def test_rejects_rahm_access(self):
        record = host_record()
        record["rahm_access"] = "READ"
        self.assertIn("hosts[0]:RAHM_ACCESS_MUST_BE_NONE", validate_registry({"hosts": [record]}))

    def test_rejects_duplicate_host_id(self):
        first = host_record()
        second = host_record()
        second["workspace_id"] = "HAIF-WORKSPACE-20261122-002"
        second["private_repository"] = "ahmadnezhadhosseini64-cloud/haif-host-haif-host-20261122-002"
        self.assertIn("hosts[1]:DUPLICATE_HOST_ID", validate_registry({"hosts": [first, second]}))

    def test_rejects_duplicate_workspace_id(self):
        first = host_record()
        second = host_record()
        second["host_id"] = "HAIF-HOST-20261122-002"
        second["private_repository"] = "ahmadnezhadhosseini64-cloud/haif-host-haif-host-20261122-002"
        self.assertIn("hosts[1]:DUPLICATE_WORKSPACE_ID", validate_registry({"hosts": [first, second]}))

    def test_rejects_live_monitoring_without_connector_read(self):
        record = host_record()
        record["connector_read_access"] = "NOT_GRANTED"
        self.assertIn("hosts[0]:LIVE_MONITORING_WITHOUT_VERIFIED_REPOSITORY_READ", validate_registry({"hosts": [record]}))

    def test_rejects_active_host_without_receipt(self):
        record = host_record()
        record["acceptance_receipt_ref"] = None
        self.assertIn("hosts[0]:ACTIVE_REQUIRES_ACCEPTANCE_RECEIPT_REF", validate_registry({"hosts": [record]}))


if __name__ == "__main__":
    unittest.main()
