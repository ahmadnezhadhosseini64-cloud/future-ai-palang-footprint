import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from parent_edge_resolution import resolve_parent_target


class ParentEdgeResolutionTests(unittest.TestCase):
    def test_source_specific_override_wins_over_global_preference(self):
        source = "docs/0.0/IN.md"
        parent = "EVT-0091"
        candidates = ["event-a.md", "event-b.md"]
        resolution, selected, warning = resolve_parent_target(
            source, parent, candidates,
            {parent: "event-b.md"},
            {(source, parent): "event-a.md"},
        )
        self.assertEqual(resolution, "SOURCE_SPECIFIC_OVERRIDE")
        self.assertEqual(selected, "event-a.md")
        self.assertIsNone(warning)

    def test_invalid_source_override_stays_ambiguous(self):
        source = "docs/0.0/IN.md"
        parent = "EVT-0091"
        resolution, selected, warning = resolve_parent_target(
            source, parent, ["event-a.md", "event-b.md"],
            {parent: "event-b.md"},
            {(source, parent): "not-a-candidate.md"},
        )
        self.assertEqual(resolution, "AMBIGUOUS")
        self.assertIsNone(selected)
        self.assertEqual(warning["reason"], "source_specific_override_not_in_candidates")

    def test_global_preference_is_preserved_when_no_source_override(self):
        resolution, selected, warning = resolve_parent_target(
            "source.md", "MASTER-ID", ["event.md", "master.md"],
            {"MASTER-ID": "master.md"}, {},
        )
        self.assertEqual(resolution, "CANONICAL_PREFERRED_WITH_DUPLICATE_OCCURRENCES")
        self.assertEqual(selected, "master.md")
        self.assertIsNone(warning)

    def test_single_candidate_is_unique(self):
        resolution, selected, warning = resolve_parent_target(
            "source.md", "EVT-1", ["event.md"], {}, {},
        )
        self.assertEqual((resolution, selected, warning), ("UNIQUE", "event.md", None))

    def test_no_candidate_is_unresolved(self):
        resolution, selected, warning = resolve_parent_target(
            "source.md", "MISSING", [], {}, {},
        )
        self.assertEqual((resolution, selected, warning), ("UNRESOLVED", None, None))


if __name__ == "__main__":
    unittest.main()
