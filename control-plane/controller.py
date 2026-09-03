#!/usr/bin/env python3
"""External execution controller for Future AI / Palang Footprint.

The repository is the canonical state store. This controller validates the
state machine and creates a durable recovery record instead of inferring
completion from prose.
"""
import json
import pathlib
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_DIR = ROOT / "control-plane" / "state"
RECOVERY_DIR = ROOT / "control-plane" / "recovery"

REQUIRED = [
    "registered",
    "persisted",
    "read_back_verified",
    "revived",
    "architecturally_placed",
    "executed",
]


def load_state(path: pathlib.Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate(state):
    errors = []
    if not state.get("stable_id"):
        errors.append("missing stable_id")
    if state.get("reference_point") != "0.0":
        errors.append("reference_point must be 0.0")
    gates = state.get("gates", {})
    for gate in REQUIRED:
        if gates.get(gate) is not True:
            errors.append(f"gate not verified: {gate}")
    return errors


def write_recovery(state, errors):
    RECOVERY_DIR.mkdir(parents=True, exist_ok=True)
    sid = state.get("stable_id", "UNKNOWN-STABLE-ID")
    out = RECOVERY_DIR / f"{sid}.json"
    payload = {
        "stable_id": sid,
        "status": "PENDING / UNVERIFIED",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "exact_gap": errors,
        "required_transition": "RETRIEVE -> RECONCILE SAME ID -> COMPLETE MISSING GATES -> READ-BACK -> VERIFY -> REVIVE/ABSORB -> ARCHITECTURAL PLACEMENT -> CLOSE",
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


def main():
    files = sorted(STATE_DIR.glob("*.json"))
    if not files:
        print("EVIDENCE_GATE=FAIL")
        print("EXECUTION_CONTROLLER=FAIL: no state records")
        return 1
    failed = False
    for path in files:
        state = load_state(path)
        errors = validate(state)
        if errors:
            failed = True
            recovery = write_recovery(state, errors)
            print(f"STABLE_ID={state.get('stable_id', 'UNKNOWN')}")
            print("EVIDENCE_GATE=FAIL")
            print("STATE=PENDING / UNVERIFIED")
            print(f"RECOVERY_RECORD={recovery}")
        else:
            print(f"STABLE_ID={state['stable_id']}")
            print("EVIDENCE_GATE=PASS")
            print("STATE=EXECUTED / CLOSED-ELIGIBLE")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
