import json
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from generate_candidate_tests import evaluate, generate

class BehaviorHunterTests(unittest.TestCase):
    def valid_record(self):
        return {
            "event_id": "EVT-TEST-001",
            "stable_id": "PALANG-TEST-001",
            "version": "1.0.0",
            "input": "Register and verify the result.",
            "output": "Repository read-back verified.",
            "evidence": [{"type": "repository_readback", "locator": "test-fixture"}],
            "destinations": {"Repository": "READ-BACK VERIFIED", "Library": "NOT VERIFIED"},
            "resume_pointer": "docs/architecture/BEHAVIOR-OBSERVATORY/",
            "expected_invariants": ["input_present", "output_present", "success_claims_have_evidence", "destination_states_explicit", "resume_pointer_present"]
        }

    def test_valid_pair_passes_definition_gate_but_is_not_execution_pass(self):
        rec = self.valid_record()
        self.assertEqual(evaluate(rec), [])

    def test_missing_output_is_rejected(self):
        rec = self.valid_record()
        rec["output"] = ""
        self.assertIn("required_field_missing:output", evaluate(rec))

    def test_success_claim_without_evidence_is_blocked(self):
        rec = self.valid_record()
        rec["evidence"] = []
        self.assertIn("success_claim_without_evidence", evaluate(rec))

    def test_destination_states_must_be_explicit_when_required(self):
        rec = self.valid_record()
        rec["destinations"] = {}
        self.assertIn("invariant_failed:destination_states_explicit", evaluate(rec))

    def test_generator_marks_candidate_not_pass(self):
        rec = self.valid_record()
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "pairs.jsonl"
            source.write_text(json.dumps(rec) + "\n", encoding="utf-8")
            report = generate(source)
        self.assertEqual(report["candidate_tests_generated"], 1)
        self.assertEqual(report["candidate_tests"][0]["status"], "CANDIDATE_READY")
        self.assertEqual(report["candidate_tests"][0]["execution_status"], "NOT_RUN")

if __name__ == "__main__":
    unittest.main()
