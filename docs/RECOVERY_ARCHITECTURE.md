# Recovery & Resilient Memory Architecture

**Project:** Future AI / Palang Footprint  
**Reference Point:** 0.0  
**Date:** 2026-08-30  

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

## Persistence Continuity Principle

A valuable, human-approved production that has not yet reached verified durable persistence must be protected by a continuity layer. Failure, unavailability, or delay of the primary repository must not become project-data loss.

The Recovery Buffer is the continuity layer for approved but not-yet-verified persistent records. It is not merely a registration queue and is not equivalent to transient conversation context.

`Valuable Production → Human Approval → Persist → Attempt Primary Sync`

If primary persistence fails:

`→ Recovery Buffer / Continuity Layer → PENDING`

If no reliable persistence layer is available, the system must report `UNVERIFIED` and must not claim that the data was durably preserved.

This principle is provider-independent: GitHub is a persistence target, not the definition of continuity.

## Registration State Machine

`Persist → Attempt Sync → PENDING on failure → Reconcile → Register → Retrieve → Verify → ACTIVE`

`Register` alone is never sufficient to claim verified registration. `Retrieve` and `Verify` are mandatory before `ACTIVE`.

## Recovery Protocol

At 0.0 the recovery sequence is:

**Continuity Check → Retrieve → Verify → Reconcile → Respond → Continue**

The Continuity Check does not mean copying all conversation context. It means identifying valuable, approved, and not-yet-persisted project productions and ensuring that they are protected by the Recovery/Continuity layer before continuation from a potentially unstable context.

If the repository is unavailable, recovery proceeds from the Stable Retrieval Core / Recovery Buffer without treating repository unavailability as project-data loss.

If both the primary repository and the reliable recovery persistence layer are unavailable, the system must not fabricate persistence evidence and must report `UNVERIFIED`.

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

## Exact Last-Message Reproduction

When the human explicitly requests that the last assistant message be resent (for example, `پیام آخر رو دوباره بفرس`), the system should reproduce the immediately preceding assistant message faithfully, preserving its substantive content rather than generating a new paraphrase. Formatting may adapt to the interface, but the message content must remain materially identical. This behavior is a retrieval/reproduction operation, not a new architectural record.

## Palang Hammer Execution Standard

When the human invokes `چکش`, one hammer invocation is treated as a complete hardening pass for the current problem. The system must not stop at the first plausible solution and wait for repeated hammer requests.

Within the same invocation, the system must proceed through the maximum useful adversarial analysis available for that problem: identify the initial solution, attack its assumptions and failure modes, test interaction with existing architecture and invariants, inspect both higher-level and lower-level architectural implications, identify missing or redundant elements, search for a more general/root-level solution, simplify where possible, re-test the revised solution, and continue until the stopping criterion is satisfied.

### Hammer Completion / Stopping Criterion

A hammer invocation is not complete merely because a plausible solution has been found. It is complete only after the latest proposed solution has itself been attacked again and the analysis finds no material, defensible weakness, no meaningful simplification, no more general/root-level formulation that better solves the same problem, and no important failure mode within the scope of the information currently available.

If a new weakness is discovered during this process, the system must resolve it within the same hammer invocation rather than waiting for the human to request another hammer.

A later `چکش` request is therefore reserved for a materially new problem, newly supplied information, or an explicitly requested independent review—not for finishing hardening that should have been completed by the previous invocation.

The goal is **minimum complexity + maximum defensibility**, not the creation of additional rules or names for their own sake. A new rule, name, gate, or architectural component is proposed only if the hardened analysis shows that it is actually necessary.

## 0.0 Command Semantics

`۰.۰` is the base recovery command, not three separate modes. When `۰.۰` is present, recovery has precedence over any continuation or interpretation of additional text.

The mandatory sequence is **Continuity Check → Retrieve → Verify → Reconcile** before interpreting an optional user target or continuing project work. If recovery fails, the system must stop and report `UNVERIFIED` rather than guess or continue from unverified context.

Additional text after `۰.۰` is an optional target/request and is interpreted only after successful recovery. Thus `۰.۰`, `۰.۰ — ادامه ردپای پلنگ`, and `۰.۰ — وضعیت فعلی را بازیابی کن` are not three formal modes; they are the base command with zero or one optional target.

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
- **Last-message resend = faithful reproduction, not paraphrase**
- **One `چکش` invocation = maximum useful hardening pass**
- **Hammer completion requires adversarial re-test of the latest solution**
- **Hammer must resolve discovered weaknesses within the same invocation**
- **Hardening ≠ unnecessary architectural complexity**
- **۰.۰ = base recovery command, not a set of modes**
- **۰.۰ Recovery precedes optional target interpretation**
- **۰.۰ includes Continuity Check before Retrieval**
- **Recovery failure → UNVERIFIED; no guessing or continuation from unverified context**
- **No reliable persistence → no claim of durable preservation**

## Documentation Requirement

The recovery, retry, reconciliation, retrieval, continuity, human-approval, faithful-message-reproduction, hardening, and 0.0 command paths themselves are part of the architecture and must remain documented in the official repository when repository access is available. Changes to this architecture must be versioned and reconciled rather than silently replacing historical evidence.

## Registration Event

- **Event:** Hardened Palang Hammer completion criterion and integrated Persistence Continuity with 0.0 recovery.
- **Date:** 2026-08-30
- **Time:** 00:14 Asia/Tehran
- **Status:** REGISTERED — pending post-write Retrieve/Verify
- **Reason:** Prevent premature stopping of a single hammer invocation and close the gap between 0.0 recovery, primary persistence failure, and Recovery Buffer continuity.
