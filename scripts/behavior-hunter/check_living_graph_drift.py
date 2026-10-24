#!/usr/bin/env python3
"""Check that the latest interaction pair remains connected to its living graph.

This is a read-only drift detector. It never edits canonical documents and it
reports repository consistency only, not host-wide capture or external persistence.
"""
import argparse
import json
from pathlib import Path

from recover_interaction_graph import recover

MASTER = "docs/reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md"
QUEUE = "docs/architecture/INTEGRATION-QUEUE/README.md"
GLOBAL_INDEX = "docs/REFERENCE_INDEX.md"
ZERO_INDEX = "docs/0.0/README.md"
TRACE_INDEX = "docs/architecture/BEHAVIOR-TRACE/README.md"
OBSERVATORY = "docs/architecture/BEHAVIOR-OBSERVATORY/README.md"

def check_graph(repo_root="."):
    root = Path(repo_root).resolve()
    from_in = recover("IN", root)
    from_out = recover("OUT", root)
    failures = []
    if from_in.get("status") != "RECOVERED":
        failures.append({"check": "recover_from_IN", "status": from_in.get("status"), "failures": from_in.get("failures", [])})
    if from_out.get("status") != "RECOVERED":
        failures.append({"check": "recover_from_OUT", "status": from_out.get("status"), "failures": from_out.get("failures", [])})
    pair_id = from_in.get("interaction_id")
    if pair_id != from_out.get("interaction_id"):
        failures.append({"check": "pair_identity_agreement", "in_pair": pair_id, "out_pair": from_out.get("interaction_id")})
    event = from_in.get("graph", {}).get("event", {})
    checkpoint = from_in.get("graph", {}).get("active_gate", {})
    in_id = from_in.get("starting_anchor") if from_in.get("starting_anchor", "").startswith("IN-") else from_in.get("paired_anchor")
    out_id = from_in.get("paired_anchor") if from_in.get("paired_anchor", "").startswith("OUT-") else from_in.get("starting_anchor")
    event_id = event.get("id")
    next_id = checkpoint.get("id")
    required_markers = [m for m in (in_id, out_id, event_id, next_id) if m]
    paths = {
        "master": MASTER,
        "queue": QUEUE,
        "global_index": GLOBAL_INDEX,
        "zero_index": ZERO_INDEX,
        "trace_index": TRACE_INDEX,
        "observatory": OBSERVATORY,
    }
    checked = []
    for name, relative in paths.items():
        target = root / relative
        if not target.is_file():
            failures.append({"check": name, "reason": "file_missing", "path": relative})
            continue
        text = target.read_text(encoding="utf-8")
        missing = [marker for marker in required_markers if marker not in text]
        checked.append({"node": name, "path": relative, "present": True, "missing_markers": missing})
        if missing:
            failures.append({"check": name, "reason": "current_graph_markers_missing", "path": relative, "markers": missing})
    receipt_dir = root / "docs/architecture/BEHAVIOR-TRACE/STATUS-RECEIPTS"
    receipt_match = None
    if receipt_dir.is_dir() and event_id and pair_id:
        for path in sorted(receipt_dir.glob("*.json")):
            try:
                receipt = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError):
                continue
            if receipt.get("event_id") == event_id and receipt.get("interaction_pair_id") == pair_id:
                receipt_match = {"path": path.relative_to(root).as_posix(), "status": receipt.get("status"), "workflow_run_id": receipt.get("workflow_run_id"), "tested_commit_sha": receipt.get("tested_commit_sha")}
    if receipt_match is None:
        failures.append({"check": "durable_status_receipt", "reason": "matching_receipt_missing", "event_id": event_id, "pair_id": pair_id})
    report = {
        "checker": "PALANG-LIVING-GRAPH-DRIFT-CHECK-1.0.0",
        "status": "PASS" if not failures else "DRIFT_DETECTED",
        "scope": "repository_graph_consistency_only",
        "pair_id": pair_id,
        "input_anchor": in_id,
        "output_anchor": out_id,
        "event_id": event_id,
        "next_checkpoint": next_id,
        "recovery_from_IN": from_in.get("status"),
        "recovery_from_OUT": from_out.get("status"),
        "nodes_checked": checked,
        "durable_status_receipt": receipt_match,
        "failures": failures,
        "canonical_mutation_performed": False,
        "host_wide_capture_proven": False,
        "fresh_session_recovery_proven": False,
        "external_persistence_proven": False,
    }
    return report

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    report = check_graph(args.repo_root)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "pair_id": report["pair_id"], "nodes_checked": len(report["nodes_checked"]), "failures": len(report["failures"])}))
    return 0 if report["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
