# HAIF GPT-6 Portable Starter v0.3.8

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
- First interactive GPT-6 host acceptance checklist included; separates archive portability from real host import, live message capture, repository write-back and restart proof.
- Host-growth/repository-sync contract included; defines behavior evidence, authorized repo return, RAHM validation and controlled Master/Child promotion.
- Interaction response/anchor protocol included; requires visible acknowledgment/status, failure disclosure, paired input/output anchors and explicit non-verified gates.
- Current continuation reference: POINT-0/053 (0+ marker on canonical root 0) → IN-091 → OUT-090 → EVT-0228 → CURRENT-103 → NEXT-051; older 0+ markers remain historical.

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
1. Read GPT6_HOST_INSTRUCTIONS.md, INDEPENDENT_HOST_RECOVERY_PROTOCOL.md and HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md.
2. Upload the canonical living master reference from docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md together with this ZIP. The mother is the architecture authority; the ZIP is the portable starter/runtime package.
2. Upload the manifest, instructions, recovery protocol and latest living master / CURRENT checkpoint / NEXT-051 where supported.
3. Verify portable bundle digest before reuse.
4. Use only authorized repository connectors; otherwise use the local engine and import/export files.
5. After a new session, follow the startup/recovery sequence and save actual receipts.

An uploaded instruction file alone is not a native plugin and does not provide automatic memory, live message capture or background execution.

## Same-package growth contract

`HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md` defines how the same package grows from real host interactions and returns validated evidence to the repository. It does not claim the interactive host producer or GitHub worker is already deployed. Those require direct acceptance receipts.

## Acceptance scope
CI tests validate the local engine and protocol presence. CI is not proof of actual independent AI-host acceptance. Real host import, negative controls, independent read-back and restart need direct evidence.


## Existing ZIP continuity rule
The package remains the same established starter package and stable identity. The canonical replacement archive filename is `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` for compatibility with the original package record. Its contents are rebuilt from this existing source folder; do not publish a second version-named ZIP. The internal manifest/version and exact ZIP digest must describe the actual rebuilt bytes. The historic v0.3.0 digest is not the digest of the updated archive.

The recovery protocol is included in the existing package line. A ZIP build or CI pass does not prove a real independent AI host accepted the package.


## Current continuous-update checkpoint

The current 0.0 chain is POINT-0/046 → IN-084 → OUT-083 → EVT-0221 → CURRENT-096 → NEXT-051. The stable package ID and canonical ZIP filename do not change. Internal version 0.3.3 identifies the next source content; the new archive digest is pending until the exact-head CI artifact is downloaded, inspected and tested. The prior 0.3.1 ZIP receipt remains historical evidence.


## First GPT-6 host transfer rule
Always transfer the canonical ZIP and the current living master together. Do not substitute an old master snapshot for the current repository master. After import, request a structured receipt for the exact package digest, recovered current point/checkpoint, NEXT-051, IN/OUT equivalence, open gaps, negative controls, and restart/persistence. A successful archive test is not host acceptance.


## First interactive GPT-6 host — acceptance gate
Read `FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md` before treating this package as integrated. Transfer the canonical ZIP and the current living master together. The source engine and CI are not a native ChatGPT plugin; automatic message capture, durable host memory and GitHub write-back are unproven until a real host/connector supplies direct receipts.

The v0.3.4 archive is historical verified evidence. Version 0.3.5 is source-only until the current workflow builds the unchanged canonical filename, uploads/downloads it, compares exact hash and inventory, and runs tests from the extracted ZIP.


## Current continuous-update receipt (2026-10-27)

- Stable package ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004` (unchanged).
- Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` (unchanged; no separate version-named ZIP product).
- Previous verified v0.3.8 build receipt (historical; not the updated artifact): run [40549743811](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40549743811), 31,487 bytes, SHA-256 `7b9d6df16f4423e3c448c3720cbb8ce95205fc2322b1194511c0b722d4e6205b`, 11 files, 23/23 extracted tests, artifact round-trip PASS.
- Historical v0.3.7 receipt remains preserved: run [40546488170](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40546488170), 30,573 bytes, SHA-256 `fcc09933dd67ca1300af051e14dbcf80c76b6f620dc6c9623323caca307969fb`.
- The test-only source change after the earlier v0.3.7 receipt changed the packaged ZIP bytes without advancing the internal version. This is an in-place update of the existing internal version 0.3.8, retaining the same package identity and canonical ZIP filename.
- Previous v0.3.8 build receipt is historical evidence only; the in-place v0.3.8 rebuild receipt is PENDING until the fresh exact-head workflow completes and its downloaded ZIP is inspected.
- Current recovery chain: POINT-0/057 (0+ marker on canonical root 0) → IN-095 → OUT-094 → EVT-0232 → CURRENT-107 → NEXT-051.
- Real independent-host acceptance remains NOT RUN.
