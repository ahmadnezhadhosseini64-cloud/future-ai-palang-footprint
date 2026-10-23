import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "behavior-hunter"))
from resolve_evidence_locators import resolve_record


class RepositoryColdStartRecoveryTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_next024_reconstructs_master_queue_event_and_next_action(self):
        checkpoint_path = "docs/0.0/anchors/PALANG-0.0-NEXT-20261023-024-CONTINUITY-HISTORIC-AND-COLD-START.md"
        checkpoint = self.read(checkpoint_path)
        master_path = "docs/reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md"
        queue_path = "docs/architecture/INTEGRATION-QUEUE/README.md"
        event_path = "docs/architecture/BEHAVIOR-TRACE/EVT-0120-EVIDENCE-LOCATOR-RESOLUTION-AND-COLD-RECOVERY-2026-10-23.md"
        master = self.read(master_path)
        queue = self.read(queue_path)
        event = self.read(event_path)

        self.assertIn("../../reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md", checkpoint)
        self.assertIn("../../architecture/INTEGRATION-QUEUE/README.md", checkpoint)
        self.assertIn("../../architecture/BEHAVIOR-TRACE/EVT-0120-EVIDENCE-LOCATOR-RESOLUTION-AND-COLD-RECOVERY-2026-10-23.md", checkpoint)
        self.assertIn("EVT-0120", master)
        self.assertIn("PALANG-COLD-START-RECOVERY-FROM-NEXT-024-2026-10-23-001", queue)
        self.assertIn("40002313474", event)
        self.assertIn("scripts/behavior-hunter/resolve_evidence_locators.py", event)
        self.assertIn("fresh-session recovery", checkpoint.lower())

    def test_smoke_evidence_resolves_without_promoting_not_run_to_pass(self):
        input_path = ROOT / "data/interaction-pairs/evidence-resolution-production-smoke.jsonl"
        record = json.loads(input_path.read_text(encoding="utf-8").splitlines()[0])
        result = resolve_record(record, ROOT, source_mode="production")
        self.assertEqual(record["test_result"], "NOT RUN")
        self.assertEqual(result["status"], "RESOLVED")
        self.assertTrue(result["evidence_integrity_verified"])
        self.assertFalse(result["production_claim_allowed"])

    def test_previous_zero_anchors_and_successor_checkpoint_are_preserved(self):
        paths = [
            "docs/0.0/anchors/PALANG-0.0-CURRENT-20261023-023-USER-CHECKPOINT-AND-CONTINUATION.md",
            "docs/0.0/anchors/PALANG-0.0-NEXT-20261023-022-HISTORIC-SOURCE-GRAPH-EXCAVATION.md",
            "docs/0.0/anchors/PALANG-0.0-NEXT-20261023-023-CONTINUITY-AND-OPEN-WORK.md",
            "docs/0.0/anchors/PALANG-0.0-NEXT-20261023-024-CONTINUITY-HISTORIC-AND-COLD-START.md",
            "docs/0.0/anchors/PALANG-0.0-NEXT-20261023-025-SOURCE-RULE-TEST-CROSSWALK-AND-COLD-START.md",
            "docs/0.0/anchors/PALANG-0.0-IN-20261023-025-STATUS-AND-VISIBLE-CONTINUATION.md",
            "docs/0.0/anchors/PALANG-0.0-OUT-20261023-025-STATUS-AND-VISIBLE-CONTINUATION.md",
        ]
        for relative in paths:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_current_request_anchors_and_active_successor_are_linked(self):
        input_anchor = self.read("docs/0.0/anchors/PALANG-0.0-IN-20261023-026-REGISTER-ACTIVE-CONTINUATION.md")
        output_anchor = self.read("docs/0.0/anchors/PALANG-0.0-OUT-20261023-026-REGISTER-ACTIVE-CONTINUATION.md")
        event = self.read("docs/architecture/BEHAVIOR-TRACE/EVT-0121-REGISTER-ACTIVE-CONTINUATION-AND-COLD-START-RESULT-2026-10-23.md")
        successor = self.read("docs/architecture/BEHAVIOR-TRACE/EVT-0122-BIDIRECTIONAL-IN-OUT-RECOVERY-2026-10-23.md")
        checkpoint = self.read("docs/0.0/anchors/PALANG-0.0-NEXT-20261023-024-CONTINUITY-HISTORIC-AND-COLD-START.md")
        master = self.read("docs/reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md")
        queue = self.read("docs/architecture/INTEGRATION-QUEUE/README.md")

        self.assertIn("OUT-026", input_anchor)
        self.assertIn("Paired output:", input_anchor)
        self.assertIn("IN-026", output_anchor)
        self.assertIn("EVT-0121", input_anchor)
        self.assertIn("EVT-0121", output_anchor)
        self.assertIn("IN-026", event)
        self.assertIn("OUT-026", event)
        self.assertIn("EVT-0122", event)
        self.assertIn("ACTIVE / LIVING / IMPLEMENTED-IN-REPOSITORY", successor)
        self.assertIn("FRESH-SESSION-NOT-RUN", successor)
        self.assertIn("IN-026", checkpoint)
        self.assertIn("OUT-026", checkpoint)
        self.assertIn("EVT-0121", checkpoint)
        self.assertIn("EVT-0122", checkpoint)
        self.assertIn("EVT-0121", master)
        self.assertIn("EVT-0122", master)
        self.assertIn("PALANG-BIDIRECTIONAL-IN-OUT-RECOVERY-2026-10-23-001", queue)

    def test_checkpoint_declares_open_historical_and_host_capture_gates(self):
        checkpoint = self.read("docs/0.0/anchors/PALANG-0.0-NEXT-20261023-024-CONTINUITY-HISTORIC-AND-COLD-START.md")
        self.assertIn("Issue #21", checkpoint)
        self.assertIn("Issue #20", checkpoint)
        self.assertIn("OPEN", checkpoint)
        self.assertIn("host-wide", checkpoint.lower())


if __name__ == "__main__":
    unittest.main()
