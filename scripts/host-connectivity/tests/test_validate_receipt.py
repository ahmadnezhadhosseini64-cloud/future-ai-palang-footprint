import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "validate_receipt.py"
SPEC = importlib.util.spec_from_file_location("validate_receipt", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def valid_receipt():
    return {
        "receipt_version": "1.0.0",
        "host": {"provider": "Example", "model": "Model-X", "session_fresh": True},
        "repository": {
            "owner": "ahmadnezhadhosseini64-cloud",
            "name": "future-ai-palang-footprint",
            "default_branch": "main",
            "head_sha": "a" * 40
        },
        "capabilities": {
            "read": "PASS", "execute": "PASS", "workspace": "PASS",
            "write": "NONE", "persistence": "PASS"
        },
        "recovery": {
            "source_recovered": True, "reference_index": "FOUND",
            "mother_version": "1.7.84", "current_checkpoint": "CURRENT-130",
            "sole_queue": "NEXT-051"
        },
        "acceptance": "HOST_RECOVERED",
        "open_gates": [],
        "security_attestation": {
            "no_credentials_stored": True,
            "oauth_authorized_in_destination_ui": True,
            "handshake_is_not_authentication": True
        }
    }


class ReceiptValidationTests(unittest.TestCase):
    def test_valid_host_recovered_receipt(self):
        self.assertEqual(MODULE.validate(valid_receipt()), [])

    def test_rejects_wrong_repository(self):
        data = valid_receipt()
        data["repository"]["name"] = "another-repository"
        self.assertTrue(any("repository identity" in e for e in MODULE.validate(data)))

    def test_rejects_host_recovered_without_restart_persistence(self):
        data = valid_receipt()
        data["capabilities"]["persistence"] = "NOT_RUN"
        self.assertTrue(any("HOST_RECOVERED requires PASS" in e for e in MODULE.validate(data)))

    def test_rejects_handshake_as_authentication(self):
        data = valid_receipt()
        data["security_attestation"]["handshake_is_not_authentication"] = False
        self.assertTrue(any("textual handshake" in e for e in MODULE.validate(data)))

    def test_rejects_credentials(self):
        data = valid_receipt()
        data["access_token"] = "do-not-store"
        self.assertTrue(any("forbidden credential field" in e for e in MODULE.validate(data)))

    def test_rejects_source_recovery_with_missing_pointer(self):
        data = valid_receipt()
        data["recovery"]["sole_queue"] = None
        self.assertTrue(any("source_recovered requires" in e for e in MODULE.validate(data)))


if __name__ == "__main__":
    unittest.main()
