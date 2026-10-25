# POINT-0/019 — Build the Initial HAIF Model into Testable Capabilities

- Stable ID: `HAIF-POINT-0-019-MODEL-CAPABILITY-BUILD-20261025`
- Production ID: `HAIF-P0-019-20261025`
- Version: 1.0.0
- Status: REGISTERED / REPOSITORY READ-BACK VERIFIED / OPEN / LIVING. Repository read-back confirms the point file exists and its identifiers/links match; exact-head tests and runtime acceptance remain OPEN.
- User intent: advance the model toward the initial HAIF model with the capabilities requested throughout the project; make this interaction a new point 0 and link all next steps as 0.0.
- Parent: [POINT-0/018](./GPT6-RAHM-USER-POINT-0-20261025-018-LIVING-REGISTRATION-AND-NEXT-STEPS.md).
- Event: [EVT-0181](../../architecture/BEHAVIOR-TRACE/EVT-0181-POINT-0-019-MODEL-CAPABILITY-BUILD-2026-10-25.md).
- Living master: [HAIF Initial Model Master Reference](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- Scope: the original Future AI / Palang Footprint repository only. Do not fork the architecture into a detached project.
- Time rule: repository registration time is the actual final-change commit timestamp in UTC; derive Tehran from the same instant. Exact user-message time is not inferred from commit time.

## Capability target

The model must grow beyond documentation into a small, executable, portable, evidence-governed continuity system. The following are acceptance targets, not claims that all are already implemented:

1. **Continuity Core:** append-only IN/OUT interaction pairs, independently addressable 0.0 anchors, event ledger, checkpoint lineage and no silent overwrite.
2. **Recoverability:** rebuild state from either IN or OUT, export/import portable JSON, verify hashes and compare reconstructed state after a clean process start.
3. **Behavior Hunter:** extract candidate patterns from user input, assistant output, correction and feedback; label OBSERVATION / INFERENCE / HYPOTHESIS / UNKNOWN; preserve negative evidence and failures; check unique IDs before writing.
4. **Context and retrieval:** search the master, events, artifacts, open gaps and past decisions; return source-backed results and distinguish exact matches from semantic candidates.
5. **Master–Child–Rahm governance:** keep experimental Child branches isolated; validate evidence, consistency, reversibility and user approval before promoting anything to the master.
6. **Evidence Gate:** separate WRITE, READ-BACK, MATCH, STRUCTURAL VALIDATION, SEMANTIC VALIDATION, INTEGRATION and EXTERNAL-RUNTIME PROOF.
7. **Portable host adapter:** package the architecture, schema, master rules, index, events and recovery instructions; prove a real import into an independent host before claiming portability.
8. **User-visible operational status:** show what actually ran, what passed, what failed, what was not run and the exact next action. No implied background processing or fake success.
9. **Single-project integration:** every new capability, rule, defect and finding must link back into the original Future AI / Palang Footprint master, reference index, 0.0 graph and integration queue.

## 0.0 implementation plan

### 0.0-01 — discover, do not guess, the live execution pointer
- Preserve historical CURRENT-065 and CURRENT-066.
- Add an independent discovery check that detects candidate checkpoints and registry/manifest declarations. If evidence conflicts, return AMBIGUOUS/BLOCKED with the conflicting sources; never choose by filename or number alone.
- Keep the existing historical CURRENT-066 reconstruction test separate from live-pointer discovery.
- Acceptance: fixture tests cover one candidate, consistent multiple references, conflict, missing target and malformed checkpoint; report includes candidate paths, source declarations and exit status.
- Status: implementation in progress; run on exact main SHA required.

### 0.0-02 — make the local continuity runtime a tested foundation
- Inspect and test `scripts/haif-runtime/haif_runtime.py` and its test suite.
- Verify append-only IN/OUT, independent anchors, hash-chain tamper detection, checkpointing, JSON export/import, no-overwrite and recovery from both roots.
- Acceptance: tests run on the exact final revision, with command, runtime version, output, exit code, UTC and commit SHA recorded.
- Status: OPEN until fresh test receipts.

### 0.0-03 — implement behavior-pair capture and candidate gate
- Use the existing Issue #20 as the work item; do not create a duplicate.
- Capture only inputs/outputs explicitly supplied to the runtime or authorized producer; do not claim automatic capture of all host conversations.
- Add schema validation, reverse lookup, evidence labels, unique-ID pre-write gate and cold-start recovery.
- Acceptance: sample IN/OUT pair survives process restart and can be found from either side; invalid pair and duplicate ID are rejected with inspectable reasons.
- Status: OPEN.

### 0.0-04 — reconcile identity and graph collisions safely
- Continue Issue #21 and BOART-FOLLOWUP-01.
- Adjudicate each Stable ID / Production ID / Reference ID / event-number / parent-edge occurrence from provenance and role; preserve alias and history.
- No bulk rename, merge or deletion.
- Acceptance: each adjudicated occurrence has a source, decision, rationale, dependency review and regression test where relevant.
- Status: OPEN.

### 0.0-05 — build evidence-backed retrieval and master promotion
- Add search over anchors, artifacts, events, open gaps and decisions with source paths and confidence labels.
- Require Rahm validation and a recorded promotion/reject/revise decision before Child findings alter the master.
- Acceptance: retrieval result is traceable to source; an unverified hypothesis cannot silently become canonical knowledge.
- Status: OPEN.

### 0.0-06 — portable export/import and independent-host proof
- Define a versioned portable bundle containing schema, manifest, master, index, anchors, event ledger, open gates and recovery runbook.
- Verify exact-byte digests and round-trip recovery in a clean local process first, then an independent host with direct evidence.
- A CI archive is not an independent AI-host import.
- Status: OPEN / NOT PROVEN.

### 0.0-07 — live master, index and status reconciliation
- Keep this point/event linked from the living master, 0.0 registry, Reference Index, behavior-trace index and integration queue.
- Preserve append-only history; update version and evidence after each accepted implementation step.
- Keep NEXT-051 active until its acceptance criteria pass; do not create NEXT-052 merely to signal movement.
- Status: OPEN / LIVING.

## Known blockers that remain open
- CURRENT-065 vs CURRENT-066: live execution-pointer conflict not adjudicated.
- Historical recovery verifier currently hard-codes CURRENT-066 lineage while using a manifest whose filename contains CURRENT-065; manifest contents identify CURRENT-066. Intended historical overlay semantics and exact-byte lineage need source-backed review before editing.
- Repository/CI proof does not prove host-wide capture, idle/background execution, external persistence or second-host recovery.
- Buffer/Persistent Memory: NOT VERIFIED. Dropbox: OPEN / NOT VERIFIED; do not activate without explicit reopening. Library newline normalization remains OPEN until supported write plus independent read-back.
- Existing NEXT-051, Issue #20, Issue #21 and BOART-FOLLOWUP-01 remain the active continuation; no duplicate work item is created.

## Recovery order
Read POINT-0/019 and EVT-0181, then the living master, runtime source/tests, pointer verifier and manifest, CURRENT-065/CURRENT-066 lineage, NEXT-051, Issues #20/#21 and BOART-FOLLOWUP-01. Compare actual evidence before changing a canonical pointer or closing a gate.

## Proof protocol
WRITE → READ-BACK → MATCH → TEST → VERIFY → RECONCILE → STATUS.
This point records an implementation plan and its current blockers; it does not claim all target capabilities already exist.
