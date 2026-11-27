"""Keep the two current host-entry authority blocks byte-identical and aligned."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[2]
START = "<!-- PALANG-HOST-ENTRY-CURRENT-AUTHORITY-BEGIN -->"
END = "<!-- PALANG-HOST-ENTRY-CURRENT-AUTHORITY-END -->"
FILES = (
    ROOT / "prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md",
    ROOT / "prototype/haif-gpt6-starter/UNIVERSAL_AI_HOST_ENTRY_FA.md",
    ROOT / "prototype/universal-host/UNIVERSAL_AI_HOST_ENTRY_FA.md",
)


def block(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    assert text.count(START) == 1, f"{path}: expected one start marker"
    assert text.count(END) == 1, f"{path}: expected one end marker"
    return text.split(START, 1)[1].split(END, 1)[0].strip()


class HostEntrySynchronizationTests(unittest.TestCase):
    def test_both_host_entry_authority_blocks_match_exactly(self):
        self.assertEqual(block(FILES[0]), block(FILES[1]))
        self.assertEqual(block(FILES[0]), block(FILES[2]))

    def test_current_authority_defines_two_distinct_messages(self):
        current = block(FILES[0])
        self.assertIn("پیام اول — شناسایی میزبان", current)
        self.assertIn("پیام دوم — مأموریت محدود", current)
        self.assertIn("منتظر پیام دوم", current)
        self.assertIn("Copy 3", current)

    def test_host_write_scope_is_copy3_only(self):
        current = block(FILES[0])
        for required in (
            "POINT-0/GOLDEN",
            "palang-safe-copy-2-current-20261127",
            "فقط در همان Copy 3 بنویس",
            "PR پیشنهادی را به Copy 2 والد بده",
            "MAIN، Copy 1، Copy 2، MASTER، RAHM",
            "STALE",
            "SECURITY CANDIDATE",
        ):
            self.assertIn(required, current)

    def test_no_stale_old_copy2_baseline_or_old_pr_target(self):
        current = block(FILES[0])
        for stale in (
            "CURRENT-145",
            "2c1f9fdc308e34b23be64153e8eec2c30f08a859",
            "palang-safe-copy-2-test-20261126",
            "PR #171",
        ):
            self.assertNotIn(stale, current)

    def test_manifest_points_to_the_two_message_copy3_contract(self):
        manifest = json.loads((ROOT / "prototype/haif-gpt6-starter/manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["host_entry_mode"], "TWO_MESSAGE_OWNER_GOVERNED")
        self.assertIn("Copy 3", manifest["copy3_model"])
        self.assertEqual(manifest["host_entry_sync_test"], "test_host_entry_sync.py")

    def test_current_copy2_sha_is_pinned_as_a_full_commit(self):
        current = block(FILES[0])
        self.assertIn("exact SHA زنده و پذیرفته‌شدهٔ Copy 2", current)


if __name__ == "__main__":
    unittest.main(verbosity=2)
