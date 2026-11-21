import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parent / "host_receipt.py"
SPEC = importlib.util.spec_from_file_location("host_receipt", MODULE_PATH)
host_receipt = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(host_receipt)


def sample_receipt():
    capabilities = {
        key: {"status": "NOT_CHECKED", "evidence_reference": None}
        for key in host_receipt.CAPABILITIES
    }
    stages = {
        key: {"status": "NOT_RUN", "evidence_reference": None}
        for key in host_receipt.STAGES
    }
    return {
        "schema_version": "1.0.0",
        "receipt_id": "test-session-0001",
        "host": {"provider": "test-provider", "model_or_host": "test-host", "session_id": "session-0001"},
        "repository": {
            "full_name": "ahmadnezhadhosseini64-cloud/future-ai-palang-footprint",
            "default_branch": "main", "observed_head_sha": None, "working_branch": None
        },
        "capabilities": capabilities, "stages": stages,
        "acceptance_level": "NOT_ACCEPTED", "secrets_present": False,
        "created_at": "2026-11-21T00:00:00Z", "evidence": []
    }


class HostReceiptTests(unittest.TestCase):
    def test_minimal_truthful_receipt_passes(self):
        self.assertEqual(host_receipt.validate_receipt(sample_receipt()), [])

    def test_available_capability_requires_evidence(self):
        receipt = sample_receipt()
        receipt["capabilities"]["github_repository_read"]["status"] = "AVAILABLE"
        self.assertTrue(any("requires evidence_reference" in e for e in host_receipt.validate_receipt(receipt)))

    def test_wrong_repository_is_rejected(self):
        receipt = sample_receipt()
        receipt["repository"]["full_name"] = "someone/else"
        self.assertTrue(any("canonical HAIF repository" in e for e in host_receipt.validate_receipt(receipt)))

    def test_secret_like_field_is_rejected(self):
        receipt = sample_receipt()
        receipt["host"]["access_token"] = "not-a-real-token"
        self.assertTrue(any("secret-like field" in e for e in host_receipt.validate_receipt(receipt)))

    def test_secret_like_value_is_rejected(self):
        receipt = sample_receipt()
        receipt["evidence"] = [{
            "kind": "debug", "reference": "log",
            "result": "Bearer abcdefghijklmnopqrstuvwxyz123456"
        }]
        self.assertTrue(any("secret-like value" in e for e in host_receipt.validate_receipt(receipt)))

    def test_host_recovered_requires_restart_and_readback(self):
        receipt = sample_receipt()
        receipt["acceptance_level"] = "HOST_RECOVERED"
        for stage in ("authorization", "source_recovery", "workspace", "execution"):
            receipt["stages"][stage] = {"status": "PASS", "evidence_reference": "evidence:" + stage}
        receipt["repository"]["observed_head_sha"] = "a" * 40
        errors = host_receipt.validate_receipt(receipt)
        self.assertTrue(any("read_back.status=PASS" in e for e in errors))
        self.assertTrue(any("restart_test.status=PASS" in e for e in errors))

    def test_host_recovered_passes_only_with_full_evidence(self):
        receipt = sample_receipt()
        receipt["acceptance_level"] = "HOST_RECOVERED"
        receipt["repository"]["observed_head_sha"] = "a" * 40
        for stage in ("authorization", "source_recovery", "workspace", "execution", "read_back", "restart_test"):
            receipt["stages"][stage] = {"status": "PASS", "evidence_reference": "evidence:" + stage}
        self.assertEqual(host_receipt.validate_receipt(receipt), [])


if __name__ == "__main__":
    unittest.main()
