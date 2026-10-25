# HAIF GPT-6 Portable Starter v0.2.1

This is an executable starter package inside the existing Future AI / Palang Footprint repository. It is not a separate project and does not replace the living master, historical anchors or NEXT-051.

## What is implemented
- Standard-library Python continuity engine.
- Independent anchor, IN, OUT and event identifiers for each interaction pair.
- Canonical point identity with aliases/markers: `0` and `0+` can be two labels on the same point; `0+` is not a duplicate point.
- Parent-linked `0.0` continuation checkpoints, with collision and lineage checks.
- Append-only hash-linked event chain with tamper detection.
- Explicit OPEN gap register; closure requires a passing test ID, exact tested revision and evidence reference.
- Master → Child proposal and promotion gate; promotion without passing evidence is rejected.
- Portable bundle export/import with SHA-256 verification.
- Atomic local writes and validated read-back.

## Run locally
From this directory:

~~~bash
python3 engine.py --state ./haif-state.json init
python3 engine.py --state ./haif-state.json record --input "user input" --output "assistant output"
python3 engine.py --state ./haif-state.json gap --title "Independent host import" --description "Not yet verified"
python3 engine.py --state ./haif-state.json audit
python3 engine.py --state ./haif-state.json export > haif-portable-bundle.json
python3 engine.py --state ./imported-state.json import haif-portable-bundle.json
python3 -m unittest -v
~~~

The engine refuses to overwrite an existing state/import target. Original user-message time is left null unless an actual timestamp is provided through a verified integration. A repository commit timestamp is not substituted for it.

## Bring it into GPT-6
1. Open GPT6_HOST_INSTRUCTIONS.md and copy its text into the host's instruction/configuration area where supported.
2. Upload manifest.json, this README, and the current living master / CURRENT checkpoint / NEXT-051 as knowledge files if file upload is supported.
3. Keep a copy of the exported portable bundle as state; verify its digest before reuse.
4. If the host has a GitHub connector, grant only the permissions needed and point it to the canonical repository. Otherwise it cannot commit changes by itself; use the engine locally and import/export files.
5. After a new session, begin with the Startup / recovery sequence in the instructions.

An uploaded instruction file alone is not a native plugin and does not provide automatic memory, live message capture or background execution. Those require a real host adapter and permissioned runtime.

## Acceptance scope
Tests in test_engine.py cover independent IDs, tamper detection, evidence-gated gap closure, evidence-gated Child promotion, portable round-trip/tamper detection and local file read-back. CI results must be read from the exact tested revision before these are described as passing.
