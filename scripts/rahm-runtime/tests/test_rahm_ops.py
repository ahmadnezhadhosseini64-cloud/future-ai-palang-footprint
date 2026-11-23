import json, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RUNTIME=ROOT/"rahm_runtime.py"
OPS=ROOT/"rahm_ops.py"

class OpsTests(unittest.TestCase):
    def run_cli(self,*args,expected=0):
        result=subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True)
        self.assertEqual(result.returncode,expected,result.stderr)
        return result

    def test_backup_restore_and_checksum_rejection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); ledger=root/"rahm.json"; backups=root/"backups"; restored=root/"restored.json"
            self.run_cli(RUNTIME,"--ledger",ledger,"init")
            result=json.loads(self.run_cli(OPS,"backup","--source",ledger,"--directory",backups).stdout)
            backup=Path(result["backup"])
            self.assertTrue(backup.exists())
            restored.write_text('{"damaged":true}',encoding="utf-8")
            recovered=json.loads(self.run_cli(OPS,"restore","--source",backup,"--target",restored).stdout)
            self.assertEqual(recovered["result"],"RESTORE_OK")
            verified=json.loads(self.run_cli(RUNTIME,"--ledger",restored,"verify").stdout)
            self.assertEqual(verified["result"],"PASS")
            backup.write_text(backup.read_text(encoding="utf-8")+" ",encoding="utf-8")
            self.run_cli(OPS,"restore","--source",backup,"--target",restored,expected=2)

if __name__=="__main__":
    unittest.main()
