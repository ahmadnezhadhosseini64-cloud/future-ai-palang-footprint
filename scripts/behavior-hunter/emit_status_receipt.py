#!/usr/bin/env python3
"""Emit a machine-readable terminal status receipt for a project workflow.

This records repository workflow state. It cannot report or instrument the ChatGPT UI,
and it does not prove external persistence or host-wide interaction capture.
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ALLOWED = {"success", "failure", "cancelled", "unknown"}

def build_receipt(*, event_id, pair_id, stage, status, run_id, tested_sha, now=None, next_action=""):
    if status not in ALLOWED:
        raise ValueError(f"invalid_status:{status}")
    instant = now or datetime.now(timezone.utc)
    if instant.tzinfo is None:
        raise ValueError("timestamp_must_be_timezone_aware")
    utc = instant.astimezone(timezone.utc)
    tehran = utc.astimezone(ZoneInfo("Asia/Tehran"))
    return {
        "schema": "PALANG-STATUS-RECEIPT-1.0.0",
        "event_id": event_id,
        "interaction_pair_id": pair_id,
        "stage": stage,
        "status": status.upper(),
        "terminal": True,
        "workflow_run_id": str(run_id) if run_id else None,
        "tested_commit_sha": tested_sha or None,
        "timestamps": {
            "utc": utc.isoformat().replace("+00:00", "Z"),
            "tehran": tehran.isoformat(),
            "canonical": "UTC",
            "tehran_derived_from_same_instant": True,
        },
        "next_action": next_action,
        "scope": "repository_workflow_status_only",
        "chat_ui_heartbeat_proven": False,
        "host_wide_capture_proven": False,
        "external_persistence_proven": False,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event-id", required=True)
    parser.add_argument("--pair-id", required=True)
    parser.add_argument("--stage", default="CI_TERMINAL")
    parser.add_argument("--status", choices=sorted(ALLOWED), required=True)
    parser.add_argument("--run-id", default="")
    parser.add_argument("--tested-sha", default="")
    parser.add_argument("--next-action", default="")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    receipt = build_receipt(event_id=args.event_id, pair_id=args.pair_id, stage=args.stage,
                            status=args.status, run_id=args.run_id, tested_sha=args.tested_sha,
                            next_action=args.next_action)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"event_id": args.event_id, "pair_id": args.pair_id,
                      "status": receipt["status"], "terminal": True,
                      "chat_ui_heartbeat_proven": False}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
