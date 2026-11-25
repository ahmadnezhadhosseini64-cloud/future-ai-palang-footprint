"""Policy tests for networked safe-base succession; no GitHub mutation occurs here."""
import re
import unittest
from dataclasses import dataclass


SHA_RE = re.compile(r"^[0-9a-f]{40}$")


@dataclass(frozen=True)
class Evidence:
    base_sha: str
    candidate_parent_sha: str
    candidate_sha: str
    dependencies_accepted: bool
    ci_passed_on_exact_head: bool
    readback_passed: bool
    semantic_security_review_passed: bool
    owner_approved: bool


def eligible(previous_safe_sha: str, evidence: Evidence) -> bool:
    values = (
        previous_safe_sha,
        evidence.base_sha,
        evidence.candidate_parent_sha,
        evidence.candidate_sha,
    )
    if not all(isinstance(value, str) and SHA_RE.fullmatch(value) for value in values):
        return False
    if evidence.base_sha != previous_safe_sha:
        return False
    if evidence.candidate_parent_sha != previous_safe_sha:
        return False
    return all((
        evidence.dependencies_accepted,
        evidence.ci_passed_on_exact_head,
        evidence.readback_passed,
        evidence.semantic_security_review_passed,
        evidence.owner_approved,
    ))


def promote_or_preserve(previous_safe_sha: str, evidence: Evidence) -> str:
    return evidence.candidate_sha if eligible(previous_safe_sha, evidence) else previous_safe_sha


class SafeBaseSuccessionTests(unittest.TestCase):
    def setUp(self):
        self.safe = "2c1f9fdc308e34b23be64153e8eec2c30f08a859"
        self.candidate = "a" * 40
        self.good = Evidence(
            base_sha=self.safe,
            candidate_parent_sha=self.safe,
            candidate_sha=self.candidate,
            dependencies_accepted=True,
            ci_passed_on_exact_head=True,
            readback_passed=True,
            semantic_security_review_passed=True,
            owner_approved=True,
        )

    def test_full_commit_sha_is_required(self):
        bad = Evidence(**{**self.good.__dict__, "candidate_sha": "main"})
        self.assertFalse(eligible(self.safe, bad))
        self.assertEqual(promote_or_preserve(self.safe, bad), self.safe)

    def test_exact_base_and_parent_are_required(self):
        stale = Evidence(**{**self.good.__dict__, "base_sha": "b" * 40})
        self.assertFalse(eligible(self.safe, stale))
        self.assertEqual(promote_or_preserve(self.safe, stale), self.safe)

    def test_every_gate_is_required(self):
        for field in (
            "dependencies_accepted",
            "ci_passed_on_exact_head",
            "readback_passed",
            "semantic_security_review_passed",
            "owner_approved",
        ):
            with self.subTest(field=field):
                blocked = Evidence(**{**self.good.__dict__, field: False})
                self.assertFalse(eligible(self.safe, blocked))
                self.assertEqual(promote_or_preserve(self.safe, blocked), self.safe)

    def test_all_gates_pass_allow_candidate(self):
        self.assertTrue(eligible(self.safe, self.good))
        self.assertEqual(promote_or_preserve(self.safe, self.good), self.candidate)

    def test_failed_candidate_never_mutates_previous_safe_base(self):
        failed = Evidence(**{**self.good.__dict__, "ci_passed_on_exact_head": False})
        self.assertEqual(promote_or_preserve(self.safe, failed), self.safe)


if __name__ == "__main__":
    unittest.main()
