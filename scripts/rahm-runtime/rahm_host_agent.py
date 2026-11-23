#!/usr/bin/env python3
"""Push a verified HAIF export from an independent host to a RAHM endpoint."""
from __future__ import annotations
import argparse, json, os, sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from rahm_runtime import verify_haif

def main(argv=None) -> int:
    parser=argparse.ArgumentParser(description="Independent HAIF host → RAHM bridge adapter")
    parser.add_argument("--source",required=True,help="HAIF JSON export file")
    parser.add_argument("--url",required=True,help="RAHM /v1/haif/ingest endpoint; HTTPS required off-loopback")
    parser.add_argument("--host-id",required=True,help="stable operator-assigned host label; not an identity credential")
    parser.add_argument("--timeout",type=float,default=15.0)
    args=parser.parse_args(argv)
    token=os.environ.get("RAHM_API_TOKEN","")
    if len(token)<32:
        print("RAHM_API_TOKEN must be set to at least 32 characters",file=sys.stderr); return 2
    if not args.url.startswith("https://") and not args.url.startswith(("http://127.0.0.1","http://localhost")):
        print("HTTPS is required for non-loopback RAHM endpoints",file=sys.stderr); return 2
    try:
        payload=json.loads(Path(args.source).read_text(encoding="utf-8"))
        errors=verify_haif(payload)
        if errors:
            raise ValueError("HAIF export failed local verification: " + "; ".join(errors))
        body=json.dumps(payload,ensure_ascii=False,separators=(",",":")).encode("utf-8")
        request=Request(args.url,data=body,method="POST",headers={
            "Content-Type":"application/json", "Authorization":"Bearer "+token,
            "X-RAHM-Host-ID":args.host_id})
        with urlopen(request,timeout=args.timeout) as response:
            result=json.loads(response.read().decode("utf-8"))
            if response.status != 200 or result.get("result") != "INGESTED":
                raise ValueError("RAHM endpoint did not confirm ingestion")
        print(json.dumps({"result":"HOST_PUSH_CONFIRMED","host_id":args.host_id,"remote":result},ensure_ascii=False))
        return 0
    except HTTPError as exc:
        print(json.dumps({"result":"REMOTE_REJECTED","http_status":exc.code},ensure_ascii=False),file=sys.stderr); return 3
    except (OSError,ValueError,json.JSONDecodeError,URLError) as exc:
        print(json.dumps({"result":"FAIL","error":str(exc)},ensure_ascii=False),file=sys.stderr); return 2

if __name__=="__main__":
    raise SystemExit(main())
