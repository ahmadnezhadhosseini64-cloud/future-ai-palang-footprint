import unittest
import random

from copy3_intake_guard import validate_copy3_receipt


BASE = "a" * 40
HEAD = "b" * 40


def receipt():
    return {
        "host_id": "host-test-01",
        "model": "declared-model",
        "platform": "declared-platform",
        "session_id": "session-test",
        "copy2_source_sha": BASE,
        "copy3_head_sha": HEAD,
        "pr_base_sha": BASE,
        "pr_head_sha": HEAD,
        "changed_paths": ["prototype/example.py"],
    }


class Copy3IntakeGuardTests(unittest.TestCase):
    def test_accepts_fresh_structural_receipt(self):
        self.assertEqual(validate_copy3_receipt(receipt(), BASE), [])

    def test_rejects_stale_copy3_source(self):
        r = receipt()
        r["copy2_source_sha"] = "c" * 40
        self.assertTrue(any("not created from the current" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_malformed_copy3_sha_fields(self):
        r = receipt()
        r["copy3_head_sha"] = "short"
        self.assertTrue(any("copy3_head_sha must be a full" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_stale_pr_base(self):
        r = receipt()
        r["pr_base_sha"] = "c" * 40
        self.assertTrue(any("PR base SHA is stale" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_pr_head_mismatch(self):
        r = receipt()
        r["pr_head_sha"] = "c" * 40
        self.assertTrue(any("PR head SHA" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_owner_protected_workflow_path(self):
        r = receipt()
        r["changed_paths"] = [".github/workflows/ci.yml"]
        self.assertTrue(any("owner-protected path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_owner_protected_governance_path(self):
        r = receipt()
        r["changed_paths"] = ["docs/architecture/SAFE-COPY/rules.md"]
        self.assertTrue(any("owner-protected path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_security_guard_modification(self):
        r = receipt()
        r["changed_paths"] = ["prototype/haif-gpt6-starter/safe_points_guard.py"]
        self.assertTrue(any("owner-protected path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_host_entry_message_modification(self):
        r = receipt()
        r["changed_paths"] = ["prototype/universal-host/UNIVERSAL_AI_HOST_ENTRY_FA.md"]
        self.assertTrue(any("owner-protected path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_two_message_bootstrap_modification(self):
        r = receipt()
        r["changed_paths"] = ["prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md"]
        self.assertTrue(any("owner-protected path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_portable_host_entry_modification(self):
        r = receipt()
        r["changed_paths"] = ["prototype/haif-gpt6-starter/UNIVERSAL_AI_HOST_ENTRY_FA.md"]
        self.assertTrue(any("owner-protected path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_package_manifest_modification(self):
        r = receipt()
        r["changed_paths"] = ["prototype/haif-gpt6-starter/manifest.json"]
        self.assertTrue(any("owner-protected path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_host_governance_source_modification(self):
        r = receipt()
        r["changed_paths"] = ["docs/architecture/HOST-SECURITY/OWNER-VERBAL-ENTRY-GATE.md"]
        self.assertTrue(any("owner-protected path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_security_test_modification(self):
        r = receipt()
        r["changed_paths"] = ["prototype/haif-gpt6-starter/test_safe_points_guard.py"]
        self.assertTrue(any("owner-protected path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_rejects_path_traversal(self):
        r = receipt()
        r["changed_paths"] = ["prototype/../../.github/CODEOWNERS"]
        self.assertTrue(any("unsafe repository path" in e for e in validate_copy3_receipt(r, BASE)))

    def test_self_declared_host_claims_are_not_authentication_inputs(self):
        r = receipt()
        del r["session_id"]
        del r["host_id"]
        self.assertEqual(validate_copy3_receipt(r, BASE), [])

    def test_rejects_malformed_expected_sha(self):
        self.assertTrue(validate_copy3_receipt(receipt(), "not-a-sha"))

    def test_pressure_rejects_2000_stale_receipts(self):
        rng = random.Random(20261127)
        for _ in range(2000):
            r = receipt()
            r["copy2_source_sha"] = "".join(rng.choice("0123456789abcdef") for _ in range(40))
            self.assertTrue(validate_copy3_receipt(r, BASE))

    def test_pressure_rejects_2000_protected_path_receipts(self):
        rng = random.Random(20261128)
        protected = [
            ".github/workflows/pipeline.yml",
            "prototype/haif-gpt6-starter/safe_points_guard.py",
            "prototype/haif-gpt6-starter/test_safe_points_guard.py",
            "docs/architecture/SAFE-COPY/policy.md",
        ]
        for _ in range(2000):
            r = receipt()
            r["changed_paths"] = [rng.choice(protected)]
            self.assertTrue(validate_copy3_receipt(r, BASE))

    def test_pressure_accepts_1000_fresh_valid_receipts(self):
        for index in range(1000):
            r = receipt()
            r["host_id"] = f"host-{index:04d}"
            r["session_id"] = f"session-{index:04d}"
            self.assertEqual(validate_copy3_receipt(r, BASE), [])

    def test_rejects_empty_changed_paths(self):
        r = receipt()
        r["changed_paths"] = []
        self.assertTrue(any("non-empty list" in e for e in validate_copy3_receipt(r, BASE)))


if __name__ == "__main__":
    unittest.main()
