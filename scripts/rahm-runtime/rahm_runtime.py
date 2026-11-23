#!/usr/bin/env python3
"""RAHM evidence-and-learning kernel: deterministic, append-only, owner-governed MVP.

Consumes exported HAIF state. It does not call an LLM, capture chats, or modify MASTER.
"""
from __future__ import annotations
import argparse, hashlib, json, os, sys, tempfile, uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA = "rahm-ledger/0.1"
HAIF_SCHEMA = "haif-runtime-state/1.0"
GENESIS = "0" * 64

def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def sha(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()

def event_body(event: dict) -> dict:
    return {k: v for k, v in event.items() if k != "event_hash"}

def new_ledger() -> dict:
    return {"schema": SCHEMA, "ledger_id": "RAHM-" + uuid.uuid4().hex,
            "created_at_utc": now(), "updated_at_utc": now(),
            "source_system": "HAIF", "source_schema": HAIF_SCHEMA,
            "events": [], "seen_source_hashes": [], "open_gates": [
                "automatic_ai_reasoning", "automatic_chat_capture", "background_wake",
                "independent_host_recovery", "signed_owner_approval", "production_deployment"
            ]}

def verify_haif(source: Any) -> list[str]:
    errors = []
    if not isinstance(source, dict) or source.get("schema") != HAIF_SCHEMA:
        return ["source schema is not " + HAIF_SCHEMA]
    events = source.get("events")
    if not isinstance(events, list):
        return ["source events must be an array"]
    previous, seen = GENESIS, set()
    for i, event in enumerate(events):
        if not isinstance(event, dict):
            errors.append(f"source.events[{i}] must be an object")
            continue
        if event.get("parent_hash") != previous:
            errors.append(f"source.events[{i}] parent hash mismatch")
        if event.get("event_hash") != sha(event_body(event)):
            errors.append(f"source.events[{i}] event hash mismatch")
        if event.get("event_id") in seen:
            errors.append(f"source.events[{i}] duplicate event id")
        seen.add(event.get("event_id"))
        previous = event.get("event_hash", previous)
    return errors

def verify_ledger(ledger: Any) -> list[str]:
    if not isinstance(ledger, dict) or ledger.get("schema") != SCHEMA:
        return ["ledger schema must equal " + SCHEMA]
    errors, previous, seen = [], GENESIS, set()
    events = ledger.get("events")
    if not isinstance(events, list):
        return ["ledger events must be an array"]
    for i, event in enumerate(events):
        if not isinstance(event, dict):
            errors.append(f"events[{i}] must be an object")
            continue
        if event.get("parent_hash") != previous:
            errors.append(f"events[{i}] parent hash mismatch")
        if event.get("event_hash") != sha(event_body(event)):
            errors.append(f"events[{i}] event hash mismatch")
        source_hash = event.get("source_event_hash")
        if not isinstance(source_hash, str) or not source_hash:
            errors.append(f"events[{i}] source_event_hash required")
        elif source_hash in seen:
            errors.append(f"events[{i}] duplicate source event")
        seen.add(source_hash)
        previous = event.get("event_hash", previous)
    if ledger.get("seen_source_hashes") != [e.get("source_event_hash") for e in events]:
        errors.append("seen_source_hashes does not match event ledger")
    return errors

def append(ledger: dict, source_event: dict, source_host_id: str = "HAIF_EXPORT") -> dict:
    source_hash = source_event["event_hash"]
    if source_hash in ledger["seen_source_hashes"]:
        return None
    kind = source_event.get("kind")
    if kind == "INTERACTION":
        assessment = "REVIEW_REQUIRED"
        proposal = "Human review: assess this interaction for a reusable lesson; no automatic learning or promotion."
    elif kind == "CHECKPOINT":
        assessment = "CONTINUITY_MARKER"
        proposal = "Verify the referenced HAIF checkpoint during the next recovery test."
    else:
        assessment = "SOURCE_EVENT_RECORDED"
        proposal = "Classify this source event before operational use."
    event = {"rahm_event_id": "RHE-" + uuid.uuid4().hex,
             "created_at_utc": now(), "source_system": "HAIF",
             "source_host_id": source_host_id,
             "source_event_id": source_event.get("event_id"),
             "source_event_hash": source_hash, "source_kind": kind,
             "assessment": assessment, "proposal": proposal,
             "authority": "PROPOSAL_ONLY_NO_MASTER_WRITE",
             "parent_hash": ledger["events"][-1]["event_hash"] if ledger["events"] else GENESIS}
    event["event_hash"] = sha(event)
    ledger["events"].append(event)
    ledger["seen_source_hashes"].append(source_hash)
    ledger["updated_at_utc"] = now()
    return event

def atomic_write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(value, f, ensure_ascii=False, indent=2)
            f.write("\n"); f.flush(); os.fsync(f.fileno())
        os.replace(tmp, path)
    except Exception:
        try: os.unlink(tmp)
        except OSError: pass
        raise

def load(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = verify_ledger(data)
    if errors: raise ValueError("; ".join(errors))
    return data

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="RAHM evidence kernel — owner-governed local MVP")
    p.add_argument("--ledger", default="rahm-ledger.json")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    ingest = sub.add_parser("ingest-haif", help="consume a verified HAIF JSON export")
    ingest.add_argument("source")
    ingest.add_argument("--source-host-id", default="HAIF_EXPORT")
    sub.add_parser("status")
    sub.add_parser("verify")
    args = p.parse_args(argv); path = Path(args.ledger)
    try:
        if args.command == "init":
            if path.exists(): raise ValueError("ledger already exists; refusing overwrite")
            ledger = new_ledger(); atomic_write(path, ledger)
            print(json.dumps({"result":"INITIALIZED","ledger_id":ledger["ledger_id"]}))
        elif args.command == "ingest-haif":
            source = json.loads(Path(args.source).read_text(encoding="utf-8"))
            errors = verify_haif(source)
            if errors: raise ValueError("HAIF source rejected: " + "; ".join(errors))
            ledger = load(path)
            added = sum(1 for event in source["events"] if append(ledger, event, args.source_host_id) is not None)
            errors = verify_ledger(ledger)
            if errors: raise ValueError("RAHM ledger invalid: " + "; ".join(errors))
            atomic_write(path, ledger)
            print(json.dumps({"result":"INGESTED","added":added,"total":len(ledger["events"]),
                              "duplicate_skipped":len(source["events"])-added,
                              "open_gates":ledger["open_gates"]}))
        elif args.command == "status":
            ledger = load(path)
            print(json.dumps({"result":"PASS","ledger_id":ledger["ledger_id"],
                              "events":len(ledger["events"]),"open_gates":ledger["open_gates"]}))
        elif args.command == "verify":
            ledger = load(path)
            print(json.dumps({"result":"PASS","events":len(ledger["events"]),
                              "head_hash":ledger["events"][-1]["event_hash"] if ledger["events"] else GENESIS}))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"result":"FAIL","error":str(exc)},ensure_ascii=False),file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
