import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.rahm.prepare_promotion import CandidateError, stage_candidate


class RAHMPromotionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "rahm"
        self.target = self.root / "master"
        self.candidate_id = "HAIF-CANDIDATE-20261122-001"
        self.candidate_dir = self.source / "candidates" / self.candidate_id
        self.candidate_dir.mkdir(parents=True)
        self.target.mkdir()
        self._write_valid_candidate()

    def tearDown(self):
        self.tmp.cleanup()

    def _write_valid_candidate(self):
        payloads = {
            "proposal.md": b"# Sanitized proposal\n",
            "evidence.json": b'{"evidence": []}\n',
            "validation.json": b'{"tests": {"status": "PASS"}}\n',
        }
        entries = []
        for name, data in payloads.items():
            (self.candidate_dir / name).write_bytes(data)
            entries.append({"path": name, "sha256": hashlib.sha256(data).hexdigest(), "size_bytes": len(data)})
        manifest = {
            "schema_version": "1.0.0",
            "candidate_id": self.candidate_id,
            "host_id": "HAIF-HOST-20261122-001",
            "workspace_id": "HAIF-WORKSPACE-20261122-001",
            "source_repository": "ahmadnezhadhosseini64-cloud/haif-host-haif-host-20261122-001",
            "source_commit_sha": "a" * 40,
            "master_commit_sha": "b" * 40,
            "source_session_id": "session-001",
            "exported_at_utc": "2026-11-22T00:00:00Z",
            "owner_export_receipt": "OWNER-EXPORT-RECEIPT-001",
            "owner_redaction_attestation": "OWNER_REVIEWED_AND_REDACTED",
            "owner_child_promotion_authorized": True,
            "owner_approval_ref": "OWNER-DECISION-001",
            "privacy_class": "PUBLIC_REDACTED",
            "redaction_status": "OWNER_VERIFIED",
            "files": entries,
        }
        (self.candidate_dir / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    def _manifest(self):
        return json.loads((self.candidate_dir / "manifest.json").read_text(encoding="utf-8"))

    def test_valid_candidate_stages_only_under_child(self):
        dest = stage_candidate(self.source, self.target, self.candidate_id)
        self.assertTrue((dest / "proposal.md").is_file())
        self.assertTrue((dest / "candidate-manifest.json").is_file())
        self.assertEqual(dest.parent.name, "CHILD-CANDIDATES")
        self.assertFalse((self.target / "docs" / "architecture" / "مدل اولیه AI" / "سند مرجع مادر مدل اولیه هوش مصنوعی.md").exists())

    def test_rejects_path_traversal(self):
        manifest = self._manifest()
        manifest["files"][0]["path"] = "../escape.md"
        (self.candidate_dir / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaises(CandidateError):
            stage_candidate(self.source, self.target, self.candidate_id)

    def test_rejects_digest_mismatch(self):
        (self.candidate_dir / "proposal.md").write_text("tampered", encoding="utf-8")
        with self.assertRaises(CandidateError):
            stage_candidate(self.source, self.target, self.candidate_id)

    def test_rejects_unredacted_candidate(self):
        manifest = self._manifest()
        manifest["privacy_class"] = "PRIVATE_RAW"
        (self.candidate_dir / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaises(CandidateError):
            stage_candidate(self.source, self.target, self.candidate_id)

    def test_rejects_missing_owner_authorization(self):
        manifest = self._manifest()
        manifest["owner_child_promotion_authorized"] = False
        (self.candidate_dir / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaises(CandidateError):
            stage_candidate(self.source, self.target, self.candidate_id)

    def test_rejects_secret_pattern(self):
        secret = b"ghp_" + b"A" * 30
        (self.candidate_dir / "proposal.md").write_bytes(secret)
        manifest = self._manifest()
        manifest["files"][0]["sha256"] = hashlib.sha256(secret).hexdigest()
        manifest["files"][0]["size_bytes"] = len(secret)
        (self.candidate_dir / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaises(CandidateError):
            stage_candidate(self.source, self.target, self.candidate_id)

    def test_rejects_symlink(self):
        (self.candidate_dir / "link.md").symlink_to(self.candidate_dir / "proposal.md")
        with self.assertRaises(CandidateError):
            stage_candidate(self.source, self.target, self.candidate_id)

    def test_rejects_duplicate_child_candidate(self):
        stage_candidate(self.source, self.target, self.candidate_id)
        with self.assertRaises(CandidateError):
            stage_candidate(self.source, self.target, self.candidate_id)


if __name__ == "__main__":
    unittest.main()
