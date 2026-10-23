import json
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "behavior-hunter"))
from extract_architecture_insights import extract, generate

class ArchitectureInsightTests(unittest.TestCase):
    def record(self, result="PASS"):
        return {
            "event_id": "EVT-TEST-117",
            "stable_id": "PALANG-TEST-117",
            "test_id": "T-01",
            "test_result": result,
            "architecture_domain": "recovery",
            "observation": "Resume pointer absent after restart.",
            "evidence": [{"type": "test_log", "locator": "fixture.log"}] if result == "PASS" else [],
            "counterexamples": []
        }

    def test_pass_creates_pattern_candidate_but_not_verified_or_master(self):
        out = extract(self.record("PASS"), 1)
        self.assertEqual(out["kind"], "PATTERN_CANDIDATE")
        self.assertEqual(out["status"], "PROPOSED")
        self.assertFalse(out["master_mutation"])
        self.assertEqual(out["promotion"], "OWNER_REVIEW_REQUIRED")

    def test_fail_creates_regression_candidate(self):
        out = extract(self.record("FAIL"), 1)
        self.assertEqual(out["kind"], "REGRESSION_OR_ANTIPATTERN_CANDIDATE")

    def test_blocked_creates_architecture_gap(self):
        out = extract(self.record("BLOCKED"), 1)
        self.assertEqual(out["kind"], "ARCHITECTURE_GAP_CANDIDATE")

    def test_not_run_creates_evidence_gap_not_success(self):
        out = extract(self.record("NOT RUN"), 1)
        self.assertEqual(out["kind"], "EVIDENCE_GAP_CANDIDATE")
        self.assertNotEqual(out["test_result"], "PASS")

    def test_pass_without_evidence_is_rejected(self):
        out = extract(self.record("PASS") | {"evidence": []}, 1)
        self.assertEqual(out["status"], "REJECTED_INPUT")
        self.assertIn("pass_without_evidence", out["issues"])

    def test_unknown_domain_is_rejected(self):
        out = extract(self.record("FAIL") | {"architecture_domain": "made_up"}, 1)
        self.assertEqual(out["status"], "REJECTED_INPUT")

    def test_manifest_keeps_source_event_and_never_promotes_master(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "outcomes.jsonl"
            source.write_text("\n".join(json.dumps(self.record(x)) for x in ("PASS", "FAIL", "BLOCKED", "NOT RUN")) + "\n", encoding="utf-8")
            report = generate(source)
        self.assertEqual(report["records_proposed"], 4)
        self.assertEqual(report["records_rejected"], 0)
        self.assertTrue(all(p["source_event_id"] == "EVT-TEST-117" for p in report["proposals"]))
        self.assertTrue(all(p["master_mutation"] is False for p in report["proposals"]))

if __name__ == "__main__":
    unittest.main()
