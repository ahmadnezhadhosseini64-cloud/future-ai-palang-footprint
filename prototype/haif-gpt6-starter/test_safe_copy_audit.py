import json
import tempfile
import unittest
from pathlib import Path

from safe_copy_audit import REQUIRED_PACKAGE, audit_workflow, audit_copy3_workflow, audit_recovery_package


GOOD_WORKFLOW = """permissions:
  contents: read
      persist-credentials: false
      ref: ${{ github.event.pull_request.head.sha || github.sha }}
      - uses: actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8
      - uses: actions/setup-python@42375524e23c412d93fb67b49958b491fce71c38
          +refs/heads/main:refs/remotes/origin/main
          +refs/heads/$copy1_branch:refs/remotes/origin/$copy1_branch
          git merge-base --is-ancestor "$copy1_sha" "$head_sha"
          changed = set(subprocess.check_output(["git", "diff", "--name-only"], text=True).splitlines())
          unexpected = changed - allowed
          assert not unexpected
      - name: pull_request
        branches:
          - palang-safe-copy-1-baseline-20261126
          - palang-safe-copy-2-current-20261127
"""


class WorkflowSecurityAuditTests(unittest.TestCase):
    def test_current_workflow_contract_passes(self):
        self.assertEqual(audit_workflow(GOOD_WORKFLOW), [])

    def test_write_permissions_fail(self):
        result = audit_workflow(GOOD_WORKFLOW.replace("contents: read", "contents: write"))
        self.assertTrue(any("write permission" in item for item in result))

    def test_floating_action_tag_fails(self):
        result = audit_workflow(GOOD_WORKFLOW + "\n      - uses: actions/checkout@v6")
        self.assertTrue(any("full 40-character commit SHA" in item for item in result))

    def test_unpinned_action_fails(self):
        result = audit_workflow(GOOD_WORKFLOW + "\n      - uses: example/action")
        self.assertTrue(any("full 40-character commit SHA" in item for item in result))

    def test_persisted_credentials_fail(self):
        result = audit_workflow(GOOD_WORKFLOW.replace("persist-credentials: false", ""))
        self.assertIn("checkout credentials must not persist", result)

    def test_old_copy2_branch_fails(self):
        result = audit_workflow(GOOD_WORKFLOW.replace(
            "palang-safe-copy-2-current-20261127", "palang-safe-copy-2-test-20261127"
        ))
        self.assertIn("current Copy 1 / Copy 2 branch mapping is missing", result)

    def test_forcing_main_equal_copy1_fails(self):
        result = audit_workflow(GOOD_WORKFLOW + '\n          test "$main_sha" = "$copy1_sha"')
        self.assertIn("MAIN and Copy 1 are incorrectly forced to share one SHA", result)

    def test_missing_live_main_ref_fails(self):
        result = audit_workflow(GOOD_WORKFLOW.replace("+refs/heads/main:refs/remotes/origin/main", ""))
        self.assertIn("workflow does not read both live MAIN and Copy 1 refs", result)

    def test_write_or_promotion_command_fails(self):
        result = audit_workflow(GOOD_WORKFLOW + "\n        run: git push origin main")
        self.assertIn("workflow contains a write or promotion command", result)


class Copy3WorkflowSecurityAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = (Path(__file__).resolve().parents[2] / ".github/workflows/palang-copy3-proposal-intake.yml").read_text(encoding="utf-8")

    def test_current_copy3_workflow_contract_passes(self):
        self.assertEqual(audit_copy3_workflow(self.workflow), [])

    def test_pull_request_target_is_rejected(self):
        result = audit_copy3_workflow(self.workflow.replace("pull_request:", "pull_request_target:", 1))
        self.assertTrue(any("pull_request_target" in item for item in result))

    def test_write_permission_is_rejected(self):
        result = audit_copy3_workflow(self.workflow.replace("contents: read", "contents: write", 1))
        self.assertTrue(any("read-only" in item for item in result))

    def test_pr_head_cannot_supply_the_trusted_guard(self):
        unsafe = self.workflow.replace(
            'git show "$LIVE_COPY2_SHA:prototype/haif-gpt6-starter/copy3_intake_guard.py"',
            'git show "$EVENT_HEAD_SHA:prototype/haif-gpt6-starter/copy3_intake_guard.py"',
        )
        result = audit_copy3_workflow(unsafe)
        self.assertTrue(any("trusted guard from the Copy 2 base" in item for item in result))

    def test_same_repository_pr_source_is_rejected(self):
        unsafe = self.workflow.replace(
            "github.event.pull_request.head.repo.full_name != github.repository", "true"
        )
        result = audit_copy3_workflow(unsafe)
        self.assertTrue(any("independent fork" in item for item in result))

    def test_persisted_credentials_are_rejected(self):
        result = audit_copy3_workflow(self.workflow.replace("persist-credentials: false", "", 1))
        self.assertTrue(any("credentials must not persist" in item for item in result))


class RecoveryPackageAuditTests(unittest.TestCase):
    def test_missing_files_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertGreater(len(audit_recovery_package(Path(directory))), 0)

    def test_valid_minimal_package_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in REQUIRED_PACKAGE:
                (root / name).write_text("fixture", encoding="utf-8")
            (root / "manifest.json").write_text(json.dumps({
                "stable_id": "S", "production_id": "P",
                "current_living_master_version": "1.0.0",
            }), encoding="utf-8")
            self.assertEqual(audit_recovery_package(root), [])

    def test_invalid_manifest_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in REQUIRED_PACKAGE:
                (root / name).write_text("fixture", encoding="utf-8")
            (root / "manifest.json").write_text("{}", encoding="utf-8")
            self.assertTrue(audit_recovery_package(root))


if __name__ == "__main__":
    unittest.main(verbosity=2)
