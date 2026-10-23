import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "behavior-hunter"))
from recover_interaction_graph import recover, PAIR, NODES

class BidirectionalRecoveryTests(unittest.TestCase):
    def build_repo(self, root):
        paths = {spec["path"] for spec in PAIR.values()} | {spec["paired_path"] for spec in PAIR.values()} | set(NODES.values())
        for relative in paths:
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("", encoding="utf-8")
        (root / PAIR["IN"]["path"]).write_text("INT-20261023-026 OUT-026 EVT-0121", encoding="utf-8")
        (root / PAIR["OUT"]["path"]).write_text("INT-20261023-026 IN-026 EVT-0121", encoding="utf-8")
        (root / NODES["event"]).write_text("IN-026 OUT-026 EVT-0122", encoding="utf-8")
        (root / NODES["active_gate"]).write_text("IN-026 OUT-026 NEXT-024 CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md INTEGRATION-QUEUE/README.md EVT-0120-RESOLVER-SMOKE-EVIDENCE.txt", encoding="utf-8")
        (root / NODES["checkpoint"]).write_text("IN-026 OUT-026 EVT-0121 EVT-0122 Issue #20 Issue #21", encoding="utf-8")
        (root / NODES["master"]).write_text("EVT-0121 EVT-0122 IN-026 OUT-026", encoding="utf-8")
        (root / NODES["queue"]).write_text("EVT-0122 IN-026 OUT-026", encoding="utf-8")

    def test_recovery_from_input_anchor(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root); result = recover("IN", root)
        self.assertEqual(result["status"], "RECOVERED")
        self.assertEqual(result["paired_anchor"], "OUT-026")

    def test_recovery_from_output_anchor(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root); result = recover("OUT", root)
        self.assertEqual(result["status"], "RECOVERED")
        self.assertEqual(result["paired_anchor"], "IN-026")

    def test_missing_pair_file_is_partial(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root); (root / PAIR["OUT"]["path"]).unlink(); result = recover("IN", root)
        self.assertEqual(result["status"], "PARTIAL")
        self.assertTrue(any(x["reason"] == "missing_required_file" for x in result["failures"]))

    def test_missing_reverse_pair_link_is_partial(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root); (root / PAIR["OUT"]["path"]).write_text("INT-20261023-026 EVT-0121", encoding="utf-8"); result = recover("IN", root)
        self.assertTrue(any(x["reason"] == "reverse_pair_link_missing" for x in result["failures"]))

    def test_mismatched_pair_identity_is_partial(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root); (root / PAIR["OUT"]["path"]).write_text("INT-20261023-999 IN-026 EVT-0121", encoding="utf-8"); result = recover("IN", root)
        self.assertTrue(any(x["reason"] == "pair_identity_missing_or_mismatched" for x in result["failures"]))

    def test_stale_master_reference_is_partial(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root); (root / NODES["master"]).write_text("EVT-0121 IN-026 OUT-026", encoding="utf-8"); result = recover("OUT", root)
        self.assertTrue(any(x["node"] == "master" and x["reference"] == "EVT-0122" for x in result["failures"]))

    def test_missing_queue_reference_is_partial(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root); (root / NODES["queue"]).write_text("IN-026 OUT-026", encoding="utf-8"); result = recover("IN", root)
        self.assertTrue(any(x["node"] == "queue" for x in result["failures"]))

    def test_external_capabilities_are_not_inferred(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root); result = recover("IN", root)
        self.assertIn("Issue #20", [x["id"] for x in result["open_gaps"]])
        self.assertIn("Issue #21", [x["id"] for x in result["open_gaps"]])
        self.assertFalse(result["host_wide_capture_proven"])
        self.assertEqual(result["fresh_chatgpt_session_test"], "NOT RUN")
        self.assertFalse(result["external_persistence_proven"])

if __name__ == "__main__":
    unittest.main()
