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
            "version": "1.0.0",
            "test_id": "T-01",
            "test_result": result,
            "architecture_domain": "recovery",
            "observation": "Resume pointer state was observed.",
            "evidence": [{
                "type": "test_log",
                "locator": "artifact://ci/run-117/test-log",
                "execution_id": "ci-run-117",
                "source_sha": "0123456789abcdef0123456789abcdef01234567",\n                "content_sha256": "a" * 64,
            }] if result == "PASS" else [],
            "counterexamples": [],
        }

    def test_pass_creates_proposed_candidate_not_verified_or_master(self):
        out = extract(self.record("PASS"), 1)
        self.assertEqual(out["kind"], "PATTERN_CANDIDATE")
        self.assertEqual(out["status"], "PROPOSED")
        self.assertFalse(out["master_mutation"])
        self.assertEqual(out["promotion"], "OWNER_REVIEW_REQUIRED")
        self.assertEqual(out["source_mode"], "PRODUCTION_CANDIDATE")

    def test_fail_creates_regression_candidate(self):
        self.assertEqual(extract(self.record("FAIL"), 1)["kind"], "REGRESSION_OR_ANTIPATTERN_CANDIDATE")

    def test_blocked_creates_architecture_gap(self):
        self.assertEqual(extract(self.record("BLOCKED"), 1)["kind"], "ARCHITECTURE_GAP_CANDIDATE")

    def test_not_run_creates_evidence_gap_not_success(self):
        out = extract(self.record("NOT RUN"), 1)
        self.assertEqual(out["kind"], "EVIDENCE_GAP_CANDIDATE")
        self.assertNotEqual(out["test_result"], "PASS")

    def test_pass_without_evidence_is_rejected(self):
        out = extract(self.record("PASS") | {"evidence": []}, 1)
        self.assertEqual(out["status"], "REJECTED_INPUT")
        self.assertIn("pass_without_evidence", out["issues"])

    def test_pass_evidence_missing_execution_provenance_is_rejected(self):
        evidence = [{"type": "test_log", "locator": "artifact://ci/run-117/log"}]
        out = extract(self.record("PASS") | {"evidence": evidence}, 1)
        self.assertIn("evidence[0]_missing_execution_id", out["issues"])
        self.assertIn("evidence[0]_missing_source_sha", out["issues"])

    def test_invalid_evidence_source_sha_and_locator_are_rejected(self):
        evidence = [{
            "type": "test_log", "locator": "not-a-uri-or-path",
            "execution_id": "ci-run-117", "source_sha": "not-a-sha"
        }]
        out = extract(self.record("PASS") | {"evidence": evidence}, 1)
        self.assertIn("evidence[0]_invalid_source_sha_format", out["issues"])
        self.assertIn("evidence[0]_locator_must_be_uri_or_path", out["issues"])

    def test_missing_content_sha256_is_rejected_for_production_pass(self):
        evidence = [{
            "type": "test_log", "locator": "artifact://ci/run-117/log",
            "execution_id": "ci-run-117", "source_sha": "0123456789abcdef0123456789abcdef01234567"
        }]
        out = extract(self.record("PASS") | {"evidence": evidence}, 1)
        self.assertIn("evidence[0]_missing_content_sha256", out["issues"])

    def test_placeholder_evidence_is_rejected_in_production(self):
        evidence = [{
            "type": "test_log", "locator": "example:fake-log",
            "execution_id": "ci-run-117", "source_sha": "0123456789abcdef0123456789abcdef01234567"
        }]
        out = extract(self.record("PASS") | {"evidence": evidence}, 1)
        self.assertIn("evidence[0]_placeholder_locator_not_allowed_in_production", out["issues"])

    def test_missing_test_id_and_version_are_rejected(self):
        record = self.record("FAIL")
        record.pop("test_id")
        record.pop("version")
        out = extract(record, 1)
        self.assertIn("required_field_missing:test_id", out["issues"])
        self.assertIn("required_field_missing:version", out["issues"])

    def test_invalid_domain_and_counterexamples_are_rejected(self):
        out = extract(self.record("FAIL") | {"architecture_domain": "made_up"}, 1)
        self.assertIn("unknown_architecture_domain:made_up", out["issues"])
        out2 = extract(self.record("FAIL") | {"counterexamples": "not-a-list"}, 1)
        self.assertIn("counterexamples_must_be_list_of_strings", out2["issues"])

    def test_fixture_mode_is_never_promoted(self):
        record = self.record("PASS")
        record["evidence"] = [{"type": "test_log", "locator": "example:illustration"}]
        out = extract(record, 1, source_mode="fixture")
        self.assertEqual(out["source_mode"], "FIXTURE_ONLY")
        self.assertEqual(out["status"], "DEMONSTRATION_ONLY")
        self.assertEqual(out["promotion"], "NONE_FIXTURE_ONLY")
        self.assertFalse(out["master_mutation"])

    def test_duplicate_event_test_pair_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "outcomes.jsonl"
            rec = self.record("FAIL")
            source.write_text("\n".join(json.dumps(rec) for _ in range(2)) + "\n", encoding="utf-8")
            report = generate(source)
        self.assertEqual(report["records_proposed"], 1)
        self.assertEqual(report["duplicate_records_rejected"], 1)

    def test_malformed_json_and_non_object_are_reported(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "outcomes.jsonl"
            source.write_text('{"bad":\n[]\n', encoding="utf-8")
            report = generate(source)
        self.assertEqual(len(report["parse_errors"]), 1)
        self.assertEqual(report["records_rejected"], 1)

    def test_fixture_manifest_is_explicitly_demonstration_only(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "outcomes.jsonl"
            rec = self.record("PASS")
            rec["evidence"] = [{"type": "test_log", "locator": "example:illustration"}]
            source.write_text(json.dumps(rec) + "\n", encoding="utf-8")
            report = generate(source, source_mode="fixture")
        self.assertEqual(report["source_mode"], "FIXTURE_ONLY")
        self.assertEqual(report["proposals"][0]["status"], "DEMONSTRATION_ONLY")

    def test_manifest_keeps_source_ids_and_never_promotes_master(self):
        with tempfile.TemporaryDirectory() as td:
            source = Path(td) / "outcomes.jsonl"
            records = []
            for outcome in ("PASS", "FAIL", "BLOCKED", "NOT RUN"):
                rec = self.record(outcome)
                rec["test_id"] = "T-" + outcome.replace(" ", "-")
                records.append(json.dumps(rec))
            source.write_text("\n".join(records) + "\n", encoding="utf-8")
            report = generate(source)
        self.assertEqual(report["records_proposed"], 4)
        self.assertEqual(report["records_rejected"], 0)
        self.assertTrue(all(p["source_event_id"] == "EVT-TEST-117" for p in report["proposals"]))
        self.assertTrue(all(p["master_mutation"] is False for p in report["proposals"]))
        self.assertEqual(len({p["insight_id"] for p in report["proposals"]}), 4)


if __name__ == "__main__":
    unittest.main()
