# Recovery & Resilient Memory Architecture

**Project:** Future AI / Palang Footprint  
**Reference Point:** 0.0  
**Date:** 2026-08-29  

## Purpose

Define a resilient memory, retrieval, recovery, registration, and repository-reconciliation architecture that prevents project knowledge from being lost when a conversation, AI session, repository connection, or external service becomes unavailable.

## Architecture Layers

1. **Working Memory** — current interaction context; useful for active work but not treated as the sole durable project memory.
2. **Recovery Buffer** — protected holding area for records produced but not yet formally registered. Pending records retain their unique identity and state.
3. **Stable Retrieval Core** — durable, structured project knowledge containing the Canonical Master, architecture, rules, checkpoints, provenance, recovery state, manifest, retrieval index, and synchronization state.
4. **Recovery Manifest** — compact map of canonical sources, latest verified checkpoint, pending records, recovery location, repository state, and last verified state.
5. **Retrieval Index** — maps unique IDs to type, version, location, status, and relationships so existence is coupled to reliable retrieval.
6. **Repository** — official external registration and verification layer; repository availability must not be the sole dependency for continuity.

## Persistence and Reconciliation

Every material project record is persisted to the Recovery Buffer before or together with an attempted repository synchronization. A repository failure such as HTTP 403 changes the record to `PENDING`; it does not delete or recreate the record.

Repository retry is performed at defined triggers, including registration requests, step/checkpoint operations, 0.0 recovery operations, explicit synchronization requests, and recovery from a previously failed connection.

Every retry begins with **Reconcile**. Retry is not permission to create a duplicate record. The existing unique ID is reconciled against the repository before registration.

## Registration State Machine

`Persist → Attempt Sync → PENDING on failure → Reconcile → Register → Retrieve → Verify → ACTIVE`

`Register` alone is never sufficient to claim verified registration. `Retrieve` and `Verify` are mandatory before `ACTIVE`.

## Recovery Protocol

At 0.0 the recovery sequence is:

**Retrieve → Verify → Reconcile → Respond → Continue**

If the repository is unavailable, recovery proceeds from the Stable Retrieval Core / Recovery Buffer without treating repository unavailability as project-data loss.

## Human Approval Gate (HAG)

AI may detect and report a potentially new architectural item, but it does not have authority to approve it as a formal project rule or architectural change.

Potentially architecture-affecting productions—including new definitions, names, laws/rules, principles, commands, Master changes, formal checkpoints, and identity changes—are presented to the human for explicit approval before formal registration.

**AI = Detect + Report**  
**Human = Approve**  
**System = Persist + Register + Retrieve + Verify**

Required transition:

`Detect → Report → Human Approval → Persist → Register → Retrieve → Verify → ACTIVE`

Without explicit approval, the item remains a candidate/review state and must not enter formal registration or the active architectural core.

Accepted approval triggers include clear commands such as `تأیید کن`, `ثبت کن`, or `رسمی کن` when the target item is unambiguous. Ambiguous conversational agreement is not treated as formal approval.

**No Human Approval → No Formal Registration**

This gate prevents autonomous AI-generated changes from silently becoming architectural truth while preserving valuable candidates for human review.

## Confirmed Interaction Behavior

The Human Approval Gate behavior described above has been explicitly reviewed and confirmed by the human project owner as correct. This confirmation does not grant autonomous approval to future candidates; future architecture-affecting candidates must still be reported and explicitly approved before formal registration.

## Batch Reconciliation

When multiple pending records exist, reconciliation is performed as a batch rather than requiring one-by-one manual prompting. Each record retains its unique identity; reconciliation precedes any registration attempt, and failures remain isolated as pending/investigation states without blocking unrelated records.

## Current Pending Record

`REG-REC-2026-08-29-001` is the existing unique recovery-registration record. Its state must be determined from repository evidence; no duplicate record may be created for the same identity.

## Architectural Invariants

- **No Record → No Transition**
- **No Human Approval → No Formal Registration**
- **No Retrieve → No Verified Registration**
- **No Verification → No Active**
- **Retry ≠ New Registration**
- **Repository outage ≠ Project-data loss**
- **No Single Memory Dependency**
- **Detect ≠ Approve**
- **Persist ≠ Active**
- **Register ≠ Verify**

## Documentation Requirement

The recovery, retry, reconciliation, retrieval, and human-approval path itself is part of the architecture and must remain documented in the official repository when repository access is available. Changes to this architecture must be versioned and reconciled rather than silently replacing historical evidence.
