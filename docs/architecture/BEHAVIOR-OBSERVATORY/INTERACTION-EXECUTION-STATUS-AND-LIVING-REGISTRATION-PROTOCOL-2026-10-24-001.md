# Interaction Execution Status and Living Registration Protocol

- Stable ID: PALANG-INTERACTION-EXECUTION-STATUS-PROTOCOL-2026-10-24-001
- Production ID: IESLP-HAIF-2026-10-24-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / REPOSITORY-REGISTERED
- Parent event: [EVT-0129](../BEHAVIOR-TRACE/EVT-0129-LIVING-REGISTRATION-ARCHITECTURE-GROWTH-AND-RECOVERY-REPAIR-2026-10-24.md)
- Current interaction: [IN-031](../../0.0/anchors/PALANG-0.0-IN-20261024-031-ACTIVATE-LIVING-ARCHITECTURE-GROWTH.md) / [OUT-031](../../0.0/anchors/PALANG-0.0-OUT-20261024-031-ACTIVATE-LIVING-ARCHITECTURE-GROWTH.md)

## Purpose
Prevent long-running work from becoming invisible to the user, and prevent a successful old test from being mistaken for proof that the newest interaction or current architecture was recovered.

## Required interaction lifecycle
1. **ACKNOWLEDGED** — acknowledge a multi-step request and state the active target.
2. **RUNNING** — report only when a real operation is underway; do not imply background work persists after the tool call ends.
3. **EVIDENCE-COLLECTED** — identify actual commits, workflow runs, logs, manifests or source files.
4. **REGISTERED** — record the exact input/output pair, event and next checkpoint in the canonical repository.
5. **READ-BACK VERIFIED** — reread the exact written paths and validate their links/content.
6. **TESTED** — report exact tested SHA, run URL, test count and artifact identity; distinguish a later HEAD from the tested SHA.
7. **RECONCILED** — update master, integration queue, indexes and append-only architecture ledger.
8. **FINAL STATUS** — provide result, remaining gaps and one next action. If the work continues across turns, the next visible response must say what is running or what remains, not leave silence as a status.

## Status vocabulary
- `RUNNING`: a real tool/job is currently in progress.
- `REGISTERED`: content was written; no read-back claim yet.
- `READ-BACK VERIFIED`: the exact saved content was fetched and checked.
- `PASS`: the defined test passed on the stated source SHA.
- `PARTIAL`: some required nodes or checks remain missing.
- `BLOCKED`: a required invariant fails or the newest interaction cannot be safely resolved.
- `OPEN / NOT RUN / NOT VERIFIED`: the relevant work is not completed or has no sufficient evidence.
- `ACTIVE / LIVING`: a durable continuation contract exists. It does not mean an external service is continuously running.

## Architecture growth/update cycle
`OBSERVE → ANCHOR IN/OUT → SOURCE-HASHED EVIDENCE → PROPOSE CHANGE → VALIDATE SCHEMA → TEST IN ISOLATION → EXPLICIT OWNER DECISION → APPEND VERSION → REGRESSION TEST → READ-BACK → UPDATE MASTER/QUEUE/INDEX → ACTIVATE NEXT CHECKPOINT`.

Prior versions are immutable history. A new architecture version is appended and linked; it does not overwrite the prior approved record. Failed tests and rejected proposals are retained as learning evidence. No bulk rename, merge, delete, or silent promotion based on identifier similarity.

## Recovery invariant
The recovery resolver must discover the latest shared interaction ID from the repository's IN/OUT anchors. It must not pass using a hard-coded historical pair. If the newest pair is incomplete or non-reciprocal, the resolver must block rather than silently fall back to an older pair. The event, NEXT checkpoint, master and queue must reference the same current pair.

## Scope boundary
This protocol governs repository artifacts and assistant response discipline. It cannot itself force the ChatGPT interface to show continuous progress, guarantee capture of every live conversation, or prove external persistence. Those require separate integration tests and explicit evidence.

## Acceptance criteria
- Current pair is discovered dynamically and recovered from either direction.
- A malformed latest pair blocks; an older pair is not used as a silent fallback.
- Master, queue, event and NEXT checkpoint all contain current pair references.
- Architecture ledger is append-only and its hash chain passes.
- A fresh-session recovery is independently performed and documented; until then it remains NOT RUN.
