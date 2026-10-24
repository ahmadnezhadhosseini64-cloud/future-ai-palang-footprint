import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "behavior-hunter"))
from recover_interaction_graph import recover, discover_latest_pair, _event_id

class LatestPairRecoveryTests(unittest.TestCase):
    def build_repo(self, root, latest=31):
        anchor_root = root / "docs/0.0/anchors"
        trace_root = root / "docs/architecture/BEHAVIOR-TRACE"
        anchor_root.mkdir(parents=True, exist_ok=True)
        trace_root.mkdir(parents=True, exist_ok=True)
        for n in (30, latest):
            if n == 30 and latest == 30:
                continue
            pair_id = f"INT-20261024-{n:03d}"
            in_id, out_id = f"IN-{n:03d}", f"OUT-{n:03d}"
            next_id, event_id = f"NEXT-{n:03d}", f"EVT-{1200+n}"
            in_path = anchor_root / f"PALANG-0.0-IN-20261024-{n:03d}-TEST.md"
            out_path = anchor_root / f"PALANG-0.0-OUT-20261024-{n:03d}-TEST.md"
            in_path.write_text(
                f"# IN-{n:03d}\n- Production ID: {in_id}\n- Interaction pair ID: {pair_id}\n"
                f"- Paired output: [{out_id}](PALANG-0.0-OUT-20261024-{n:03d}-TEST.md)\n"
                f"- Result event: [{event_id}]({event_id}-TEST.md)\n"
                f"- Current checkpoint: [{next_id}](PALANG-0.0-NEXT-20261024-{n:03d}-TEST.md)\n",
                encoding="utf-8")
            out_path.write_text(
                f"# OUT-{n:03d}\n- Production ID: {out_id}\n- Interaction pair ID: {pair_id}\n"
                f"- Input: [{in_id}](PALANG-0.0-IN-20261024-{n:03d}-TEST.md)\n"
                f"- Event: [{event_id}](../../architecture/BEHAVIOR-TRACE/{event_id}-TEST.md)\n"
                f"- Current checkpoint: [{next_id}](PALANG-0.0-NEXT-20261024-{n:03d}-TEST.md)\n",
                encoding="utf-8")
            (trace_root / f"{event_id}-TEST.md").write_text(f"{in_id} {out_id} {next_id}", encoding="utf-8")
            (anchor_root / f"PALANG-0.0-NEXT-20261024-{n:03d}-TEST.md").write_text(f"{in_id} {out_id} {event_id}", encoding="utf-8")
        (root / "docs/reference/REFERENCE-DOCUMENTS").mkdir(parents=True, exist_ok=True)
        (root / "docs/reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md").write_text(
            f"IN-{latest:03d} OUT-{latest:03d} EVT-{1200+latest} NEXT-{latest:03d}", encoding="utf-8")
        (root / "docs/architecture/INTEGRATION-QUEUE").mkdir(parents=True, exist_ok=True)
        (root / "docs/architecture/INTEGRATION-QUEUE/README.md").write_text(
            f"IN-{latest:03d} OUT-{latest:03d} EVT-{1200+latest} NEXT-{latest:03d}", encoding="utf-8")
        (root / "data/interaction-pairs/evidence").mkdir(parents=True, exist_ok=True)
        (root / "data/interaction-pairs/evidence/EVT-0120-RESOLVER-SMOKE-EVIDENCE.txt").write_text("controlled evidence", encoding="utf-8")

    def test_discovers_latest_reciprocal_pair_instead_of_old_hardcoded_pair(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root, latest=31)
            pair, failures = discover_latest_pair(root)
        self.assertFalse(failures)
        self.assertEqual(pair["interaction_id"], "INT-20261024-031")
        self.assertEqual(pair["IN"]["id"], "IN-031")
        self.assertEqual(pair["OUT"]["id"], "OUT-031")

    def test_recovery_from_latest_input_anchor(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root, latest=31); result = recover("IN", root)
        self.assertEqual(result["status"], "RECOVERED", result.get("failures"))
        self.assertEqual(result["starting_anchor"], "IN-031")
        self.assertEqual(result["paired_anchor"], "OUT-031")
        self.assertEqual(result["interaction_id"], "INT-20261024-031")

    def test_recovery_from_latest_output_anchor(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root, latest=31); result = recover("OUT", root)
        self.assertEqual(result["status"], "RECOVERED")
        self.assertEqual(result["starting_anchor"], "OUT-031")
        self.assertEqual(result["paired_anchor"], "IN-031")

    def test_missing_reverse_pair_link_is_not_silently_recovered(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root, latest=31)
            out = root / "docs/0.0/anchors/PALANG-0.0-OUT-20261024-031-TEST.md"
            out.write_text(out.read_text(encoding="utf-8").replace("IN-031", "IN-999"), encoding="utf-8")
            result = recover("IN", root)
        self.assertEqual(result["status"], "BLOCKED", result.get("failures"))

    def test_current_master_reference_is_required(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root, latest=31)
            master = root / "docs/reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md"
            master.write_text("old reference only", encoding="utf-8")
            result = recover("IN", root)
        self.assertEqual(result["status"], "PARTIAL")
        self.assertTrue(any(x["node"] == "master" for x in result["failures"]))

    def test_external_capabilities_are_not_inferred(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); self.build_repo(root, latest=31); result = recover("IN", root)
        self.assertFalse(result["host_wide_capture_proven"])
        self.assertEqual(result["fresh_chatgpt_session_test"], "NOT RUN")
        self.assertFalse(result["external_persistence_proven"])
        self.assertIn("Issue #20", [x["id"] for x in result["open_gaps"]])
        self.assertIn("Issue #21", [x["id"] for x in result["open_gaps"]])

    def test_current_result_event_wins_over_prior_event_reference(self):
        text = (
            "- Previous event: [EVT-0130](./EVT-0130-prior.md)\n"
            "- Result event: [EVT-0131](./EVT-0131-current.md)\n"
        )
        self.assertEqual(_event_id(text), "EVT-0131")

    def test_event_label_without_markdown_link_is_supported(self):
        self.assertEqual(_event_id("- Event: EVT-0131"), "EVT-0131")

if __name__ == "__main__":
    unittest.main()
