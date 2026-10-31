#!/usr/bin/env python3
"""Verify the latest global Point-0/0.0 chain separately from historical overlay recovery."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = ROOT / "docs/0.0/README.md"
MASTER_PATH = ROOT / "docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md"
REFERENCE_INDEX_PATH = ROOT / "docs/REFERENCE_INDEX.md"
BEHAVIOR_INDEX_PATH = ROOT / "docs/architecture/BEHAVIOR-TRACE/README.md"
QUEUE_INDEX_PATH = ROOT / "docs/architecture/INTEGRATION-QUEUE/README.md"
EXPORT_MANIFEST_PATH = ROOT / "docs/portable/RAHM/EXPORT_MANIFEST.json"
PACKAGE_MANIFEST_PATH = ROOT / "prototype/haif-gpt6-starter/manifest.json"
MIRROR_EVENT = "docs/architecture/BEHAVIOR-TRACE/EVT-0241-LIVE-MIRROR-SYNC-RECHECK-2026-10-31.md"
MIRROR_TIME_BINDING = "docs/architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0241-LIVE-MIRROR-SYNC-2026-10-31.md"

PRESERVED_PATHS = {
    "POINT-0/016": "docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-016-MIRROR-DELTA-AND-ARCHITECTURE-RECOVERY.md",
    "POINT-0/017": "docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-017-UNIFIED-PALANG-ARCHITECTURE-HARD-AUDIT.md",
    "POINT-0/018": "docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-018-LIVING-REGISTRATION-AND-NEXT-STEPS.md",
    "EVT-0180": "docs/architecture/BEHAVIOR-TRACE/EVT-0180-USER-POINT-0-018-LIVING-REGISTRATION-AND-NEXT-STEPS-2026-10-25.md",
    "TIME-BINDING-EVT-0180": "docs/architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0180-POINT-0-018-2026-10-25.md",
    "EVT-0177": "docs/architecture/BEHAVIOR-TRACE/EVT-0177-LIVE-MIRROR-SYNC-RECHECK-2026-10-25.md",
    "TIME-BINDING-EVT-0177": "docs/architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0177-LIVE-MIRROR-SYNC-2026-10-25.md",
    "EVT-0178 canonical": "docs/architecture/BEHAVIOR-TRACE/EVT-0178-UNIFIED-PALANG-ARCHITECTURE-HARD-AUDIT-2026-10-25.md",
    "EVT-0178 quarantined draft": "docs/architecture/BEHAVIOR-TRACE/EVT-0178-CURRENT-066-POINTER-RECONCILIATION-2026-10-25.md",
    "EVT-0179 collision record": "docs/architecture/BEHAVIOR-TRACE/EVT-0179-UNIQUE-ID-COLLISION-AND-POINTER-RECONCILIATION-2026-10-25.md",
}

GATE_PATTERNS = {
    "full_state_recovery": [r"full state recovery", r"reconstruct independently from IN and OUT"],
    "clean_host_import": [r"clean host import", r"clean interactive AI-host session"],
    "second_host_import": [r"second[- ]host import", r"second[- ]host acceptance"],
    "restart_persistence": [r"restart persistence", r"restart/new-session recovery"],
    "idle_background_capture": [r"automatic live message capture", r"idle/background capture"],
    "graph_identity_parent_time_triage": [r"graph/identity/parent/time triage", r"duplicate IDs", r"ambiguous parents"],
}


def parse_latest_chain(index_text: str) -> dict[str, object]:
    headings = list(re.finditer(r"^##\s*تازه‌ترین زنجیره\b.*$", index_text, re.MULTILINE))
    if not headings:
        raise ValueError("LATEST_CHAIN_HEADING_NOT_FOUND")
    start = headings[-1].end()
    following = re.search(r"^##\s+", index_text[start:], re.MULTILINE)
    section = index_text[start : start + following.start()] if following else index_text[start:]
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", section)
    required = {"point":"POINT-0/","input":"IN-","output":"OUT-","event":"EVT-","current":"CURRENT-","next":"NEXT-"}
    labels, targets, positions = {}, {}, []
    for key, prefix in required.items():
        matches = [(label.strip(), target.strip()) for label, target in links if label.strip().startswith(prefix)]
        if len(matches) != 1:
            raise ValueError(f"LATEST_CHAIN_{key.upper()}_LINK_COUNT_{len(matches)}")
        labels[key], targets[key] = matches[0]
        positions.append(section.find(f"[{labels[key]}]({targets[key]})"))
    if positions != sorted(positions):
        raise ValueError("LATEST_CHAIN_LINK_ORDER_INVALID")
    return {"labels": labels, "targets": targets, "section": section}


def resolve_local(source_path: Path, target: str) -> Path | None:
    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    resolved = (source_path.parent / unquote(parsed.path)).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        return None
    return resolved


def local_links(source_path: Path, content: str):
    for label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content):
        resolved = resolve_local(source_path, target)
        if resolved is not None:
            yield label.strip(), target.strip(), resolved


def require_one_link(source_path: Path, content: str, suffix: str) -> str:
    matches = [(target, resolved) for _, target, resolved in local_links(source_path, content) if resolved.name == suffix]
    if not matches:
        raise ValueError(f"{source_path.relative_to(ROOT)}: no link to {suffix}")
    unique_paths = {resolved for _, resolved in matches}
    if len(unique_paths) != 1:
        raise ValueError(f"{source_path.relative_to(ROOT)}: ambiguous links to {suffix}; {len(unique_paths)} distinct targets")
    for target, resolved in matches:
        if not resolved.is_file():
            raise ValueError(f"{source_path.relative_to(ROOT)}: broken link {target}")
    # Repeated navigation links are acceptable only when every occurrence resolves
    # to the same canonical file. This avoids treating repeated index links as
    # ambiguous while still rejecting same-name links to different destinations.
    return matches[0][0]


def read_text(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(path.relative_to(ROOT).as_posix())
    return path.read_text(encoding="utf-8")


def has_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def main() -> int:
    failures = []
    try:
        index_text = read_text(INDEX_PATH)
        chain = parse_latest_chain(index_text)
        paths = {key: resolve_local(INDEX_PATH, target) for key, target in chain["targets"].items()}
        for key, path in paths.items():
            if path is None or not path.is_file():
                failures.append(f"current_chain_{key}_missing")
        if failures:
            raise ValueError(";".join(failures))

        point_path, in_path, out_path = paths["point"], paths["input"], paths["output"]
        event_path, current_path, next_path = paths["event"], paths["current"], paths["next"]
        docs = {
            "point": read_text(point_path),
            "in": read_text(in_path),
            "out": read_text(out_path),
            "event": read_text(event_path),
            "current": read_text(current_path),
            "next": read_text(next_path),
            "mirror_event": read_text(ROOT / MIRROR_EVENT),
            "mirror_time_binding": read_text(ROOT / MIRROR_TIME_BINDING),
            "master": read_text(MASTER_PATH),
            "reference_index": read_text(REFERENCE_INDEX_PATH),
            "behavior_index": read_text(BEHAVIOR_INDEX_PATH),
            "queue_index": read_text(QUEUE_INDEX_PATH),
        }

        markers = [chain["labels"][k] for k in ("point","input","output","event","current","next")]
        expected_by_doc = {
            "point": markers,
            "in": [chain["labels"]["point"],chain["labels"]["output"],chain["labels"]["event"],chain["labels"]["current"],chain["labels"]["next"]],
            "out": [chain["labels"]["point"],chain["labels"]["input"],chain["labels"]["event"],chain["labels"]["current"],chain["labels"]["next"]],
            "event": markers,
            "current": markers,
            "next": [chain["labels"]["point"],chain["labels"]["current"],chain["labels"]["next"],"EVT-0241"],
        }
        for key, expected in expected_by_doc.items():
            for marker in expected:
                if marker not in docs[key]:
                    failures.append(f"{key}_missing_marker_{marker}")

        common_suffixes = {
            "current": current_path.name,
            "next": next_path.name,
            "master": "سند مرجع مادر مدل اولیه هوش مصنوعی.md",
            "protocol": "INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md",
            "package_protocol": "INDEPENDENT_HOST_RECOVERY_PROTOCOL.md",
            "manifest": "EXPORT_MANIFEST.json",
        }
        recovered = {}
        for side, path in (("IN",in_path),("OUT",out_path)):
            content = docs["in" if side=="IN" else "out"]
            state = {key:require_one_link(path,content,suffix) for key,suffix in common_suffixes.items()}
            recovered[side] = state
            for suffix in (point_path.name,event_path.name,next_path.name):
                require_one_link(path,content,suffix)
        if recovered["IN"] != recovered["OUT"]:
            failures.append("IN_OUT_SHARED_TARGETS_MISMATCH")

        for source_path, key in ((current_path,"current"),(next_path,"next")):
            content = docs[key]
            names = [point_path.name,in_path.name,out_path.name,event_path.name,current_path.name,next_path.name]
            for name in names:
                if name == source_path.name:
                    continue
                try:
                    require_one_link(source_path,content,name)
                except Exception:
                    failures.append(f"{source_path.name}_missing_or_broken_link_{name}")
            for name in (Path(MIRROR_EVENT).name,Path(MIRROR_TIME_BINDING).name):
                try:
                    require_one_link(source_path,content,name)
                except Exception:
                    failures.append(f"{source_path.name}_missing_mirror_link_{name}")

        for key in ("master","reference_index","behavior_index","queue_index"):
            for marker in (chain["labels"]["point"],chain["labels"]["current"],chain["labels"]["next"],"EVT-0241","TIME-BINDING-EVT-0241"):
                if marker not in docs[key]:
                    failures.append(f"{key}_missing_{marker}")

        current_text = docs["current"].lower()
        next_text = docs["next"].lower()
        pointer_open = (
            "current-065/current-066" in current_text and "open" in current_text
            and ("no winner selected" in current_text or "no winner is selected" in current_text)
            and "current-065/current-066" in next_text and "open" in next_text
            and "no winner selected" in next_text
        )
        if not pointer_open:
            failures.append("CURRENT_065_066_CONFLICT_NOT_PRESERVED_OPEN")

        open_gates = {}
        for name, patterns in GATE_PATTERNS.items():
            in_next = has_any(docs["next"],patterns)
            in_current = has_any(docs["current"],patterns)
            open_status = bool(re.search(r"OPEN|NOT RUN|NOT VERIFIED|REVIEW_REQUIRED",docs["next"],re.I)) and bool(re.search(r"OPEN|NOT RUN|NOT VERIFIED|REVIEW_REQUIRED",docs["current"],re.I))
            open_gates[name] = {"present_in_NEXT":in_next,"present_in_CURRENT":in_current,"open_status_preserved":open_status}
            if not in_next or not in_current or not open_status:
                failures.append(f"open_gate_not_preserved_{name}")

        for issue in ("Issue #20","Issue #21"):
            if issue not in docs["next"] or issue not in docs["current"]:
                failures.append(f"{issue.replace(' ','_')}_not_preserved")
        for marker in ("POINT-0/016","POINT-0/017","POINT-0/018"):
            if marker not in index_text:
                failures.append(f"historical_root_not_preserved_{marker}")

        preserved = {label:(ROOT/rel).is_file() for label,rel in PRESERVED_PATHS.items()}
        for label, exists in preserved.items():
            if not exists:
                failures.append(f"preserved_history_missing_{label}")

        package = json.loads(read_text(PACKAGE_MANIFEST_PATH))
        parents = package.get("parent_architecture",[])
        for marker in markers:
            if not any(marker in str(x) for x in parents):
                failures.append(f"package_parent_architecture_missing_{marker}")
        identity = {
            "stable_id":package.get("stable_id"),
            "version":package.get("version"),
            "canonical_filename":package.get("archive_policy",{}).get("canonical_filename"),
        }
        if identity["stable_id"]!="HAIF-GPT6-PORTABLE-STARTER-20261025-004" or identity["version"]!="0.3.8":
            failures.append("portable_package_identity_or_version_changed")
        if not any("NEXT-051" in str(x) for x in parents):
            failures.append("package_parent_architecture_missing_NEXT_051")

        export_manifest=json.loads(read_text(EXPORT_MANIFEST_PATH))
        live=set(export_manifest.get("live_reference_files",[]))
        required_live={
            point_path.relative_to(ROOT).as_posix(),in_path.relative_to(ROOT).as_posix(),
            out_path.relative_to(ROOT).as_posix(),event_path.relative_to(ROOT).as_posix(),
            current_path.relative_to(ROOT).as_posix(),next_path.relative_to(ROOT).as_posix(),
            MIRROR_EVENT,MIRROR_TIME_BINDING,
            "scripts/behavior-hunter/verify_latest_current_0_0_chain.py",
            "scripts/behavior-hunter/tests/test_verify_latest_current_0_0_chain.py",
        }
        for path in sorted(required_live-live):
            failures.append(f"export_manifest_live_reference_missing_{path}")

        result={
            "test_id":f"RAHM-LATEST-CURRENT-0-0-RECONSTRUCTION-{chain['labels']['current']}",
            "status":"PASS" if not failures else "FAIL",
            "result":"PASS" if not failures else "FAIL",
            "latest_chain":{k:chain["labels"][k] for k in ("point","input","output","event","current","next")},
            "in_out_shared_targets":recovered,
            "open_gates":open_gates,
            "pointer_conflict":{"CURRENT-065/CURRENT-066":"OPEN","winner_selected":False},
            "preserved_history":preserved,
            "package_identity":identity,
            "package_sync_status":"SOURCE_MANIFEST_ALIGNED_PENDING_EXACT_SHA_CONFORMANCE",
            "release_ready":False,
            "external_host_acceptance":"NOT_RUN",
            "buffer":"NOT_VERIFIED",
            "persistent_memory":"NOT_VERIFIED",
            "dropbox":"OPEN / NOT VERIFIED",
            "scope":"Repository current-chain reconstruction and linked-reference equivalence only; no independent-host import, restart persistence, background execution or external-destination acceptance.",
            "failures":failures,
        }
        outdir=ROOT/"audit-output"
        outdir.mkdir(parents=True,exist_ok=True)
        (outdir/"latest-current-0-0-recovery-verification.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        portable={
            "test_id":f"RAHM-IN-OUT-LINK-EQUIVALENCE-{chain['labels']['input'].split('-')[-1]}-{chain['labels']['output'].split('-')[-1]}",
            "result":result["result"],
            "recovered_from":f"{chain['labels']['input']} and {chain['labels']['output']} independently",
            "canonical_state":recovered,
            "open_gates_preserved":all(v["present_in_NEXT"] and v["present_in_CURRENT"] and v["open_status_preserved"] for v in open_gates.values()),
            "scope":result["scope"],
        }
        Path("rahm-recovery-equivalence.json").write_text(json.dumps(portable,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        print(json.dumps(result,indent=2,ensure_ascii=False))
        print("LATEST_CURRENT_0_0_RECONSTRUCTION="+result["result"])
        return 0 if not failures else 1
    except Exception as exc:
        print(f"LATEST_CURRENT_0_0_RECONSTRUCTION=FAIL: {exc}",file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
