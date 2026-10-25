import importlib.util
import json
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "discover_current_0_0_pointer.py"
SPEC = importlib.util.spec_from_file_location("discover_pointer", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def inputs(manifest_id="CURRENT-066", verifier_id="CURRENT-066", portable_id="CURRENT-066", registry=""):
    manifest = json.dumps({"current_checkpoint": f"docs/0.0/anchors/PALANG-0.0-{manifest_id}-TEST.md"})
    verifier = f'"current": "docs/0.0/anchors/PALANG-0.0-{verifier_id}-TEST.md"'
    portable = f"- Current 0.0: [{portable_id}](docs/0.0/anchors/PALANG-0.0-{portable_id}-TEST.md)"
    return manifest, verifier, portable, {"0.0 registry": registry}


class PointerDiscoveryTests(unittest.TestCase):
    def test_consistent_explicit_declarations(self):
        values = inputs()
        result = MODULE.discover_from_texts(*values)
        self.assertEqual(result["status"], "CONSISTENT")
        self.assertEqual(result["candidate_ids"], ["CURRENT-066"])
        self.assertFalse(result["winner_selected"])

    def test_date_bearing_checkpoint_filenames_are_recognized(self):
        values = inputs(manifest_id="CURRENT-20261025-066", verifier_id="CURRENT-20261025-066", portable_id="CURRENT-20261025-066")
        result = MODULE.discover_from_texts(*values)
        self.assertEqual(result["status"], "CONSISTENT")
        self.assertEqual(result["candidate_ids"], ["CURRENT-066"])
        self.assertFalse(result["winner_selected"])

    def test_conflict_returns_ambiguous_without_winner(self):
        values = inputs(manifest_id="CURRENT-066", verifier_id="CURRENT-066",
                        portable_id="CURRENT-066",
                        registry="- CURRENT-065 remains current; NEXT-051 remains active.")
        result = MODULE.discover_from_texts(*values)
        self.assertEqual(result["status"], "AMBIGUOUS")
        self.assertEqual(result["candidate_ids"], ["CURRENT-065", "CURRENT-066"])
        self.assertFalse(result["winner_selected"])

    def test_historical_heading_is_not_live_claim(self):
        values = inputs(registry="## CURRENT-065 — historical checkpoint\n- Previous checkpoint preserved.")
        result = MODULE.discover_from_texts(*values)
        self.assertEqual(result["status"], "CONSISTENT")

    def test_missing_manifest_pointer_blocks(self):
        result = MODULE.discover_from_texts("{}", '"current": "docs/0.0/anchors/PALANG-0.0-CURRENT-066-TEST.md"',
                                             "- Current 0.0: [CURRENT-066](x)", {})
        self.assertEqual(result["status"], "BLOCKED")
        self.assertFalse(result["winner_selected"])

    def test_malformed_manifest_blocks(self):
        result = MODULE.discover_from_texts("{", '"current": "docs/0.0/anchors/PALANG-0.0-CURRENT-066-TEST.md"',
                                             "- Current 0.0: [CURRENT-066](x)", {})
        self.assertEqual(result["status"], "BLOCKED")


if __name__ == "__main__":
    unittest.main()
