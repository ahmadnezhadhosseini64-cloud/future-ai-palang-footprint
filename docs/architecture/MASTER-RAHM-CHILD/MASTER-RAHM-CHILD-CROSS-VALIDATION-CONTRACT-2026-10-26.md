# Master–Rahm–Child cross-validation contract

- Stable ID: HAIF-MRCC-20261026-001
- Production ID: HAIF-MRCC-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN FOR TESTING
- Owner: Ahmad Nezhadhosseini / احمد پلنگ
- Parent root: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INITIAL-MODEL-BRIDGE.md)
- Event: [EVT-0201](../BEHAVIOR-TRACE/EVT-0201-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION-2026-10-26.md)
- Current checkpoint: [CURRENT-079](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-079-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION.md)
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## 1. Roles and authority

### MASTER — original Future AI / Palang Footprint
Owns the canonical graph, approved architecture, behavior patterns, source provenance, policies, version history, evidence references and final promotion/rejection decisions. The Master is the authority of record.

### RAHM — new initial-model project
A subordinate, isolated experimental space attached to the Master. It receives a versioned input bundle, reconstructs context from that bundle, tests hypotheses and candidate changes, records both passes and failures, and returns evidence-backed proposals. It is not an independent source of truth and may not overwrite Master records.

### CHILD — candidate and promoted version
A Child starts as CHILD_CANDIDATE, not as an approved model. Promotion requires explicit acceptance criteria, repeatable tests, evidence receipts, regression checks, provenance, a clean-context recovery test and an explicit Master decision. A passing test alone is not approval.

## 2. Canonical lifecycle

MASTER → RAHM INPUT SNAPSHOT → OBSERVATION → HYPOTHESIS → TEST → EVIDENCE REVIEW → CHILD CANDIDATE → MASTER ACCEPT / REJECT / RETURN FOR WORK

Accepted Child changes return to Master through a versioned proposal/merge record. Rejected or deferred proposals remain retrievable; deferral never deletes their evidence.

## 3. Minimum exchange envelope

Every Master-to-Rahm package and Rahm-to-Master proposal must contain:
- stable ID, production ID, version and parent checkpoint;
- source repository/ref/commit and exact source paths;
- UTC timestamps from actual receipts; Tehran equivalent derived from the same instant;
- declared host/model/capabilities, with unknowns explicitly marked;
- input snapshot or content digest, intended change and rationale;
- observed facts separated from hypotheses and recommendations;
- test cases, expected invariants, actual outputs, pass/fail, logs/artifact URLs and exact tested SHA;
- open gaps, reversible covers, failed attempts, conflicts and reopening triggers;
- recovery pointer and explicit next action;
- promotion status: NOT PROPOSED, CHILD_CANDIDATE, MASTER ACCEPTED, MASTER REJECTED, or RETURNED FOR WORK.

## 4. Required validation tests in the actual interactive project environment

The following are a test plan until an actual environment returns receipts:
1. **Cold start:** open only the exported package in a new project context; recover Master/Rahm roles, current checkpoint, active queue and all open gates without relying on hidden chat history.
2. **IN/OUT symmetry:** independently reconstruct state from the input record and from the output record; compare IDs, parent chain, evidence, open gaps and next action.
3. **Provenance preservation:** feed a candidate with conflicting IDs/parent candidates; verify that the system preserves the conflict instead of silently choosing a winner.
4. **Reversible cover:** defer a gap; verify the gap remains indexed, OPEN, discoverable and reopenable.
5. **Candidate isolation:** attempt a candidate update; verify it cannot modify the Master before explicit approval.
6. **Promotion gate:** provide a candidate with passing tests but no Master decision; expected result is CHILD_CANDIDATE, never MASTER ACCEPTED.
7. **Failure recovery:** inject a failing test and ensure failure logs and the prior known-good checkpoint remain recoverable.
8. **Round-trip export/import:** export the Rahm state, import it into a fresh instance, and compare the canonical-state digest and unresolved-gate set.

For each test, store a result receipt containing test ID, host/project identity (if visible), exact source commit, start/end UTC from actual logs, expected result, actual result, verdict, artifact/log link, and independent read-back. If the interactive environment cannot return a receipt, record NOT RUN / BLOCKED, not PASS.

## 5. Promotion gate

A candidate may be submitted for Master review only when:
- all required tests have explicit outcomes;
- no hidden failing test or untracked conflict remains;
- package files and digests match the exact tested revision;
- rollback/recovery pointer exists;
- source provenance and behavioral evidence are attached;
- limitations and unsupported host capabilities are declared.

Master review then records ACCEPT, REJECT, or RETURN FOR WORK with reason and timestamped evidence. Only ACCEPT creates a promoted Child version. The Child keeps its own version lineage and never overwrites its ancestors.

## 6. Reversible gap cover

A cover record must include gap ID, current status, why deferred, preserved evidence, dependencies, reopening trigger, owner/queue and last verified checkpoint. Underlying status remains OPEN / ACTIVE / LIVING. A cover cannot be used as evidence of resolution.

## 7. Current unresolved gates

- exact-final-SHA repository audit and portable package conformance;
- real interactive-project test receipts;
- independent-host import and clean-context recovery;
- durable memory across restart and automatic capture;
- background/idle execution;
- historic graph, provenance, duplicate-ID and ambiguous-parent reconciliation;
- CURRENT-065/CURRENT-066 and EVT-0195 conflicts;
- Issues #20/#21 and other NEXT-051 findings.

These remain OPEN / NOT VERIFIED until evidence changes their state.

## 8. Relationship to existing model initial package

This contract extends, rather than replaces, the initial-model mother, portable RAHM package, canonical continuation master, graph inventory and behavior trace. The repository index and current checkpoint are recovery entry points. Keep one canonical Master; do not create a second parallel authority.


## Executable interactive-project runbook
Use [INTERACTIVE-PROJECT-VALIDATION-RUNBOOK.md](./INTERACTIVE-PROJECT-VALIDATION-RUNBOOK.md) as the copy/paste test procedure in the actual RAHM project. The runbook is a protocol, not a test receipt; every IPV test remains NOT RUN until actual destination output is returned and independently read back.

## 9. Canonical role definition confirmed from user-provided prior output — 2026-10-26

This section preserves the user's supplied earlier assistant output as a project baseline; it is not treated as proof that external runtime tests already passed.

- **MASTER — original project:** durable rules, interaction history, behavioral patterns, accepted architecture, provenance and evidence. MASTER is the final decision authority. A new proposal does not automatically become accepted policy.
- **RAHM — womb / growth and validation environment:** the existing initial-model AI package plus its intended interactive-project runtime. It receives a versioned MASTER package, reconstructs state, runs tests, records failures and produces candidates. It must not silently turn raw data or unresolved gaps into accepted rules.
- **CHILD — candidate initial version:** a specifically versioned result that passes defined tests, carries evidence and limitations, and is submitted for MASTER review. A failed or partially verified result does not become MASTER policy.
- **Growth cycle:** MASTER → RAHM → tests/evidence → CHILD candidate → MASTER review → ACCEPT or RETURN FOR WORK. Rejected versions, errors and gaps remain preserved.

### Implementation consequence
The initial-model AI package and HAIF executable sample already exist in the repository. Extend and connect those existing artifacts; do not create a parallel model folder or a competing Master. Keep two evidence classes separate:
1. **Repository-executable verification:** code, schema, links, package digests and CI tests against a named exact commit.
2. **Real interactive-project/independent-host verification:** destination-side import, reconstruction, restart, isolation, round-trip and receipt.

Passing class 1 never proves class 2. Promotion to an accepted CHILD requires both the required test evidence and an explicit MASTER decision. Until then, status stays OPEN / CANDIDATE / NOT VERIFIED.

## 9. Canonical role definition confirmed from user-provided prior output — 2026-10-26

This section preserves the user's supplied earlier assistant output as a project baseline; it is not treated as proof that external runtime tests already passed.

- **MASTER — original project:** durable rules, interaction history, behavioral patterns, accepted architecture, provenance and evidence. MASTER is the final decision authority. A new proposal does not automatically become accepted policy.
- **RAHM — womb / growth and validation environment:** the existing initial-model AI package plus its intended interactive-project runtime. It receives a versioned MASTER package, reconstructs state, runs tests, records failures and produces candidates. It must not silently turn raw data or unresolved gaps into accepted rules.
- **CHILD — candidate initial version:** a specifically versioned result that passes defined tests, carries evidence and limitations, and is submitted for MASTER review. A failed or partially verified result does not become MASTER policy.
- **Growth cycle:** MASTER → RAHM → tests/evidence → CHILD candidate → MASTER review → ACCEPT or RETURN FOR WORK. Rejected versions, errors and gaps remain preserved.

### Implementation consequence
The initial-model AI package and HAIF executable sample already exist in the repository. Extend and connect those existing artifacts; do not create a parallel model folder or a competing Master. Keep two evidence classes separate:
1. **Repository-executable verification:** code, schema, links, package digests and CI tests against a named exact commit.
2. **Real interactive-project/independent-host verification:** destination-side import, reconstruction, restart, isolation, round-trip and receipt.

Passing class 1 never proves class 2. Promotion to an accepted CHILD requires both the required test evidence and an explicit MASTER decision. Until then, status stays OPEN / CANDIDATE / NOT VERIFIED.


## Latest excavation checkpoint — 2026-10-26
The current continuation is [POINT-0/033](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-033-EXCAVATION-AND-MASTER-RAHM-CHILD-CONTINUATION.md) → [CURRENT-081](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-081-EXCAVATION-AND-MASTER-RAHM-CHILD-CONTINUATION.md). The excavation register preserves the unresolved POINT-0/032 source-path ambiguity. Both paths remain intact until Git provenance and consumer references establish lineage.

