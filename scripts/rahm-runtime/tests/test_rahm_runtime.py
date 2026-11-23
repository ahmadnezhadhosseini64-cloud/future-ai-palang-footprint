import json, subprocess, sys, tempfile, unittest
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1] / "rahm_runtime.py"
HAIF_GENESIS = "0" * 64

def digest(value):
    import hashlib
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def haif_fixture():
    event = {"event_id":"EVT-test-1","kind":"INTERACTION","created_at_utc":"2026-11-23T00:00:00Z",
             "parent_hash":HAIF_GENESIS,"input":"hello","output":"world"}
    event["event_hash"] = digest(event)
    return {"schema":"haif-runtime-state/1.0","events":[event]}

class RahmTests(unittest.TestCase):
    def cli(self, *args, expected=0):
        result = subprocess.run([sys.executable,str(RUNTIME),*map(str,args)],text=True,capture_output=True)
        self.assertEqual(result.returncode,expected,result.stderr)
        return result
    def test_init_ingest_idempotence_and_verify(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); ledger=root/"rahm.json"; source=root/"haif.json"
            source.write_text(json.dumps(haif_fixture()),encoding="utf-8")
            self.cli("--ledger",ledger,"init")
            first=json.loads(self.cli("--ledger",ledger,"ingest-haif",source).stdout)
            self.assertEqual(first["added"],1)
            second=json.loads(self.cli("--ledger",ledger,"ingest-haif",source).stdout)
            self.assertEqual(second["added"],0)
            self.assertEqual(second["duplicate_skipped"],1)
            status=json.loads(self.cli("--ledger",ledger,"verify").stdout)
            self.assertEqual(status["result"],"PASS")
            data=json.loads(ledger.read_text())
            self.assertEqual(data["events"][0]["authority"],"PROPOSAL_ONLY_NO_MASTER_WRITE")
    def test_reject_tampered_haif_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); ledger=root/"rahm.json"; source=root/"haif.json"
            source.write_text(json.dumps(haif_fixture()),encoding="utf-8")
            self.cli("--ledger",ledger,"init")
            data=json.loads(source.read_text()); data["events"][0]["output"]="tampered"
            source.write_text(json.dumps(data),encoding="utf-8")
            self.cli("--ledger",ledger,"ingest-haif",source,expected=2)
            self.assertEqual(len(json.loads(ledger.read_text())["events"]),0)
    def test_refuse_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger=Path(tmp)/"rahm.json"
            self.cli("--ledger",ledger,"init")
            self.cli("--ledger",ledger,"init",expected=2)

    def test_real_haif_runtime_to_rahm_end_to_end(self):
        haif_cli = Path(__file__).resolve().parents[2] / "haif-runtime" / "haif_runtime.py"
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); haif_state=root/"haif.json"; export=root/"haif-export.json"; ledger=root/"rahm.json"
            def run_haif(*args):
                result=subprocess.run([sys.executable,str(haif_cli),"--state",str(haif_state),*map(str,args)],
                                      text=True,capture_output=True)
                self.assertEqual(result.returncode,0,result.stderr)
                return result
            run_haif("init")
            run_haif("record","--input","real HAIF request","--output","real HAIF response")
            run_haif("checkpoint")
            exported=run_haif("export")
            export.write_text(exported.stdout,encoding="utf-8")
            self.cli("--ledger",ledger,"init")
            ingested=json.loads(self.cli("--ledger",ledger,"ingest-haif",export).stdout)
            self.assertEqual(ingested["added"],2)
            verified=json.loads(self.cli("--ledger",ledger,"verify").stdout)
            self.assertEqual(verified["result"],"PASS")
            # Replaying the same genuine HAIF export must not duplicate RAHM evidence.
            replay=json.loads(self.cli("--ledger",ledger,"ingest-haif",export).stdout)
            self.assertEqual(replay["added"],0)
            self.assertEqual(replay["duplicate_skipped"],2)

if __name__ == "__main__":
    unittest.main()
