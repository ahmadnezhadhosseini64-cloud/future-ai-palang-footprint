#!/usr/bin/env python3
"""Verify the current canonical Point-0/0.0 repository chain from IN and OUT.

This is a repository-state/link equivalence check, not proof of a real external AI-host import.
"""
from pathlib import Path
import json
import re
import sys
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[2]
OUTDIR = ROOT / "audit-output"
OUTDIR.mkdir(exist_ok=True)

FILES = {
    "point": "docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-20261028-056-0PLUS-INPLACE-UPDATE-VERSION-GOVERNANCE.md",
    "in": "docs/0.0/anchors/PALANG-0.0-IN-20261028-094-POINT-056-INPLACE-VERSION-GOVERNANCE.md",
    "out": "docs/0.0/anchors/PALANG-0.0-OUT-20261028-093-POINT-056-INPLACE-VERSION-GOVERNANCE.md",
    "event": "docs/architecture/BEHAVIOR-TRACE/EVT-0231-POINT-056-INPLACE-VERSION-GOVERNANCE-2026-10-28.md",
    "current": "docs/0.0/anchors/PALANG-0.0-CURRENT-20261028-106-INPLACE-VERSION-GOVERNANCE.md",
    "next": "docs/0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md",
    "master": "docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md",
    "index": "docs/REFERENCE_INDEX.md",
    "queue": "docs/architecture/INTEGRATION-QUEUE/README.md",
    "package_manifest": "prototype/haif-gpt6-starter/manifest.json",
    "package_protocol": "prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md",
}
CHAIN = ["POINT-0/056", "IN-094", "OUT-093", "EVT-0231", "CURRENT-106", "NEXT-051"]
OPEN_GATES = {
    "full_state_recovery": ("full project evidence reconstruction", "open proof gates"),
    "clean_host_import": ("clean independent AI-host import", "open proof gates"),
    "second_host_import": ("second AI-host import", "open proof gates"),
    "persistence_restart": ("restart persistence", "open proof gates"),
    "idle_background": ("automatic live message capture", "open proof gates"),
    "graph_triage": ("ambiguous parent", "open proof gates"),
}

def read(key):
    path = ROOT / FILES[key]
    if not path.is_file():
        raise FileNotFoundError(FILES[key])
    return path.read_text(encoding="utf-8")

def links(text):
    return [m.group(2).strip().split()[0].strip("<>") for m in re.finditer(r"!??\[([^\]]*)\]\(([^)]+)\)", text)]

def link_exists(key, text, fragment):
    src = ROOT / FILES[key]
    matches = [target for target in links(text) if fragment.casefold() in target.casefold()]
    if not matches:
        return False
    for target in matches:
        parsed = urlparse(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        dest = (src.parent / unquote(parsed.path)).resolve()
        if not dest.is_file():
            return False
    return True

def main():
    docs = {key: read(key) for key in FILES}
    failures = []
    expected_links = {
        "point": [("in", "PALANG-0.0-IN-20261028-094"), ("out", "PALANG-0.0-OUT-20261028-093"),
                  ("event", "EVT-0231-POINT-056"), ("current", "PALANG-0.0-CURRENT-20261028-106"), ("next", "PALANG-0.0-NEXT-20261024-051")],
        "in": [("out", "PALANG-0.0-OUT-20261028-093"), ("event", "EVT-0231-POINT-056"),
               ("current", "PALANG-0.0-CURRENT-20261028-106"), ("next", "PALANG-0.0-NEXT-20261024-051")],
        "out": [("in", "PALANG-0.0-IN-20261028-094"), ("event", "EVT-0231-POINT-056"),
                ("current", "PALANG-0.0-CURRENT-20261028-106"), ("next", "PALANG-0.0-NEXT-20261024-051")],
        "event": [("point", "GPT6-RAHM-USER-POINT-0-20261028-056"), ("in", "PALANG-0.0-IN-20261028-094"),
                  ("out", "PALANG-0.0-OUT-20261028-093"), ("current", "PALANG-0.0-CURRENT-20261028-106"),
                  ("next", "PALANG-0.0-NEXT-20261024-051")],
        "current": [("point", "GPT6-RAHM-USER-POINT-0-20261028-056"), ("in", "PALANG-0.0-IN-20261028-094"),
                    ("out", "PALANG-0.0-OUT-20261028-093"), ("event", "EVT-0231-POINT-056"),
                    ("next", "PALANG-0.0-NEXT-20261024-051")],
    }
    for source, checks in expected_links.items():
        for target_key, fragment in checks:
            if not link_exists(source, docs[source], fragment):
                failures.append({"check":"required_link_missing_or_broken","source":source,"target":target_key,"fragment":fragment})
    for key in ("point", "in", "out", "event", "current"):
        for target in links(docs[key]):
            parsed = urlparse(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            if not (ROOT / FILES[key]).parent.joinpath(unquote(parsed.path)).resolve().is_file():
                failures.append({"check":"broken_local_link","source":key,"target":target})
    canonical = " → ".join(CHAIN)
    for key in ("point", "out", "event", "current", "master", "index", "queue", "package_protocol"):
        if "POINT-0/056" not in docs[key] or "CURRENT-106" not in docs[key] or "NEXT-051" not in docs[key]:
            failures.append({"check":"canonical_chain_not_visible","source":key})
    manifest = json.loads(docs["package_manifest"])
    if manifest.get("version") != "0.3.8" or manifest.get("supersedes") != "0.3.7":
        failures.append({"check":"package_version_governance","version":manifest.get("version"),"supersedes":manifest.get("supersedes")})
    if manifest.get("stable_id") != "HAIF-GPT6-PORTABLE-STARTER-20261025-004":
        failures.append({"check":"package_stable_id_changed"})
    if manifest.get("archive_policy", {}).get("canonical_filename") != "haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip":
        failures.append({"check":"canonical_zip_filename_changed"})
    architecture = manifest.get("parent_architecture", [])
    positions = []
    for marker in CHAIN:
        try:
            positions.append(architecture.index(marker))
        except ValueError:
            failures.append({"check":"manifest_chain_marker_missing","marker":marker})
    if len(positions) == len(CHAIN) and positions != sorted(positions):
        failures.append({"check":"manifest_current_chain_order","positions":positions})
    next_text = docs["next"].casefold()
    current_text = docs["current"].casefold()
    gates = {}
    for name, (next_marker, current_marker) in OPEN_GATES.items():
        in_next = next_marker.casefold() in next_text
        in_current = ("open / not run" in current_text or "not verified" in current_text or "open proof gates" in current_text)
        gates[name] = {"present_in_NEXT":in_next,"current_checkpoint_preserves_open_status":in_current,"preserved_open":in_next and in_current}
        if not gates[name]["preserved_open"]:
            failures.append({"check":"open_gate_not_preserved","gate":name,"state":gates[name]})
    result = {
        "test_id":"RAHM-CURRENT-106-IN-OUT-STATE-RECOVERY-2026-10-28-001",
        "scope":"Current repository-chain reconstruction from IN and OUT anchors; not real external-host acceptance.",
        "canonical_chain":canonical,
        "version":"0.3.8",
        "stable_id":manifest.get("stable_id"),
        "open_gates":gates,
        "failures":failures,
        "status":"PASS" if not failures else "FAIL",
    }
    (OUTDIR / "current-0-0-recovery-verification.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False))
    return 0 if not failures else 1

if __name__ == "__main__":
    sys.exit(main())
