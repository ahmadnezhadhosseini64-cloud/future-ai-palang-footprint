# RAHM_ARCHITECTURE — portable architecture contract
Version 1.0.2 | Package ID: HAIF-RAHM-PORTABLE-20261024-001

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

## Current canonical binding — CURRENT-059 / Point 0/008

- Current checkpoint: [CURRENT-059](../../0.0/anchors/PALANG-0.0-CURRENT-20261025-059-DEEP-AUDIT-AND-CORRECTED-CONFORMANCE.md).
- User return point: [POINT-0/008](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261025-008-DEEP-AUDIT-AND-NO-SILENT-GAP.md).
- Interaction chain: [IN-052](../../0.0/anchors/PALANG-0.0-IN-20261025-052-DEEP-AUDIT-NO-SILENT-GAP-AND-EXECUTION.md) → [OUT-051](../../0.0/anchors/PALANG-0.0-OUT-20261025-051-DEEP-AUDIT-NO-SILENT-GAP-AND-EXECUTION.md) → [EVT-0161](../../architecture/BEHAVIOR-TRACE/EVT-0161-DEEP-AUDIT-STALE-GATE-AND-NO-SILENT-GAP-2026-10-25.md) → CURRENT-059 → [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).
- Portable master: [FIRST-LIVING-MASTER](./FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md); startup contract: [RAHM_BOOT](./RAHM_BOOT.md); manifest: [EXPORT_MANIFEST](./EXPORT_MANIFEST.json).
- Transfer contract: stable core files have pinned exact-byte SHA-256 values; mutable current-state references are included and hashed per build; the package archive SHA-256 binds the exact snapshot. A successful CI package does not prove independent AI-host import.
- Latest successful strict conformance and audit receipts are linked from the workflow history. Use the latest successful run for the exact commit being transferred.

## No-silent-gap continuity contract — CURRENT-059
- Every input is linked to a Point 0/IN record and a delivered OUT/event/current state; if execution cannot finish, expose a useful partial result with the exact resume step.
- A new input does not overwrite or close prior open work. Preserve branches and update the existing NEXT with receipts.
- A NEXT file is a plan, not proof of execution. Never mint a successor NEXT until the current acceptance criteria have evidence.
- Keep all unverified gates OPEN: clean host import, second host, persistent-memory restart, automatic capture, idle/background execution, and unresolved graph identity/parent/time findings.
- The architecture is ACTIVE/LIVING as repository artifacts; host runtime activation and permanent background operation remain NOT VERIFIED until tested in a real authorized host.
