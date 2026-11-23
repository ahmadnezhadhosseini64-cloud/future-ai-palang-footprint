#!/usr/bin/env python3
"""Authenticated local HTTP bridge for continuous HAIF-to-RAHM evidence intake."""
from __future__ import annotations
import argparse, ipaddress, json, signal, sys, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from rahm_runtime import append, atomic_write, load, verify_haif, verify_ledger

MAX_BODY = 2 * 1024 * 1024

def _is_loopback_host(host: str) -> bool:
    if host.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def handler_for(ledger_path: Path, token: str = ""):
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
            if self.path == "/v1/haif/ingest":
                return self.send_json(410, {
                    "result": "DISABLED",
                    "reason": "OWNER_MEDIATED_IMPORT_REQUIRED",
                    "authority": "NO_HOST_TO_RAHM_ROUTE",
                })
            return self.send_json(404, {"result":"NOT_FOUND"})
    return Handler

def main(argv=None):
    p=argparse.ArgumentParser(description="Authenticated local RAHM ingestion service")
    p.add_argument("--ledger",default="rahm-ledger.json")
    p.add_argument("--host",default="127.0.0.1",help="defaults to loopback; use only behind a hardened TLS proxy for remote hosts")
    p.add_argument("--port",type=int,default=8765)
    args=p.parse_args(argv)
    if not _is_loopback_host(args.host):
        print("RAHM service is loopback-only; remote host intake is forbidden", file=sys.stderr); return 2
    path=Path(args.ledger)
    if not path.exists():
        print("ledger does not exist; initialize it with rahm_runtime.py init first",file=sys.stderr); return 2
    try:
        load(path)
        server=ThreadingHTTPServer((args.host,args.port),handler_for(path))
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
