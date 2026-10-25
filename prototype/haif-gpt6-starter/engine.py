#!/usr/bin/env python3
"""HAIF GPT-host starter: local, portable, evidence-first continuity engine.

Standard-library only. This is a local reference engine, not a GPT plugin or cloud service.
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

SCHEMA = "haif-gpt-starter-state/0.1"
GENESIS = "0" * 64
EVIDENCE_CLASSES = {"OBSERVATION", "INFERENCE", "HYPOTHESIS", "UNKNOWN"}
GAP_STATES = {"OPEN", "IN_PROGRESS", "BLOCKED", "CLOSED_VERIFIED"}
CLOSED_PROOF = {"test_id", "tested_revision", "result", "evidence_ref"}


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def digest(value: Any) -> str:
    return sha256_bytes(canonical(value))


def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


def new_state(project: str = "Future AI / Palang Footprint") -> dict:
    return {
        "schema": SCHEMA,
        "project": project,
        "state_id": new_id("HAIF-STATE"),
        "created_at_utc": now_utc(),
        "updated_at_utc": now_utc(),
        "events": [],
        "points": [],
        "gaps": [],
        "children": [],
        "checkpoint": None,
        "capability_boundaries": {
            "automatic_chat_capture": "NOT_PROVEN",
            "independent_gpt_host_import": "NOT_PROVEN",
            "background_execution": "NOT_PROVEN",
            "external_repository_write": "NOT_PROVEN",
            "durable_cross_device_storage": "NOT_PROVEN"
        }
    }


def payload(event: dict) -> dict:
    return {k: v for k, v in event.items() if k != "event_hash"}


def verify_state(state: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(state, dict) or state.get("schema") != SCHEMA:
        return [f"schema must equal {SCHEMA}"]
    if not isinstance(state.get("state_id"), str) or not state["state_id"]:
        errors.append("state_id is required")
    events = state.get("events")
    if not isinstance(events, list):
        return errors + ["events must be an array"]
    previous = GENESIS
    seen = set()
    anchors = set()
    input_ids = set()
    output_ids = set()
    point_registration_events = []
    for i, event in enumerate(events):
        p = f"events[{i}]"
        if not isinstance(event, dict):
            errors.append(f"{p} must be an object")
            continue
        for key in ("event_id", "kind", "created_at_utc", "parent_hash", "event_hash"):
            if not isinstance(event.get(key), str) or not event[key]:
                errors.append(f"{p}.{key} is required")
        eid = event.get("event_id")
        if eid in seen:
            errors.append(f"{p}.event_id duplicate: {eid}")
        seen.add(eid)
        if event.get("parent_hash") != previous:
            errors.append(f"{p}.parent_hash mismatch")
        if event.get("event_hash") != digest(payload(event)):
            errors.append(f"{p}.event_hash mismatch")
        if event.get("kind") == "POINT_REGISTERED":
            point_registration_events.append(event)
        if event.get("kind") == "INTERACTION":
            for key in ("anchor_id", "input_id", "output_id", "input", "output"):
                if not event.get(key):
                    errors.append(f"{p}.{key} is required")
            aid = event.get("anchor_id")
            iid = event.get("input_id")
            oid = event.get("output_id")
            if aid in anchors:
                errors.append(f"{p}.anchor_id duplicate: {aid}")
            if iid in input_ids:
                errors.append(f"{p}.input_id duplicate: {iid}")
            if oid in output_ids:
                errors.append(f"{p}.output_id duplicate: {oid}")
            anchors.add(aid)
            input_ids.add(iid)
            output_ids.add(oid)
        previous = event.get("event_hash", previous)
    points = state.get("points", [])
    if not isinstance(points, list):
        errors.append("points must be an array")
    else:
        point_ids = set()
        labels_seen = {}
        for i, point in enumerate(points):
            p = f"points[{i}]"
            if not isinstance(point, dict):
                errors.append(f"{p} must be an object")
                continue
            pid = point.get("point_id")
            labels = point.get("labels")
            if not isinstance(pid, str) or not pid:
                errors.append(f"{p}.point_id is required")
            prior_point_ids = set(point_ids)
            if pid in point_ids:
                errors.append(f"{p}.point_id duplicate: {pid}")
            point_ids.add(pid)
            if not isinstance(labels, list) or not labels or any(not isinstance(x, str) or not x for x in labels):
                errors.append(f"{p}.labels must be a non-empty string array")
            else:
                if len(set(labels)) != len(labels):
                    errors.append(f"{p}.labels contains duplicate aliases")
                for label in labels:
                    if label in labels_seen and labels_seen[label] != pid:
                        errors.append(f"{p}.label alias collision: {label}")
                    labels_seen[label] = pid
                if "0+" in labels and "0" not in labels:
                    errors.append(f"{p}: 0+ production marker must share the canonical 0 point")
                if "0+" in labels and point.get("production_marker") is not True:
                    errors.append(f"{p}: 0+ requires production_marker=true")
            if point.get("kind") not in {"ROOT", "CONTINUATION"}:
                errors.append(f"{p}.kind is invalid")
            if point.get("kind") == "CONTINUATION" and not point.get("parent_point_id"):
                errors.append(f"{p}: continuation requires parent_point_id")
            if point.get("kind") == "CONTINUATION" and point.get("parent_point_id") not in prior_point_ids:
                errors.append(f"{p}: continuation parent must precede the child")
        point_event_by_id = {}
        for event in point_registration_events:
            pid = event.get("point_id")
            if pid in point_event_by_id:
                errors.append(f"POINT_REGISTERED event duplicates point_id: {pid}")
            point_event_by_id[pid] = event
        point_by_id = {point.get("point_id"): point for point in points if isinstance(point, dict)}
        if set(point_event_by_id) != set(point_by_id):
            errors.append("points and POINT_REGISTERED event ledger do not match")
        for pid in set(point_event_by_id) & set(point_by_id):
            event = point_event_by_id[pid]
            point = point_by_id[pid]
            expected = {
                "labels": event.get("labels"),
                "kind": event.get("point_kind"),
                "parent_point_id": event.get("parent_point_id"),
                "production_marker": event.get("production_marker"),
                "purpose": event.get("purpose"),
                "created_at_utc": event.get("point_created_at_utc")
            }
            for key, value in expected.items():
                if point.get(key) != value:
                    errors.append(f"point {pid} disagrees with event ledger field {key}")
    gaps = state.get("gaps")
    if not isinstance(gaps, list):
        errors.append("gaps must be an array")
    else:
        gap_ids = set()
        for i, gap in enumerate(gaps):
            if not isinstance(gap, dict):
                errors.append(f"gaps[{i}] must be an object")
                continue
            gid = gap.get("gap_id")
            if not isinstance(gid, str) or not gid:
                errors.append(f"gaps[{i}].gap_id is required")
            if gid in gap_ids:
                errors.append(f"gaps[{i}].gap_id duplicate: {gid}")
            gap_ids.add(gid)
            if gap.get("status") not in GAP_STATES:
                errors.append(f"gaps[{i}].status is invalid")
            if gap.get("status") == "CLOSED_VERIFIED":
                proof = gap.get("closure_evidence")
                if not isinstance(proof, dict) or not CLOSED_PROOF.issubset(proof):
                    errors.append(f"gaps[{i}] closed without full closure_evidence")
                elif proof.get("result") != "PASS":
                    errors.append(f"gaps[{i}] closure result must be PASS")
    children = state.get("children")
    if not isinstance(children, list):
        errors.append("children must be an array")
    else:
        for i, child in enumerate(children):
            if not isinstance(child, dict) or child.get("status") not in {"PROPOSED", "VALIDATING", "PROMOTED", "REJECTED", "REVISE"}:
                errors.append(f"children[{i}] has invalid status")
            if isinstance(child, dict) and child.get("status") == "PROMOTED":
                proof = child.get("promotion_evidence")
                if not isinstance(proof, dict) or not CLOSED_PROOF.issubset(proof) or proof.get("result") != "PASS":
                    errors.append(f"children[{i}] promoted without passing promotion_evidence")
    boundaries = state.get("capability_boundaries")
    if not isinstance(boundaries, dict):
        errors.append("capability_boundaries must be an object")
    return errors


def append_event(state: dict, kind: str, **fields: Any) -> dict:
    previous = state["events"][-1]["event_hash"] if state["events"] else GENESIS
    event = {
        "event_id": new_id("EVT"),
        "kind": kind,
        "created_at_utc": now_utc(),
        "parent_hash": previous,
        **fields,
    }
    event["event_hash"] = digest(event)
    state["events"].append(event)
    state["updated_at_utc"] = now_utc()
    return event


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    except Exception:
        try:
            os.unlink(temp)
        except OSError:
            pass
        raise


def save_state(path: Path, state: dict) -> None:
    errors = verify_state(state)
    if errors:
        raise ValueError("refusing invalid state: " + "; ".join(errors))
    atomic_write(path, (json.dumps(state, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def load_state(path: Path) -> dict:
    state = json.loads(path.read_text(encoding="utf-8"))
    errors = verify_state(state)
    if errors:
        raise ValueError("state verification failed: " + "; ".join(errors))
    return state


def record_interaction(state: dict, user_input: str, assistant_output: str,
                       source_ref: str = "current-host", user_message_time_utc: str | None = None) -> dict:
    if not user_input.strip() or not assistant_output.strip():
        raise ValueError("input and output must be non-empty")
    event = append_event(
        state, "INTERACTION",
        anchor_id=new_id("HAIF-ANCHOR"),
        input_id=new_id("HAIF-IN"),
        output_id=new_id("HAIF-OUT"),
        input=user_input,
        output=assistant_output,
        source_ref=source_ref,
        user_message_time_utc=user_message_time_utc,
        evidence_class="OBSERVATION",
        registration_status="WRITE_READBACK_PENDING"
    )
    event["registration_status"] = "WRITE_READBACK_VERIFIED"
    event["event_hash"] = digest(payload(event))
    return event


def register_point(state: dict, point_id: str, labels: list[str], kind: str = "ROOT",
                   parent_point_id: str | None = None, production_marker: bool = False,
                   purpose: str = "") -> dict:
    if not point_id.strip() or not labels or any(not isinstance(x, str) or not x.strip() for x in labels):
        raise ValueError("point_id and non-empty labels are required")
    if len(set(labels)) != len(labels):
        raise ValueError("duplicate aliases within point")
    if kind not in {"ROOT", "CONTINUATION"}:
        raise ValueError("kind must be ROOT or CONTINUATION")
    if "0+" in labels and ("0" not in labels or not production_marker):
        raise ValueError("0+ is a production marker on the same canonical point as 0; include both labels and production_marker=true")
    if kind == "CONTINUATION" and not parent_point_id:
        raise ValueError("continuation requires parent_point_id")
    existing = state.setdefault("points", [])
    if any(p.get("point_id") == point_id for p in existing):
        raise ValueError("duplicate canonical point_id")
    occupied = {label for point in existing for label in point.get("labels", [])}
    if any(label in occupied for label in labels):
        raise ValueError("point label already belongs to another canonical point")
    if parent_point_id and not any(p.get("point_id") == parent_point_id for p in existing):
        raise ValueError("parent point does not exist")
    point = {
        "point_id": point_id, "labels": list(labels), "kind": kind,
        "parent_point_id": parent_point_id, "production_marker": production_marker,
        "purpose": purpose, "created_at_utc": now_utc()
    }
    existing.append(point)
    append_event(state, "POINT_REGISTERED", point_id=point_id, labels=list(labels),
                 point_kind=kind, parent_point_id=parent_point_id,
                 production_marker=production_marker, purpose=purpose,
                 point_created_at_utc=point["created_at_utc"])
    return point


def add_gap(state: dict, title: str, description: str, evidence_class: str = "UNKNOWN",
            source_ref: str | None = None) -> dict:
    if not title.strip() or evidence_class not in EVIDENCE_CLASSES:
        raise ValueError("gap title required and evidence_class must be a known class")
    gap = {
        "gap_id": new_id("HAIF-GAP"),
        "title": title,
        "description": description,
        "evidence_class": evidence_class,
        "source_ref": source_ref,
        "status": "OPEN",
        "created_at_utc": now_utc(),
        "closure_evidence": None
    }
    state["gaps"].append(gap)
    append_event(state, "GAP_OPENED", gap_id=gap["gap_id"], title=title,
                 evidence_class=evidence_class, source_ref=source_ref)
    state["updated_at_utc"] = now_utc()
    return gap


def close_gap(state: dict, gap_id: str, evidence: dict) -> dict:
    gap = next((g for g in state["gaps"] if g.get("gap_id") == gap_id), None)
    if gap is None:
        raise KeyError("GAP_NOT_FOUND")
    if not CLOSED_PROOF.issubset(evidence) or evidence.get("result") != "PASS":
        raise ValueError("closure requires test_id, tested_revision, result=PASS, evidence_ref")
    gap["status"] = "CLOSED_VERIFIED"
    gap["closure_evidence"] = {key: evidence[key] for key in CLOSED_PROOF}
    gap["closed_at_utc"] = now_utc()
    append_event(state, "GAP_CLOSED_VERIFIED", gap_id=gap_id,
                 closure_evidence=gap["closure_evidence"])
    state["updated_at_utc"] = now_utc()
    return gap


def propose_child(state: dict, name: str, parent_ref: str, purpose: str) -> dict:
    if not name.strip() or not parent_ref.strip() or not purpose.strip():
        raise ValueError("child name, parent_ref and purpose are required")
    child = {
        "child_id": new_id("HAIF-CHILD"),
        "name": name,
        "parent_ref": parent_ref,
        "purpose": purpose,
        "status": "PROPOSED",
        "created_at_utc": now_utc(),
        "promotion_evidence": None
    }
    state["children"].append(child)
    append_event(state, "CHILD_PROPOSED", child_id=child["child_id"], name=name,
                 parent_ref=parent_ref, purpose=purpose)
    state["updated_at_utc"] = now_utc()
    return child


def decide_child(state: dict, child_id: str, decision: str, evidence: dict | None = None) -> dict:
    allowed = {"VALIDATING", "REJECTED", "REVISE", "PROMOTED"}
    if decision not in allowed:
        raise ValueError("decision must be VALIDATING, REJECTED, REVISE or PROMOTED")
    child = next((c for c in state["children"] if c.get("child_id") == child_id), None)
    if child is None:
        raise KeyError("CHILD_NOT_FOUND")
    if decision == "PROMOTED":
        if not isinstance(evidence, dict) or not CLOSED_PROOF.issubset(evidence) or evidence.get("result") != "PASS":
            raise ValueError("promotion requires test_id, tested_revision, result=PASS, evidence_ref")
        child["promotion_evidence"] = {key: evidence[key] for key in CLOSED_PROOF}
    child["status"] = decision
    child["updated_at_utc"] = now_utc()
    append_event(state, "CHILD_DECISION", child_id=child_id, decision=decision,
                 promotion_evidence=child.get("promotion_evidence"))
    state["updated_at_utc"] = now_utc()
    return child


def audit(state: dict) -> dict:
    errors = verify_state(state)
    open_gaps = [g for g in state["gaps"] if g.get("status") != "CLOSED_VERIFIED"]
    return {
        "result": "PASS" if not errors else "FAIL",
        "state_id": state.get("state_id"),
        "event_count": len(state.get("events", [])),
        "open_gap_count": len(open_gaps),
        "open_gaps": [{"gap_id": g["gap_id"], "title": g["title"], "status": g["status"]} for g in open_gaps],
        "child_status_counts": {status: sum(1 for c in state.get("children", []) if c.get("status") == status)
                                for status in ("PROPOSED", "VALIDATING", "PROMOTED", "REJECTED", "REVISE")},
        "capability_boundaries": state.get("capability_boundaries", {}),
        "head_hash": state["events"][-1]["event_hash"] if state.get("events") else GENESIS,
        "errors": errors
    }


def export_bundle(state: dict) -> dict:
    errors = verify_state(state)
    if errors:
        raise ValueError("cannot export invalid state: " + "; ".join(errors))
    raw = canonical(state)
    return {
        "bundle_schema": "haif-portable-bundle/0.1",
        "exported_at_utc": now_utc(),
        "payload_sha256": sha256_bytes(raw),
        "payload": state
    }


def import_bundle(bundle: Any) -> dict:
    if not isinstance(bundle, dict) or bundle.get("bundle_schema") != "haif-portable-bundle/0.1":
        raise ValueError("unsupported portable bundle schema")
    state = bundle.get("payload")
    if not isinstance(state, dict):
        raise ValueError("bundle payload missing")
    if bundle.get("payload_sha256") != sha256_bytes(canonical(state)):
        raise ValueError("portable bundle SHA-256 mismatch")
    errors = verify_state(state)
    if errors:
        raise ValueError("portable bundle state invalid: " + "; ".join(errors))
    return state


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="HAIF GPT-host starter (local reference engine)")
    parser.add_argument("--state", default="haif-starter-state.json")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    record = sub.add_parser("record")
    record.add_argument("--input", required=True)
    record.add_argument("--output", required=True)
    record.add_argument("--source-ref", default="current-host")
    gap = sub.add_parser("gap")
    gap.add_argument("--title", required=True)
    gap.add_argument("--description", default="")
    gap.add_argument("--evidence-class", choices=sorted(EVIDENCE_CLASSES), default="UNKNOWN")
    gap.add_argument("--source-ref")
    point = sub.add_parser("point")
    point.add_argument("--point-id", required=True)
    point.add_argument("--labels", required=True, help="Comma-separated aliases for one canonical point")
    point.add_argument("--kind", choices=["ROOT", "CONTINUATION"], default="ROOT")
    point.add_argument("--parent-point-id")
    point.add_argument("--production-marker", action="store_true")
    point.add_argument("--purpose", default="")
    sub.add_parser("audit")
    sub.add_parser("export")
    imp = sub.add_parser("import")
    imp.add_argument("bundle")
    args = parser.parse_args(argv)
    path = Path(args.state)
    try:
        if args.command == "init":
            if path.exists():
                raise ValueError("refusing to overwrite existing state")
            state = new_state()
            save_state(path, state)
            result = {"result": "INITIALIZED", "state_id": state["state_id"], "state_path": str(path)}
        elif args.command == "import":
            bundle = json.loads(Path(args.bundle).read_text(encoding="utf-8"))
            state = import_bundle(bundle)
            if path.exists():
                raise ValueError("refusing to overwrite import target")
            save_state(path, state)
            result = {"result": "IMPORTED_AND_VERIFIED", "state_id": state["state_id"]}
        else:
            state = load_state(path)
            if args.command == "point":
                item = register_point(state, args.point_id, [x.strip() for x in args.labels.split(",") if x.strip()],
                                      args.kind, args.parent_point_id, args.production_marker, args.purpose)
                save_state(path, state)
                result = {"result": "POINT_REGISTERED_AND_READBACK_VERIFIED", **item}
            elif args.command == "record":
                event = record_interaction(state, args.input, args.output, args.source_ref)
                save_state(path, state)
                result = {"result": "RECORDED_AND_READBACK_VERIFIED", "anchor_id": event["anchor_id"],
                          "input_id": event["input_id"], "output_id": event["output_id"], "event_id": event["event_id"]}
            elif args.command == "gap":
                item = add_gap(state, args.title, args.description, args.evidence_class, args.source_ref)
                save_state(path, state)
                result = {"result": "GAP_OPENED", **item}
            elif args.command == "audit":
                result = audit(state)
                if result["result"] != "PASS":
                    print(json.dumps(result, ensure_ascii=False, indent=2), file=sys.stderr)
                    return 2
            elif args.command == "export":
                result = export_bundle(state)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"result": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
