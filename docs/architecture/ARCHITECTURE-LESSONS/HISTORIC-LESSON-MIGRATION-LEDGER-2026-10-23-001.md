# Historic Architecture Lesson Migration Ledger — 2026-10-23

- Stable ID: PALANG-HISTORIC-ARCHITECTURE-LESSON-MIGRATION-LEDGER-2026-10-23-001
- Production ID: HALML-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / PARTIAL INVENTORY / OPEN
- Governing registry: [ARCHITECTURE-LESSONS](./README.md)
- Governing master: [CMIND](../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)
- Execution event: [EVT-0108](../BEHAVIOR-TRACE/EVT-0108-LIVING-ARCHITECTURE-EXECUTION-AND-EVIDENCE-CYCLE-2026-10-23.md)

## Purpose and scope boundary

This is the first evidence-backed excavation batch for the dedicated architecture-lessons folder. It is not a claim that all historic lessons in the repository have been found. Each candidate remains linked to its source of truth; this ledger classifies and routes candidates rather than copying whole source documents or merging identities.

## Candidate inventory — first pass

| Candidate | Source of truth | Classification | Operational lesson | Migration status |
|---|---|---|---|---|
| Interaction is a unit of architecture growth | [EVT-0093](../BEHAVIOR-TRACE/EVT-0093-LIVING-INBOX-AND-INTERACTION-TO-GROWTH-CHAIN-2026-10-22.md) | CONFIRMED EXISTING RULE | Preserve IN/OUT/event/inbox/master/action/evidence chain | LINKED; full source-level adjudication pending |
| Behavior-hunter missed detection and ID collision | [EVT-0103](../BEHAVIOR-TRACE/EVT-0103-BEHAVIOR-HUNTER-MISSED-DETECTION-AND-ID-COLLISION-CORRECTION-2026-10-22.md) | CONFIRMED INCIDENT + RULE | Separate capture from behavioral discovery; enforce ID uniqueness before write; preserve false negatives | LINKED; runtime enforcement OPEN |
| Current continuation target is model-initial, not Dropbox | [EVT-0106](../BEHAVIOR-TRACE/EVT-0106-RESUME-HAIF-EXECUTION-NOT-DROPBOX-2026-10-23.md) | CONFIRMED ROUTING RULE | Read latest 0.0/master/queue before selecting work; keep Dropbox separate | LINKED; active routing rule |
| Do not repeat a closed, valid test without a trigger | [REG-2026-09-03-NO-REDUNDANT-RETEST-001](../../registrations/REG-2026-09-03-NO-REDUNDANT-RETEST-001.md) | CONFIRMED GOVERNANCE RULE | TEST → CORRECT RESULT → RECORD → VERIFY → CLOSE → DO NOT REPEAT; retest on material trigger | LINKED; preserve existing canonical registration |
| Living lesson lifecycle and append-only recovery | [LAL-20261023-001](./lessons/LAL-20261023-001-LIVING-APPEND-ONLY-VERIFY-RECOVER-CYCLE.md) | CONFIRMED GOVERNANCE RULE | Version successor, preserve failures, test recovery, promote only with evidence | CURRENT LESSON |
| Audit evaluator false-negative correction | [EVT-0035](../BEHAVIOR-TRACE/EVT-0035-BEHAVIOR-EVALUATOR-FALSE-NEGATIVE-C4-2026-10-22.md) and [Behavior Observatory recovery test](../BEHAVIOR-OBSERVATORY/BEHAVIOR-OBSERVATORY-RECOVERY-TEST-2026-10-22-001.md) | CONFIRMED TEST/INTERPRETATION LESSON | Treat automated negative as a finding to investigate; compare with source evidence; preserve initial and corrected results | LINKED; duplicate/lineage adjudication pending |
| Persistence continuity, version succession and recovery | [Persistence Continuity / No-Drop Recovery Architecture](../../../architecture/memory/PERSISTENCE-CONTINUITY-NO-DROP-RECOVERY-ARCHITECTURE-2026-09-29.md) | EXISTING ARCHITECTURE RULESET | Preserve lineage, version succession, rollback and recovery as explicit events | SOURCE FOUND; map individual clauses in next pass |
| Recovery bootstrap and rollback as a lineage event | [Memory Persistence Proof / Master Archive Recovery Bootstrap](../../../architecture/memory/MEMORY-PERSISTENCE-PROOF-MASTER-ARCHIVE-RECOVERY-BOOTSTRAP-2026-09-29.md) | EXISTING RECOVERY RULESET | Rollback creates a new lineage event; it does not erase the defective version | SOURCE FOUND; cross-check against current governance pending |
| Path-selection error and proof boundaries | [EVT-0108](../BEHAVIOR-TRACE/EVT-0108-LIVING-ARCHITECTURE-EXECUTION-AND-EVIDENCE-CYCLE-2026-10-23.md) and prior [EVT-0106](../BEHAVIOR-TRACE/EVT-0106-RESUME-HAIF-EXECUTION-NOT-DROPBOX-2026-10-23.md) | CONFIRMED ROUTING / EVIDENCE LESSON | Distinguish file exists, previous CI pass, new test executed, and end-to-end proof | LINKED |

## Classification rules

- CONFIRMED RULE: directly supported by an existing canonical rule/document or test result.
- CONFIRMED INCIDENT: an event with recorded evidence; do not automatically generalize its cause.
- EXISTING ARCHITECTURE RULESET: source exists but clause-by-clause normalization has not been completed.
- HYPOTHESIS: keep separate until tested; do not silently upgrade to confirmed.
- DUPLICATE CANDIDATE: keep both source identities until provenance and semantic equivalence are adjudicated.

## Next migration actions

1. Expand the search across canonical docs/, architecture/, registration records, master references, behavior traces, inbox entries, queues and historical drafts.
2. Build a candidate-to-source graph with Stable ID, Production ID, source path, version, evidence class, affected component and duplicate/lineage notes.
3. Compare candidates semantically; never merge merely because IDs or wording resemble each other.
4. Promote a candidate to a standalone lesson only after source provenance, operational rule, acceptance criteria and test evidence are recorded.
5. Reconcile this ledger with the registry, CMIND, reference index, behavior-trace index, 0.0 index and integration queue.
6. Preserve all findings and failed searches; an empty search result is not proof that no lesson exists.

## Acceptance and status

- Initial evidence-backed candidate batch recorded: YES.
- Complete historical inventory: NO — OPEN.
- All candidates normalized into standalone lesson files: NO — OPEN.
- Runtime enforcement: NOT PROVEN.
- Global rollback/recovery: NOT PROVEN.
