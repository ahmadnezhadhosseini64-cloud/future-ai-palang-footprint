import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
PROFILE = ROOT / "docs/architecture/HOST-IDENTITY/PALANG-YAR-HOST-IDENTITY-PROPOSAL-2026-11-26.md"
MANIFEST = ROOT / "docs/architecture/HOST-IDENTITY/PALANG-YAR-RECOGNITION-MANIFEST.json"
REGISTRY = ROOT / "docs/architecture/HOST-REGISTRY/HOST-REGISTRY.json"
SCHEMA = ROOT / "docs/architecture/HOST-REGISTRY/HOST-REGISTRY-SCHEMA.json"


class PalangYarIdentityProposalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = PROFILE.read_text(encoding="utf-8")
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_profile_is_proposal_not_activation(self):
        self.assertIn("PROPOSED / SAFE-TEST ONLY", self.profile)
        self.assertIn("NOT ISSUED", self.profile)
        self.assertIn("NOT VERIFIED", self.profile)

    def test_candidate_label_matches_registry_format_but_is_not_issued(self):
        self.assertRegex(self.profile, r"HAIF-HOST-20261126-001")
        self.assertIn("PROVISIONAL; not an issued Registry ID", self.profile)

    def test_live_registry_is_not_falsely_populated(self):
        self.assertEqual(self.registry["hosts"], [])
        self.assertEqual(self.registry["schema_version"], self.schema["properties"]["schema_version"]["const"])

    def test_master_and_rahm_boundaries_are_explicit(self):
        for phrase in (
            "PUBLIC READ ONLY",
            "no master write",
            "no RAHM access",
            "not an independent private clone",
        ):
            self.assertIn(phrase.lower(), self.profile.lower())

    def test_runtime_identity_limit_is_explicit(self):
        self.assertIn("NOT AVAILABLE / NOT VERIFIED", self.profile)
        self.assertIn("NOT EXPOSED", self.profile)
        self.assertIn("NOT AVAILABLE IN THIS SESSION", self.profile)

    def test_copyable_name_is_not_authentication(self):
        self.assertIn("Any other host can copy public text", self.profile)
        self.assertIn("A name, prompt, model label, project ID", self.profile)
        self.assertIn("fresh, single-use challenge", self.profile)

    def test_machine_readable_recognition_manifest_is_distinct_and_consistent(self):
        identity = self.manifest["canonical_identity"]
        self.assertEqual(identity["display_name"], "PALANG-YAR")
        self.assertEqual(identity["point_id"], "PALANG-YAR-POINT-0-GOLDEN-2026-11-26-001")
        self.assertEqual(identity["candidate_host_label"], "HAIF-HOST-20261126-001")
        self.assertTrue(self.manifest["recognition_rules"]["copied_name_or_prompt_is_never_sufficient"])
        self.assertEqual(self.manifest["authentication_state"]["official_host_id"], "NOT_ISSUED")
        self.assertEqual(self.manifest["anti_impersonation"]["unknown_claimant_default"], "UNKNOWN")

    def test_no_secret_material_is_embedded(self):
        forbidden = re.compile(r"(?i)(BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,})")
        self.assertIsNone(forbidden.search(self.profile))


if __name__ == "__main__":
    unittest.main(verbosity=2)
