# POINT-0/GOLDEN — current portable host contract

- Living master: 1.8.2
- Package version: 0.5.1 candidate
- Current chain: POINT-0/GOLDEN → CURRENT-150 → POINT-0/089 → IN-133 → OUT-132 → EVT-0320 → TIME-BINDING-EVT-0320 → CURRENT-151 → NEXT-051
- Master access for hosts: PUBLIC READ ONLY; no direct or indirect host write path.
- RAHM: central, private, owner-only, outside host workspaces; only owner-commanded export is permitted.
- Child promotion: trusted bot-authored PR plus owner review; no auto-merge.
- Old snapshots and embedded chains are historical; always resolve current pointers from the Reference Index.

# Independent-host recovery proof protocol

Package version: 0.5.1 candidate
Latest canonical chain: POINT-0/GOLDEN → CURRENT-150 → POINT-0/089 → IN-133 → OUT-132 → EVT-0320 → TIME-BINDING-EVT-0320 → CURRENT-151 → NEXT-051
The current point is POINT-0/GOLDEN on the existing canonical root; follow UNIVERSAL_AI_HOST_ENTRY_FA.md for model/platform-neutral entry.
Project: Future AI / Palang Footprint
Preserved historical baseline chain: POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051. Prior chain POINT-0/071 → IN-114 → OUT-113 → EVT-0289 → TIME-BINDING-EVT-0289 → CURRENT-124 is preserved as parent history. Prior chain POINT-0/066 → CURRENT-119 → POINT-0/067 → IN-110 → OUT-109 → EVT-0285 → TIME-BINDING-EVT-0285 → CURRENT-120 → POINT-0/068 → IN-111 → OUT-110 → EVT-0286 → TIME-BINDING-EVT-0286 → CURRENT-121 → POINT-0/069 → IN-112 → OUT-111 → EVT-0287 → TIME-BINDING-EVT-0287 → CURRENT-122 → POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051 is preserved as parent history.
Preserved prior chain: POINT-0/058 (0+ marker on canonical root 0) → IN-096 → OUT-095 → EVT-0233 → CURRENT-108 → NEXT-051; historical point retained, not current pointer.

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
The receiving GPT-6 host must receive this canonical ZIP, which includes a build-time snapshot named `LIVING_MASTER_REFERENCE.md` and `INDEPENDENT_HOST_ACCEPTANCE_PROMPT_FA.md`; use the prompt to run positive, negative-anchor and fresh-session tests, and compare the snapshot with the current repository living master. The mother is the governing architecture; this ZIP is the portable starter. Uploading both is a transfer attempt, not proof of successful import. Record direct host receipts and keep restart/persistence as separate gates.


## First GPT-6 host integration gate
The package can be uploaded as files, but it is not a native plugin and does not itself subscribe to ChatGPT messages. To prove integration, follow `FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md`. A direct producer and authorized repository write path must be supplied by the actual host environment or connector. The repository adapter is separately deployed; its worker requires a secret held outside the conversation. If the host has no such connector, record manual export / NOT SUPPORTED instead of claiming live automatic sync.


## Host growth contract
Follow `HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md` for the controlled host → event evidence → authorized repository worker → read-back → RAHM → Child/Master loop. The host producer and worker deployment are separate acceptance gates; package documentation does not prove they are connected.


## Decision continuity recovery test

Preserved historical chain: POINT-0/066 → CURRENT-119 → POINT-0/067 → IN-110 → OUT-109 → EVT-0285 → TIME-BINDING-EVT-0285 → CURRENT-120 → POINT-0/068 → IN-111 → OUT-110 → EVT-0286 → TIME-BINDING-EVT-0286 → CURRENT-121 → POINT-0/069 → IN-112 → OUT-111 → EVT-0287 → TIME-BINDING-EVT-0287 → CURRENT-122. Canonical governance: [DCRG](../../docs/reference/REFERENCE-DOCUMENTS/DECISION-CONTINUITY-AND-REVIEW-GOVERNANCE-2026-11-03-001.md).

During clean-host import, the receiving host must retrieve settled decisions with rationale, scope, constraints and reopening triggers. Test at least one decision with no new trigger (must remain settled) and one with valid new evidence (may be reopened only with an explicit evidence explanation and preserved prior state). Record the host's raw output and independent read-back. This test is NOT RUN until a separate host supplies a receipt; repository documentation alone is not a pass.


## Interactive evolution acceptance — package v0.4.1

The receiving host must treat the archive as a living, updateable package, not a frozen export. It must preserve the canonical ZIP filename and stable package identity while accepting only provenance-backed, validated changes to the living mother, architecture, runtime and package sources. Each accepted change requires updated tests, a fresh exact-byte receipt and SHA-256, and repository read-back. This contract does not imply automatic capture of every conversation, background execution, model-weight retraining or successful host recovery.


## Historical package and bootstrap — POINT-0/071

Package version: 0.4.5
Current chain tail: POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051
Use `ONE_MESSAGE_HOST_BOOTSTRAP_FA.md` as the single-message setup procedure for a new GPT host. It must establish read-only access to the canonical repository, verify the latest pointer and paired master/ZIP, run extracted tests and create a private host workspace. Actual connector authorization, persistent workspace and independent host acceptance remain separate gates.


## Historical canonical chain — package v0.4.5

POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051

Living master version: 1.7.79. The current conversation point is a child continuation under canonical POINT-0, not a new independent root. NEXT-051 remains the only active queue. Package v0.4.4 must be accepted only after exact-current-source build, archive round-trip, SHA-256, inventory, CRC and extracted tests. Independent-host import and restart remain separate gates.


## Current canonical chain — package v0.4.5

POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051

Living master version: 1.7.80. The prior POINT-0/072 / CURRENT-125 continuation is preserved as parent history. Package v0.4.5 must be accepted only from an exact-current-source build with a fresh receipt, ZIP round-trip, SHA-256, inventory, CRC, paired-master byte match and extracted tests. Independent-host import and restart remain separate OPEN gates.


## Historical package — 0.4.5 / POINT-0/074 (0++ marker)

Internal package version: 0.4.5. Living master: 1.7.81. Current chain: POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → TIME-BINDING-EVT-0293 → CURRENT-127 → NEXT-051. The 0++ marker belongs to the single canonical Point 0 root; the next target is completion of the existing 0.0 continuation. NEXT-051 remains the sole active queue. The canonical package ID and ZIP filename remain unchanged. Exact-head tests, fresh build receipt, SHA-256, ZIP CRC/inventory/read-back and paired-master byte match are required before PACKAGE_VERIFIED. Independent-host acceptance, OAuth, live capture, durable workspace and restart persistence remain OPEN / NOT VERIFIED until direct receipts exist.


## Public repository READ — POINT-0/080
The canonical repository is Public. A clean host must attempt anonymous HTTPS READ/clone/fetch before asking for OAuth. OAuth is not required to read public source; it is only needed for private resources or authenticated write-back. EXECUTE, isolated workspace, persistence and restart are independent destination-host gates. The owner retains MASTER and merge authority.


## Current source candidate — POINT-0/082

Living master target: 1.8.2. Package source candidate: 0.5.1, same stable package ID and canonical ZIP filename. The 0.4.9 build receipt is historical to its exact source SHA and must not be reused. Fresh exact-main package verification is REQUIRED / NOT RUN until a new receipt proves archive SHA-256, byte size, inventory, CRC, paired-master read-back, extracted tests and artifact round-trip. Independent-host import and restart remain NOT RUN until direct destination receipts exist.
