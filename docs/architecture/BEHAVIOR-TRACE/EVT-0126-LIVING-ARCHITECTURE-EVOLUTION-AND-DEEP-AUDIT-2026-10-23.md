# EVT-0126 — Living architecture evolution and deep audit

- Event ID: EVT-0126
- Stable ID: PALANG-LIVING-ARCHITECTURE-EVOLUTION-2026-10-23-001
- Production ID: LAE-HAIF-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / IMPLEMENTED-IN-REPOSITORY / CI-PASS / ARTIFACT-READBACK-VERIFIED
- Parent: EVT-0125
- Interaction pair: INT-20261023-029; [IN-029](../../0.0/anchors/PALANG-0.0-IN-20261023-029-LIVING-ARCHITECTURE-EVOLUTION.md) / [OUT-029](../../0.0/anchors/PALANG-0.0-OUT-20261023-029-LIVING-ARCHITECTURE-EVOLUTION.md)
- Canonical master: [CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE](../../reference/REFERENCE-DOCUMENTS/CURRENT-CANONICAL-CONTINUATION-MASTER-REFERENCE-2026-10-21-001.md)
- Learning-loop reference: [TALL](../BEHAVIOR-OBSERVATORY/TEST-TO-ARCHITECTURE-LEARNING-LOOP-2026-10-23-001.md)

## User direction
Preserve all previous architecture updates; integrate and verify the next update; keep the input/output, evidence, master, indexes and next action live; deep-audit additional capabilities that enable growth.

## Why this update is necessary
The evidence-gated proposal validator could verify a proposal, but the project also needs an explicit append-only history that catches duplicate versions, broken supersedes links, non-increasing sequences, missing evidence references and integrations without approval. Otherwise an update might be technically valid yet overwrite or disconnect the evolution history.

## Implementation
- `scripts/behavior-hunter/validate_architecture_update_ledger.py` validates the ordered JSONL change ledger.
- `tests/behavior-hunter/test_architecture_update_ledger.py` adds regression tests for first record, valid successor version, duplicate change/version, broken supersedes, duplicate sequence, integration/approval, missing evidence and empty ledger.
- `data/interaction-pairs/architecture-update-ledger.jsonl` preserves version 1.0.0 and appends version 1.1.0. The latter records the user-authorized integration of the ledger-validation capability; it does not approve every future proposal.
- `.github/workflows/palang-behavior-hunter.yml` runs the ledger validator and uploads `architecture-update-ledger.json`.
- TALL, canonical master, integration queue, global reference index, 0.0 index and next checkpoint are to be updated and independently read back.

## Lifecycle invariant
`OBSERVE → ANCHOR → PROPOSE → VERIFY EVIDENCE → VALIDATE VERSION CHAIN → TEST IN ISOLATION → EXPLICIT OWNER DECISION → INTEGRATE → REGRESSION → READ-BACK → PRESERVE NEXT CHECKPOINT`

No prior update is deleted. New versions supersede by explicit link; they do not replace historical records. No unrestricted self-modification is enabled.

## Current verification
- Previous run [40012363037](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40012363037) passed 56 tests on tested SHA `cabb1666e56a02f723390bf1f16efe95e67146ea`. Artifact `12526114189` was downloaded and inspected: proposal gate READY_FOR_OWNER_REVIEW, evidence VERIFIED, promotion false, both recovery directions RECOVERED with zero failures.
- That run predates the append-only ledger implementation. The new run, added test count, ledger manifest and artifact contents must be read back before claiming CI PASS for EVT-0126.
- Separate fresh-session recovery is still NOT RUN. Runtime-wide capture and external persistence are NOT PROVEN. Issue #20 and #21 remain OPEN.

## Next
Verify the exact CI run and tested SHA for this update; inspect every generated manifest; run the separate fresh-session recovery without supplying the answer key; then continue historic census and runtime capture as separate open tracks.


## Post-run HEAD boundary
- Tested SHA: `11499b652676d6d89eea0fca42d528acc1d8b2e4`, repository commit time `2026-10-23T19:46:19Z` / Tehran `2026-10-23T23:16:19+03:30`.
- Current main subsequently advanced to evidence-only automation commit `de703573646fd5afad69432f90328d8366ffe8e1` at `2026-10-23T19:46:26Z` / Tehran `2026-10-23T23:16:26+03:30`; that exact post-bot SHA was not rerun.
- ZIP SHA-256 is verified from the downloaded bytes. Fresh-session recovery remains NOT RUN; runtime-wide capture and external persistence remain NOT PROVEN.


## Hash-chain hardening and final CI proof — run 40014712373
- Deep audit identified that version links alone could not detect silent edits to an earlier ledger row. Added `previous_record_sha256` and `record_sha256` to every row, computed from canonical JSON; the first row uses `GENESIS` and each later row must point to the preceding verified hash.
- Added regression tests for record tampering and hash-chain link break/reordering. Earlier versions remain in the ledger and are now hash-linked.
- [Run 40014712373](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40014712373): SUCCESS; 67 tests passed on tested/current-main SHA `965713b2ef2ca4873176015128313da9c03c1b48`, commit time `2026-10-23T19:51:32Z` / Tehran `2026-10-23T23:21:32+03:30`.
- Artifact ID `12527726978`; downloaded and inspected; ZIP SHA-256 `6ddf0b23d3f33db2cdfc6cb4b1e7154899bf1477a0466ba5c01a2a3c7325c07b`.
- `architecture-update-ledger.json`: PASS, 2 records, 2 unique versions, 1 change stream, hash chain verified, zero errors.
- Proposal gate: READY_FOR_OWNER_REVIEW, evidence VERIFIED, fixture owner decision PENDING, canonical mutation false, promotion false. Both recovery manifests RECOVERED with zero failures; host-wide capture false, fresh-session test NOT RUN, external persistence false.
- Two interim failures were preserved: one run caught tests not yet updated for newly required hash fields; another caught the fixture ledger missing its hashes. Both were corrected by sealing the fixture and adding hash-aware test helpers. These failures are part of the architecture's evidence trail.
- At verification time the tested SHA equaled main HEAD. Any later doc/evidence-only commit must be distinguished from a tested source SHA; do not claim a later SHA was rerun unless a new run proves it.
