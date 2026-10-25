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
