import json, os, socket, subprocess, sys, tempfile, time, unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

RUNTIME=Path(__file__).resolve().parents[1]/"rahm_runtime.py"
SERVICE=Path(__file__).resolve().parents[1]/"rahm_service.py"
TOKEN="test-token-that-is-at-least-32-characters-long"

def make_haif():
    import hashlib
    event={"event_id":"EVT-http-test","kind":"INTERACTION","created_at_utc":"2026-11-23T00:00:00Z",
           "parent_hash":"0"*64,"input":"hello","output":"world"}
    event["event_hash"]=hashlib.sha256(json.dumps(event,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
    return {"schema":"haif-runtime-state/1.0","events":[event]}

class ServiceTests(unittest.TestCase):
    def test_authenticated_http_ingest_and_health(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger=Path(tmp)/"ledger.json"
            init=subprocess.run([sys.executable,str(RUNTIME),"--ledger",str(ledger),"init"],capture_output=True,text=True)
            self.assertEqual(init.returncode,0,init.stderr)
            with socket.socket() as sock:
                sock.bind(("127.0.0.1",0)); port=sock.getsockname()[1]
            env=os.environ.copy(); env["RAHM_API_TOKEN"]=TOKEN
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
                payload=json.dumps(make_haif()).encode()
                unauth=Request(base+"/v1/haif/ingest",data=payload,headers={"Content-Type":"application/json"},method="POST")
                with self.assertRaises(HTTPError) as err: urlopen(unauth,timeout=2)
                self.assertEqual(err.exception.code,401)
                auth=Request(base+"/v1/haif/ingest",data=payload,headers={"Content-Type":"application/json","Authorization":"Bearer "+TOKEN},method="POST")
                with urlopen(auth,timeout=2) as response:
                    result=json.loads(response.read())
                self.assertEqual(result["added"],1)
                with urlopen(auth,timeout=2) as response:
                    replay=json.loads(response.read())
                self.assertEqual(replay["added"],0)
            finally:
                proc.terminate()
                try: proc.wait(timeout=3)
                except subprocess.TimeoutExpired: proc.kill()
            status=subprocess.run([sys.executable,str(RUNTIME),"--ledger",str(ledger),"verify"],capture_output=True,text=True)
            self.assertEqual(status.returncode,0,status.stderr)
            self.assertEqual(json.loads(status.stdout)["events"],1)

if __name__=="__main__":
    unittest.main()
