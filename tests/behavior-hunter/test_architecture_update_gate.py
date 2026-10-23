import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "behavior-hunter"))
from architecture_update_gate import validate_proposal

class ArchitectureUpdateGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        evidence = self.root / "evidence" / "test.txt"
        evidence.parent.mkdir(parents=True)
        evidence.write_text("grounded test evidence\n", encoding="utf-8")
        self.digest = hashlib.sha256(evidence.read_bytes()).hexdigest()
        self.proposal = {
            "insight_id": "INSIGHT-TEST-001",
            "title": "Test proposal",
            "version": "1.0.0",
            "originating_event_ids": ["EVT-TEST"],
            "category": "verification",
            "affected_components": ["test gate"],
            "observed_facts": ["A repository evidence file exists."],
            "hypothesis": "An explicit evidence gate reduces unsupported promotions.",
            "evidence": [{"locator": "repo://evidence/test.txt", "sha256": self.digest}],
            "counterexamples": ["A mismatched digest must be blocked."],
            "proposed_change": "Validate evidence before review.",
            "required_tests": ["unit-test"],
            "rollback_plan": "Revert the isolated prototype commit.",
            "state": "PROPOSED",
            "owner_decision": "PENDING",
            "target_paths": ["docs/architecture/example.md"],
        }

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_proposal_is_reviewable_not_auto_promoted(self):
        result = validate_proposal(self.proposal, self.root)
        self.assertEqual(result["status"], "READY_FOR_OWNER_REVIEW")
        self.assertEqual(result["evidence_checked"][0]["integrity"], "VERIFIED")
        self.assertFalse(result["canonical_mutation_performed"])
        self.assertFalse(result["promotion_allowed"])

    def test_missing_required_fields_block(self):
        proposal = dict(self.proposal)
        del proposal["rollback_plan"]
        result = validate_proposal(proposal, self.root)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertTrue(any(e["code"] == "required_fields_missing" for e in result["errors"]))

    def test_wrong_digest_blocks(self):
        proposal = dict(self.proposal)
        proposal["evidence"] = [{"locator": "repo://evidence/test.txt", "sha256": "0" * 64}]
        result = validate_proposal(proposal, self.root)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertTrue(any(e["code"] == "evidence_sha256_mismatch" for e in result["errors"]))

    def test_missing_evidence_blocks(self):
        proposal = dict(self.proposal)
        proposal["evidence"] = [{"locator": "repo://evidence/missing.txt", "sha256": "0" * 64}]
        result = validate_proposal(proposal, self.root)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertTrue(any(e["code"] == "evidence_file_missing" for e in result["errors"]))

    def test_path_traversal_blocks(self):
        proposal = dict(self.proposal)
        proposal["evidence"] = [{"locator": "repo://../outside.txt", "sha256": self.digest}]
        result = validate_proposal(proposal, self.root)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertTrue(any(e["code"] == "evidence_path_escape" for e in result["errors"]))

    def test_protected_target_requires_owner_approval(self):
        proposal = dict(self.proposal)
        proposal["target_paths"] = ["docs/reference/REFERENCE-DOCUMENTS/master.md"]
        result = validate_proposal(proposal, self.root)
        self.assertIn("protected_architecture_targets_require_owner_approval", result["warnings"])
        self.assertFalse(result["promotion_allowed"])

    def test_integrated_without_owner_approval_blocks(self):
        proposal = dict(self.proposal)
        proposal["state"] = "INTEGRATED"
        result = validate_proposal(proposal, self.root)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertTrue(any(e["code"] == "integration_without_owner_approval" for e in result["errors"]))

    def test_approved_state_requires_explicit_decision(self):
        proposal = dict(self.proposal)
        proposal["state"] = "APPROVED"
        result = validate_proposal(proposal, self.root)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertTrue(any(e["code"] == "approved_state_without_owner_decision" for e in result["errors"]))

    def test_approved_proposal_still_does_not_mutate_canonical(self):
        proposal = dict(self.proposal)
        proposal["state"] = "APPROVED"
        proposal["owner_decision"] = "APPROVED"
        result = validate_proposal(proposal, self.root)
        self.assertEqual(result["status"], "APPROVAL_RECORDED")
        self.assertFalse(result["canonical_mutation_performed"])
        self.assertFalse(result["promotion_allowed"])

if __name__ == "__main__":
    unittest.main()
