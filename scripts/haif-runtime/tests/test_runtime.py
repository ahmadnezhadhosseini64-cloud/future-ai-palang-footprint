import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1] / "haif_runtime.py"


class RuntimeTests(unittest.TestCase):
    def run_cli(self, *args, expected=0):
        result = subprocess.run([sys.executable, str(RUNTIME), *map(str, args)], text=True, capture_output=True)
        self.assertEqual(result.returncode, expected, result.stderr)
        return result

    def test_init_record_checkpoint_export_import_verify(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source.json"
            target = root / "restored.json"
            self.run_cli("--state", source, "init")
            self.run_cli("--state", source, "record", "--input", "user request", "--output", "recorded response")
            self.run_cli("--state", source, "record", "--input", "next request", "--output", "next response")
            self.run_cli("--state", source, "checkpoint")
            verified = json.loads(self.run_cli("--state", source, "verify").stdout)
            self.assertEqual(verified["result"], "PASS")
            self.assertEqual(verified["events"], 3)
            exported = json.loads(self.run_cli("--state", source, "export").stdout)
            self.assertEqual(len(exported["events"]), 3)
            self.run_cli("--state", target, "import", source)
            restored = json.loads(self.run_cli("--state", target, "verify").stdout)
            self.assertEqual(restored["result"], "PASS")
            self.assertEqual(restored["head_hash"], verified["head_hash"])
            self.assertIn("independent_host_import", restored["open_gates"])

    def test_stable_int_in_out_ids_and_reverse_lookup(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "state.json"
            self.run_cli("--state", state_path, "init")
            recorded = json.loads(self.run_cli(
                "--state", state_path, "record", "--input", "owner input", "--output", "assistant output"
            ).stdout)
            self.assertEqual(recorded["result"], "RECORDED_AND_READ_BACK")
            self.assertEqual(recorded["readback"], "PASS")
            self.assertRegex(recorded["interaction_id"], r"^INT-[0-9]{8}-001$")
            self.assertRegex(recorded["input_id"], r"^IN-[0-9]{8}-001$")
            self.assertRegex(recorded["output_id"], r"^OUT-[0-9]{8}-001$")
            for anchor in (recorded["input_id"], recorded["output_id"]):
                found = json.loads(self.run_cli("--state", state_path, "lookup", "--id", anchor).stdout)
                self.assertEqual(found["result"], "FOUND")
                self.assertEqual(found["record"]["interaction_record"]["input_id"], recorded["input_id"])
                self.assertEqual(found["record"]["interaction_record"]["output_id"], recorded["output_id"])

    def test_interaction_record_matches_repository_json_schema_when_validator_available(self):
        try:
            from jsonschema import Draft202012Validator, FormatChecker
        except ImportError:
            self.skipTest("jsonschema is installed by the portable conformance workflow")
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "state.json"
            self.run_cli("--state", state_path, "init")
            self.run_cli("--state", state_path, "record", "--input", "schema input", "--output", "schema output")
            exported = json.loads(self.run_cli("--state", state_path, "export").stdout)
            record = exported["events"][0]["interaction_record"]
            schema_path = Path(__file__).resolve().parents[3] / "docs/architecture/BEHAVIOR-TRACE/interaction-pair-ledger.schema.json"
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            Draft202012Validator(schema, format_checker=FormatChecker()).validate(record)
            self.assertEqual(record["verification"]["runtime_capture"], "NOT_VERIFIED")

    def test_tampering_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "state.json"
            self.run_cli("--state", state_path, "init")
            self.run_cli("--state", state_path, "record", "--input", "before", "--output", "after")
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["events"][0]["output_text"] = "tampered"
            state_path.write_text(json.dumps(state), encoding="utf-8")
            result = self.run_cli("--state", state_path, "verify", expected=2)
            self.assertIn("hash mismatch", result.stderr)

    def test_empty_input_and_output_rejected_by_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "state.json"
            self.run_cli("--state", state_path, "init")
            self.run_cli("--state", state_path, "record", "--input", " ", "--output", "valid", expected=2)
            self.run_cli("--state", state_path, "record", "--input", "valid", "--output", " ", expected=2)

    def test_import_never_overwrites_existing_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source.json"
            target = root / "target.json"
            self.run_cli("--state", source, "init")
            self.run_cli("--state", target, "init")
            result = self.run_cli("--state", target, "import", source, expected=2)
            self.assertIn("must be new", result.stderr)


if __name__ == "__main__":
    unittest.main()
