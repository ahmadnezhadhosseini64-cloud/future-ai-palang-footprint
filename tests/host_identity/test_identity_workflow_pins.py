import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKFLOWS = (
    ROOT / ".github/workflows/palang-yar-identity-validation.yml",
    ROOT / ".github/workflows/palang-safe-copy2-validation.yml",
)
CHECKOUT_V5_SHA = "08c6903cd8c0fde910a37f88322edcfb5dd907a8"


def external_action_ref(uses: str) -> bool:
    uses = uses.strip()
    if uses.startswith("./") or uses.startswith("docker://"):
        return True
    if "@" not in uses:
        return False
    action, ref = uses.rsplit("@", 1)
    return bool(action and re.fullmatch(r"[0-9a-f]{40}", ref))


def action_uses(workflow_text: str) -> list[str]:
    refs = []
    for line in workflow_text.splitlines():
        match = re.match(r"^\s*uses:\s*(\S+)", line)
        if match:
            refs.append(match.group(1))
    return refs


class WorkflowActionPinAuditTests(unittest.TestCase):
    def test_workflows_exist_and_have_actions(self):
        for workflow in WORKFLOWS:
            self.assertTrue(workflow.is_file(), workflow)
            self.assertTrue(action_uses(workflow.read_text(encoding="utf-8")), workflow)

    def test_all_external_actions_use_full_commit_sha(self):
        for workflow in WORKFLOWS:
            text = workflow.read_text(encoding="utf-8")
            refs = action_uses(text)
            for ref in refs:
                self.assertTrue(external_action_ref(ref), f"{workflow.name}: mutable/unpinned action {ref}")

    def test_checkout_v5_is_pinned_to_verified_release_commit(self):
        identity_workflow = WORKFLOWS[0].read_text(encoding="utf-8")
        self.assertIn(f"actions/checkout@{CHECKOUT_V5_SHA} # v5.0.0", identity_workflow)

    def test_mutable_tags_branches_and_missing_refs_are_rejected(self):
        for ref in (
            "actions/checkout@v5",
            "actions/checkout@main",
            "actions/checkout@refs/tags/v5.0.0",
            "actions/checkout",
        ):
            with self.subTest(ref=ref):
                self.assertFalse(external_action_ref(ref))

    def test_full_sha_reference_is_accepted(self):
        self.assertTrue(external_action_ref(f"actions/checkout@{CHECKOUT_V5_SHA}"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
