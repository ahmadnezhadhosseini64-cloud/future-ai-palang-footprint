from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "host-bridge" / "build_bridge.py"
SPEC = importlib.util.spec_from_file_location("build_bridge", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class HostBridgeBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.output = self.root / "output"
        self.source.mkdir()
        for name in MODULE.ALLOWLIST:
            (self.source / name).write_text(f"safe:{name}\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_build_contains_only_allowlisted_files_and_manifest(self):
        (self.source / "PRIVATE-SECRET.md").write_text("must never publish", encoding="utf-8")
        (self.source / "nested").mkdir()
        (self.source / "nested" / "private.txt").write_text("must never publish", encoding="utf-8")
        manifest = MODULE.build(self.source, self.output)
        expected = set(MODULE.ALLOWLIST.values()) | {"manifest.json"}
        self.assertEqual({p.name for p in self.output.iterdir()}, expected)
        self.assertEqual(len(manifest["files"]), len(MODULE.ALLOWLIST))
        self.assertNotIn("PRIVATE-SECRET.md", {p.name for p in self.output.iterdir()})

    def test_manifest_hashes_match_published_files(self):
        manifest = MODULE.build(self.source, self.output)
        for record in manifest["files"]:
            self.assertEqual(
                MODULE.sha256(self.output / record["path"]),
                record["sha256"],
            )
        saved = json.loads((self.output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["schema"], "palang-host-bridge-manifest/1.0")

    def test_missing_allowlisted_file_fails_closed(self):
        (self.source / "CHARTER.md").unlink()
        with self.assertRaises(ValueError):
            MODULE.build(self.source, self.output)

    def test_symlink_allowlisted_file_fails_closed(self):
        target = self.root / "outside.txt"
        target.write_text("outside", encoding="utf-8")
        (self.source / "CHARTER.md").unlink()
        (self.source / "CHARTER.md").symlink_to(target)
        with self.assertRaises(ValueError):
            MODULE.build(self.source, self.output)


if __name__ == "__main__":
    unittest.main()
