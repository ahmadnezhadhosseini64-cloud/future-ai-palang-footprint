#!/usr/bin/env python3
"""Small dependency-free HAIF continuity runtime (local JSON state, append-only hash chain).

This is a runnable local reference implementation, not a cloud sync service or an AI-host plugin.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
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
            input_text = event.get("input_text")
            output_text = event.get("output_text")
            if not isinstance(input_text, str) or not input_text.strip():
                errors.append(f"{prefix}.input_text must be non-empty")
            if not isinstance(output_text, str) or not output_text.strip():
                errors.append(f"{prefix}.output_text must be non-empty")
            record = event.get("interaction_record")
            if not isinstance(record, dict):
                errors.append(f"{prefix}.interaction_record must be an object")
            else:
                required = ("interaction_id", "input_id", "output_id", "sequence", "version", "status",
                            "time_evidence", "input", "output", "behavior_analysis", "lineage", "verification")
                for field in required:
                    if field not in record:
                        errors.append(f"{prefix}.interaction_record.{field} is required")
                sequence = record.get("sequence")
                created = event.get("created_at_utc", "")
                date_part = created[:10].replace("-", "") if isinstance(created, str) else ""
                if not isinstance(sequence, int) or sequence < 1 or sequence > 999:
                    errors.append(f"{prefix}.interaction_record.sequence must be 1..999")
                elif date_part:
                    suffix = f"{date_part}-{sequence:03d}"
                    expected = {
                        "interaction_id": f"INT-{suffix}",
                        "input_id": f"IN-{suffix}",
                        "output_id": f"OUT-{suffix}",
                    }
                    for field, value in expected.items():
                        if record.get(field) != value:
                            errors.append(f"{prefix}.interaction_record.{field} does not match sequence/date")
                for field in ("interaction_id", "input_id", "output_id"):
                    value = record.get(field)
                    if not isinstance(value, str) or not re.fullmatch(r"(?:INT|IN|OUT)-[0-9]{8}-[0-9]{3}", value):
                        errors.append(f"{prefix}.interaction_record.{field} has invalid stable ID format")
                    elif value in seen:
                        errors.append(f"{prefix}.interaction_record.{field} is duplicated")
                    else:
                        seen.add(value)
                input_record = record.get("input")
                output_record = record.get("output")
                if not isinstance(input_record, dict) or input_record.get("content_status") != "PRESERVED" or input_record.get("summary") != input_text:
                    errors.append(f"{prefix}.interaction_record.input does not match preserved input")
                if not isinstance(output_record, dict) or output_record.get("content_status") != "PRESERVED" or output_record.get("summary") != output_text:
                    errors.append(f"{prefix}.interaction_record.output does not match preserved output")
                time_evidence = record.get("time_evidence")
                if not isinstance(time_evidence, dict) or time_evidence.get("operation_timestamp") != created:
                    errors.append(f"{prefix}.interaction_record.time_evidence operation timestamp mismatch")
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
    created_at = utc_now()
    if kind == "INTERACTION":
        input_text = fields.pop("input_text", None)
        output_text = fields.pop("output_text", None)
        date_part = created_at[:10].replace("-", "")
        sequence = 1 + sum(
            1 for existing in state["events"]
            if existing.get("kind") == "INTERACTION"
            and isinstance(existing.get("interaction_record"), dict)
            and existing["interaction_record"].get("interaction_id", "").startswith(f"INT-{date_part}-")
        )
        if sequence > 999:
            raise ValueError("daily interaction sequence exhausted (maximum 999)")
        suffix = f"{date_part}-{sequence:03d}"
        fields.update({
            "input_text": input_text,
            "output_text": output_text,
            "interaction_record": {
                "interaction_id": f"INT-{suffix}",
                "input_id": f"IN-{suffix}",
                "output_id": f"OUT-{suffix}",
                "sequence": sequence,
                "version": "1.0.0",
                "status": "OBSERVED",
                "time_evidence": {
                    "repository_commit_utc": None,
                    "tehran_equivalent": None,
                    "operation_timestamp": created_at,
                    "message_timestamp_status": "NOT_EXPOSED",
                },
                "input": {"content_ref": None, "content_status": "PRESERVED", "summary": input_text},
                "output": {"content_ref": None, "content_status": "PRESERVED", "summary": output_text},
                "behavior_analysis": [],
                "lineage": {
                    "parent_ids": [],
                    "related_event_ids": [],
                    "architecture_refs": [],
                    "gap_ids": [],
                    "evidence_refs": [],
                    "recovery_pointer": None,
                },
                "verification": {
                    "schema_validation": "NOT_RUN",
                    "readback": "NOT_RUN",
                    "runtime_capture": "NOT_VERIFIED",
                    "notes": ["Manual local CLI record; automatic host capture is not implemented."],
                },
            },
        })
    event = {
        "event_id": "EVT-" + uuid.uuid4().hex,
        "kind": kind,
        "created_at_utc": created_at,
        "parent_hash": parent,
        **fields,
    }
    event["event_hash"] = digest(event)
    state["events"].append(event)
    state["updated_at_utc"] = utc_now()
    return event


def lookup_interaction(state: dict, anchor_id: str) -> dict | None:
    for event in state.get("events", []):
        record = event.get("interaction_record", {})
        if anchor_id in (record.get("interaction_id"), record.get("input_id"), record.get("output_id")):
            return event
    return None


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
    record = sub.add_parser("record", help="append one stable INT/IN/OUT interaction")
    record.add_argument("--input", required=True)
    record.add_argument("--output", required=True)
    lookup = sub.add_parser("lookup", help="reverse-lookup an interaction by INT, IN or OUT ID")
    lookup.add_argument("--id", required=True)
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
                event = append_event(state, "INTERACTION", input_text=args.input, output_text=args.output)
                save_state(path, state)
                readback = load_state(path)
                verified = lookup_interaction(readback, event["interaction_record"]["input_id"])
                if verified != event:
                    raise ValueError("interaction read-back mismatch")
                record = event["interaction_record"]
                print(json.dumps({
                    "result": "RECORDED_AND_READ_BACK",
                    "event_id": event["event_id"],
                    "interaction_id": record["interaction_id"],
                    "input_id": record["input_id"],
                    "output_id": record["output_id"],
                    "sequence": record["sequence"],
                    "event_hash": event["event_hash"],
                    "events": len(state["events"]),
                    "readback": "PASS",
                    "automatic_host_capture": "NOT_IMPLEMENTED",
                }))
            elif args.command == "lookup":
                found = lookup_interaction(state, args.id)
                if found is None:
                    print(json.dumps({"result": "NOT_FOUND", "anchor_id": args.id}))
                    return 3
                print(json.dumps({"result": "FOUND", "record": found}, ensure_ascii=False))
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
