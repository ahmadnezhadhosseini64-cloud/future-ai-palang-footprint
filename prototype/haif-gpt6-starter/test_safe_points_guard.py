import subprocess
import tempfile
import unittest
from pathlib import Path
from safe_points_guard import Evidence, Gate, evaluate, bridge_destination, DEFAULT_ALLOWED_PATHS

def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()

class RepositoryBackedGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        git(self.root, "init", "-b", "main")
        git(self.root, "config", "user.email", "test@example.invalid")
        git(self.root, "config", "user.name", "Test")
        (self.root / "README.md").write_text("golden\n", encoding="utf-8")
        git(self.root, "add", "README.md")
        git(self.root, "commit", "-m", "golden")
        self.golden = git(self.root, "rev-parse", "HEAD")
        git(self.root, "branch", "copy1", self.golden)
        git(self.root, "checkout", "-b", "copy2", self.golden)
        (self.root / "prototype.txt").write_text("candidate\n", encoding="utf-8")
        git(self.root, "add", "prototype.txt")
        git(self.root, "commit", "-m", "candidate")
        self.head = git(self.root, "rev-parse", "HEAD")

    def tearDown(self):
        self.tmp.cleanup()

    def evidence(self, **kw):
        data = dict(repo_root=self.root, main_ref="main", copy1_ref="copy1",
                    copy2_base_sha=self.golden, copy2_head_sha=self.head,
                    allowed_paths=frozenset({"prototype.txt"}))
        data.update(kw)
        return Evidence(**data)

    def test_live_repository_proof_stops_at_owner_review(self):
        self.assertEqual(evaluate(self.evidence(), self.golden), Gate.OWNER_REVIEW)
        self.assertEqual(bridge_destination(), "OWNER_REVIEW_ONLY")

    def test_forged_main_or_copy1_ref_is_blocked(self):
        git(self.root, "branch", "-f", "copy1", self.head)
        self.assertEqual(evaluate(self.evidence(), self.golden), Gate.BLOCKED)

    def test_wrong_base_sha_is_blocked(self):
        self.assertEqual(evaluate(self.evidence(copy2_base_sha=self.head), self.golden), Gate.BLOCKED)

    def test_forged_or_missing_head_is_blocked(self):
        self.assertEqual(evaluate(self.evidence(copy2_head_sha="a" * 40), self.golden), Gate.BLOCKED)
        self.assertEqual(evaluate(self.evidence(copy2_head_sha=""), self.golden), Gate.BLOCKED)

    def test_unrelated_history_is_blocked(self):
        git(self.root, "checkout", "--orphan", "unrelated")
        git(self.root, "rm", "-rf", ".")
        (self.root / "prototype.txt").write_text("unrelated\n", encoding="utf-8")
        git(self.root, "add", "prototype.txt")
        git(self.root, "commit", "-m", "unrelated")
        unrelated = git(self.root, "rev-parse", "HEAD")
        self.assertEqual(evaluate(self.evidence(copy2_head_sha=unrelated), self.golden), Gate.BLOCKED)

    def test_unauthorized_changed_path_is_blocked(self):
        (self.root / "secret.txt").write_text("outside allowlist\n", encoding="utf-8")
        git(self.root, "add", "secret.txt")
        git(self.root, "commit", "-m", "unauthorized path")
        head = git(self.root, "rev-parse", "HEAD")
        self.assertEqual(evaluate(self.evidence(copy2_head_sha=head), self.golden), Gate.BLOCKED)

    def test_empty_golden_is_blocked(self):
        self.assertEqual(evaluate(self.evidence(), ""), Gate.BLOCKED)

    def test_no_boolean_claims_are_accepted(self):
        with self.assertRaises(TypeError):
            Evidence(repo_root=self.root, main_ref="main", copy1_ref="copy1",
                     copy2_base_sha=self.golden, copy2_head_sha=self.head,
                     tests_pass=True, paths_authorized=True, bridge_matches=True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
