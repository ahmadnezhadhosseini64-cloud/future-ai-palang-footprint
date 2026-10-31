import importlib.util
from pathlib import Path
import tempfile
from unittest.mock import patch
import unittest

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "verify_latest_current_0_0_chain.py"
SPEC = importlib.util.spec_from_file_location("latest_chain_verifier", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class LatestChainParserTests(unittest.TestCase):
    def test_parses_latest_global_chain_and_all_six_links(self):
        fixture = """## تازه‌ترین زنجیره — POINT-0/061 → CURRENT-111

[POINT-0/061](anchors/point.md) → [IN-099](anchors/in.md) → [OUT-098](anchors/out.md) → [EVT-0240](../architecture/BEHAVIOR-TRACE/event.md) → [CURRENT-111](anchors/current.md) → [NEXT-051](anchors/next.md).

## Mirror event
[EVT-0241](../architecture/BEHAVIOR-TRACE/mirror.md)
"""
        chain = MODULE.parse_latest_chain(fixture)
        self.assertEqual(chain["labels"], {
            "point":"POINT-0/061","input":"IN-099","output":"OUT-098",
            "event":"EVT-0240","current":"CURRENT-111","next":"NEXT-051"
        })
        self.assertEqual(chain["targets"]["next"],"anchors/next.md")

    def test_uses_last_latest_chain_heading(self):
        fixture = """## تازه‌ترین زنجیره — POINT-0/060 → CURRENT-110
[POINT-0/060](old-point.md) → [IN-098](old-in.md) → [OUT-097](old-out.md) → [EVT-0237](old-event.md) → [CURRENT-110](old-current.md) → [NEXT-051](next.md).

## زنجیرهٔ پیشین
historical material

## تازه‌ترین زنجیره — POINT-0/061 → CURRENT-111
[POINT-0/061](point.md) → [IN-099](in.md) → [OUT-098](out.md) → [EVT-0240](event.md) → [CURRENT-111](current.md) → [NEXT-051](next.md).
"""
        chain = MODULE.parse_latest_chain(fixture)
        self.assertEqual(chain["labels"]["point"],"POINT-0/061")
        self.assertEqual(chain["labels"]["current"],"CURRENT-111")


    def test_accepts_repeated_navigation_links_to_the_same_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "docs" / "0.0" / "anchors"
            folder.mkdir(parents=True)
            source = folder / "source.md"
            target = folder / "target.md"
            source.write_text("source", encoding="utf-8")
            target.write_text("target", encoding="utf-8")
            body = "[first](target.md)\\n[second](./target.md)"
            with patch.object(MODULE, "ROOT", root):
                self.assertEqual(MODULE.require_one_link(source, body, "target.md"), "target.md")

    def test_rejects_same_name_links_to_different_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "docs" / "0.0" / "anchors"
            other = root / "docs" / "other"
            folder.mkdir(parents=True)
            other.mkdir(parents=True)
            source = folder / "source.md"
            (folder / "target.md").write_text("a", encoding="utf-8")
            (other / "target.md").write_text("b", encoding="utf-8")
            source.write_text("source", encoding="utf-8")
            body = "[first](target.md)\\n[second](../../other/target.md)"
            with patch.object(MODULE, "ROOT", root):
                with self.assertRaises(ValueError):
                    MODULE.require_one_link(source, body, "target.md")

    def test_rejects_unlinked_next_queue(self):
        fixture = """## تازه‌ترین زنجیره — POINT-0/061 → CURRENT-111
[POINT-0/061](point.md) → [IN-099](in.md) → [OUT-098](out.md) → [EVT-0240](event.md) → [CURRENT-111](current.md) → NEXT-051.
"""
        with self.assertRaises(ValueError):
            MODULE.parse_latest_chain(fixture)


if __name__ == "__main__":
    unittest.main()
