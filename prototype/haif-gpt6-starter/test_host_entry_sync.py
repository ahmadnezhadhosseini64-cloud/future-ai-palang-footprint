"""Keep the two canonical host-entry authority blocks byte-identical."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
START = "<!-- PALANG-HOST-ENTRY-CURRENT-AUTHORITY-BEGIN -->"
END = "<!-- PALANG-HOST-ENTRY-CURRENT-AUTHORITY-END -->"
FILES = (
    ROOT / "prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md",
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

    def test_current_authority_preserves_two_copy_boundaries(self):
        current = block(FILES[0])
        for required in (
            "POINT-0/GOLDEN", "CURRENT-145", "NEXT-051",
            "2c1f9fdc308e34b23be64153e8eec2c30f08a859",
            "palang-safe-copy-2-test-20261126",
            "NOT VERIFIED", "OWNER_REVIEW_ONLY",
            "MAIN، MASTER، GOLDEN یا Copy 1",
        ):
            self.assertIn(required, current)

    def test_previous_ci_is_scoped_to_its_exact_sha(self):
        current = block(FILES[0])
        self.assertIn("305605bfb16a8c71146c5c7d3348fae34b66ec01", current)
        self.assertIn("45807829545", current)
        self.assertIn("هر تغییر بعدی باید روی HEAD دقیق جدید دوباره CI شود", current)

if __name__ == "__main__":
    unittest.main(verbosity=2)
