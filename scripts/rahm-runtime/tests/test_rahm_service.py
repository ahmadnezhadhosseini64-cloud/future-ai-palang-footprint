import json, os, socket, subprocess, sys, tempfile, time, unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
RUNTIME=ROOT/"rahm_runtime.py"
SERVICE=ROOT/"rahm_service.py"
AGENT=ROOT/"rahm_host_agent.py"
HEALTH=ROOT/"rahm_healthcheck.py"

def make_haif():
    import hashlib
    event={"event_id":"EVT-http-test","kind":"INTERACTION","created_at_utc":"2026-11-23T00:00:00Z",
           "parent_hash":"0"*64,"input":"hello","output":"world"}
    event["event_hash"]=hashlib.sha256(json.dumps(event,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
    return {"schema":"haif-runtime-state/1.0","events":[event]}

class ServiceTests(unittest.TestCase):
    def test_loopback_health_only_and_disabled_host_ingestion(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); ledger=root/"ledger.json"; source=root/"haif-export.json"
            source.write_text(json.dumps(make_haif()),encoding="utf-8")
            init=subprocess.run([sys.executable,str(RUNTIME),"--ledger",str(ledger),"init"],capture_output=True,text=True)
            self.assertEqual(init.returncode,0,init.stderr)
            with socket.socket() as sock:
                sock.bind(("127.0.0.1",0)); port=sock.getsockname()[1]
            remote=subprocess.run([sys.executable,str(SERVICE),"--ledger",str(ledger),"--host","0.0.0.0"],capture_output=True,text=True)
            self.assertEqual(remote.returncode,2)
            self.assertIn("loopback-only",remote.stderr)
            env=os.environ.copy(); env.pop("RAHM_API_TOKEN",None)
            proc=subprocess.Popen([sys.executable,str(SERVICE),"--ledger",str(ledger),"--port",str(port)],
                                  env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            base=f"http://127.0.0.1:{port}"
            try:
                for _ in range(40):
                    try:
                        with urlopen(base+"/health",timeout=0.2) as response:
                            self.assertEqual(json.loads(response.read())["service"],"RAHM")
                        break
                    except Exception:
                        time.sleep(0.1)
                else:
                    self.fail("RAHM service did not become healthy")
                probe=subprocess.run([sys.executable,str(HEALTH),"--url",base+"/health"],capture_output=True,text=True)
                self.assertEqual(probe.returncode,0,probe.stderr)
                payload=json.dumps(make_haif()).encode()
                unauth=Request(base+"/v1/haif/ingest",data=payload,headers={"Content-Type":"application/json"},method="POST")
                with self.assertRaises(HTTPError) as err: urlopen(unauth,timeout=2)
                self.assertEqual(err.exception.code,410)
                response=json.loads(err.exception.read().decode("utf-8"))
                self.assertEqual(response["result"],"DISABLED")
                self.assertEqual(response["reason"],"OWNER_MEDIATED_IMPORT_REQUIRED")
                command=[sys.executable,str(AGENT),"--source",str(source),
                         "--url",base+"/v1/haif/ingest","--host-id","host-independent-01"]
                pushed=subprocess.run(command,env=env,capture_output=True,text=True,timeout=5)
                self.assertEqual(pushed.returncode,4)
                self.assertIn("DISABLED_BY_POINT_0_GOLDEN",pushed.stderr)
                replay=subprocess.run(command,env=env,capture_output=True,text=True,timeout=5)
                self.assertEqual(replay.returncode,4)
                self.assertIn("DISABLED_BY_POINT_0_GOLDEN",replay.stderr)
            finally:
                proc.terminate()
                proc.wait(timeout=3)
            self.assertEqual(proc.returncode,0,"SIGTERM must complete a graceful server shutdown")
            state=json.loads(ledger.read_text(encoding="utf-8"))
            self.assertEqual(len(state["events"]),0)
            status=subprocess.run([sys.executable,str(RUNTIME),"--ledger",str(ledger),"verify"],capture_output=True,text=True)
            self.assertEqual(status.returncode,0,status.stderr)

if __name__=="__main__":
    unittest.main()
