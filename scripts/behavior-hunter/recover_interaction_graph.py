#!/usr/bin/env python3
"""Recover the latest valid HAIF IN/OUT interaction pair from repository state.

The resolver discovers the latest reciprocal pair from the anchors themselves;
it must not keep passing merely because an old hard-coded pair still exists.
Repository-state recovery only: no claim of live-host capture or external persistence.
"""
import argparse
import json
import re
from pathlib import Path

ANCHOR_ROOT = "docs/0.0/anchors"
MASTER = "docs/reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md"
QUEUE = "docs/architecture/INTEGRATION-QUEUE/README.md"
EVIDENCE = "data/interaction-pairs/evidence/EVT-0120-RESOLVER-SMOKE-EVIDENCE.txt"
OPEN_GAPS = [
    {"id": "Issue #20", "meaning": "runtime capture and end-to-end recovery", "status": "OPEN"},
    {"id": "Issue #21", "meaning": "historic source census and semantic reconciliation", "status": "OPEN"},
    {"id": "Issue #19", "meaning": "six real-document ingestion and restart-recovery acceptance", "status": "OPEN"},
]
NEXT_ACTIONS = [
    "Recover the latest reciprocal IN/OUT pair, not a hard-coded historical pair.",
    "Run both recovery directions on the exact source SHA and inspect both JSON manifests.",
    "Perform and separately record fresh-session ChatGPT recovery; do not infer it from repository CI.",
    "Continue open runtime capture, real-document acceptance and historic semantic reconciliation without replacing prior 0.0 anchors.",
]

def _production_id(text):
    m = re.search(r"(?m)^\s*-?\s*Production ID:\s*(IN|OUT)-(\d+)\s*$", text)
    return (m.group(1), int(m.group(2))) if m else None

def _pair_id(text):
    m = re.search(r"(?m)^\s*-?\s*Interaction pair ID:\s*(INT-\d{8}-\d+)\s*$", text)
    return m.group(1) if m else None

def _event_id(text):
    # Prefer the explicitly labeled current/result event. A prior-event reference
    # may appear earlier in the anchor and must not become the current graph root.
    for line in text.splitlines():
        explicit = re.match(
            r"^\s*-?\s*(?:Result event|Event):\s*\[?(EVT-\d{4})\]?",
            line,
            flags=re.IGNORECASE,
        )
        if explicit:
            return explicit.group(1)
    candidates = re.findall(r"\bEVT-\d{4}\b", text)
    return candidates[0] if candidates else None

def discover_latest_pair(root):
    anchor_root = root / ANCHOR_ROOT
    grouped = {}
    if not anchor_root.is_dir():
        return None, [{"node": "anchors", "reason": "anchor_directory_missing", "path": ANCHOR_ROOT}]
    for path in sorted(anchor_root.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        prod = _production_id(text)
        interaction = _pair_id(text)
        if not prod or not interaction:
            continue
        role, number = prod
        grouped.setdefault(interaction, {})[role] = {
            "id": f"{role}-{number:03d}",
            "number": number,
            "path": path.relative_to(root).as_posix(),
            "text": text,
        }
    if not grouped:
        return None, [{"node": "interaction_pair", "reason": "no_pair_identity_found"}]
    interaction = max(grouped, key=lambda value: (value.split("-")[1], int(value.split("-")[2])))
    pair = grouped[interaction]
    if "IN" not in pair or "OUT" not in pair:
        return None, [{"node": "interaction_pair", "reason": "latest_pair_incomplete_no_historical_fallback", "interaction_id": interaction, "roles_found": sorted(pair)}]
    incoming, outgoing = pair["IN"], pair["OUT"]
    if incoming["number"] != outgoing["number"]:
        return None, [{"node": "interaction_pair", "reason": "latest_pair_anchor_number_mismatch", "interaction_id": interaction}]
    if f"OUT-{outgoing['number']:03d}" not in incoming["text"] or f"IN-{incoming['number']:03d}" not in outgoing["text"]:
        return None, [{"node": "interaction_pair", "reason": "latest_pair_not_reciprocal_no_historical_fallback", "interaction_id": interaction}]
    return {"interaction_id": interaction, **pair}, []

def _linked_id(text, prefix):
    vals = re.findall(rf"\b{prefix}-(\d{{3}})\b", text)
    return f"{prefix}-{max(vals, key=int)}" if vals else None

def recover(start, repo_root="."):
    start = str(start).strip().upper()
    if start not in {"IN", "OUT"}:
        return {"status": "BLOCKED", "reason": "start_must_be_IN_or_OUT", "start": start}
    root = Path(repo_root).resolve()
    pair, failures = discover_latest_pair(root)
    if pair is None:
        return {"resolver": "PALANG-LATEST-BIDIRECTIONAL-INTERACTION-RECOVERY-2.0.0", "status": "BLOCKED", "scope": "repository_state_only", "failures": failures}
    incoming, outgoing = pair["IN"], pair["OUT"]
    starting, paired = (incoming, outgoing) if start == "IN" else (outgoing, incoming)
    interaction = pair["interaction_id"]
    current_event_id = _event_id(incoming["text"]) or _event_id(outgoing["text"])
    next_id = _linked_id(incoming["text"] + "\n" + outgoing["text"], "NEXT")
    event_candidates = sorted((root / "docs/architecture/BEHAVIOR-TRACE").glob(f"{current_event_id}-*.md")) if current_event_id else []
    event_path = event_candidates[0].relative_to(root).as_posix() if len(event_candidates) == 1 else None
    next_number = next_id.split("-")[1] if next_id else None
    next_candidates = sorted((root / ANCHOR_ROOT).glob(f"PALANG-0.0-NEXT-*-{next_number}-*.md")) if next_number else []
    checkpoint_path = next_candidates[0].relative_to(root).as_posix() if len(next_candidates) == 1 else None
    nodes = {
        "event": event_path,
        "checkpoint": checkpoint_path,
        "master": MASTER,
        "queue": QUEUE,
        "evidence": EVIDENCE,
    }
    content = {starting["id"]: starting["text"], paired["id"]: paired["text"]}
    if not current_event_id or not event_path:
        failures.append({"node": "event", "reason": "event_reference_missing_or_ambiguous", "event_id": current_event_id})
    if not next_id or not checkpoint_path:
        failures.append({"node": "checkpoint", "reason": "next_checkpoint_missing_or_ambiguous", "checkpoint_id": next_id})
    for name, relative in nodes.items():
        if not relative:
            continue
        target = root / relative
        if not target.is_file():
            failures.append({"node": name, "reason": "missing_required_file", "path": relative})
            continue
        try:
            content[name] = target.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            failures.append({"node": name, "reason": "unreadable_required_file", "path": relative, "detail": str(exc)})
    if "event" in content:
        for marker in (incoming["id"], outgoing["id"]):
            if marker not in content["event"]:
                failures.append({"node": "event", "reason": "current_pair_reference_missing", "reference": marker})
    if "checkpoint" in content:
        for marker in (incoming["id"], outgoing["id"]):
            if marker not in content["checkpoint"]:
                failures.append({"node": "checkpoint", "reason": "current_pair_reference_missing", "reference": marker})
    for node in ("master", "queue"):
        if node in content:
            for marker in (incoming["id"], outgoing["id"], current_event_id or "", next_id or ""):
                if marker and marker not in content[node]:
                    failures.append({"node": node, "reason": "current_graph_reference_missing", "reference": marker})
    graph = {
        "starting_anchor": {"id": starting["id"], "path": starting["path"]},
        "paired_anchor": {"id": paired["id"], "path": paired["path"]},
        "event": {"id": current_event_id, "path": event_path, "present": "event" in content},
        "active_gate": {"id": next_id, "path": checkpoint_path, "present": "checkpoint" in content},
        "master": {"path": MASTER, "present": "master" in content},
        "queue": {"path": QUEUE, "present": "queue" in content},
        "evidence": {"path": EVIDENCE, "present": "evidence" in content},
    }
    return {
        "resolver": "PALANG-LATEST-BIDIRECTIONAL-INTERACTION-RECOVERY-2.0.0",
        "status": "RECOVERED" if not failures else "PARTIAL",
        "scope": "repository_state_only",
        "starting_anchor": starting["id"],
        "paired_anchor": paired["id"],
        "interaction_id": interaction,
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
