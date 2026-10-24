import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "behavior-hunter"))
from check_living_graph_drift import check_graph

class LivingGraphDriftTests(unittest.TestCase):
    def build_repo(self, root):
        anchors = root / "docs/0.0/anchors"
        trace = root / "docs/architecture/BEHAVIOR-TRACE"
        receipts = trace / "STATUS-RECEIPTS"
        for p in (anchors, trace, receipts, root / "docs/reference/REFERENCE-DOCUMENTS",
                  root / "docs/architecture/INTEGRATION-QUEUE",
                  root / "docs/architecture/BEHAVIOR-OBSERVATORY"):
            p.mkdir(parents=True, exist_ok=True)
        (anchors / "PALANG-0.0-IN-20261024-033-TEST.md").write_text(
            "- Production ID: IN-033\n- Interaction pair ID: INT-20261024-033\n"
            "- Paired output: OUT-033\n- Result event: [EVT-0131](EVT-0131-TEST.md)\n"
            "- Current checkpoint: NEXT-033\n", encoding="utf-8")
        (anchors / "PALANG-0.0-OUT-20261024-033-TEST.md").write_text(
            "- Production ID: OUT-033\n- Interaction pair ID: INT-20261024-033\n"
            "- Input: IN-033\n- Event: [EVT-0131](EVT-0131-TEST.md)\n"
            "- Current checkpoint: NEXT-033\n", encoding="utf-8")
        (anchors / "PALANG-0.0-NEXT-20261024-033-TEST.md").write_text(
            "IN-033 OUT-033 EVT-0131 NEXT-033", encoding="utf-8")
        (trace / "EVT-0131-TEST.md").write_text(
            "IN-033 OUT-033 NEXT-033", encoding="utf-8")
        (root / "docs/reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md").write_text(
            "IN-033 OUT-033 EVT-0131 NEXT-033", encoding="utf-8")
        (root / "docs/architecture/INTEGRATION-QUEUE/README.md").write_text(
            "IN-033 OUT-033 EVT-0131 NEXT-033", encoding="utf-8")
        (root / "docs/REFERENCE_INDEX.md").write_text("IN-033 OUT-033 EVT-0131 NEXT-033", encoding="utf-8")
        (root / "docs/0.0/README.md").write_text("IN-033 OUT-033 EVT-0131 NEXT-033", encoding="utf-8")
        (trace / "README.md").write_text("IN-033 OUT-033 EVT-0131 NEXT-033", encoding="utf-8")
        (root / "docs/architecture/BEHAVIOR-OBSERVATORY/README.md").write_text(
            "IN-033 OUT-033 EVT-0131 NEXT-033", encoding="utf-8")
        receipt = {"event_id":"EVT-0131","interaction_pair_id":"INT-20261024-033",
                   "status":"SUCCESS","workflow_run_id":"test-run","tested_commit_sha":"abc"}
        (receipts / "STATUS-TEST.json").write_text(json.dumps(receipt), encoding="utf-8")
        evidence = root / "data/interaction-pairs/evidence/EVT-0120-RESOLVER-SMOKE-EVIDENCE.txt"
        evidence.parent.mkdir(parents=True, exist_ok=True)
        evidence.write_text("evidence", encoding="utf-8")

    def test_current_graph_passes_when_all_links_exist(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); self.build_repo(root); report=check_graph(root)
        self.assertEqual(report["status"], "PASS", report["failures"])
        self.assertEqual(report["recovery_from_IN"], "RECOVERED")
        self.assertEqual(report["recovery_from_OUT"], "RECOVERED")
        self.assertFalse(report["canonical_mutation_performed"])

    def test_missing_master_link_is_reported_as_drift(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); self.build_repo(root)
            (root / "docs/reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md").write_text("IN-033 only", encoding="utf-8")
            report=check_graph(root)
        self.assertEqual(report["status"], "DRIFT_DETECTED")
        self.assertTrue(any(x.get("check")=="master" for x in report["failures"]))

    def test_missing_durable_receipt_is_reported(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); self.build_repo(root)
            for p in (root/"docs/architecture/BEHAVIOR-TRACE/STATUS-RECEIPTS").glob("*.json"):
                p.unlink()
            report=check_graph(root)
        self.assertEqual(report["status"], "DRIFT_DETECTED")
        self.assertTrue(any(x.get("check")=="durable_status_receipt" for x in report["failures"]))

if __name__ == "__main__":
    unittest.main()
