import base64
import hashlib
import json
import os
import subprocess
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

from safe_points_guard import Gate, evaluate_attestation, bridge_destination, DEFAULT_ALLOWED_PATHS


REPOSITORY = "ahmadnezhadhosseini64-cloud/future-ai-palang-footprint"
ALLOWED_PATH = "docs/architecture/SAFE-COPY/COPY2-OWNER-COMMAND-CONTROL-PLANE.md"


def git(root, *args, input_text=None):
    result = subprocess.run(
        ["git", "-C", str(root), *args], input=input_text,
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise AssertionError(result.stderr)
    return result.stdout.strip()


class SignedExternalAttestationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.keys = tempfile.TemporaryDirectory()
        cls.private_key = Path(cls.keys.name) / "private.pem"
        cls.public_key = Path(cls.keys.name) / "public.pem"
        subprocess.run(
            ["openssl", "genpkey", "-algorithm", "RSA", "-pkeyopt",
             "rsa_keygen_bits:2048", "-out", str(cls.private_key)],
            check=True, capture_output=True,
        )
        subprocess.run(
            ["openssl", "pkey", "-in", str(cls.private_key), "-pubout",
             "-out", str(cls.public_key)],
            check=True, capture_output=True,
        )
        cls.public_pem = cls.public_key.read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        cls.keys.cleanup()

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        git(self.root, "init", "-b", "main")
        git(self.root, "config", "user.email", "test@example.invalid")
        git(self.root, "config", "user.name", "Palang Test")
        (self.root / "README.md").write_text("main baseline\n", encoding="utf-8")
        git(self.root, "add", "README.md")
        git(self.root, "commit", "-m", "main baseline")
        self.main_sha = git(self.root, "rev-parse", "HEAD")

        # Copy 1 is intentionally a distinct, owner-approved safe reference.
        git(self.root, "checkout", "-b", "copy1")
        (self.root / "copy1-reference.txt").write_text("safe reference\n", encoding="utf-8")
        git(self.root, "add", "copy1-reference.txt")
        git(self.root, "commit", "-m", "Copy 1 safe reference")
        self.copy1_sha = git(self.root, "rev-parse", "HEAD")

        git(self.root, "checkout", "-b", "copy2")
        target = self.root / ALLOWED_PATH
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("candidate proposal\n", encoding="utf-8")
        git(self.root, "add", ALLOWED_PATH)
        git(self.root, "commit", "-m", "Copy 2 candidate")
        self.head_sha = git(self.root, "rev-parse", "HEAD")

        self.env = patch.dict(os.environ, {
            "PALANG_TRUSTED_VERIFIER_PUBLIC_KEY": self.public_pem,
            "PALANG_GOLDEN_MAIN_SHA": self.main_sha,
            "PALANG_SAFE_COPY1_SHA": self.copy1_sha,
            "PALANG_GOLDEN_MAIN_REF": "main",
            "PALANG_SAFE_COPY1_REF": "copy1",
        })
        self.env.start()
        self.addCleanup(self.env.stop)

    def tearDown(self):
        self.tmp.cleanup()

    def packet(self, **overrides):
        diff = subprocess.check_output(
            ["git", "-C", str(self.root), "diff", "--binary",
             f"{self.copy1_sha}...{self.head_sha}"]
        )
        now = int(time.time())
        value = {
            "schema": "palang.external-verification.v2",
            "issuer": "palang-independent-verifier",
            "repository": REPOSITORY,
            "main_sha": self.main_sha,
            "copy1_sha": self.copy1_sha,
            "copy2_base_sha": self.copy1_sha,
            "copy2_head_sha": self.head_sha,
            "diff_sha256": hashlib.sha256(diff).hexdigest(),
            "changed_paths": [ALLOWED_PATH],
            "tests_pass": True,
            "paths_authorized": True,
            "bridge_matches": True,
            "verifier_run_id": "verifier-run-test-001",
            "issued_at": now - 5,
            "expires_at": now + 300,
            "nonce": "fresh-one-use-nonce-001",
        }
        value.update(overrides)
        return value

    def sign(self, packet):
        payload = json.dumps(
            packet, sort_keys=True, separators=(",", ":"), ensure_ascii=False
        ).encode("utf-8")
        result = subprocess.run(
            ["openssl", "dgst", "-sha256", "-sign", str(self.private_key)],
            input=payload, capture_output=True, check=True,
        )
        return base64.b64encode(result.stdout).decode("ascii")

    def evaluate(self, packet=None, signature=None, **kwargs):
        packet = packet or self.packet()
        signature = signature or self.sign(packet)
        return evaluate_attestation(
            packet, signature, repo_root=self.root, repository=REPOSITORY, **kwargs
        )

    def test_copy3_intake_files_are_in_signed_candidate_allowlist(self):
        self.assertIn(".github/workflows/palang-copy3-proposal-intake.yml", DEFAULT_ALLOWED_PATHS)
        self.assertIn("prototype/haif-gpt6-starter/copy3_intake_guard.py", DEFAULT_ALLOWED_PATHS)
        self.assertIn("prototype/haif-gpt6-starter/test_safe_copy3_intake_guard.py", DEFAULT_ALLOWED_PATHS)
        self.assertIn("prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md", DEFAULT_ALLOWED_PATHS)
        self.assertIn("prototype/haif-gpt6-starter/UNIVERSAL_AI_HOST_ENTRY_FA.md", DEFAULT_ALLOWED_PATHS)
        self.assertIn("prototype/universal-host/UNIVERSAL_AI_HOST_ENTRY_FA.md", DEFAULT_ALLOWED_PATHS)
        self.assertIn("prototype/haif-gpt6-starter/test_host_entry_sync.py", DEFAULT_ALLOWED_PATHS)
        self.assertIn("prototype/haif-gpt6-starter/manifest.json", DEFAULT_ALLOWED_PATHS)

    def test_real_signature_passes_and_main_may_differ_from_copy1(self):
        self.assertNotEqual(self.main_sha, self.copy1_sha)
        self.assertEqual(self.evaluate().gate, Gate.OWNER_REVIEW)
        self.assertEqual(bridge_destination(), "OWNER_REVIEW_ONLY")

    def test_malformed_signature_blocks(self):
        self.assertEqual(self.evaluate(signature=123).gate, Gate.BLOCKED)

    def test_missing_trusted_verifier_blocks(self):
        with patch.dict(os.environ, {"PALANG_TRUSTED_VERIFIER_PUBLIC_KEY": ""}):
            self.assertEqual(self.evaluate().gate, Gate.BLOCKED)

    def test_main_pin_drift_blocks(self):
        with patch.dict(os.environ, {"PALANG_GOLDEN_MAIN_SHA": "f" * 40}):
            self.assertEqual(self.evaluate().gate, Gate.BLOCKED)

    def test_copy1_pin_drift_blocks(self):
        with patch.dict(os.environ, {"PALANG_SAFE_COPY1_SHA": "f" * 40}):
            self.assertEqual(self.evaluate().gate, Gate.BLOCKED)

    def test_wrong_repository_blocks(self):
        packet = self.packet(repository="attacker/repo")
        self.assertEqual(self.evaluate(packet).gate, Gate.BLOCKED)

    def test_wrong_copy2_base_blocks(self):
        packet = self.packet(copy2_base_sha=self.main_sha)
        self.assertEqual(self.evaluate(packet).gate, Gate.BLOCKED)

    def test_attestation_must_bind_live_head(self):
        packet = self.packet(copy2_head_sha=self.copy1_sha)
        self.assertEqual(self.evaluate(packet).gate, Gate.BLOCKED)

    def test_tampered_payload_fails_signature(self):
        packet = self.packet()
        signature = self.sign(packet)
        packet["verifier_run_id"] = "tampered-after-signing"
        self.assertEqual(self.evaluate(packet, signature).gate, Gate.BLOCKED)

    def test_pressure_rejects_32_tampered_signed_attestations(self):
        for index in range(32):
            packet = self.packet(nonce=f"stress-nonce-{index:04d}-unique")
            signature = self.sign(packet)
            packet["verifier_run_id"] = f"tampered-run-{index:04d}"
            self.assertEqual(self.evaluate(packet, signature).gate, Gate.BLOCKED)

    def test_diff_digest_mismatch_blocks(self):
        packet = self.packet(diff_sha256="0" * 64)
        self.assertEqual(self.evaluate(packet).gate, Gate.BLOCKED)

    def test_expired_attestation_blocks(self):
        now = int(time.time())
        packet = self.packet(issued_at=now - 100, expires_at=now - 1)
        self.assertEqual(self.evaluate(packet, now=now).gate, Gate.BLOCKED)

    def test_failed_independent_check_blocks(self):
        packet = self.packet(tests_pass=False)
        self.assertEqual(self.evaluate(packet).gate, Gate.BLOCKED)

    def test_unauthorized_changed_path_blocks(self):
        target = self.root / "unapproved.txt"
        target.write_text("not allowed\n", encoding="utf-8")
        git(self.root, "add", "unapproved.txt")
        git(self.root, "commit", "-m", "unauthorized path")
        self.head_sha = git(self.root, "rev-parse", "HEAD")
        diff = subprocess.check_output(
            ["git", "-C", str(self.root), "diff", "--binary",
             f"{self.copy1_sha}...{self.head_sha}"]
        )
        packet = self.packet(
            copy2_head_sha=self.head_sha,
            diff_sha256=hashlib.sha256(diff).hexdigest(),
            changed_paths=sorted([ALLOWED_PATH, "unapproved.txt"]),
        )
        self.assertEqual(self.evaluate(packet).gate, Gate.BLOCKED)

    def test_missing_required_field_blocks(self):
        packet = self.packet()
        del packet["nonce"]
        self.assertEqual(self.evaluate(packet).gate, Gate.BLOCKED)


if __name__ == "__main__":
    unittest.main(verbosity=2)
