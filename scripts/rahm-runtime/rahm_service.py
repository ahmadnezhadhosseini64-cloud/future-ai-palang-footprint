#!/usr/bin/env python3
"""Authenticated local HTTP bridge for continuous HAIF-to-RAHM evidence intake."""
from __future__ import annotations
import argparse, hmac, json, os, re, signal, sys, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from rahm_runtime import append, atomic_write, load, verify_haif, verify_ledger

MAX_BODY = 2 * 1024 * 1024

def handler_for(ledger_path: Path, token: str):
    class Handler(BaseHTTPRequestHandler):
        server_version = "RAHM-Bridge/0.3"
        def log_message(self, fmt, *args):
            sys.stderr.write("RAHM bridge: " + (fmt % args) + "\n")
        def send_json(self, status, payload):
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status); self.send_header("Content-Type","application/json; charset=utf-8")
            self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
        def do_GET(self):
            if self.path != "/health":
                return self.send_json(404, {"result":"NOT_FOUND"})
            try:
                ledger=load(ledger_path)
                return self.send_json(200, {"result":"PASS","service":"RAHM","events":len(ledger["events"]),
                                            "authority":"PROPOSAL_ONLY_NO_MASTER_WRITE"})
            except Exception:
                return self.send_json(503, {"result":"UNAVAILABLE"})
        def do_POST(self):
            if self.path != "/v1/haif/ingest":
                return self.send_json(404, {"result":"NOT_FOUND"})
            supplied=self.headers.get("Authorization","")
            if not hmac.compare_digest(supplied, "Bearer " + token):
                return self.send_json(401, {"result":"UNAUTHORIZED"})
            try:
                length=int(self.headers.get("Content-Length","0"))
                if length <= 0 or length > MAX_BODY:
                    return self.send_json(413, {"result":"INVALID_BODY_SIZE","max_bytes":MAX_BODY})
                source=json.loads(self.rfile.read(length).decode("utf-8"))
                errors=verify_haif(source)
                if errors:
                    return self.send_json(422, {"result":"SOURCE_REJECTED","errors":errors})
                host_id=self.headers.get("X-RAHM-Host-ID","UNSPECIFIED")
                if not re.fullmatch(r"[A-Za-z0-9._-]{1,64}", host_id):
                    return self.send_json(400, {"result":"INVALID_HOST_ID"})
                ledger=load(ledger_path)
                added=sum(1 for event in source["events"] if append(ledger,event,host_id) is not None)
                errors=verify_ledger(ledger)
                if errors:
                    return self.send_json(500, {"result":"LEDGER_INVALID","errors":errors})
                atomic_write(ledger_path,ledger)
                return self.send_json(200, {"result":"INGESTED","added":added,
                                            "total":len(ledger["events"]),
                                            "duplicate_skipped":len(source["events"])-added,
                                            "source_host_id":host_id})
            except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
                return self.send_json(400, {"result":"INVALID_JSON"})
            except Exception:
                return self.send_json(500, {"result":"INTERNAL_ERROR"})
    return Handler

def main(argv=None):
    p=argparse.ArgumentParser(description="Authenticated local RAHM ingestion service")
    p.add_argument("--ledger",default="rahm-ledger.json")
    p.add_argument("--host",default="127.0.0.1",help="defaults to loopback; use only behind a hardened TLS proxy for remote hosts")
    p.add_argument("--port",type=int,default=8765)
    args=p.parse_args(argv)
    token=os.environ.get("RAHM_API_TOKEN","")
    if len(token)<32:
        print("RAHM_API_TOKEN must be set to at least 32 characters",file=sys.stderr); return 2
    path=Path(args.ledger)
    if not path.exists():
        print("ledger does not exist; initialize it with rahm_runtime.py init first",file=sys.stderr); return 2
    try:
        load(path)
        server=ThreadingHTTPServer((args.host,args.port),handler_for(path,token))
        def request_shutdown(_signum, _frame):
            threading.Thread(target=server.shutdown,daemon=True).start()
        signal.signal(signal.SIGTERM,request_shutdown)
        print(f"RAHM bridge listening on {args.host}:{args.port}; ledger={path}",flush=True)
        try:
            server.serve_forever(poll_interval=0.5)
        finally:
            server.server_close()
        return 0
    except OSError as exc:
        print(f"RAHM bridge failed: {exc}",file=sys.stderr); return 2
    except KeyboardInterrupt:
        return 0

if __name__=="__main__":
    raise SystemExit(main())
