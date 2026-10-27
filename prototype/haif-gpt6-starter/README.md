# HAIF GPT-6 Portable Starter v0.3.3

This is the updated release of the existing HAIF starter package, not a separate project. It updates the existing v0.3.0 0/0+ bootstrap package at the same stable package identity and canonical ZIP filename; history and prior digests remain preserved. It does not replace the living master, historical anchors or NEXT-051.

## What is implemented
- Standard-library Python continuity engine.
- Independent anchor, IN, OUT and event identifiers for each interaction pair.
- Canonical point identity: 0 and 0+ are labels on the same point; 0+ is not a duplicate point.
- One-command bootstrap creates the 0/0+ root, linked 0.0 continuation and six explicitly OPEN host-capability gaps; it refuses to overwrite existing state.
- Parent-linked 0.0 continuation checkpoints, collision and lineage checks, append-only hash-linked events and tamper detection.
- Evidence-gated gap closure and Master → Child promotion.
- Portable bundle export/import with SHA-256 verification, atomic local writes and validated read-back.
- Independent-host recovery protocol included in this package: exact package digest, clean-host import, independent reconstruction from IN and OUT, negative controls, read-back and restart/persistence acceptance.
- Current continuation reference: POINT-0/046 → IN-084 → OUT-083 → EVT-0221 → CURRENT-096 → NEXT-051; POINT-0/043 remains the 0+ production marker.

## Bootstrap
~~~bash
python3 bootstrap_0plus.py --state ./haif-state.json
python3 engine.py --state ./haif-state.json audit
python3 engine.py --state ./haif-state.json export > ./haif-portable-bundle.json
~~~

The bootstrap preserves six host/runtime gates as OPEN.

## Run locally
~~~bash
python3 engine.py --state ./haif-state.json init
python3 engine.py --state ./haif-state.json record --input "user input" --output "assistant output"
python3 engine.py --state ./haif-state.json audit
python3 engine.py --state ./haif-state.json export > haif-portable-bundle.json
python3 engine.py --state ./imported-state.json import haif-portable-bundle.json
python3 -m unittest -v
~~~

The engine refuses to overwrite existing state/import targets. Original user-message time remains null unless supplied by a verified integration. Repository commit time is separate UTC evidence; Tehran time is derived from the same instant.

## Bring it into GPT-6
1. Read GPT6_HOST_INSTRUCTIONS.md and INDEPENDENT_HOST_RECOVERY_PROTOCOL.md.
2. Upload the manifest, instructions, recovery protocol and latest living master / CURRENT checkpoint / NEXT-051 where supported.
3. Verify portable bundle digest before reuse.
4. Use only authorized repository connectors; otherwise use the local engine and import/export files.
5. After a new session, follow the startup/recovery sequence and save actual receipts.

An uploaded instruction file alone is not a native plugin and does not provide automatic memory, live message capture or background execution.

## Acceptance scope
CI tests validate the local engine and protocol presence. CI is not proof of actual independent AI-host acceptance. Real host import, negative controls, independent read-back and restart need direct evidence.


## Existing ZIP continuity rule
The package remains the same established starter package and stable identity. The canonical replacement archive filename is `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` for compatibility with the original package record. Its contents are rebuilt from this existing source folder; do not publish a second version-named ZIP. The internal manifest/version and exact ZIP digest must describe the actual rebuilt bytes. The historic v0.3.0 digest is not the digest of the updated archive.

The recovery protocol is included in the existing package line. A ZIP build or CI pass does not prove a real independent AI host accepted the package.


## Current continuous-update checkpoint

The current 0.0 chain is POINT-0/046 → IN-084 → OUT-083 → EVT-0221 → CURRENT-096 → NEXT-051. The stable package ID and canonical ZIP filename do not change. Internal version 0.3.3 identifies the next source content; the new archive digest is pending until the exact-head CI artifact is downloaded, inspected and tested. The prior 0.3.1 ZIP receipt remains historical evidence.
