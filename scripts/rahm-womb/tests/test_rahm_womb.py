import json, threading, unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from rahm_womb import OpenAICompatibleProvider, RahmWomb

GOOD={"analysis":"Evidence is incomplete.","proposed_actions":["Collect a reproducible test."],
"risks":["Source may be stale."],"verification_plan":["Read back and rerun."],
"unresolved_questions":["Which commit is authoritative?"]}

class FakeProvider:
    model_name="test-model"
    def generate(self,system_prompt,user_prompt):
        self.prompts=(system_prompt,user_prompt)
        return json.dumps(GOOD)

class Handler(BaseHTTPRequestHandler):
    seen={}
    def do_POST(self):
        n=int(self.headers.get("Content-Length","0"))
        Handler.seen={"path":self.path,"auth":self.headers.get("Authorization"),
                      "payload":json.loads(self.rfile.read(n))}
        body=json.dumps({"choices":[{"message":{"content":json.dumps(GOOD)}}]}).encode()
        self.send_response(200); self.send_header("Content-Length",str(len(body)))
        self.end_headers(); self.wfile.write(body)
    def log_message(self,*args): pass

class WombTests(unittest.TestCase):
    def test_owner_gate_and_no_master_write(self):
        p=FakeProvider(); r=RahmWomb(p).reason("Audit proposal","Safe excerpt")
        self.assertEqual(r.disposition,"OWNER_REVIEW_REQUIRED")
        self.assertFalse(r.master_written)
        self.assertEqual(r.model,"test-model")
        self.assertIn("untrusted",p.prompts[0].lower())
    def test_task_required_and_size_limited(self):
        w=RahmWomb(FakeProvider())
        with self.assertRaises(ValueError): w.reason(" ")
        with self.assertRaises(ValueError): w.reason("x"*12001)
    def test_context_size_limited(self):
        with self.assertRaises(ValueError): RahmWomb(FakeProvider()).reason("ok","x"*40001)
    def test_invalid_json_rejected(self):
        class Bad:
            model_name="bad"
            def generate(self,*a): return "not-json"
        with self.assertRaisesRegex(RuntimeError,"valid JSON"): RahmWomb(Bad()).reason("test")
    def test_schema_rejected(self):
        class Bad:
            model_name="bad"
            def generate(self,*a): return json.dumps({"analysis":"only"})
        with self.assertRaisesRegex(RuntimeError,"proposed_actions"): RahmWomb(Bad()).reason("test")
    def test_real_http_contract_and_no_tools(self):
        server=HTTPServer(("127.0.0.1",0),Handler)
        t=threading.Thread(target=server.serve_forever,daemon=True); t.start()
        try:
            p=OpenAICompatibleProvider(f"http://127.0.0.1:{server.server_port}/v1","test-key","test-model")
            self.assertTrue(p.generate("system","user"))
            self.assertEqual(Handler.seen["path"],"/v1/chat/completions")
            self.assertEqual(Handler.seen["auth"],"Bearer test-key")
            self.assertNotIn("tools",Handler.seen["payload"])
        finally:
            server.shutdown(); t.join(timeout=2); server.server_close()
    def test_remote_http_rejected(self):
        with self.assertRaises(ValueError): OpenAICompatibleProvider("http://example.com/v1","k","m")

if __name__=="__main__": unittest.main()
