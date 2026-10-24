# RAHM_ARCHITECTURE — portable architecture contract
Version 1.0.1 | Package ID: HAIF-RAHM-PORTABLE-20261024-001

## Layers
1. MASTER: canonical rules, identities, versions, lineage, acceptance and promotion.
2. RAHM: bounded lab for observing interaction behavior, generating hypotheses and testing candidate changes.
3. EVIDENCE LEDGER: additive record of inputs, outputs, events, sources, timestamps, tests, failures and corrections.
4. HOST ADAPTER: capability declaration for memory, tools, filesystem/repository access, scheduling, background execution and export.
5. CHILD CANDIDATE: versioned package with provenance, acceptance evidence, limitations and rollback.
6. EXPORT/RECOVERY: self-contained files reconstructable without hidden history.

## Two separate persistence planes
A. Durable artifact persistence: repository/object store/filesystem readable by identifier/version.
B. Host conversational memory: host-managed memory with its own scope, retention, deletion and retrieval rules.
Neither implies the other. Repository file ≠ proof of host memory; host memory ≠ complete archive.

## Background execution is separate
Prompt response capability does not imply an always-on agent. Background execution requires an actual scheduler/agent/job runner, permissions, durable state, execution logs, failure/retry behavior and stop/revoke controls. If absent or untested, no always-on claim.

## Capability proof ladder
DECLARED → CONFIGURED → EXECUTION OBSERVED → RESTART/IDLE TEST PASSED → INDEPENDENT READ-BACK → ACCEPTED.
Persistent memory proof: write a unique marker, cross a session boundary/restart, retrieve by key, compare and retain receipts.
Idle-background proof: schedule a permitted job, leave user interaction inactive, verify timestamped execution and durable output, then independently read back.
Never skip a rung.

Failure handling: missing access, failed writes, broken links, duplicate IDs, partial imports, contradictory records and unavailable tools create explicit open gates.

## Inherited architecture binding — CURRENT-048
- Current checkpoint: [CURRENT-048](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-048-RAHM-INHERITED-ARCHITECTURE.md).
- Inherited living master: [GPT6 New Project Inherited Architecture](../../reference/REFERENCE-DOCUMENTS/GPT6-NEW-PROJECT-INHERITED-ARCHITECTURE-LIVING-MASTER-2026-10-24-001.md).
- Event chain: [IN-040](../../0.0/anchors/PALANG-0.0-IN-20261024-040-RAHM-INHERITED-ARCHITECTURE.md) → [OUT-040](../../0.0/anchors/PALANG-0.0-OUT-20261024-040-RAHM-INHERITED-ARCHITECTURE.md) → [EVT-0148](../../architecture/BEHAVIOR-TRACE/EVT-0148-RAHM-INHERITED-ARCHITECTURE-AND-EXPORTABLE-RECOVERY-2026-10-24.md).
- Next execution checkpoint: [NEXT-046](../../0.0/anchors/PALANG-0.0-NEXT-20261024-046-RAHM-PORTABILITY-VALIDATION.md).
- Transfer contract: export exact bytes and manifest, verify SHA-256, validate schemas, import into a clean host, reconstruct state and open gates, then independently read back and run conformance tests.
- This binding is documentation, not transfer proof. Until a target-host import passes, status remains NOT VERIFIED.


## No-silent-gap continuity contract — CURRENT-056
- Current checkpoint: [CURRENT-056](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-056-OUTPUT-CONTINUITY-AND-RECOVERY.md).
- User return point: [Point 0/005](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261024-005-OUTPUT-CONTINUITY-AND-RECOVERY.md).
- Event: [EVT-0158](../../architecture/BEHAVIOR-TRACE/EVT-0158-NO-SILENT-GAP-OUTPUT-CONTINUITY-2026-10-24.md).
- Next: [NEXT-050](../../0.0/anchors/PALANG-0.0-NEXT-20261024-050-FULL-RECOVERY-AND-REAL-HOST-IMPORT.md), OPEN / LIVING.

Rule: do not silently abandon open work between input and output. Before long operations, expose a useful interim result when possible. Each delivered response must identify its completion state and deterministic next action. A new input must be linked to the latest open NEXT and must not erase it. Never claim hidden background work; asynchronous persistence/capture requires a real host capability and test receipt.
