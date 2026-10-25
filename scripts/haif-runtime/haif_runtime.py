#!/usr/bin/env python3
"""Small dependency-free HAIF continuity runtime (local JSON state, append-only hash chain).

This is a runnable local reference implementation, not a cloud sync service or an AI-host plugin.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA = "haif-runtime-state/1.0"
GENESIS = "0" * 64
OPEN_GATES = [
    "independent_host_import",
    "cross_device_persistence",
    "automatic_chat_capture",
    "background_execution",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def new_state(project: str = "Future AI / Palang Footprint") -> dict:
    return {
        "schema": SCHEMA,
        "project": project,
        "state_id": "STATE-" + uuid.uuid4().hex,
        "created_at_utc": utc_now(),
        "updated_at_utc": utc_now(),
        "events": [],
        "checkpoint": None,
        "open_gates": list(OPEN_GATES),
    }


def event_payload(event: dict) -> dict:
    return {k: v for k, v in event.items() if k != "event_hash"}


def verify_state(state: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(state, dict) or state.get("schema") != SCHEMA:
        return ["schema must equal " + SCHEMA]
    if not isinstance(state.get("state_id"), str) or not state["state_id"]:
        errors.append("state_id is required")
    events = state.get("events")
    if not isinstance(events, list):
        return errors + ["events must be an array"]
    previous_hash = GENESIS
    seen = set()
    for i, event in enumerate(events):
        prefix = f"events[{i}]"
        if not isinstance(event, dict):
            errors.append(prefix + " must be an object")
            continue
        for field in ("event_id", "kind", "created_at_utc", "parent_hash", "event_hash"):
            if not isinstance(event.get(field), str) or not event[field]:
                errors.append(f"{prefix}.{field} is required")
        if event.get("event_id") in seen:
            errors.append(f"{prefix}.event_id is duplicated")
        seen.add(event.get("event_id"))
        if event.get("parent_hash") != previous_hash:
            errors.append(f"{prefix}.parent_hash does not match previous event")
        expected = digest(event_payload(event))
        if event.get("event_hash") != expected:
            errors.append(f"{prefix}.event_hash mismatch")
        if event.get("kind") == "INTERACTION":
            if not isinstance(event.get("input"), str) or not event["input"].strip():
                errors.append(f"{prefix}.input must be non-empty")
            if not isinstance(event.get("output"), str) or not event["output"].strip():
                errors.append(f"{prefix}.output must be non-empty")
        elif event.get("kind") not in ("CHECKPOINT", "IMPORT"):
            errors.append(f"{prefix}.kind is unsupported")
        previous_hash = event.get("event_hash", previous_hash)
    checkpoint = state.get("checkpoint")
    if checkpoint is not None:
        if not isinstance(checkpoint, dict):
            errors.append("checkpoint must be an object or null")
        elif checkpoint.get("event_count") != len(events):
            errors.append("checkpoint event_count does not match event list")
        elif checkpoint.get("head_hash") != (events[-1]["event_hash"] if events else GENESIS):
            errors.append("checkpoint head_hash does not match event chain")
    if state.get("open_gates") != OPEN_GATES:
        errors.append("open_gates must preserve all explicitly unimplemented capabilities")
    return errors


def append_event(state: dict, kind: str, **fields: Any) -> dict:
    parent = state["events"][-1]["event_hash"] if state["events"] else GENESIS
    event = {
        "event_id": "EVT-" + uuid.uuid4().hex,
        "kind": kind,
        "created_at_utc": utc_now(),
        "parent_hash": parent,
        **fields,
    }
    event["event_hash"] = digest(event)
    state["events"].append(event)
    state["updated_at_utc"] = utc_now()
    return event


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def save_state(path: Path, state: dict) -> None:
    errors = verify_state(state)
    if errors:
        raise ValueError("refusing to save invalid state: " + "; ".join(errors))
    atomic_write(path, (json.dumps(state, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def load_state(path: Path) -> dict:
    state = json.loads(path.read_text(encoding="utf-8"))
    errors = verify_state(state)
    if errors:
        raise ValueError("invalid state: " + "; ".join(errors))
    return state


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local HAIF append-only continuity runtime")
    parser.add_argument("--state", default="haif-state.json", help="local JSON state path")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init", help="create a new state file")
    record = sub.add_parser("record", help="append one IN/OUT interaction")
    record.add_argument("--input", required=True)
    record.add_argument("--output", required=True)
    cp = sub.add_parser("checkpoint", help="append a checkpoint and pin current chain head")
    export = sub.add_parser("export", help="print the validated portable JSON state")
    imp = sub.add_parser("import", help="validate and import a JSON state file")
    imp.add_argument("source")
    sub.add_parser("verify", help="verify schema, parent links and event hashes")
    args = parser.parse_args(argv)
    path = Path(args.state)
    try:
        if args.command == "init":
            if path.exists():
                raise ValueError(f"{path} already exists; refusing to overwrite")
            state = new_state()
            save_state(path, state)
            print(json.dumps({"result": "INITIALIZED", "state": str(path), "state_id": state["state_id"]}))
        elif args.command == "import":
            incoming = load_state(Path(args.source))
            if path.exists():
                raise ValueError(f"{path} already exists; import target must be new to avoid silent overwrite")
            save_state(path, incoming)
            print(json.dumps({"result": "IMPORTED_AND_VERIFIED", "state": str(path), "events": len(incoming["events"])}))
        else:
            state = load_state(path)
            if args.command == "record":
                event = append_event(state, "INTERACTION", input=args.input, output=args.output)
                save_state(path, state)
                print(json.dumps({"result": "RECORDED", "event_id": event["event_id"], "event_hash": event["event_hash"], "events": len(state["events"])}))
            elif args.command == "checkpoint":
                checkpoint_id = "CHECKPOINT-" + uuid.uuid4().hex
                checkpoint_event = append_event(state, "CHECKPOINT", checkpoint_id=checkpoint_id)
                state["checkpoint"] = {
                    "checkpoint_id": checkpoint_id,
                    "created_at_utc": checkpoint_event["created_at_utc"],
                    "event_count": len(state["events"]),
                    "head_hash": checkpoint_event["event_hash"],
                }
                save_state(path, state)
                print(json.dumps({"result": "CHECKPOINTED", **state["checkpoint"], "open_gates": state["open_gates"]}))
            elif args.command == "export":
                sys.stdout.write(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
            elif args.command == "verify":
                print(json.dumps({"result": "PASS", "events": len(state["events"]), "head_hash": state["events"][-1]["event_hash"] if state["events"] else GENESIS, "checkpoint": state["checkpoint"], "open_gates": state["open_gates"]}))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"result": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
