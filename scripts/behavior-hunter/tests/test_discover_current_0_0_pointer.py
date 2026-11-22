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

    def test_historical_recovery_verifier_does_not_compete_with_live_overlay_pointer(self):
        manifest, verifier, portable, _ = inputs(verifier_id="CURRENT-109", portable_id="CURRENT-150.01")
        registry = {
            "0.0 registry": "> **CURRENT POINT-0++:** [CURRENT-150](docs/0.0/anchors/CURRENT-150.md)\n- CURRENT-065 remains current in an older historical note.",
            "integration queue": "## Current continuation pointer — POINT-0/GOLDEN / CURRENT-150 / NEXT-051",
            "reference index": "> **CURRENT POINT-0++:** [CURRENT-150](docs/0.0/anchors/CURRENT-150.md)",
        }
        result = MODULE.discover_from_texts(manifest, verifier, portable, registry)
        self.assertEqual(result["status"], "SCOPED_CONSISTENT")
        self.assertEqual(result["scopes"]["overlay_recovery_current"], ["CURRENT-066"])
        self.assertEqual(result["scopes"]["global_project_current"], ["CURRENT-150"])
        self.assertEqual(result["candidate_ids"], ["CURRENT-066", "CURRENT-150"])
        historical = [d for d in result["declarations"] if d["scope"] == "historical_recovery_test"]
        self.assertEqual([d["current_id"] for d in historical], ["CURRENT-109"])

    def test_decimal_revision_resolves_to_fixed_current_family(self):
        manifest, verifier, portable, _ = inputs(verifier_id="CURRENT-109", portable_id="CURRENT-150.01")
        registry = {
            "0.0 registry": "> **CURRENT POINT-0++:** [CURRENT-150.01](docs/0.0/anchors/PALANG-0.0-CURRENT-20261122-150-REVISION-01-STABLE-ANCHOR-IDENTITY-LOCK.md)",
            "integration queue": "## Current continuation pointer — POINT-0/GOLDEN / CURRENT-150.01 / NEXT-051.01",
            "reference index": "> **CURRENT POINT-0++:** [CURRENT-150.01](docs/0.0/anchors/PALANG-0.0-CURRENT-20261122-150-REVISION-01-STABLE-ANCHOR-IDENTITY-LOCK.md)",
        }
        result = MODULE.discover_from_texts(manifest, verifier, portable, registry)
        self.assertEqual(result["status"], "SCOPED_CONSISTENT")
        self.assertEqual(result["scopes"]["overlay_recovery_current"], ["CURRENT-066"])
        self.assertEqual(result["scopes"]["global_project_current"], ["CURRENT-150"])
        self.assertEqual(result["candidate_ids"], ["CURRENT-066", "CURRENT-150"])
        self.assertFalse(result["winner_selected"])

    def test_authoritative_registry_header_supersedes_older_live_claims(self):
        values = inputs()
        registry = {
            "0.0 registry": "> **CURRENT POINT-0++:** [CURRENT-150](docs/0.0/anchors/CURRENT-150.md)\\n- CURRENT-065 remains current; this is historical text.",
        }
        result = MODULE.discover_from_texts(values[0], values[1], values[2], registry)
        self.assertEqual(result["scopes"]["global_project_current"], ["CURRENT-150"])

    def test_missing_manifest_pointer_blocks(self):
        result = MODULE.discover_from_texts("{}", '"current": "docs/0.0/anchors/PALANG-0.0-CURRENT-066-TEST.md"',
                                             "- Current 0.0: [CURRENT-066](x)", {})
        self.assertEqual(result["status"], "BLOCKED")
        self.assertFalse(result["winner_selected"])

    def test_malformed_manifest_blocks(self):
        result = MODULE.discover_from_texts("{", '"current": "docs/0.0/anchors/PALANG-0.0-CURRENT-066-TEST.md"',
                                             "- Current 0.0: [CURRENT-066](x)", {})
        self.assertEqual(result["status"], "BLOCKED")


    def test_scoped_overlay_and_global_current_are_consistent(self):
        manifest, verifier, portable, _ = inputs()
        registry = {
            "0.0 registry": "- Current continuation: [CURRENT-072](docs/0.0/anchors/CURRENT-072.md)",
            "integration queue": "- Current point: [CURRENT-072](docs/0.0/anchors/CURRENT-072.md)",
            "reference index": "- Current continuation: [CURRENT-072](docs/0.0/anchors/CURRENT-072.md)",
        }
        result = MODULE.discover_from_texts(manifest, verifier, portable, registry)
        self.assertEqual(result["status"], "SCOPED_CONSISTENT")
        self.assertEqual(result["scopes"]["overlay_recovery_current"], ["CURRENT-066"])
        self.assertEqual(result["scopes"]["global_project_current"], ["CURRENT-072"])
        self.assertFalse(result["winner_selected"])

    def test_latest_live_claim_supersedes_historical_registry_claim(self):
        values = inputs()
        registry = {
            "0.0 registry": "- CURRENT-065 remains current; historical notes preserved.\n- Current continuation: CURRENT-072.",
            "integration queue": "- Current point: CURRENT-072.",
            "reference index": "- Current continuation: CURRENT-072.",
        }
        result = MODULE.discover_from_texts(values[0], values[1], values[2], registry)
        self.assertEqual(result["status"], "SCOPED_CONSISTENT")
        self.assertEqual(result["scopes"]["global_project_current"], ["CURRENT-072"])


if __name__ == "__main__":
    unittest.main()
