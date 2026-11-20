# HAIF GPT-6 Portable Starter v0.4.0

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
- Latest verified export and on-demand delivery contract included; requires exact-current-main package receipts and paired living-master delivery.
- Current continuation reference: POINT-0/065 → IN-105 → OUT-104 → EVT-0280 → CURRENT-116 → IN-106 → OUT-105 → EVT-0281 → CURRENT-117 → NEXT-051. Preserve all earlier roots, the certificate child branch, the unresolved CURRENT-065/CURRENT-066 lineage and all open gates; older 0+ markers remain historical. The canonical living mother reference is included in the built ZIP as `LIVING_MASTER_REFERENCE.md`; the Persian external-host test is included as `INDEPENDENT_HOST_ACCEPTANCE_PROMPT_FA.md`. Transfer the ZIP with its included master snapshot and use the prompt on a genuinely independent host.

## Bootstrap
~~~bash
python3 bootstrap_0plus.py --state ./haif-state.json
python3 engine.py --state ./haif-state.json audit
python3 engine.py --state ./haif-state.json export > ./haif-portable-bundle.json
~~~

The bootstrap preserves six host/runtime gates as OPEN. The package build copies the current repository mother reference into `LIVING_MASTER_REFERENCE.md`; that copy is build-time synchronized, and the receiver must compare it with the repository master before relying on freshness.

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
1. Read GPT6_HOST_INSTRUCTIONS.md, INDEPENDENT_HOST_RECOVERY_PROTOCOL.md, HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md and LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT.md.
2. Upload the canonical living master reference from docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md together with this ZIP. The mother is the architecture authority; the ZIP is the portable starter/runtime package.
2. Upload the manifest, instructions, recovery protocol and latest living master / CURRENT checkpoint / NEXT-051 where supported.
3. Verify portable bundle digest before reuse.
4. Use only authorized repository connectors; otherwise use the local engine and import/export files.
5. After a new session, follow the startup/recovery sequence and save actual receipts.

An uploaded instruction file alone is not a native plugin and does not provide automatic memory, live message capture or background execution.

## Latest verified export and on-demand delivery

`LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT.md` defines the exact procedure for resolving the current main SHA, checking the newest successful package receipt, verifying ZIP bytes and delivering the canonical ZIP with its matching living mother and receipt. Readiness levels SOURCE_CURRENT, PACKAGE_BUILT, PACKAGE_VERIFIED and HOST_RECOVERED are distinct. A passing package build does not prove an independent AI-host import. The current Actions artifact is temporary; a permanent latest-release endpoint remains an implementation gap.

## Same-package growth contract

`HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md` defines how the same package grows from real host interactions and returns validated evidence to the repository. It does not claim the interactive host producer or GitHub worker is already deployed. Those require direct acceptance receipts.

## Acceptance scope
CI tests validate the local engine and protocol presence. CI is not proof of actual independent AI-host acceptance. Real host import, negative controls, independent read-back and restart need direct evidence.


## Existing ZIP continuity rule
The package remains the same established starter package and stable identity. The canonical replacement archive filename is `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` for compatibility with the original package record. Its contents are rebuilt from this existing source folder; do not publish a second version-named ZIP. The internal manifest/version and exact ZIP digest must describe the actual rebuilt bytes. The historic v0.3.0 digest is not the digest of the updated archive.

The recovery protocol is included in the existing package line. A ZIP build or CI pass does not prove a real independent AI host accepted the package.


## Current continuous-update checkpoint

Historical chain snapshot only: POINT-0/046 → IN-084 → OUT-083 → EVT-0221 → CURRENT-096 → NEXT-051. It is not the current pointer. The stable package ID and canonical ZIP filename do not change.


## First GPT-6 host transfer rule
Always transfer the canonical ZIP and the current living master together. Do not substitute an old master snapshot for the current repository master. After import, request a structured receipt for the exact package digest, recovered current point/checkpoint, NEXT-051, IN/OUT equivalence, open gaps, negative controls, and restart/persistence. A successful archive test is not host acceptance.


## First interactive GPT-6 host — acceptance gate
Read `FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md` before treating this package as integrated. Transfer the canonical ZIP and the current living master together. The source engine and CI are not a native ChatGPT plugin; automatic message capture, durable host memory and GitHub write-back are unproven until a real host/connector supplies direct receipts.

The v0.3.4 archive is historical verified evidence. Version 0.3.5 is source-only until the current workflow builds the unchanged canonical filename, uploads/downloads it, compares exact hash and inventory, and runs tests from the extracted ZIP.


## Historical package receipts before v0.3.9

- Stable package ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004` (unchanged).
- Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` (unchanged; no separate version-named ZIP product).
- Previous verified v0.3.8 build receipt (historical; not the updated artifact): run [40549743811](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40549743811), 31,487 bytes, SHA-256 `7b9d6df16f4423e3c448c3720cbb8ce95205fc2322b1194511c0b722d4e6205b`, 11 files, 23/23 extracted tests, artifact round-trip PASS.
- Historical v0.3.7 receipt remains preserved: run [40546488170](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40546488170), 30,573 bytes, SHA-256 `fcc09933dd67ca1300af051e14dbcf80c76b6f620dc6c9623323caca307969fb`.
- The test-only source change after the earlier v0.3.7 receipt changed the packaged ZIP bytes without advancing the internal version. This was the historical in-place v0.3.8 update, retaining the same package identity and canonical ZIP filename.
- The v0.3.8 build receipt is historical evidence only. The current v0.3.9 archive must be resolved from the newest successful exact-main-SHA workflow receipt.
- Current recovery chain: POINT-0/065 → IN-105 → OUT-104 → EVT-0280 → CURRENT-116 → IN-106 → OUT-105 → EVT-0281 → CURRENT-117 → NEXT-051. The living master source is v1.7.69; the package workflow copies that exact source from the same checkout and verifies the paired artifact. This README is package source, not a substitute for the external build receipt.
- Real independent-host acceptance remains NOT RUN.


## Living-master snapshot and receipt integrity
The bundled `LIVING_MASTER_REFERENCE.md` is copied byte-for-byte from the canonical repository master at the exact build checkout. The resulting ZIP SHA-256, byte count, inventory, extracted-test result and tested repository SHA belong in the external workflow artifact receipt and linked OUT record; never rewrite the bundled master to insert the digest of the ZIP that contains it. Resolve current package status from the latest successful Portable RAHM Conformance run on the exact main SHA. A passing CI/build proves package integrity only, not acceptance by an independent AI host.


## POINT-0/060 (0+) — historical verified transfer baseline
This is a preserved historical baseline, not the current pointer. Its prior receipt and historical roots remain intact. The current chain and latest living mother are identified above and in the canonical repository. Independent-host acceptance remains NOT RUN until a separate host returns a raw receipt.


## CURRENT-117 — latest exact-source delivery baseline

- Current chain: POINT-0/065 → IN-105 → OUT-104 → EVT-0280 → CURRENT-116 → IN-106 → OUT-105 → EVT-0281 → CURRENT-117 → NEXT-051.
- Delivery contract: `LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT.md`.
- Internal package version: 0.3.9. Stable package ID and canonical ZIP filename remain unchanged.
- The matching living mother is copied into the ZIP as `LIVING_MASTER_REFERENCE.md` by the exact-checkout workflow.
- The external build receipt, not this README, is authoritative for source SHA, run ID, ZIP byte count and SHA-256.
- PACKAGE_VERIFIED is not HOST_RECOVERED. Clean independent-host import and restart remain NOT RUN.


## Permanent latest delivery locator — verified baseline

- Stable release: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified
- Direct canonical ZIP: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/download/haif-latest-verified/haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip
- Verified current main SHA: `8859b3b8aa4017585540a0720687eed070fddda2`; Run 44734261656 PASS; internal version 0.3.9; ZIP 206531 bytes; SHA-256 `a3df4951fbd03cc59845beee78bb0c7d3acedc815842a1cfcc30fd18fd525c99`.
- Release ID 452647521 contains the canonical ZIP, `LIVING_MASTER_REFERENCE.md`, receipt JSON, latest pointer JSON and checksum. The exact main SHA and package digest are recorded in the release receipt.
- Runbook: `docs/portable/RAHM/LATEST-VERIFIED-EXPORT-DELIVERY-RUNBOOK.md`. Independent-host acceptance remains NOT RUN.


## Permanent latest delivery locator — latest verified receipt

- Stable release: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified
- Direct canonical ZIP: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/download/haif-latest-verified/haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip
- Latest verified package v0.3.9: 207402 bytes; SHA-256 `36966dc71f951021a68defe72677a35b58c8fb5b25100b7e59e5d63c90109be2`; Run 44734731537 PASS.
- Build source SHA `df6fef994b9c33edbc62612ff9b3db905fd666fb`; release-time current main SHA `1d28f83cbb427e90c36fdae75d865496dea03907`; intervening Evidence Gate-only file recorded and verified in latest pointer.
- Release contains canonical ZIP, `LIVING_MASTER_REFERENCE.md`, receipt JSON, latest pointer JSON and checksum. Independent-host acceptance remains NOT RUN.


## Current living evolution checkpoint — POINT-0/066 / CURRENT-118

- Latest continuation for this package: [POINT-0/066 (0+)](../../docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-20261120-066-INTERACTIVE-EVOLUTION-0PLUS.md) → IN-107 → OUT-106 → EVT-0282 → CURRENT-118 → NEXT-051.
- The canonical living mother is synchronized from the repository's HAIF mother at build time. Every accepted interaction-derived advance must update the mother and applicable package sources, pass validation and extracted tests, then rebuild this same ZIP filename with a fresh receipt and SHA-256.
- Package stable ID, production ID, canonical filename and stable release tag do not change. Internal version is now 0.4.0; prior receipts remain historical.
- This package's update loop is interaction-driven and evidence-gated. Automatic capture of every ChatGPT message, model-weight retraining, idle/background execution and independent-host recovery remain NOT PROVEN.
