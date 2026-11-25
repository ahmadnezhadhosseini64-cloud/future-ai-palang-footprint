"""Executable fail-closed safe-base evidence checks and atomic CAS tests."""
import json
import tempfile
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "architecture"))
import unittest
from pathlib import Path

from safe_base_resolver import EvidenceError, advance_safe_point, resolve


SAFE = "2c1f9fdc308e34b23be64153e8eec2c30f08a859"
CANDIDATE = "c" * 40
TREE = "d" * 40


def valid_manifest():
    checks = [
        {"name": name, "run_id": str(50000 + i), "tested_sha": CANDIDATE, "conclusion": "success"}
        for i, name in enumerate(("unit-tests", "architecture-audit", "security-negative-tests"))
    ]
    return {
        "safe_base_sha": SAFE,
        "candidate_base_sha": SAFE,
        "candidate_sha": CANDIDATE,
        "candidate_tree_sha": TREE,
        "tested_sha": CANDIDATE,
        "owner_approved_sha": CANDIDATE,
        "point0_golden_id": "POINT-0/GOLDEN",
        "current_id": "CURRENT-145",
        "sole_next_id": "NEXT-051",
        "source_ref": "main",
        "readback_receipt": "readback-abc",
        "security_review_receipt": "security-review-xyz",
        "owner_approval_receipt": "owner-approval-123",
        "validation_profile": "strict-v1",
        "time_binding_utc": "2026-11-25T17:00:00Z",
        "source_identity": {"commit_sha": SAFE, "tree_sha": "e" * 40},
        "checks": checks,
    }


class SafeBaseResolverTests(unittest.TestCase):
    def test_complete_exact_sha_evidence_resolves(self):
        result = resolve(valid_manifest(), SAFE)
        self.assertEqual(result["status"], "VALIDATED_CANDIDATE")
        self.assertEqual(result["candidate_sha"], CANDIDATE)

    def test_missing_check_fails_closed(self):
        m = valid_manifest()
        m["checks"].pop()
        with self.assertRaisesRegex(EvidenceError, "required checks missing"):
            resolve(m, SAFE)

    def test_duplicate_check_fails_closed(self):
        m = valid_manifest()
        m["checks"].append(dict(m["checks"][0]))
        with self.assertRaisesRegex(EvidenceError, "duplicate check"):
            resolve(m, SAFE)

    def test_failed_check_rejects_candidate(self):
        m = valid_manifest()
        m["checks"][0]["conclusion"] = "failure"
        with self.assertRaisesRegex(EvidenceError, "not successful"):
            resolve(m, SAFE)

    def test_tested_sha_mismatch_is_stale(self):
        m = valid_manifest()
        m["tested_sha"] = "f" * 40
        with self.assertRaisesRegex(EvidenceError, "stale"):
            resolve(m, SAFE)

    def test_owner_approval_must_bind_exact_candidate(self):
        m = valid_manifest()
        m["owner_approved_sha"] = "f" * 40
        with self.assertRaisesRegex(EvidenceError, "approval is not bound"):
            resolve(m, SAFE)

    def test_wrong_source_snapshot_rejected(self):
        m = valid_manifest()
        m["source_identity"]["commit_sha"] = "f" * 40
        with self.assertRaisesRegex(EvidenceError, "source snapshot"):
            resolve(m, SAFE)

    def test_stale_safe_base_rejected(self):
        m = valid_manifest()
        m["safe_base_sha"] = "f" * 40
        with self.assertRaisesRegex(EvidenceError, "safe-base mismatch"):
            resolve(m, SAFE)

    def test_stacked_candidate_requires_dependency_chain(self):
        m = valid_manifest()
        m["candidate_base_sha"] = "a" * 40
        m["accepted_dependency_chain"] = False
        with self.assertRaisesRegex(EvidenceError, "accepted dependency"):
            resolve(m, SAFE)
        m["accepted_dependency_chain"] = True
        m["dependency_shas"] = ["b" * 40]
        self.assertEqual(resolve(m, SAFE)["candidate_sha"], CANDIDATE)

    def test_cas_advances_atomically_when_expected_sha_matches(self):
        with tempfile.TemporaryDirectory() as td:
            state = Path(td) / "safe.json"
            state.write_text(json.dumps({"safe_sha": SAFE}), encoding="utf-8")
            result = advance_safe_point(state, SAFE, valid_manifest())
            readback = json.loads(state.read_text(encoding="utf-8"))
            self.assertEqual(result["status"], "SAFE_POINT_ADVANCED")
            self.assertEqual(readback["safe_sha"], CANDIDATE)
            self.assertEqual(readback["previous_safe_sha"], SAFE)

    def test_cas_rejects_stale_writer_and_preserves_state(self):
        with tempfile.TemporaryDirectory() as td:
            state = Path(td) / "safe.json"
            actual = "b" * 40
            state.write_text(json.dumps({"safe_sha": actual}), encoding="utf-8")
            before = state.read_text(encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "compare-and-swap failed"):
                advance_safe_point(state, SAFE, valid_manifest())
            self.assertEqual(state.read_text(encoding="utf-8"), before)

    def test_failed_validation_preserves_safe_point_file(self):
        with tempfile.TemporaryDirectory() as td:
            state = Path(td) / "safe.json"
            state.write_text(json.dumps({"safe_sha": SAFE}), encoding="utf-8")
            before = state.read_text(encoding="utf-8")
            m = valid_manifest()
            m["checks"][0]["conclusion"] = "cancelled"
            with self.assertRaises(EvidenceError):
                advance_safe_point(state, SAFE, m)
            self.assertEqual(state.read_text(encoding="utf-8"), before)


if __name__ == "__main__":
    unittest.main()
