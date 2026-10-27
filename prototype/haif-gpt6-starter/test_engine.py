import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from engine import (
    add_gap, audit, close_gap, decide_child, export_bundle, import_bundle,
    new_state, propose_child, record_interaction, save_state, load_state,
    verify_state, digest, payload, register_point,
)


class HaifStarterEngineTests(unittest.TestCase):
    def test_interaction_has_independent_anchor_in_out_and_hash_chain(self):
        state = new_state()
        event = record_interaction(state, "input text", "output text")
        self.assertTrue(event["anchor_id"].startswith("HAIF-ANCHOR-"))
        self.assertTrue(event["input_id"].startswith("HAIF-IN-"))
        self.assertTrue(event["output_id"].startswith("HAIF-OUT-"))
        self.assertIsNone(event["user_message_time_utc"])
        self.assertEqual(event["registration_status"], "WRITE_READBACK_VERIFIED")
        self.assertEqual(verify_state(state), [])

    def test_modified_event_is_rejected(self):
        state = new_state()
        record_interaction(state, "in", "out")
        bad = copy.deepcopy(state)
        bad["events"][0]["output"] = "tampered"
        self.assertTrue(any("event_hash mismatch" in e for e in verify_state(bad)))

    def test_zero_plus_is_a_marker_on_the_same_canonical_zero_point(self):
        state = new_state()
        root = register_point(state, "HAIF-POINT-0-PLUS-20261025", ["0", "0+"],
                              kind="ROOT", production_marker=True,
                              purpose="Important initial architecture package")
        next_point = register_point(state, "HAIF-POINT-0-0-20261025", ["0.0"],
                                    kind="CONTINUATION", parent_point_id=root["point_id"],
                                    purpose="Next execution checkpoint")
        self.assertEqual(root["point_id"], state["points"][0]["point_id"])
        self.assertEqual(state["points"][0]["labels"], ["0", "0+"])
        self.assertEqual(next_point["parent_point_id"], root["point_id"])
        self.assertEqual(verify_state(state), [])

    def test_zero_plus_cannot_be_a_separate_canonical_point(self):
        state = new_state()
        with self.assertRaises(ValueError):
            register_point(state, "HAIF-POINT-0-PLUS", ["0+"], production_marker=True)
        root = register_point(state, "HAIF-POINT-0", ["0", "0+"], production_marker=True)
        with self.assertRaises(ValueError):
            register_point(state, "HAIF-POINT-0-PLUS-SECOND", ["0+"], kind="CONTINUATION",
                           parent_point_id=root["point_id"], production_marker=True)

    def test_point_record_must_match_append_only_event_ledger(self):
        state = new_state()
        root = register_point(state, "HAIF-POINT-0", ["0", "0+"], production_marker=True)
        register_point(state, "HAIF-POINT-0-0", ["0.0"], kind="CONTINUATION",
                       parent_point_id=root["point_id"])
        state["points"][0]["purpose"] = "tampered without event"
        self.assertTrue(any("disagrees with event ledger field purpose" in error
                            for error in verify_state(state)))

    def test_continuation_cannot_parent_itself(self):
        state = new_state()
        root = register_point(state, "HAIF-POINT-0", ["0", "0+"], production_marker=True)
        child = register_point(state, "HAIF-POINT-0-0", ["0.0"], kind="CONTINUATION",
                               parent_point_id=root["point_id"])
        child["parent_point_id"] = child["point_id"]
        errors = verify_state(state)
        self.assertTrue(any("continuation parent must precede the child" in error for error in errors))

    def test_duplicate_input_or_output_ids_are_rejected_even_with_valid_hash(self):
        state = new_state()
        first = record_interaction(state, "in-1", "out-1")
        second = record_interaction(state, "in-2", "out-2")
        second["input_id"] = first["input_id"]
        second["output_id"] = first["output_id"]
        second["event_hash"] = digest(payload(second))
        errors = verify_state(state)
        self.assertTrue(any("input_id duplicate" in error for error in errors))
        self.assertTrue(any("output_id duplicate" in error for error in errors))

    def test_gaps_remain_open_until_evidence_closes_them(self):
        state = new_state()
        gap = add_gap(state, "External host import", "Not yet tested")
        self.assertEqual(gap["status"], "OPEN")
        with self.assertRaises(ValueError):
            close_gap(state, gap["gap_id"], {"test_id": "t", "tested_revision": "abc", "result": "PASS"})
        close_gap(state, gap["gap_id"], {
            "test_id": "test-1", "tested_revision": "abc", "result": "PASS", "evidence_ref": "ci://run/1"
        })
        self.assertEqual(audit(state)["open_gap_count"], 0)

    def test_child_cannot_be_promoted_without_passing_proof(self):
        state = new_state()
        child = propose_child(state, "Child A", "MASTER-001", "Test a capability")
        with self.assertRaises(ValueError):
            decide_child(state, child["child_id"], "PROMOTED")
        decide_child(state, child["child_id"], "PROMOTED", {
            "test_id": "test-child", "tested_revision": "rev-a", "result": "PASS", "evidence_ref": "ci://run/2"
        })
        self.assertEqual(audit(state)["child_status_counts"]["PROMOTED"], 1)

    def test_portable_bundle_round_trip_and_digest_tamper_detection(self):
        state = new_state()
        record_interaction(state, "question", "answer")
        bundle = export_bundle(state)
        imported = import_bundle(bundle)
        self.assertEqual(imported["state_id"], state["state_id"])
        tampered = copy.deepcopy(bundle)
        tampered["payload"]["events"][0]["output"] = "tampered"
        with self.assertRaises(ValueError):
            import_bundle(tampered)

    def test_clean_process_cli_export_import_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.json"
            bundle_path = root / "bundle.json"
            imported = root / "imported.json"
            script = Path(__file__).with_name("engine.py")

            def run(*args):
                return subprocess.run(
                    [sys.executable, str(script), *args],
                    check=True, capture_output=True, text=True
                )

            run("--state", str(source), "init")
            run("--state", str(source), "record", "--input", "cold-start input", "--output", "cold-start output")
            bundle = run("--state", str(source), "export").stdout
            bundle_path.write_text(bundle, encoding="utf-8")
            imported_result = run("--state", str(imported), "import", str(bundle_path))
            self.assertEqual(json.loads(imported_result.stdout)["result"], "IMPORTED_AND_VERIFIED")
            audit_result = run("--state", str(imported), "audit")
            self.assertEqual(json.loads(audit_result.stdout)["result"], "PASS")
            self.assertEqual(json.loads(audit_result.stdout)["event_count"], 1)

    def test_one_command_bootstrap_creates_0_plus_root_and_open_gates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state_path = root / "haif-state.json"
            script = Path(__file__).with_name("bootstrap_0plus.py")
            result = subprocess.run(
                [sys.executable, str(script), "--state", str(state_path)],
                check=True, capture_output=True, text=True
            )
            output = json.loads(result.stdout)
            self.assertEqual(output["result"], "BOOTSTRAPPED_AND_READBACK_VERIFIED")
            self.assertEqual(output["canonical_root"]["labels"], ["0", "0+"])
            self.assertEqual(output["next_0_0"]["parent_point_id"], output["canonical_root"]["point_id"])
            self.assertEqual(output["open_gaps_preserved"], 6)
            state = load_state(state_path)
            self.assertEqual(audit(state)["result"], "PASS")
            self.assertEqual(len(state["points"]), 2)
            self.assertEqual(len(state["gaps"]), 6)
            retry = subprocess.run(
                [sys.executable, str(script), "--state", str(state_path)],
                capture_output=True, text=True
            )
            self.assertNotEqual(retry.returncode, 0)
            self.assertIn("refusing to overwrite existing state", retry.stderr)

    def test_atomic_file_readback(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = new_state()
            record_interaction(state, "in", "out")
            save_state(path, state)
            fetched = load_state(path)
            self.assertEqual(fetched["events"][0]["event_hash"], state["events"][0]["event_hash"])


if __name__ == "__main__":
    unittest.main(verbosity=2)


class PortablePackageProtocolTests(unittest.TestCase):
    def test_package_manifest_is_version_038_and_keeps_existing_stable_id(self):
        package = Path(__file__).parent
        manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], "0.3.8")
        self.assertEqual(manifest["supersedes"], "0.3.7")
        self.assertEqual(manifest["stable_id"], "HAIF-GPT6-PORTABLE-STARTER-20261025-004")
        self.assertEqual(manifest["recovery_protocol"], "INDEPENDENT_HOST_RECOVERY_PROTOCOL.md")

    def test_independent_host_protocol_preserves_acceptance_boundaries(self):
        package = Path(__file__).parent
        protocol = (package / "INDEPENDENT_HOST_RECOVERY_PROTOCOL.md").read_text(encoding="utf-8")
        for required in ("clean host", "Negative controls", "Independent read-back", "Restart/persistence", "NOT RUN"):
            self.assertIn(required.casefold(), protocol.casefold())


    def test_current_chain_does_not_promote_point_044_to_a_second_zero_root(self):
        package = Path(__file__).parent
        manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
        architecture = manifest["parent_architecture"]
        self.assertIn("POINT-0/043 (0+ marker)", architecture)
        self.assertIn("POINT-0/044 (0.0 continuation anchor; canonical root identity remains 0/0+)", architecture)
        self.assertIn("CURRENT-094 — latest 0.0 continuation checkpoint", architecture)


    def test_manifest_declares_paired_first_host_transfer_and_current_audit_chain(self):
        package = Path(__file__).parent
        manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], "0.3.8")
        self.assertIn("POINT-0/049 (0+ marker on canonical point 0)", manifest["parent_architecture"])
        self.assertIn("CURRENT-099", manifest["parent_architecture"])
        self.assertIn("POINT-0/050 (0+ marker on canonical root 0)", manifest["parent_architecture"])
        self.assertIn("CURRENT-100", manifest["parent_architecture"])
        self.assertIn("POINT-0/051 (0+ marker on canonical root 0)", manifest["parent_architecture"])
        self.assertIn("CURRENT-101", manifest["parent_architecture"])
        self.assertIn("POINT-0/052 (0+ marker on canonical root 0)", manifest["parent_architecture"])
        self.assertIn("CURRENT-102", manifest["parent_architecture"])
        self.assertIn("POINT-0/053 (0+ marker on canonical root 0)", manifest["parent_architecture"])
        self.assertIn("CURRENT-103", manifest["parent_architecture"])
        self.assertIn("INTERACTION-RESPONSE-AND-ANCHOR-PROTOCOL.md", manifest["parent_architecture"])
        self.assertIn("HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md", manifest["parent_architecture"])
        self.assertEqual(manifest["host_acceptance_checklist"], "FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md")


    def test_first_host_checklist_keeps_live_host_and_writeback_gates_open(self):
        package = Path(__file__).parent
        checklist = (package / "FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md").read_text(encoding="utf-8")
        for required in ("clean interactive GPT-6 session", "live producer", "repository write-back", "restart/persistence", "NOT RUN / NOT VERIFIED"):
            self.assertIn(required.casefold(), checklist.casefold())


class HostGrowthRepositoryContractTests(unittest.TestCase):
    def test_growth_contract_is_packaged_and_preserves_open_host_gates(self):
        root = Path(__file__).parent
        contract = (root / "HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md").read_text(encoding="utf-8")
        required = [
            "same initial package", "canonical ZIP filename", "repository worker",
            "read-back", "RAHM gate", "Master/Child promotion",
            "NOT VERIFIED", "hidden chain-of-thought", "NEXT-051",
        ]
        for phrase in required:
            self.assertIn(phrase.casefold(), contract.casefold())

    def test_recovery_protocol_version_matches_manifest(self):
        root = Path(__file__).parent
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        protocol = (root / "INDEPENDENT_HOST_RECOVERY_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertIn(f"Package version: {manifest['version']}", protocol)
        self.assertIn("POINT-0/053", protocol)
        self.assertIn("CURRENT-103", protocol)

    def test_package_manifest_version_and_identity_remain_continuous(self):
        root = Path(__file__).parent
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], "0.3.8")
        self.assertEqual(manifest["supersedes"], "0.3.7")
        self.assertEqual(manifest["stable_id"], "HAIF-GPT6-PORTABLE-STARTER-20261025-004")
        self.assertEqual(manifest["recovery_protocol"], "INDEPENDENT_HOST_RECOVERY_PROTOCOL.md")


class InteractionResponseAnchorProtocolTests(unittest.TestCase):
    def test_response_protocol_requires_truthful_visible_statuses(self):
        root = Path(__file__).parent
        protocol = (root / "INTERACTION-RESPONSE-AND-ANCHOR-PROTOCOL.md").read_text(encoding="utf-8")
        for phrase in ("ACKNOWLEDGED", "COMPLETED", "BLOCKED", "FAILED", "PARTIAL", "never claim success", "NOT VERIFIED"):
            self.assertIn(phrase.casefold(), protocol.casefold())

    def test_response_protocol_preserves_same_zip_identity_and_open_host_gates(self):
        root = Path(__file__).parent
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        protocol = (root / "INTERACTION-RESPONSE-AND-ANCHOR-PROTOCOL.md").read_text(encoding="utf-8")
        self.assertEqual(manifest["version"], "0.3.8")
        self.assertEqual(manifest["stable_id"], "HAIF-GPT6-PORTABLE-STARTER-20261025-004")
        self.assertEqual(manifest["archive_policy"]["canonical_filename"], "haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip")
        self.assertIn("actual host integration", protocol.casefold())
        self.assertIn("NOT VERIFIED", protocol)
