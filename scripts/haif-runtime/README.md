# HAIF Canonical MVP Runtime v0.2

This is the single canonical, dependency-free MVP implementation of the HAIF local continuity core. The former FastAPI/SQLite prototype is retained under `archive/implementations/haif-v0/` as a recoverable reference, not as a second active runtime.

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
- Checkpoint pins a verified event-chain prefix; later events do not invalidate the older checkpoint, and a new checkpoint can advance it.
- JSON export and import into a **new target path**, with validation before save.
- Atomic local file replacement and refusal to overwrite an existing state or import target.
- Explicit open-gate fields preserved in every state.

## Canonical implementation decision\n- Use this runtime as the only active MVP core. Do not develop a second runtime in parallel.\n- The archived `haif-v0` implementation is preserved byte-for-byte in the recoverable archive and may be consulted or restored if a specific capability is needed.\n- Archive does not mean permanent deletion. Its source files and original blob identities are retained in Git history and the archive folder.\n\n## What is not implemented
- This CLI does not automatically capture ChatGPT conversations.
- It is not a cloud database, encrypted vault, multi-user system or background agent.
- Hashes detect accidental/unsophisticated modification; they do not prove authorship, prevent an attacker from rewriting the entire chain, or replace digital signatures.
- Local files can be lost; independent backup and cross-device synchronization remain future work.
- Real browser/AI-host integration and clean-host import must be tested separately.

## Acceptance
The automated tests exercise init → multiple IN/OUT records → checkpoint → append after checkpoint → checkpoint advancement → export → import into a new file → verify, plus tamper detection, blank input/output rejection, and no-overwrite behavior. A passing local or CI test proves only this runtime's coded behavior, not a live external-host integration.
