# HAIF Local Continuity Runtime v0.1

This is the first runnable, dependency-free implementation of the core loop, not another design document.

## Requirements
- Python 3.10+
- No third-party packages
- A local folder where the process can read/write one JSON state file

## Quick start
```bash
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json init
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json record --input "user input" --output "assistant output"
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json checkpoint
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json verify
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json export > ./haif-export.json
python scripts/haif-runtime/haif_runtime.py --state ./haif-restored.json import ./haif-export.json
python scripts/haif-runtime/haif_runtime.py --state ./haif-restored.json verify
python -m unittest discover -s scripts/haif-runtime/tests -v
```

## What is implemented
- Local JSON state initialization.
- Append-only interaction events with explicit IN, OUT, UTC operation time, parent hash and SHA-256 event hash.
- Chain verification to detect event edits, reordering and broken parent links.
- Checkpoint pins the current event count and chain head.
- JSON export and import into a **new target path**, with validation before save.
- Atomic local file replacement and refusal to overwrite an existing state or import target.
- Explicit open-gate fields preserved in every state.

## What is not implemented
- This CLI does not automatically capture ChatGPT conversations.
- It is not a cloud database, encrypted vault, multi-user system or background agent.
- Hashes detect accidental/unsophisticated modification; they do not prove authorship, prevent an attacker from rewriting the entire chain, or replace digital signatures.
- Local files can be lost; independent backup and cross-device synchronization remain future work.
- Real browser/AI-host integration and clean-host import must be tested separately.

## Acceptance
The automated tests exercise init → multiple IN/OUT records → checkpoint → export → import into a new file → verify, plus tamper detection, blank input/output rejection, and no-overwrite behavior. A passing local or CI test proves only this runtime's coded behavior, not a live external-host integration.
