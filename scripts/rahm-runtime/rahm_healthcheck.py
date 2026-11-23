#!/usr/bin/env python3
"""Exit non-zero when the RAHM service or its ledger is unhealthy."""
from __future__ import annotations
import argparse, json, sys
from urllib.request import urlopen
from urllib.error import URLError

def main(argv=None) -> int:
    parser=argparse.ArgumentParser(description="RAHM service health probe")
    parser.add_argument("--url",default="http://127.0.0.1:8765/health")
    parser.add_argument("--timeout",type=float,default=4.0)
    args=parser.parse_args(argv)
    try:
        with urlopen(args.url,timeout=args.timeout) as response:
            data=json.loads(response.read().decode("utf-8"))
            if response.status != 200 or data.get("result") != "PASS" or data.get("service") != "RAHM":
                raise ValueError("health endpoint returned an unexpected response")
        print(json.dumps({"result":"HEALTHY","events":data.get("events")}))
        return 0
    except (OSError,ValueError,json.JSONDecodeError,URLError) as exc:
        print(json.dumps({"result":"UNHEALTHY","error":str(exc)}),file=sys.stderr)
        return 1

if __name__=="__main__":
    raise SystemExit(main())
