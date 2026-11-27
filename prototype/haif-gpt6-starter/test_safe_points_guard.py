import base64
import json
import os
import unittest
from unittest.mock import patch
from safe_points_guard import (
    Gate, REQUIRED_FIELDS, Verification, evaluate_attestation, bridge_destination,
)


GOLDEN = "a" * 40
REPOSITORY = "ahmadnezhadhosseini64-cloud/future-ai-palang-footprint"


def packet(**overrides):
    value = {
        "schema": "palang.external-verification.v1",
        "issuer": "palang-independent-verifier",
        "repository": REPOSITORY,
        "main_sha": GOLDEN,
        "copy1_sha": GOLDEN,
        "copy2_base_sha": GOLDEN,
        "copy2_head_sha": "b" * 40,
        "diff_sha256": "c" * 64,
        "tests_pass": True,
        "paths_authorized": True,
        "bridge_matches": True,
    }
    value.update(overrides)
    return value


class ExternalAttestationGateTests(unittest.TestCase):
    def setUp(self):
        self.env = patch.dict(os.environ, {
            "PALANG_TRUSTED_VERIFIER_PUBLIC_KEY": "TEST PUBLIC KEY",
            "PALANG_GOLDEN_SHA": GOLDEN,
        })
        self.env.start()
        self.addCleanup(self.env.stop)

    def test_missing_trusted_key_blocks(self):
        with patch.dict(os.environ, {"PALANG_TRUSTED_VERIFIER_PUBLIC_KEY": ""}):
            result = evaluate_attestation(packet(), "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.BLOCKED)
        self.assertIn("key or golden pin", result.reason)

    def test_missing_golden_pin_blocks(self):
        with patch.dict(os.environ, {"PALANG_GOLDEN_SHA": ""}):
            result = evaluate_attestation(packet(), "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.BLOCKED)

    def test_candidate_boolean_packet_is_not_enough(self):
        with patch("safe_points_guard._verify_signature", return_value=False):
            result = evaluate_attestation(packet(), "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.BLOCKED)
        self.assertIn("signature", result.reason)

    def test_signed_valid_attestation_stops_at_owner(self):
        with patch("safe_points_guard._verify_signature", return_value=True):
            result = evaluate_attestation(packet(), "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.OWNER_REVIEW)

    def test_wrong_repository_blocks(self):
        with patch("safe_points_guard._verify_signature", return_value=True):
            result = evaluate_attestation(packet(), "c2ln", repository="attacker/repo")
        self.assertEqual(result.gate, Gate.BLOCKED)

    def test_wrong_issuer_blocks(self):
        with patch("safe_points_guard._verify_signature", return_value=True):
            result = evaluate_attestation(packet(issuer="candidate"), "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.BLOCKED)

    def test_main_drift_blocks(self):
        with patch("safe_points_guard._verify_signature", return_value=True):
            result = evaluate_attestation(packet(main_sha="d" * 40), "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.BLOCKED)

    def test_copy1_drift_blocks(self):
        with patch("safe_points_guard._verify_signature", return_value=True):
            result = evaluate_attestation(packet(copy1_sha="d" * 40), "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.BLOCKED)

    def test_wrong_copy2_base_blocks(self):
        with patch("safe_points_guard._verify_signature", return_value=True):
            result = evaluate_attestation(packet(copy2_base_sha="d" * 40), "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.BLOCKED)

    def test_each_failed_check_blocks(self):
        for field in ("tests_pass", "paths_authorized", "bridge_matches"):
            with self.subTest(field=field), patch("safe_points_guard._verify_signature", return_value=True):
                result = evaluate_attestation(packet(**{field: False}), "c2ln", repository=REPOSITORY)
                self.assertEqual(result.gate, Gate.BLOCKED)

    def test_missing_required_field_blocks(self):
        value = packet()
        del value["diff_sha256"]
        result = evaluate_attestation(value, "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.BLOCKED)

    def test_malformed_sha_blocks(self):
        with patch("safe_points_guard._verify_signature", return_value=True):
            result = evaluate_attestation(packet(copy2_head_sha="not a sha"), "c2ln", repository=REPOSITORY)
        self.assertEqual(result.gate, Gate.BLOCKED)

    def test_bridge_is_owner_review_only(self):
        self.assertEqual(bridge_destination(), "OWNER_REVIEW_ONLY")


if __name__ == "__main__":
    unittest.main(verbosity=2)
