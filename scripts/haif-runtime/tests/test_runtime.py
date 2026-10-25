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

    def test_tampering_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "state.json"
            self.run_cli("--state", state_path, "init")
            self.run_cli("--state", state_path, "record", "--input", "before", "--output", "after")
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["events"][0]["output"] = "tampered"
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
