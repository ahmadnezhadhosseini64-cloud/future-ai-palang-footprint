# RAHM_BOOT — Portable startup contract
Package ID: HAIF-RAHM-PORTABLE-20261024-001 | Version: 1.0.2
Purpose: initialize an evidence-based Rahm growth/testing environment without assuming hidden chat history, persistent memory, tools, or background execution.

## First response on a new host
1. Identify package/version and list files actually supplied.
2. State host/model/version only if visible; otherwise UNKNOWN.
3. Report missing files and broken references.
4. Fill HOST_CAPABILITY_MANIFEST from observed evidence; use UNKNOWN/UNTESTED rather than guessing.
5. Reconstruct mission, checkpoint, open gates, and next action from package evidence only.
6. Declare separately whether memory survives a new session and whether jobs can run while idle.
7. Never say an interaction was automatically saved without a write receipt and independent read-back.

## Governing lifecycle
MASTER → RAHM → OBSERVATION → BEHAVIOR STUDY → VALIDATION → CHILD CANDIDATE → MASTER REVIEW.

## Non-negotiable rules
- UTC is canonical. Tehran time is the same instant converted to Asia/Tehran (+03:30).
- Observation ≠ hypothesis; recommendation ≠ approval; repository presence ≠ runtime operation.
- Never invent IDs, hashes, timestamps, files, tests, or host capabilities.
- Preserve failed tests, conflicts, corrections, old versions and unresolved gaps.
- No Child promotion without acceptance criteria, evidence, regression tests, review, read-back and explicit Master decision.
- Unsupported = UNSUPPORTED; untested = NOT TESTED.

## Status vocabulary
REGISTERED = written; READ-BACK VERIFIED = fetched again and matched; VALIDATED = acceptance tests passed; ACTIVE = selected; LIVING = additive evolution; OPEN/PENDING = unfinished; NOT VERIFIED = insufficient evidence; NOT RUN = no execution evidence.

Required response envelope: host capabilities → package integrity → reconstructed state → observations vs hypotheses → tests → failures/gaps → next action → persistence/background proof status.

## Current authoritative return anchor — CURRENT-059 / Point 0/008

- Start from [CURRENT-059](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-059-DEEP-AUDIT-AND-CORRECTED-CONFORMANCE.md), not any earlier CURRENT-048/056/057/058 pointer.
- User Point 0: [POINT-0/008](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-008-DEEP-AUDIT-AND-NO-SILENT-GAP.md).
- Canonical chain: [IN-052](../../0.0/anchors/PALANG-0.0-IN-20261025-052-DEEP-AUDIT-NO-SILENT-GAP-AND-EXECUTION.md) → [OUT-051](../../0.0/anchors/PALANG-0.0-OUT-20261025-051-DEEP-AUDIT-NO-SILENT-GAP-AND-EXECUTION.md) → [EVT-0161](../../architecture/BEHAVIOR-TRACE/EVT-0161-DEEP-AUDIT-STALE-GATE-AND-NO-SILENT-GAP-2026-10-25.md) → [CURRENT-059](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-059-DEEP-AUDIT-AND-CORRECTED-CONFORMANCE.md) → [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Read [FIRST-LIVING-MASTER](./FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md) and [EXPORT_MANIFEST](./EXPORT_MANIFEST.json) after this boot contract; treat CURRENT-059 as the current checkpoint and NEXT-051 as the existing unfinished work item.
- No-silent-gap rule: every new input must receive a visible state/output. If work is partial, record what actually ran, what did not run, the blocker and exact resume point. Never create a new NEXT merely to disguise unfinished work.
- Latest tested package is commit-scoped. Use the latest successful Portable RAHM Conformance run for the exact package commit; do not reuse a prior hash after package contents change.
- Open gates remain: clean independent AI-host import, second-host import, durable memory after restart, automatic live capture, idle/background execution, and graph identity/parent/time adjudication. These are not implied by CI package success.


## Current highlighted continuation — POINT-0+ / CURRENT-076
- Current canonical root: [POINT-0/028](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-028-PORTABLE-GPT6-EXECUTION-AND-RECOVERY.md); its emphasis marker is [POINT-0+](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-PLUS-20261026-028-PORTABLE-GPT6-MILESTONE.md). The plus is a highlight only; all POINT-0 rules apply unchanged.
- Current checkpoint: [CURRENT-076](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-076-POINT-0-PLUS-ARCHITECTURE-CLOSURE.md). Active queue remains NEXT-051. Do not create NEXT-052.
- Latest milestone event: [EVT-0197](../../architecture/BEHAVIOR-TRACE/EVT-0197-POINT-0-PLUS-HIGHLIGHT-AND-ARCHITECTURE-CLOSURE-2026-10-26.md). Two existing EVT-0195 files remain a collision; preserve both and do not merge/renumber by inference.
- Eight CI checks passed on SHA 282cb1acd859c188f4cbb2443a960a013380d385, but a follow-up Evidence Gate commit 3924818996f679d80a8335cab2429177c2ceba36 moved main after those checks. That follow-up SHA and every newer HEAD are unverified until exact-SHA conformance and audit pass.
- Transfer goal is clean host recovery, not just file copy. External consumer GPT-6 host import remains NOT RUN absent a direct receipt. Buffer/Persistent Memory NOT VERIFIED; Dropbox OPEN/NOT VERIFIED; Issues #20/#21 OPEN; CURRENT-065/CURRENT-066 OPEN.


## Latest authoritative return point — POINT-0/029 / CURRENT-077
- Begin at [POINT-0/029](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-029-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md) and [CURRENT-077](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-077-REVERSIBLE-GAP-COVERS.md). Earlier pointers in this file are historical unless independently confirmed current.
- Read [IN-065](../../0.0/anchors/PALANG-0.0-IN-20261026-065-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md), [OUT-064](../../0.0/anchors/PALANG-0.0-OUT-20261026-064-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER.md), [EVT-0199](../../architecture/BEHAVIOR-TRACE/EVT-0199-REVERSIBLE-GAP-COVERS-AND-FAST-HOST-TRANSFER-2026-10-26.md), and the existing [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Use the [QUICK-TRANSFER-CHECKLIST](./QUICK-TRANSFER-CHECKLIST.md) to prepare the minimum package and the independent destination receipt. Do not divert this continuation into Dropbox.
- The covers are reversible and do not close any gate. Keep CURRENT-065/CURRENT-066 ambiguity, EVT-0195 collision, historic graph findings, Issues #20/#21, external persistence, actual host import, and runtime/background claims OPEN until evidence-based acceptance.
- Before declaring package readiness, fetch current main HEAD, regenerate the manifest using the workflow, validate exact bytes on the exact final SHA, and repeat if Evidence Gate commits a newer head. A passing parent SHA does not validate its child.
- Do not create NEXT-052. Keep user-visible milestone outputs explicit; no silent work or claim of background execution between turns.


## Latest root and reversible gap-cover contract — POINT-0/031 / CURRENT-078
- Start from [POINT-0/031](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-031-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md), then [CURRENT-078](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-078-REVERSIBLE-GRAPH-GAP-COVERS.md), [IN-066](../../0.0/anchors/PALANG-0.0-IN-20261026-066-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md), [OUT-065](../../0.0/anchors/PALANG-0.0-OUT-20261026-065-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER.md), [EVT-0200](../../architecture/BEHAVIOR-TRACE/EVT-0200-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER-2026-10-26.md), and [GAP-COVER-REGISTER](../../architecture/BEHAVIOR-TRACE/GAP-COVER-REGISTER-2026-10-26.md).
- “Cover / set aside / close for now” means COVERED / DEFERRED; the underlying issue stays OPEN / ACTIVE / LIVING and retrievable. Never convert a cover into CLOSED or VERIFIED.
- Behavior Hunter is scan/CI-driven unless a real always-on scheduler/runtime receipt exists. Never claim silent/background work between turns.
- Keep NEXT-051; do not create NEXT-052. Preserve CURRENT-065/CURRENT-066, EVT-0195, graph/source/parent gaps, Issues #20/#21, host-import and persistence gaps as OPEN.
- Prioritize portable clean-host transfer, exact-SHA conformance, and a real destination receipt. Do not divert to Dropbox.


## Latest Master–Rahm–Child bridge — CURRENT-079 / POINT-0/032
- Root: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INITIAL-MODEL-BRIDGE.md)
- Current checkpoint: [CURRENT-079](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-079-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION.md)
- Cross-validation contract: [Master–Rahm–Child](../../architecture/MASTER-RAHM-CHILD/MASTER-RAHM-CHILD-CROSS-VALIDATION-CONTRACT-2026-10-26.md)
- The original Future AI / Palang Footprint is MASTER; the initial-model package is subordinate RAHM; outputs remain CHILD CANDIDATES until explicit Master acceptance.
- Continue NEXT-051 only. Interactive-project tests, exact-final-SHA conformance, clean-host import, persistent memory and background execution are OPEN / NOT RUN until direct receipts exist.


## Current Master–Rahm–Child bridge — POINT-0/032 / CURRENT-079
- Canonical root: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INITIAL-MODEL-BRIDGE.md)
- Current checkpoint: [CURRENT-079](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-079-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION.md)
- Governing contract: [MASTER–RAHM–CHILD cross-validation](../../architecture/MASTER-RAHM-CHILD/MASTER-RAHM-CHILD-CROSS-VALIDATION-CONTRACT-2026-10-26.md)
- Copy/paste runbook: [INTERACTIVE-PROJECT-VALIDATION-RUNBOOK](../../architecture/MASTER-RAHM-CHILD/INTERACTIVE-PROJECT-VALIDATION-RUNBOOK.md)
- Treat the original project as MASTER and the initial-model environment as RAHM. A candidate is not a promoted CHILD until explicit Master review is recorded. Interactive-project tests are NOT RUN until actual destination receipts exist.

- Latest continuation: [POINT-0/033](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-033-EXCAVATION-AND-MASTER-RAHM-CHILD-CONTINUATION.md) → [CURRENT-081](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-081-EXCAVATION-AND-MASTER-RAHM-CHILD-CONTINUATION.md). Preserve both POINT-0/032 source candidates until provenance-based reconciliation; no automatic promotion.


## Latest continuation — POINT-0/034 / CURRENT-082

- Root: [POINT-0/034](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-034-INTERACTIVE-RAHM-EXECUTION.md)
- Current checkpoint: [CURRENT-082](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-082-INTERACTIVE-RAHM-EXECUTION.md)
- Runbook: [interactive-project validation](../../architecture/MASTER-RAHM-CHILD/INTERACTIVE-PROJECT-VALIDATION-RUNBOOK.md)
- Required proof: repository conformance on exact final SHA, then a destination receipt from the actual interactive project for I1–I8. Neither should be inferred from file registration.
- Continue NEXT-051 only. Preserve all historical gaps as OPEN; do not create NEXT-052.

