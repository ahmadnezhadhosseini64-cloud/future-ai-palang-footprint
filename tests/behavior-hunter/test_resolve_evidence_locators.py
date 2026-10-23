import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "behavior-hunter"))
from resolve_evidence_locators import generate, resolve_locator, resolve_record


class EvidenceLocatorResolverTests(unittest.TestCase):
    def test_resolves_repo_file_when_sha256_matches(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            target = root / "evidence.txt"
            target.write_text("immutable evidence\n", encoding="utf-8")
            digest = hashlib.sha256(target.read_bytes()).hexdigest()
            result = resolve_locator("repo://evidence.txt", digest, root)
        self.assertEqual(result["status"], "RESOLVED")
        self.assertEqual(result["content_sha256"], digest)

    def test_hash_mismatch_is_not_resolved(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "evidence.txt").write_text("actual bytes", encoding="utf-8")
            result = resolve_locator("repo://evidence.txt", "0" * 64, root)
        self.assertEqual(result["status"], "HASH_MISMATCH")

    def test_missing_file_is_unresolved(self):
        with tempfile.TemporaryDirectory() as td:
            result = resolve_locator("repo://missing.txt", "0" * 64, td)
        self.assertEqual(result["status"], "UNRESOLVED")

    def test_parent_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            result = resolve_locator("repo://../outside.txt", "0" * 64, td)
        self.assertEqual(result["status"], "UNRESOLVED")
        self.assertEqual(result["reason"], "unsafe_relative_path")

    def test_absolute_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            result = resolve_locator("repo:///tmp/outside.txt", "0" * 64, td)
        self.assertEqual(result["status"], "UNRESOLVED")

    def test_symlink_escape_is_rejected_when_supported(self):
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as outside:
            outside_file = Path(outside) / "outside.txt"
            outside_file.write_text("secret", encoding="utf-8")
            link = Path(td) / "escape.txt"
            try:
                link.symlink_to(outside_file)
            except (OSError, NotImplementedError):
                self.skipTest("symlink creation is not supported")
            digest = hashlib.sha256(outside_file.read_bytes()).hexdigest()
            result = resolve_locator("repo://escape.txt", digest, td)
        self.assertEqual(result["status"], "UNRESOLVED")
        self.assertEqual(result["reason"], "path_escapes_repository_root")

    def test_external_url_is_explicitly_unsupported(self):
        with tempfile.TemporaryDirectory() as td:
            result = resolve_locator("https://example.org/evidence", "0" * 64, td)
        self.assertEqual(result["status"], "UNSUPPORTED_LOCATOR")

    def test_missing_or_malformed_content_sha_is_unresolved(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "evidence.txt").write_text("evidence", encoding="utf-8")
            result = resolve_locator("repo://evidence.txt", "not-a-sha", root)
        self.assertEqual(result["status"], "UNRESOLVED")
        self.assertEqual(result["reason"], "invalid_or_missing_content_sha256")

    def test_fixture_mode_never_resolves_or_promotes(self):
        record = {"event_id": "EVT-FIXTURE", "test_id": "T-FIXTURE", "test_result": "PASS",
                  "evidence": [{"locator": "example:placeholder", "content_sha256": "0" * 64}]}
        result = resolve_record(record, ".", source_mode="fixture")
        self.assertEqual(result["status"], "FIXTURE_ONLY")
        self.assertFalse(result["production_claim_allowed"])

    def test_pass_without_evidence_is_unresolved(self):
        record = {"event_id": "EVT-PASS", "test_id": "T-PASS", "test_result": "PASS", "evidence": []}
        result = resolve_record(record, ".")
        self.assertEqual(result["status"], "UNRESOLVED")
        self.assertFalse(result["production_claim_allowed"])

    def test_generate_labels_all_fixture_records(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = root / "outcomes.jsonl"
            source.write_text(json.dumps({"event_id": "EVT-X", "test_id": "T-X", "test_result": "PASS",
                                          "evidence": [{"locator": "example:fixture"}]}) + "\n", encoding="utf-8")
            report = generate(source, root, source_mode="fixture")
        self.assertEqual(report["records_fixture_only"], 1)
        self.assertEqual(report["records_unresolved"], 0)


if __name__ == "__main__":
    unittest.main()
