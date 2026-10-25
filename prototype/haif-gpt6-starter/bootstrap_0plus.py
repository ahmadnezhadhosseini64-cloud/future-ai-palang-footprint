#!/usr/bin/env python3
"""One-command bootstrap for the Future AI / Palang Footprint 0+ prototype."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from engine import add_gap, audit, load_state, new_state, register_point, save_state


OPEN_GAPS = [
    ("Independent GPT-6 host import", "Import and run the package in the intended separate GPT-6 host.", "host-import"),
    ("Host Python runtime availability", "Confirm the target host actually exposes a Python execution environment.", "host-python"),
    ("Host durable memory and restart", "Prove state survives a new session/restart in the target host.", "host-persistence"),
    ("Automatic interaction capture", "Prove or explicitly mark unavailable automatic capture of every IN/OUT pair.", "auto-capture"),
    ("External GitHub write permission", "Verify authorized write plus read-back in the target host; current repository access is not inherited.", "github-write"),
    ("Background execution", "Prove host-supported background/idle execution or keep it unavailable.", "background"),
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap canonical 0/0+ root and linked 0.0 continuation.")
    parser.add_argument("--state", default="haif-state.json", help="new state file path; existing files are never overwritten")
    args = parser.parse_args()
    path = Path(args.state)
    if path.exists():
        raise SystemExit(json.dumps({"result": "FAIL", "error": "refusing to overwrite existing state"}, ensure_ascii=False))

    state = new_state()
    root = register_point(
        state, "HAIF-POINT-0-024", ["0", "0+"], kind="ROOT",
        production_marker=True,
        purpose="Important initial architecture production; 0+ is a marker on canonical 0"
    )
    continuation = register_point(
        state, "HAIF-POINT-0-0-071", ["0.0"], kind="CONTINUATION",
        parent_point_id=root["point_id"],
        purpose="First executable continuation from the 0/0+ root"
    )
    for title, description, source in OPEN_GAPS:
        add_gap(state, title, description, evidence_class="UNKNOWN", source_ref=source)

    save_state(path, state)
    readback = load_state(path)
    result = audit(readback)
    if result["result"] != "PASS":
        raise SystemExit(json.dumps({"result": "FAIL", "audit": result}, ensure_ascii=False, indent=2))
    print(json.dumps({
        "result": "BOOTSTRAPPED_AND_READBACK_VERIFIED",
        "state_path": str(path),
        "state_id": readback["state_id"],
        "canonical_root": {"point_id": root["point_id"], "labels": root["labels"]},
        "next_0_0": {"point_id": continuation["point_id"], "parent_point_id": continuation["parent_point_id"]},
        "open_gaps_preserved": len([g for g in readback["gaps"] if g["status"] != "CLOSED_VERIFIED"]),
        "audit": result
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
