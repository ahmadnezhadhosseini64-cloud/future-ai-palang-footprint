import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from semantic_role_decisions import apply_role_decisions

class SemanticRoleDecisionTests(unittest.TestCase):
    def setUp(self):
        self.group = {"key": "SAME-ID", "paths": ["event.md", "reference.md"]}
        self.nodes = [
            {"path": "event.md", "sha256": "a" * 64},
            {"path": "reference.md", "sha256": "b" * 64},
        ]
        self.decision = {
            "decision_id": "D-001",
            "decision_type": "ROLE_ADJUDICATION",
            "identifier_value": "SAME-ID",
            "status": "ROLE-ADJUDICATED",
            "source_manifest_commit": "abc",
            "paths": [
                {"path": "event.md", "content_sha256": "a" * 64, "role": "EVENT_PROVENANCE"},
                {"path": "reference.md", "content_sha256": "b" * 64, "role": "CANONICAL_REFERENCE"},
            ],
            "rationale": "Distinct roles; same concept.",
            "evidence_refs": ["EVT-0128"],
            "preserve_history": True,
            "no_rename": True,
            "no_delete": True,
        }

    def test_valid_decision_is_applied_without_erasing_raw_group(self):
        groups, summary = apply_role_decisions([self.group], self.nodes, [self.decision])
        self.assertEqual(groups[0]["key"], "SAME-ID")
        self.assertEqual(groups[0]["paths"], ["event.md", "reference.md"])
        self.assertEqual(groups[0]["semantic_review"]["status"], "ROLE-ADJUDICATED")
        self.assertEqual(summary["groups_reviewed"], 1)
        self.assertEqual(summary["groups_unreviewed"], 0)

    def test_stale_source_hash_is_rejected(self):
        bad = dict(self.decision)
        bad["paths"] = [dict(x) for x in self.decision["paths"]]
        bad["paths"][0]["content_sha256"] = "0" * 64
        groups, summary = apply_role_decisions([self.group], self.nodes, [bad])
        self.assertEqual(groups[0]["semantic_review"]["status"], "UNREVIEWED")
        self.assertEqual(summary["groups_reviewed"], 0)
        self.assertEqual(summary["decisions_rejected"][0]["reason"], "source_hash_verification_failed")

    def test_path_set_mismatch_is_rejected(self):
        bad = dict(self.decision)
        bad["paths"] = [dict(self.decision["paths"][0])]
        groups, summary = apply_role_decisions([self.group], self.nodes, [bad])
        self.assertEqual(groups[0]["semantic_review"]["status"], "UNREVIEWED")
        self.assertEqual(summary["decisions_rejected"][0]["reason"], "path_set_mismatch")

    def test_wrong_identifier_does_not_apply(self):
        bad = dict(self.decision)
        bad["identifier_value"] = "OTHER-ID"
        groups, summary = apply_role_decisions([self.group], self.nodes, [bad])
        self.assertEqual(groups[0]["semantic_review"]["status"], "UNREVIEWED")
        self.assertEqual(summary["groups_reviewed"], 0)

    def test_wrong_identifier_type_does_not_apply(self):
        groups, summary = apply_role_decisions([self.group], self.nodes, [self.decision], "PRODUCTION_ID")
        self.assertEqual(groups[0]["semantic_review"]["status"], "UNREVIEWED")
        self.assertEqual(summary["groups_reviewed"], 0)

    def test_unreviewed_decision_is_not_promoted(self):
        bad = dict(self.decision)
        bad["status"] = "PROPOSED"
        groups, summary = apply_role_decisions([self.group], self.nodes, [bad])
        self.assertEqual(groups[0]["semantic_review"]["status"], "UNREVIEWED")
        self.assertEqual(summary["groups_reviewed"], 0)

if __name__ == "__main__":
    unittest.main()
