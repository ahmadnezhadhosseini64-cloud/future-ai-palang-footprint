import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rewrite_living_master_links import rewrite_links


class LivingMasterLinkRewriteTests(unittest.TestCase):
    def test_rewrites_links_from_canonical_source_to_portable_mirror(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs/architecture/مدل اولیه AI").mkdir(parents=True)
            (root / "docs/0.0/anchors").mkdir(parents=True)
            (root / "docs/architecture/BEHAVIOR-TRACE").mkdir(parents=True)
            (root / "prototype/haif-gpt6-starter").mkdir(parents=True)
            (root / "docs/0.0/anchors/a.md").write_text("a", encoding="utf-8")
            (root / "docs/architecture/BEHAVIOR-TRACE/e.md").write_text("e", encoding="utf-8")
            source = "docs/architecture/مدل اولیه AI/mother.md"
            destination = "prototype/haif-gpt6-starter/LIVING_MASTER_REFERENCE.md"
            original = "[a](../../0.0/anchors/a.md) [e](../BEHAVIOR-TRACE/e.md) [web](https://example.com) [anchor](#section)"
            rewritten, report = rewrite_links(original, root, source, destination)
            self.assertIn("../../docs/0.0/anchors/a.md", rewritten)
            self.assertIn("../../docs/architecture/BEHAVIOR-TRACE/e.md", rewritten)
            self.assertIn("https://example.com", rewritten)
            self.assertIn("#section", rewritten)
            self.assertEqual(report["rewritten_links"], 2)
            self.assertEqual(report["unresolved_count"], 0)

    def test_missing_targets_are_reported_not_guessed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs/architecture/مدل اولیه AI").mkdir(parents=True)
            (root / "prototype/haif-gpt6-starter").mkdir(parents=True)
            source = "docs/architecture/مدل اولیه AI/mother.md"
            destination = "prototype/haif-gpt6-starter/LIVING_MASTER_REFERENCE.md"
            rewritten, report = rewrite_links("[missing](../../0.0/anchors/missing.md)", root, source, destination)
            self.assertEqual(rewritten, "[missing](../../0.0/anchors/missing.md)")
            self.assertEqual(report["unresolved_count"], 1)
            self.assertEqual(report["unresolved_links"][0]["reason"], "TARGET_NOT_FOUND")


if __name__ == "__main__":
    unittest.main()
