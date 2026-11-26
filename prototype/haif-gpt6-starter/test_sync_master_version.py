import json
import tempfile
import unittest
from pathlib import Path
from sync_master_version import extract_version, synchronize

class MasterVersionSyncTests(unittest.TestCase):
    def test_version_bump_updates_exact_mother_and_manifest_without_changing_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "canonical.md"
            target = root / "starter.md"
            manifest_path = root / "manifest.json"
            source_bytes = "## نسخهٔ 1.7.99 — test\nمتن مادر\n".encode("utf-8")
            source.write_bytes(source_bytes)
            target.write_bytes(b"old mother")
            original = {"stable_id":"STABLE-001","production_id":"PROD-001","current_living_master_version":"1.7.98"}
            manifest_path.write_text(json.dumps(original),encoding="utf-8")
            receipt = synchronize(source,target,manifest_path)
            current = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(receipt["status"],"SYNCED_AND_READBACK_VERIFIED")
            self.assertEqual(target.read_bytes(),source_bytes)
            self.assertEqual(current["current_living_master_version"],"1.7.99")
            self.assertEqual(current["stable_id"],"STABLE-001")
            self.assertEqual(current["production_id"],"PROD-001")

    def test_bad_source_version_fails_without_mutating_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/"source.md"; target=root/"target.md"; manifest=root/"manifest.json"
            source.write_text("not a version heading\n",encoding="utf-8")
            target.write_bytes(b"baseline")
            original=b'{"stable_id":"S","production_id":"P","current_living_master_version":"1.7.98"}'
            manifest.write_bytes(original)
            with self.assertRaises(ValueError): synchronize(source,target,manifest)
            self.assertEqual(target.read_bytes(),b"baseline")
            self.assertEqual(manifest.read_bytes(),original)

    def test_missing_stable_identity_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/"source.md"; target=root/"target.md"; manifest=root/"manifest.json"
            source.write_text("## نسخهٔ 1.7.99 — test\n",encoding="utf-8")
            target.write_bytes(b"baseline")
            original=b'{"current_living_master_version":"1.7.98"}'
            manifest.write_bytes(original)
            with self.assertRaises(ValueError): synchronize(source,target,manifest)
            self.assertEqual(target.read_bytes(),b"baseline")
            self.assertEqual(manifest.read_bytes(),original)

    def test_extract_version_rejects_invalid_utf8(self):
        with self.assertRaises(ValueError): extract_version(b"\\xff")

if __name__ == "__main__":
    unittest.main(verbosity=2)
