"""Tests for reproducible packaging and secret/path exclusions."""
import hashlib
import tempfile
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "architecture"))
import unittest
import zipfile
from pathlib import Path

from build_canonical_zip import build_archive


class CanonicalZipTests(unittest.TestCase):
    def test_identical_source_builds_identical_bytes_and_sha(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/"src"; root.mkdir()
            (root/"z.txt").write_text("last\n",encoding="utf-8")
            (root/"a.txt").write_text("first\n",encoding="utf-8")
            out1=Path(td)/"one.zip"; out2=Path(td)/"two.zip"
            r1=build_archive(root,out1); r2=build_archive(root,out2)
            self.assertEqual(r1["sha256"],r2["sha256"])
            self.assertEqual(out1.read_bytes(),out2.read_bytes())
            self.assertEqual(r1["paths"],["a.txt","z.txt"])
            self.assertEqual(r1["sha256"],hashlib.sha256(out1.read_bytes()).hexdigest())

    def test_secret_and_generated_dirs_excluded(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/"src"; root.mkdir()
            (root/"good.md").write_text("keep")
            (root/".env").write_text("SECRET")
            (root/"private.key").write_text("SECRET")
            (root/".git").mkdir(); (root/".git"/"config").write_text("SECRET")
            (root/"__pycache__").mkdir(); (root/"__pycache__"/"junk.pyc").write_bytes(b"x")
            out=Path(td)/"pkg.zip"
            build_archive(root,out)
            with zipfile.ZipFile(out) as z:
                self.assertEqual(z.namelist(),["good.md"])

    def test_receipt_is_written_and_hash_matches_archive(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/"src"; root.mkdir(); (root/"x").write_text("ok")
            out=Path(td)/"bundle.zip"; receipt=Path(td)/"bundle.sha256.json"
            result=build_archive(root,out,receipt)
            self.assertTrue(receipt.exists())
            self.assertEqual(result["sha256"],__import__("json").loads(receipt.read_text())["sha256"])

    def test_symlink_directory_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/"src"; root.mkdir()
            target=Path(td)/"outside"; target.mkdir(); (target/"secret.txt").write_text("x")
            (root/"linked-dir").symlink_to(target, target_is_directory=True)
            with self.assertRaisesRegex(ValueError,"symlink rejected"):
                build_archive(root,Path(td)/"bundle.zip")

    def test_receipt_contains_per_file_hashes(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/"src"; root.mkdir(); (root/"f.txt").write_text("payload")
            result=build_archive(root,Path(td)/"archive.zip")
            self.assertEqual(result["files"][0]["sha256"],hashlib.sha256(b"payload").hexdigest())

    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/"src"; root.mkdir()
            target=Path(td)/"target"; target.write_text("data")
            (root/"escape").symlink_to(target)
            with self.assertRaisesRegex(ValueError,"symlink rejected"):
                build_archive(root,Path(td)/"bundle.zip")


if __name__ == "__main__":
    unittest.main()
