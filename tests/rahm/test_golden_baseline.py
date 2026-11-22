import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class GoldenBaselineGovernanceTests(unittest.TestCase):
    def read(self, path):
        return (ROOT / path).read_text(encoding="utf-8")

    def test_single_point_zero_root_and_single_queue(self):
        point = self.read("docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md")
        current = self.read("docs/0.0/anchors/PALANG-0.0-CURRENT-20261122-140-GOLDEN-BASELINE.md")
        self.assertIn("single root", point)
        self.assertIn("not a new root", point)
        self.assertIn("NEXT-051", point)
        self.assertIn("Sole active queue: NEXT-051", current)

    def test_rahm_is_central_owner_only(self):
        policy = self.read("docs/architecture/RAHM/README.md")
        point = self.read("docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md")
        self.assertIn("outside every host workspace", policy)
        self.assertIn("Hosts cannot access", policy)
        self.assertIn("owner-only", point)
        self.assertIn("Only the owner", point)

    def test_host_entry_prompts_prohibit_master_and_rahm_access(self):
        paths = [
            "prototype/haif-gpt6-starter/GPT6_HOST_INSTRUCTIONS.md",
            "prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md",
            "prototype/universal-host/ONE_MESSAGE_MULTI_HOST_ENROLLMENT_FA.md",
        ]
        for path in paths:
            text = self.read(path)
            self.assertIn("GOLDEN BASELINE", text, path)
            self.assertIn("PUBLIC READ ONLY", text, path)
            self.assertIn("RAHM", text, path)
            self.assertIn("No host", text, path)

    def test_legacy_github_worker_is_fail_closed(self):
        worker = self.read("scripts/host_adapter_github_worker.py")
        self.assertIn("LEGACY_DIRECT_GITHUB_WORKER_DISABLED", worker)
        self.assertIn("NO_GITHUB_WRITE_ATTEMPTED", worker)
        self.assertIn("return 2", worker)
        self.assertNotIn("requests.", worker)
        self.assertNotIn("urllib.request", worker)

    def test_old_host_intake_is_not_an_active_write_route(self):
        paths = [
            "docs/architecture/مدل اولیه AI/معماری اتصال چندمیزبانی و تکامل تحت حاکمیت مالک.md",
            "docs/architecture/HOST-WORKSPACES/README.md",
            "prototype/haif-gpt6-starter/PERMANENT_INTERACTION_LEDGER_CONTRACT.md",
            "prototype/haif-gpt6-starter/README.md",
        ]
        for path in paths:
            text = self.read(path)
            if "host-intake" in text:
                self.assertTrue(
                    any(term in text.lower() for term in ("frozen", "disabled", "superseded", "historical")),
                    path,
                )
            self.assertNotIn("worker writes exclusively to the dedicated", text.lower(), path)
            self.assertNotIn("فقط به شاخه host-intake", text, path)

    def test_owner_promotion_workflow_never_auto_merges(self):
        workflow = self.read(".github/workflows/rahm-owner-controlled-child-promotion.yml")
        self.assertIn("github.actor == 'ahmadnezhadhosseini64-cloud'", workflow)
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertIn("actions/create-github-app-token@v3.2.0", workflow)
        self.assertIn("permission-contents: write", workflow)
        self.assertIn("permission-pull-requests: write", workflow)
        self.assertIn("gh pr create", workflow)
        self.assertNotIn("gh pr merge", workflow)
        self.assertNotIn("git push origin main", workflow)

    def test_pages_workflows_have_deploy_only_permissions(self):
        for path in [".github/workflows/pages.yml", ".github/workflows/playground-pages.yml"]:
            workflow = self.read(path)
            self.assertIn("pages: write", workflow)
            self.assertIn("id-token: write", workflow)
            self.assertNotIn("contents: write", workflow)
            self.assertNotIn("git push", workflow)

    def test_release_write_is_not_a_master_commit_path(self):
        workflow = self.read(".github/workflows/rahm-portable-conformance.yml")
        self.assertIn("contents: write", workflow)
        self.assertIn("gh release upload", workflow)
        self.assertNotIn("git push", workflow)
        self.assertNotIn("git commit", workflow)
        self.assertIn("github.actor == 'ahmadnezhadhosseini64-cloud'", workflow)


if __name__ == "__main__":
    unittest.main()
