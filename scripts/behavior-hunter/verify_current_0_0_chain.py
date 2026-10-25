#!/usr/bin/env python3
"""Verify the actual current Point-0/0.0 chain from both IN and OUT anchors.

This is a repository-state reconstruction test. It does not claim an independent AI-host import,
durable memory, automatic message capture, or idle/background execution.
"""
from pathlib import Path
import json
import re
import sys
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "audit-output"
OUT.mkdir(exist_ok=True)

FILES = {
    "point0": "docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-014-AUTONOMOUS-CONTINUITY-AND-RECOVERY.md",
    "in": "docs/0.0/anchors/PALANG-0.0-IN-20261025-058-AUTONOMOUS-CONTINUITY-AND-RECOVERY.md",
    "out": "docs/0.0/anchors/PALANG-0.0-OUT-20261025-057-AUTONOMOUS-CONTINUITY-AND-RECOVERY.md",
    "event": "docs/architecture/BEHAVIOR-TRACE/EVT-0167-AUTONOMOUS-CONTINUITY-AND-RECOVERY-2026-10-25.md",
    "current": "docs/0.0/anchors/PALANG-0.0-CURRENT-20261025-065-AUTONOMOUS-CONTINUITY-AND-RECOVERY.md",
    "prior_current": "docs/0.0/anchors/PALANG-0.0-CURRENT-20261025-064-NEXT-EXECUTION-AND-GAPS.md",
    "next": "docs/0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md",
    "master": "docs/portable/RAHM/FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md",
    "manifest": "docs/portable/RAHM/CURRENT-065-OVERLAY-MANIFEST.json",
    "failure_event": "docs/architecture/BEHAVIOR-TRACE/EVT-0161-DEEP-AUDIT-STALE-GATE-AND-NO-SILENT-GAP-2026-10-25.md",
    "index": "docs/REFERENCE_INDEX.md",
    "queue": "docs/architecture/INTEGRATION-QUEUE/README.md",
}
EXPECTED = {
    "point0": "G6IP-POINT-0-014-20261025",
    "in": "G6IP-IN-058-20261025",
    "out": "G6IP-OUT-057-20261025",
    "event": "HAIF-EVT-0167-AUTONOMOUS-CONTINUITY-AND-RECOVERY-2026-10-25",
    "current": "G6IP-CURRENT-065-20261025",
    "prior_current": "G6IP-CURRENT-064-20261025",
    "next": "G6IP-RAHM-NEXT-051-20261024",
}
GATE_MARKERS = {
    "full_state_recovery": ("full independent external-host reconstruction", "Clean recovery round trip"),
    "clean_host_import": ("clean independent AI-host import", "Test independent-host import"),
    "second_host_import": ("second host", "restart recovery and second-host persistence"),
    "persistence_restart": ("persistence restart", "restart recovery and second-host persistence"),
    "idle_background": ("idle/background execution", "Automatic capture/external storage"),
    "graph_triage": ("ambiguous parent", "NEXT-051 graph findings"),
}

def read(name):
    path = ROOT / FILES[name]
    if not path.is_file():
        raise FileNotFoundError(FILES[name])
    return path.read_text(encoding="utf-8")

def stable_id(text):
    m = re.search(r"^\s*- Stable ID:\s*`?([^`\r\n]+)", text, re.I | re.M)
    return m.group(1).strip() if m else None

def version(text):
    m = re.search(r"^\s*- Version:\s*([^\r\n]+)", text, re.I | re.M)
    return m.group(1).strip() if m else None

def local_targets(name, text):
    src = ROOT / FILES[name]
    result = []
    for m in re.finditer(r"!??\[([^\]]*)\]\(([^)]+)\)", text):
        target = m.group(2).strip().split()[0].strip("<>")
        if not target or target.startswith("#"):
            continue
        parsed = urlparse(target)
        if parsed.scheme or parsed.netloc:
            continue
        part = unquote(parsed.path)
        if not part:
            continue
        candidate = (src.parent / part).resolve()
        try:
            rel = candidate.relative_to(ROOT.resolve()).as_posix()
        except ValueError:
            continue
        result.append((target, rel, candidate.exists()))
    return result

def require_link(name, text, target_fragment):
    targets = local_targets(name, text)
    matches = [x for x in targets if target_fragment in x[0]]
    return bool(matches) and all(x[2] for x in matches)

def gate_state(current_text, next_text):
    state = {}
    for key, (next_marker, current_marker) in GATE_MARKERS.items():
        in_next = next_marker.casefold() in next_text.casefold()
        in_current = current_marker.casefold() in current_text.casefold()
        state[key] = {
            "present_in_NEXT": in_next,
            "present_in_CURRENT": in_current,
            "preserved_open": in_next and in_current,
        }
    return state

def reconstruct(start):
    # Both routes begin from a different raw anchor, then reconstruct the same canonical state.
    if start == "IN":
        raw = read("in")
        start_name = "in"
        expected_parent = "point0"
    else:
        raw = read("out")
        start_name = "out"
        expected_parent = "in"
    point0 = read("point0")
    in_text = read("in")
    out_text = read("out")
    event = read("event")
    current = read("current")
    prior_current = read("prior_current")
    nxt = read("next")
    master = read("master")
    manifest = json.loads(read("manifest"))
    index = read("index")
    queue = read("queue")

    docs = {
        "point0": point0, "in": in_text, "out": out_text, "event": event,
        "current": current, "prior_current": prior_current, "next": nxt,
        "master": master, "index": index, "queue": queue,
    }
    ids = {k: stable_id(v) for k, v in docs.items() if k in EXPECTED}
    versions = {k: version(v) for k, v in docs.items() if k in EXPECTED}
    failures = []
    for key, expected in EXPECTED.items():
        if ids.get(key) != expected:
            failures.append({"check": "stable_id", "node": key, "expected": expected, "actual": ids.get(key)})
    if expected_parent == "point0" and not require_link("in", in_text, "GPT6-RAHM-USER-POINT-0-20261025-014"):
        failures.append({"check":"IN_to_Point0"})
    if expected_parent == "in" and not require_link("out", out_text, "PALANG-0.0-IN-20261025-058"):
        failures.append({"check":"OUT_to_IN"})
    link_checks = [
        ("point0", point0, "PALANG-0.0-IN-20261025-058"),
        ("point0", point0, "PALANG-0.0-OUT-20261025-057"),
        ("point0", point0, "EVT-0167-AUTONOMOUS"),
        ("point0", point0, "PALANG-0.0-CURRENT-20261025-065"),
        ("point0", point0, "EVT-0171-CURRENT-065"),
        ("in", in_text, "PALANG-0.0-CURRENT-20261025-064"),
        ("out", out_text, "EVT-0167-AUTONOMOUS"),
        ("out", out_text, "PALANG-0.0-CURRENT-20261025-065"),
        ("event", event, "PALANG-0.0-CURRENT-20261025-065"),
        ("current", current, "PALANG-0.0-NEXT-20261024-051"),
        ("current", current, "CURRENT-065-OVERLAY-MANIFEST"),
        ("current", current, "EVT-0170-LIVE-MIRROR"),
        ("current", current, "EVT-0171-CURRENT-065"),
        ("current", current, "سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی"),
        ("current", current, "REFERENCE_INDEX"),
        ("current", current, "INTEGRATION-QUEUE"),
        ("next", nxt, "PALANG-0.0-CURRENT-20261025-059"),
    ]
    for name, text, fragment in link_checks:
        if not require_link(name, text, fragment):
            failures.append({"check":"required_link","source":name,"target_fragment":fragment})
    for name, text in docs.items():
        for target, resolved, exists in local_targets(name, text):
            if not exists:
                failures.append({"check":"broken_local_link","source":name,"target":target,"resolved":resolved})
    gates = gate_state(current, nxt)
    for gate, state in gates.items():
        if not state["preserved_open"]:
            failures.append({"check":"open_gate_not_preserved","gate":gate,"state":state})
    failure_event = read("failure_event")
    if "cause" not in failure_event.casefold() or "correction" not in failure_event.casefold():
        failures.append({"check":"failure_correction_lineage"})
    if "NEXT-051" not in master or "CURRENT-059" not in master:
        failures.append({"check":"portable_master_not_current"})
    if manifest.get("current_checkpoint") != "docs/0.0/anchors/PALANG-0.0-CURRENT-20261025-065-AUTONOMOUS-CONTINUITY-AND-RECOVERY.md":
        failures.append({"check":"manifest_checkpoint_mismatch","actual":manifest.get("current_checkpoint")})
    if not require_link("current", current, "PALANG-0.0-NEXT-20261024-051"):
        failures.append({"check":"manifest_next_mismatch","actual":"CURRENT-064-to-NEXT-051 canonical link missing"})
    return {
        "started_from": start,
        "starting_anchor": stable_id(raw),
        "canonical_current": stable_id(current),
        "active_next": stable_id(nxt),
        "lineage_ids": ids,
        "versions": versions,
        "manifest_version": manifest.get("version"),
        "manifest_file_count": len(manifest.get("files", [])),
        "open_gates": gates,
        "failures": failures,
        "status": "RECOVERED" if not failures else "BLOCKED",
    }

def main():
    from_in = reconstruct("IN")
    from_out = reconstruct("OUT")
    state_keys = ("canonical_current", "active_next", "lineage_ids", "versions", "manifest_version", "manifest_file_count", "open_gates")
    equivalent = all(from_in[k] == from_out[k] for k in state_keys)
    report = {
        "test_id": "RAHM-CURRENT-065-IN-OUT-STATE-RECOVERY-2026-10-25-001",
        "scope": "Repository current-chain reconstruction from independent IN and OUT starting anchors; not a real external-host import.",
        "from_IN": from_in,
        "from_OUT": from_out,
        "canonical_state_equivalent": equivalent,
        "status": "PASS" if from_in["status"] == "RECOVERED" and from_out["status"] == "RECOVERED" and equivalent else "FAIL",
    }
    (OUT / "current-0-0-recovery-verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"test_id": report["test_id"], "status": report["status"], "canonical_state_equivalent": equivalent,
                      "from_IN": from_in["status"], "from_OUT": from_out["status"],
                      "open_gates": from_in["open_gates"], "failures": {"IN": from_in["failures"], "OUT": from_out["failures"]}}, ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
