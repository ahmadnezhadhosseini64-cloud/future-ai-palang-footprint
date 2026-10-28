# Independent-host recovery proof protocol

Package version: 0.3.8
Project: Future AI / Palang Footprint
Canonical chain: POINT-0/057 (0+ marker on canonical root 0) → IN-095 → OUT-094 → EVT-0232 → CURRENT-107 → NEXT-051

## Purpose
Prove that a genuinely separate AI host can reconstruct the project from the package without relying on this chat's hidden history. Repository presence, a CI pass, or a runtime-to-runtime test is not independent-host acceptance.

## Required procedure
1. Freeze the package: record repository commit SHA, package version, manifest bytes/SHA-256, ZIP bytes/SHA-256 and exact file inventory.
2. Verify integrity: extract into a clean directory, check the package digest and required files, reject altered/missing files.
3. Prove host independence: use a separate host/session with no prior conversation context. Record host/model/version only when visible; otherwise UNKNOWN.
4. Import: provide only the package and its included instructions. The host must identify current point, active queue, master reference, parent lineage, version inventory and every open gap without inventing missing data.
5. Reconstruct from IN and OUT separately: both paths must recover the same normalized chain, checkpoint, event IDs, package version, evidence references and open-gate statuses.
6. Negative controls: modify one byte, remove a required file, and supply invalid state. Each defect must be detected or rejected.
7. Independent read-back: export or display reconstructed state and compare it with frozen expected state. Save raw receipts and hashes.
8. Restart/persistence: close the session or restart the host and repeat recovery. If persistence is unavailable, record NOT SUPPORTED / NOT VERIFIED.

## PASS criteria
PASS requires direct evidence for package hash, complete inventory, clean host identity, independent import, IN/OUT equivalence, preserved open gaps, negative controls and read-back. Restart persistence is a separate gate.

## Status at package build
- Latest exact-head receipt: Portable Conformance run 40638629879; 32,235 bytes; SHA-256 `6ef2a5b0eab4c527db6f47ad8ef330f9854e692cd02fc3b2a02298636fa5bb78`; 11 ZIP files; 23/23 extracted tests PASS on source commit `db5d960c80d47c39b75d2b8821312eba9ad38cfa`. The next package rebuild adds the living mother as a companion file and will therefore produce a new digest.
- Same-package identity: HAIF-GPT6-PORTABLE-STARTER-20261025-004; canonical ZIP filename remains haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip.
- Previous v0.3.7 ZIP receipt: run 40546488170; 30,573 bytes; SHA-256 `fcc09933dd67ca1300af051e14dbcf80c76b6f620dc6c9623323caca307969fb`; 11 files; 23/23 extracted tests PASS.
- Earlier v0.3.8 ZIP receipts are historical only; never copy their digest to a newer archive.
- Real independent AI-host import: NOT RUN.
- Second-host and restart persistence: NOT RUN.
- Automatic message capture and background execution: NOT PROVEN.

Never mark a host gate PASS from documentation alone.


## Existing ZIP replacement identity
The deliverable is the existing starter package continuously updated under the canonical filename `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`; do not publish a second version-named ZIP. The historic v0.3.0 digest (297b3b329143c4b99f55373db0c4bb97896b0e484253622e63eeb32a4429f164) is historical only. The updated archive must carry a fresh digest and byte count from its own build receipt.


## Paired transfer requirement
The receiving GPT-6 host must receive this canonical ZIP, which includes a build-time snapshot named `LIVING_MASTER_REFERENCE.md`, and compare that snapshot with the current repository living master. The mother is the governing architecture; this ZIP is the portable starter. Uploading both is a transfer attempt, not proof of successful import. Record direct host receipts and keep restart/persistence as separate gates.


## First GPT-6 host integration gate
The package can be uploaded as files, but it is not a native plugin and does not itself subscribe to ChatGPT messages. To prove integration, follow `FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md`. A direct producer and authorized repository write path must be supplied by the actual host environment or connector. The repository adapter is separately deployed; its worker requires a secret held outside the conversation. If the host has no such connector, record manual export / NOT SUPPORTED instead of claiming live automatic sync.


## Host growth contract
Follow `HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md` for the controlled host → event evidence → authorized repository worker → read-back → RAHM → Child/Master loop. The host producer and worker deployment are separate acceptance gates; package documentation does not prove they are connected.
