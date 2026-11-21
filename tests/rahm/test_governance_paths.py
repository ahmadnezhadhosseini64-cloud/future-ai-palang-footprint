import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class GovernancePathTests(unittest.TestCase):
    def read(self, path):
        return (ROOT / path).read_text(encoding="utf-8")

    def test_evidence_gate_does_not_write_to_main(self):
        workflow = self.read(".github/workflows/main.yml")
        self.assertNotIn("contents: write", workflow)
        self.assertNotIn("git push", workflow)
        self.assertNotIn("Commit durable evidence record", workflow)

    def test_pending_registration_is_read_only(self):
        workflow = self.read(".github/workflows/pending-registration-drain.yml")
        self.assertIn("contents: read", workflow)
        self.assertNotIn("contents: write", workflow)
        self.assertNotIn("git push", workflow)
        self.assertIn("MASTER_WRITE=DISABLED", workflow)
        self.assertIn("AUTOMATIC_PROMOTION=DISABLED", workflow)

    def test_execution_controller_has_no_git_write_path(self):
        workflow = self.read(".github/workflows/execution-controller.yml")
        controller = self.read("control-plane/controller.py")
        self.assertIn("contents: read", workflow)
        self.assertNotIn("contents: write", workflow)
        self.assertNotIn('["git", "push"', controller)
        self.assertNotIn("subprocess.run", controller)

    def test_conformance_workflow_is_read_only(self):
        workflow = self.read(".github/workflows/rahm-portable-conformance.yml")
        self.assertIn("contents: read", workflow)
        self.assertNotIn("contents: write", workflow)

    def test_legacy_host_worker_hard_stops_on_master(self):
        worker = self.read("scripts/host_adapter_github_worker.py")
        self.assertIn("LEGACY_DIRECT_GITHUB_WORKER_DISABLED", worker)
        self.assertIn("NO_GITHUB_WRITE_ATTEMPTED", worker)
        self.assertIn("raise SystemExit", worker)

    def test_rahm_workflow_is_owner_only_and_bot_pr_only(self):
        workflow = self.read(".github/workflows/rahm-owner-controlled-child-promotion.yml")
        self.assertIn("github.actor == 'ahmadnezhadhosseini64-cloud'", workflow)
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertIn("actions/create-github-app-token@v3.2.0", workflow)
        self.assertIn("permission-contents: write", workflow)
        self.assertIn("permission-pull-requests: write", workflow)
        self.assertIn("future-ai-palang-rahm", workflow)
        self.assertIn("gh pr create", workflow)
        self.assertNotIn("gh pr merge", workflow)
        self.assertNotIn("git push origin main", workflow)

    def test_child_is_not_master(self):
        policy = self.read("docs/architecture/CHILD-CANDIDATES/README.md")
        self.assertIn("NOT automatically part of the living Master", policy)
        self.assertIn("No automatic transition to MASTER", policy)


if __name__ == "__main__":
    unittest.main()
