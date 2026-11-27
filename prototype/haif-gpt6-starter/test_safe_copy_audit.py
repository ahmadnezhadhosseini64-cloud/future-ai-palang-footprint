import tempfile
import unittest
from pathlib import Path
from safe_copy_audit import REQUIRED_PACKAGE, audit_workflow, audit_recovery_package

GOOD_WORKFLOW = """permissions:
  contents: read
      persist-credentials: false
      ref: ${{ github.event.pull_request.head.sha || github.sha }}
      branches:
        - palang-safe-copy-1-baseline-20261126
        - palang-safe-copy-2-workbench-20261127
      - uses: actions/checkout@0123456789abcdef0123456789abcdef01234567
      - name: verify paths
        run: git diff --name-only
        assert changed == expected
"""

class WorkflowSecurityAuditTests(unittest.TestCase):
    def test_good_workflow_passes(self):
        self.assertEqual(audit_workflow(GOOD_WORKFLOW), [])
    def test_write_permissions_fail(self):
        self.assertIn("write permission found", audit_workflow(GOOD_WORKFLOW.replace("contents: read", "contents: write")))
    def test_dash_uses_floating_branch_fails(self):
        result = audit_workflow(GOOD_WORKFLOW + "\n      - uses: example/action@main")
        self.assertTrue(any("full 40-character commit SHA" in x for x in result))
    def test_dash_uses_version_tag_fails(self):
        result = audit_workflow(GOOD_WORKFLOW + "\n      - uses: example/action@v4")
        self.assertTrue(any("full 40-character commit SHA" in x for x in result))
    def test_unpinned_action_fails(self):
        result = audit_workflow(GOOD_WORKFLOW + "\n      - uses: example/action")
        self.assertTrue(any("full 40-character commit SHA" in x for x in result))
    def test_full_sha_action_passes(self):
        self.assertEqual(audit_workflow(GOOD_WORKFLOW), [])
    def test_credentials_persistence_fails(self):
        self.assertIn("checkout credentials must not persist in git config", audit_workflow(GOOD_WORKFLOW.replace("persist-credentials: false", "")))
    def test_checkout_not_sha_bound_fails(self):
        self.assertIn("checkout is not bound to event head SHA", audit_workflow(GOOD_WORKFLOW.replace("ref: ${{ github.event.pull_request.head.sha || github.sha }}", "ref: main")))
    def test_promotion_command_fails(self):
        self.assertIn("promotion/write command found", audit_workflow(GOOD_WORKFLOW + "\n        run: git push origin main"))

class RecoveryPackageAuditTests(unittest.TestCase):
    def test_missing_files_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertGreater(len(audit_recovery_package(Path(directory))), 0)
    def test_valid_minimal_package_passes(self):
        import json
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in REQUIRED_PACKAGE:
                (root / name).write_text("fixture", encoding="utf-8")
            (root / "manifest.json").write_text(json.dumps({
                "stable_id": "S", "production_id": "P",
                "current_living_master_version": "1.0.0"
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
