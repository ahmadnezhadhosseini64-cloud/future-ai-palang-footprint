#!/usr/bin/env python3
"""External execution controller for Future AI / Palang Footprint."""
import json
import os
import pathlib
import subprocess
import sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_DIR = ROOT / "control-plane" / "state"
RECOVERY_DIR = ROOT / "control-plane" / "recovery"
EVIDENCE_DIR = ROOT / "control-plane" / "evidence"
REQUIRED = ["registered", "persisted", "read_back_verified", "revived", "architecturally_placed", "executed"]


def load_state(path):
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
    payload = {"stable_id": sid, "status": "PENDING / UNVERIFIED", "recorded_at": datetime.now(timezone.utc).isoformat(), "exact_gap": errors, "required_transition": "RETRIEVE -> RECONCILE SAME ID -> COMPLETE MISSING GATES -> READ-BACK -> VERIFY -> REVIVE/ABSORB -> ARCHITECTURAL PLACEMENT -> CLOSE"}
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


def write_runtime_proof(state):
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    sid = state["stable_id"]
    out = EVIDENCE_DIR / f"RUNTIME-PROOF-{sid}.json"
    payload = {"stable_id": sid, "reference_point": "0.0", "status": "RUNTIME VERIFIED", "controller": "control-plane/controller.py", "verified_at_utc": datetime.now(timezone.utc).isoformat(), "evidence": ["GitHub Actions runner executed controller.py successfully", "controller loaded canonical state", "all required gates validated", "controller wrote this proof record from the runner"], "next_state": "CLOSED"}
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    subprocess.run(["git", "config", "user.name", "palang-execution-controller"], cwd=ROOT, check=True)
    subprocess.run(["git", "config", "user.email", "actions@users.noreply.github.com"], cwd=ROOT, check=True)
    subprocess.run(["git", "add", str(out.relative_to(ROOT))], cwd=ROOT, check=True)
    result = subprocess.run(["git", "commit", "-m", f"runtime proof: {sid}"], cwd=ROOT, text=True, capture_output=True)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.strip())
    if result.returncode == 0:
        subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=ROOT, check=True)
    return out


def main():
    files = sorted(STATE_DIR.glob("*.json"))
    if not files:
        print("EVIDENCE_GATE=FAIL")
        print("EXECUTION_CONTROLLER=FAIL: no state records")
        return 1
    failed = False
    passed = []
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
            passed.append(state)
    if failed:
        return 1
    for state in passed:
        proof = write_runtime_proof(state)
        print(f"RUNTIME_PROOF={proof}")
        print("STATE=EXECUTED / CLOSED")
    print("EXECUTION_CONTROLLER=PASS")
    print("EVIDENCE_GATE=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
