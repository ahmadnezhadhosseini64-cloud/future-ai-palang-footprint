#!/usr/bin/env python3
"""Recover HAIF interaction graph from either IN-026 or OUT-026.

Repository-state recovery only; this does not claim runtime capture or external persistence.
"""
import argparse
import json
from pathlib import Path

PAIR = {
    "IN": {"id": "IN-026", "path": "docs/0.0/anchors/PALANG-0.0-IN-20261023-026-REGISTER-ACTIVE-CONTINUATION.md", "paired_id": "OUT-026", "paired_path": "docs/0.0/anchors/PALANG-0.0-OUT-20261023-026-REGISTER-ACTIVE-CONTINUATION.md"},
    "OUT": {"id": "OUT-026", "path": "docs/0.0/anchors/PALANG-0.0-OUT-20261023-026-REGISTER-ACTIVE-CONTINUATION.md", "paired_id": "IN-026", "paired_path": "docs/0.0/anchors/PALANG-0.0-IN-20261023-026-REGISTER-ACTIVE-CONTINUATION.md"},
}
NODES = {
    "event": "docs/architecture/BEHAVIOR-TRACE/EVT-0121-REGISTER-ACTIVE-CONTINUATION-AND-COLD-START-RESULT-2026-10-23.md",
    "active_gate": "docs/architecture/BEHAVIOR-TRACE/EVT-0122-BIDIRECTIONAL-IN-OUT-RECOVERY-2026-10-23.md",
    "checkpoint": "docs/0.0/anchors/PALANG-0.0-NEXT-20261023-024-CONTINUITY-HISTORIC-AND-COLD-START.md",
    "master": "docs/reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md",
    "queue": "docs/architecture/INTEGRATION-QUEUE/README.md",
    "evidence": "data/interaction-pairs/evidence/EVT-0120-RESOLVER-SMOKE-EVIDENCE.txt",
}
OPEN_GAPS = [
    {"id": "Issue #20", "meaning": "runtime capture and end-to-end recovery", "status": "OPEN"},
    {"id": "Issue #21", "meaning": "historic source census and semantic reconciliation", "status": "OPEN"},
]
NEXT_ACTIONS = [
    "Run both recovery directions on the exact final main HEAD and inspect both JSON manifests.",
    "Perform and separately record a fresh ChatGPT session recovery; do not infer it from repository CI.",
    "Continue historic source census / Issue #21 and runtime capture / Issue #20 without replacing prior 0.0 anchors.",
]

def recover(start, repo_root):
    start = str(start).strip().upper()
    if start not in PAIR:
        return {"status": "BLOCKED", "reason": "start_must_be_IN_or_OUT", "start": start}
    spec = PAIR[start]
    root = Path(repo_root).resolve()
    failures, content = [], {}
    paths = {spec["id"]: spec["path"], spec["paired_id"]: spec["paired_path"], **NODES}
    for name, relative in paths.items():
        target = root / relative
        if not target.is_file():
            failures.append({"node": name, "reason": "missing_required_file", "path": relative})
            continue
        try:
            content[name] = target.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            failures.append({"node": name, "reason": "unreadable_required_file", "path": relative, "detail": str(exc)})
    if spec["id"] in content and spec["paired_id"] in content:
        a, b = content[spec["id"]], content[spec["paired_id"]]
        if spec["paired_id"] not in a:
            failures.append({"node": spec["id"], "reason": "paired_anchor_link_missing"})
        if spec["id"] not in b:
            failures.append({"node": spec["paired_id"], "reason": "reverse_pair_link_missing"})
        if "INT-20261023-026" not in a or "INT-20261023-026" not in b:
            failures.append({"node": "interaction_pair", "reason": "pair_identity_missing_or_mismatched"})
    required = {
        "event": ["IN-026", "OUT-026", "EVT-0122"],
        "active_gate": ["IN-026", "OUT-026", "NEXT-024", "CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md", "INTEGRATION-QUEUE/README.md", "EVT-0120-RESOLVER-SMOKE-EVIDENCE.txt"],
        "checkpoint": ["IN-026", "OUT-026", "EVT-0121", "EVT-0122", "Issue #20", "Issue #21"],
        "master": ["EVT-0121", "EVT-0122", "IN-026", "OUT-026"],
        "queue": ["EVT-0122", "IN-026", "OUT-026"],
    }
    for node, markers in required.items():
        if node in content:
            for marker in markers:
                if marker not in content[node]:
                    failures.append({"node": node, "reason": "required_reference_missing", "reference": marker})
    graph = {
        "starting_anchor": {"id": spec["id"], "path": spec["path"]},
        "paired_anchor": {"id": spec["paired_id"], "path": spec["paired_path"]},
        **{key: {"path": value, "present": key in content} for key, value in NODES.items()},
    }
    return {
        "resolver": "PALANG-BIDIRECTIONAL-INTERACTION-RECOVERY-1.0.0",
        "status": "RECOVERED" if not failures else "PARTIAL",
        "scope": "repository_state_only",
        "starting_anchor": spec["id"],
        "paired_anchor": spec["paired_id"],
        "interaction_id": "INT-20261023-026",
        "graph": graph,
        "open_gaps": OPEN_GAPS,
        "next_actions": NEXT_ACTIONS,
        "failures": failures,
        "host_wide_capture_proven": False,
        "fresh_chatgpt_session_test": "NOT RUN",
        "external_persistence_proven": False,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", required=True, choices=("IN", "OUT", "in", "out"))
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    report = recover(args.start, args.repo_root)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0 if report["status"] == "RECOVERED" else 1

if __name__ == "__main__":
    raise SystemExit(main())
