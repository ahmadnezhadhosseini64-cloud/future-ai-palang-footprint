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
    verify_state, digest, payload, register_point, lookup_interaction,
)


class HaifStarterEngineTests(unittest.TestCase):
    def test_interaction_has_independent_anchor_in_out_and_hash_chain(self):
        state = new_state()
        event = record_interaction(state, "input text", "output text")
        self.assertTrue(event["anchor_id"].startswith("HAIF-ANCHOR-"))
        self.assertTrue(event["input_id"].startswith("HAIF-IN-"))
        self.assertTrue(event["output_id"].startswith("HAIF-OUT-"))
        self.assertTrue(event["bridge_id"].startswith("HAIF-BRIDGE-"))
        self.assertEqual(event["bridge"]["bridge_id"], event["bridge_id"])
        self.assertEqual(event["bridge"]["input_id"], event["input_id"])
        self.assertEqual(event["bridge"]["output_id"], event["output_id"])
        self.assertEqual(event["bridge"]["event_id"], event["event_id"])
        self.assertEqual(event["bridge"]["parent_event_hash"], event["parent_hash"])
        self.assertEqual(event["bridge"]["status"], "MATCHED")
        for anchor in (event["input_id"], event["output_id"], event["bridge_id"]):
            self.assertIs(lookup_interaction(state, anchor), event)
        self.assertIsNone(event["user_message_time_utc"])
        self.assertEqual(event["registration_status"], "WRITE_READBACK_VERIFIED")
        self.assertEqual(verify_state(state), [])

    def test_bridge_mismatch_rejected_even_with_rehashed_event(self):
        state = new_state()
        event = record_interaction(state, "input", "output")
        event["bridge"]["output_id"] = "HAIF-OUT-TAMPERED"
        event["event_hash"] = digest(payload(event))
        errors = verify_state(state)
        self.assertTrue(any("bridge.output_id mismatch" in error for error in errors))

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
        second["bridge_id"] = first["bridge_id"]
        second["bridge"]["bridge_id"] = first["bridge_id"]
        second["event_hash"] = digest(payload(second))
        errors = verify_state(state)
        self.assertTrue(any("input_id duplicate" in error for error in errors))
        self.assertTrue(any("output_id duplicate" in error for error in errors))
        self.assertTrue(any("bridge_id duplicate" in error for error in errors))

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
    def test_package_manifest_is_current_version_and_keeps_existing_stable_id(self):
        package = Path(__file__).parent
        manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], manifest["archive_policy"]["current_internal_version"])
        self.assertEqual(manifest["supersedes"], "0.5.0")
        self.assertEqual(manifest["stable_id"], "HAIF-GPT6-PORTABLE-STARTER-20261025-004")
        packaged_master = (package / "LIVING_MASTER_REFERENCE.md").read_text(encoding="utf-8")
        master_version_line = next((line for line in packaged_master.splitlines() if line.startswith("## نسخهٔ ")), None)
        self.assertIsNotNone(master_version_line, "packaged living master must expose its version")
        packaged_master_version = master_version_line.split("## نسخهٔ ", 1)[1].split(" ", 1)[0]
        self.assertEqual(manifest["current_living_master_version"], packaged_master_version)
        self.assertIn("CURRENT-150", manifest["parent_architecture"])
        self.assertIn("CURRENT-151", manifest["parent_architecture"])
        self.assertIn("POINT-0/088", manifest["parent_architecture"])
        self.assertEqual(manifest["recovery_protocol"], "INDEPENDENT_HOST_RECOVERY_PROTOCOL.md")
        self.assertEqual(manifest["universal_host_entry"], "UNIVERSAL_AI_HOST_ENTRY_FA.md")
        self.assertTrue((package / manifest["universal_host_entry"]).is_file())
        self.assertEqual(manifest["archive_policy"]["current_internal_version"], manifest["version"])
        self.assertEqual(manifest["archive_policy"]["update_mode"], "REBUILD_IN_PLACE_SAME_PACKAGE_IDENTITY")
        chain = manifest["parent_architecture"]
        self.assertEqual(manifest["current_continuation_chain"], "POINT-0/GOLDEN → CURRENT-150.04 → IN-138 → BRIDGE-0138 → OUT-137 → EVT-0325 → TIME-BINDING-EVT-0325 → CURRENT-150.05 → NEXT-051.05")
        self.assertLess(chain.index("POINT-0/057 (0+ marker on canonical root 0)"), chain.index("IN-095"))
        self.assertLess(chain.index("IN-095"), chain.index("OUT-094"))
        self.assertLess(chain.index("OUT-094"), chain.index("EVT-0232"))
        self.assertLess(chain.index("EVT-0232"), chain.index("CURRENT-107"))
        self.assertLess(chain.index("CURRENT-107"), chain.index("NEXT-051"))
        self.assertLess(chain.index("POINT-0/069 (0+ permanent interaction ledger)"), chain.index("IN-112"))
        self.assertLess(chain.index("IN-112"), chain.index("OUT-111"))
        self.assertLess(chain.index("OUT-111"), chain.index("EVT-0287"))
        self.assertLess(chain.index("EVT-0287"), chain.index("CURRENT-122"))
        self.assertLess(chain.index("POINT-0/071 (0++ marker on canonical root 0)"), chain.index("IN-114"))
        self.assertLess(chain.index("IN-114"), chain.index("OUT-113"))
        self.assertLess(chain.index("OUT-113"), chain.index("EVT-0289"))
        self.assertLess(chain.index("EVT-0289"), chain.index("CURRENT-124"))
        self.assertLess(chain.index("POINT-0/072 (current conversation continuation under canonical root 0)"), chain.index("IN-115"))
        self.assertLess(chain.index("IN-115"), chain.index("OUT-114"))
        self.assertLess(chain.index("OUT-114"), chain.index("EVT-0291"))
        self.assertLess(chain.index("EVT-0291"), chain.index("CURRENT-125"))
        self.assertLess(chain.index("POINT-0/073"), chain.index("IN-116"))
        self.assertLess(chain.index("IN-116"), chain.index("OUT-115"))
        self.assertLess(chain.index("OUT-115"), chain.index("EVT-0292"))
        self.assertLess(chain.index("EVT-0292"), chain.index("CURRENT-126"))
        self.assertLess(chain.index("POINT-0/074 (0++ marker on canonical root 0)"), chain.index("IN-117"))
        self.assertLess(chain.index("IN-117"), chain.index("OUT-116"))
        self.assertLess(chain.index("OUT-116"), chain.index("EVT-0293"))
        self.assertLess(chain.index("EVT-0293"), chain.index("CURRENT-127"))
        self.assertLess(chain.index("POINT-0/077 (0++ marker on canonical root 0)"), chain.index("IN-120"))
        self.assertLess(chain.index("IN-120"), chain.index("OUT-119"))
        self.assertLess(chain.index("OUT-119"), chain.index("EVT-0296"))
        self.assertLess(chain.index("EVT-0296"), chain.index("CURRENT-130"))
        self.assertLess(chain.index("POINT-0/078 (0++ marker on canonical root 0)"), chain.index("IN-121"))
        self.assertLess(chain.index("IN-121"), chain.index("OUT-120"))
        self.assertLess(chain.index("OUT-120"), chain.index("EVT-0298"))
        self.assertLess(chain.index("EVT-0298"), chain.index("CURRENT-131"))
        self.assertLess(chain.index("CURRENT-131"), chain.index("POINT-0/079 (0++ marker on canonical root 0)"))
        self.assertLess(chain.index("POINT-0/079 (0++ marker on canonical root 0)"), chain.index("IN-122"))
        self.assertLess(chain.index("IN-122"), chain.index("OUT-121"))
        self.assertLess(chain.index("OUT-121"), chain.index("EVT-0299"))
        self.assertLess(chain.index("EVT-0299"), chain.index("CURRENT-132"))
        self.assertEqual(chain.count("NEXT-051"), 1, "only one canonical active NEXT-051 pointer is allowed")
        self.assertGreaterEqual(chain.count("NEXT-051 (historical queue reference)"), 1)
        expected_current = ["IN-105", "OUT-104", "EVT-0280", "CURRENT-116", "IN-106", "OUT-105", "EVT-0281", "TIME-BINDING-EVT-0281", "CURRENT-117", "POINT-0/066 (0+ — interactive evolution)", "IN-107", "OUT-106", "EVT-0282", "TIME-BINDING-EVT-0282", "CURRENT-118", "POINT-0/067 (0+ continuation marker)", "CURRENT-120", "POINT-0/068", "CURRENT-121", "POINT-0/069 (0+ permanent interaction ledger)", "IN-112", "OUT-111", "EVT-0287", "TIME-BINDING-EVT-0287", "CURRENT-122", "POINT-0/071 (0++ marker on canonical root 0)", "IN-114", "OUT-113", "EVT-0289", "TIME-BINDING-EVT-0289", "CURRENT-124", "POINT-0/072 (current conversation continuation under canonical root 0)", "IN-115", "OUT-114", "EVT-0291", "TIME-BINDING-EVT-0291", "CURRENT-125", "POINT-0/073", "IN-116", "OUT-115", "EVT-0292", "TIME-BINDING-EVT-0292", "CURRENT-126", "POINT-0/074 (0++ marker on canonical root 0)", "IN-117", "OUT-116", "EVT-0293", "TIME-BINDING-EVT-0293", "CURRENT-127"]
        for identifier in expected_current:
            self.assertIn(identifier, chain)
        self.assertIn("LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT.md", chain)
        self.assertIn("PERMANENT_INTERACTION_LEDGER_CONTRACT.md", manifest["governance_documents"])
        self.assertIn("HOST_REGISTRY_SCHEMA.json", manifest["governance_documents"])
        for filename in manifest["governance_documents"]:
            if filename != "LIVING_MASTER_REFERENCE.md":
                self.assertTrue((package / filename).is_file(), filename)
        self.assertEqual(chain.count("NEXT-051 (sole active queue; current)"), 1)

    def test_latest_verified_export_delivery_contract_is_packaged(self):
        package = Path(__file__).parent
        contract = (package / "LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT.md").read_text(encoding="utf-8")
        for required in ("exact current main SHA", "PACKAGE_VERIFIED", "HOST_RECOVERED", "canonical ZIP filename", "living mother", "never silently substitute"):
            self.assertIn(required.casefold(), contract.casefold())

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
        self.assertEqual(manifest["version"], manifest["archive_policy"]["current_internal_version"])
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
        self.assertIn("POINT-0/055 (0+ marker on canonical root 0)", manifest["parent_architecture"])
        self.assertIn("POINT-0/056 (0+ marker on canonical root 0)", manifest["parent_architecture"])
        self.assertIn("CURRENT-105", manifest["parent_architecture"])
        self.assertIn("CURRENT-107", manifest["parent_architecture"])
        self.assertIn("NEXT-051", manifest["parent_architecture"])
        self.assertIn("INTERACTION-RESPONSE-AND-ANCHOR-PROTOCOL.md", manifest["parent_architecture"])
        self.assertIn("HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md", manifest["parent_architecture"])
        self.assertIn("ONE_MESSAGE_HOST_BOOTSTRAP_FA.md", manifest["governance_documents"])
        self.assertEqual(manifest["host_acceptance_checklist"], "FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md")
        self.assertEqual(manifest["independent_host_acceptance_prompt"], "INDEPENDENT_HOST_ACCEPTANCE_PROMPT_FA.md")


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
        self.assertIn("POINT-0/058", protocol)
        self.assertIn("CURRENT-108", protocol)

    def test_package_manifest_version_and_identity_remain_continuous(self):
        root = Path(__file__).parent
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], manifest["archive_policy"]["current_internal_version"])
        self.assertEqual(manifest["supersedes"], "0.5.0")
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
        self.assertEqual(manifest["version"], manifest["archive_policy"]["current_internal_version"])
        self.assertEqual(manifest["stable_id"], "HAIF-GPT6-PORTABLE-STARTER-20261025-004")
        self.assertEqual(manifest["archive_policy"]["canonical_filename"], "haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip")
        self.assertIn("actual host integration", protocol.casefold())
        self.assertIn("NOT VERIFIED", protocol)
        expected_chain = manifest["current_continuation_chain"]
        for filename in (
            "GPT6_HOST_INSTRUCTIONS.md",
            "INDEPENDENT_HOST_RECOVERY_PROTOCOL.md",
            "INTERACTION-RESPONSE-AND-ANCHOR-PROTOCOL.md",
            "HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md",
        ):
            text = (root / filename).read_text(encoding="utf-8")
            self.assertIn(expected_chain, text, filename)
            self.assertIn("0.5.2", text, filename)
        readme = (root / "README.md").read_text(encoding="utf-8")
        self.assertIn("v0.5.2", readme)
        self.assertIn("external build receipt", readme)
        self.assertIn("Previous verified v0.4.3 build receipt", readme)
        self.assertIn(expected_chain, readme)
        self.assertIn("CURRENT-150", manifest["parent_architecture"])
        self.assertIn("POINT-0/088", manifest["parent_architecture"])
        packaged_master = (root / "LIVING_MASTER_REFERENCE.md").read_text(encoding="utf-8")
        master_version_line = next((line for line in packaged_master.splitlines() if line.startswith("## نسخهٔ ")), None)
        self.assertIsNotNone(master_version_line, "packaged living master must expose its version")
        packaged_master_version = master_version_line.split("## نسخهٔ ", 1)[1].split(" ", 1)[0]
        self.assertEqual(manifest["current_living_master_version"], packaged_master_version)
        for anchor in ("POINT-0/GOLDEN", "CURRENT-150.04", "IN-138", "BRIDGE-0138",
                       "OUT-137", "EVT-0325", "TIME-BINDING-EVT-0325",
                       "CURRENT-150.05", "NEXT-051.05"):
            self.assertIn(anchor, packaged_master)
