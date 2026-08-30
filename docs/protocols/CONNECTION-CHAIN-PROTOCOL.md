# Connection Chain Protocol

**Project:** Future AI / Palang Footprint  
**Protocol ID:** CCP-2026-08-30-001  
**Status:** ACTIVE — CANONICAL REGISTRATION  
**Version:** 1.3  
**Reference Point:** 0.0  
**Date:** 2026-08-30  

## 1. Purpose

This protocol prevents loss of continuity between separate chats, temporary context detours, and returns to a prior checkpoint. A new chat or a return from command `00` must establish a traceable connection to the previous verified state before substantive continuation.

## 2. Mandatory Transition Rule

> **No Connection Record → No Continuation Transition**

A connection record is a prerequisite for continuation. The assistant must not silently infer continuity from conversation similarity alone.

## 3. Connection Header

At the start of every new chat, continuation from a previous chat, or return from `00`, create a Connection Header containing at minimum:

- Connection ID
- Date
- Exact local time
- Timezone
- Country and city, with `VERIFIED`, `ESTIMATED`, or `UNVERIFIED` status
- Project
- Previous Checkpoint / Reference
- Previous state
- Current state
- Last verified step
- Unverified gaps
- Continuation target
- Verification status
- Registration status

## 4. Required Execution Order

1. **STOP** — identify the transition point.
2. **RECORD** — create the Connection Header.
3. **RETRIEVE** — when a prior `0.0`/checkpoint is referenced, retrieve the stable reference before relying on memory or inference.
4. **RECONCILE** — inspect all open durable-registration/recovery records before substantive continuation.
5. **RECOVER PATH** — recover the exact prior project path, including whether the prior work was unfinished or completed, the last completed action, the exact next action, and any active detour/return state.
6. **VERIFY** — distinguish proven facts from unverified information.
7. **REGISTER** — register the new production in all required durable destinations.
8. **CONTINUE** — only after the preceding gates pass, except where an explicitly documented unavailable capability blocks the gate.

## 5. Continuity State Must Preserve the Work Path

A checkpoint is not only a timestamp or a list of rules. Every project checkpoint intended for later continuation must preserve a **Continuation Path Record** containing, at minimum:

- Checkpoint ID
- Project and branch/path identity
- Exact goal at the stop point
- Work status: `UNFINISHED`, `COMPLETED — CONTINUE`, `PAUSED`, or `CLOSED`
- Last verified action
- Last verified artifact/evidence
- Exact unfinished task(s), if any
- Exact next intended action
- Decisions/rules that must govern continuation
- Active temporary detours (`00`) and their return target
- Open reconciliation records
- Proven/verified items
- Unverified items
- Dependencies/blockers
- Recovery source(s)
- Version/date/time metadata

### 5.1 Unfinished vs Completed Continuation

The recovery system must distinguish these two cases explicitly:

**A. `UNFINISHED`** — resume the exact unfinished task before inventing a new direction.

**B. `COMPLETED — CONTINUE`** — do not reopen completed work as unfinished; resume from the recorded next growth/refinement target of the same path.

A greeting such as `درود و مهر` is a **connection event, not a new project command**. It must never reset, replace, or redirect the recovered project path.

## 6. Path Lock / Continuation Anchor

Every `0.0` checkpoint creates or updates a **Continuation Anchor**. On the next connection transition, the anchor is the default continuation target unless the user explicitly changes the target.

> **No Explicit New Target → Resume the Last Valid Continuation Anchor**

A new chat, greeting, temporary detour, context loss, or tool limitation cannot by itself create a new project direction.

If retrieval of the exact anchor fails, the system must enter `RECOVERY REQUIRED / NO GUESS` and must not substitute a merely similar topic as the continuation path.

## 7. New Production Registration Chain

For every newly produced rule, command, principle, protocol, architecture element, structure, artifact, or other formal project production, the following chain applies:

**Production → Identity → Classification → Architecture/Structure → Playground/Runtime placement → Documentation → Persistent Memory (when appropriate) → Canonical Repository → Verification → Final Status**

Registration in memory alone is not equivalent to canonical project registration.

## 8. Dual Durable Registration Gate

Every required durable destination is an independent gate. The two primary durable destinations are:

1. **Persistent Memory**, when the production is appropriate for memory.
2. **Canonical Project Repository**, when the production belongs in the project's independent repository.

Each destination must have its own explicit state: `SUCCESS`, `PENDING`, `FAILED`, or `UNAVAILABLE`.

Success at one destination must never be inferred for the other, and a failed destination must not cause an already successful destination to be rolled back.

## 9. Failure, Recovery, and First-Opportunity Reconciliation

If any required durable destination cannot be completed, the production immediately enters an explicit `PENDING / UNVERIFIED` state for that destination. A recovery/reconciliation record must be created with:

- Reconciliation ID
- Production ID
- Failed destination
- Attempt timestamp
- Failure/unavailability state
- Evidence of any successful destination
- Required next action
- Reconciliation status
- Completion timestamp and evidence when later resolved

A pending item is never considered complete, but it is also never considered lost.

The **first-valid-opportunity trigger** is mandatory. A reconciliation attempt must be initiated whenever the required capability becomes available and, at minimum, at the beginning of every new chat, continuation from a prior chat, return from `00`, or other project transition where the recovery records can be retrieved. Open reconciliation items must be checked **before new substantive project production or continuation**.

The reconciliation cycle is:

**DETECT → RECORD → PRESERVE SUCCESS → QUEUE FAILURE → FIRST VALID OPPORTUNITY → RETRY → VERIFY → CLOSE**

If retry is still impossible, retain the item as `PENDING / UNVERIFIED` with an updated attempt timestamp and explicit next action. No silent dropping, overwriting, or indefinite untracked deferral is permitted.

## 10. Reconciliation Gate Before Continuation

At every connection transition, the system must first retrieve open reconciliation records. If a required destination is now available, reconciliation must be attempted before proceeding with unrelated substantive work. If the destination remains unavailable, the system may continue only with the limitation explicitly recorded in the Connection Header and reconciliation record.

## 11. Evidence Integrity

No operation may be claimed as completed, synchronized, canonicalized, tested, or verified without recoverable evidence for that operation. Access, intent, design, or an instruction to perform an operation is not evidence that the operation occurred.

## 12. Scope

This protocol is part of the Future AI / Palang Footprint execution architecture and applies to future production and continuity transitions unless a later canonical rule explicitly supersedes it.

## 13. Initial Registration Record

**Trigger:** Identified continuity/path-loss gap on 2026-08-30.  
**Production:** Connection Chain / Connection Header / Continuation Anchor extension.  
**Current version:** 1.3.  
**Current status:** Canonical repository artifact updated to preserve unfinished/completed continuation state and prevent a greeting or temporary context transition from redirecting the project path.  
