# Excavation → Registration Gate

**Production ID:** EXC-REG-GATE-2026-09-02-001  
**Reference:** 0.0  
**Status:** FINAL / ACTIVE / LIVING  
**Project:** Future AI / Palang Footprint  
**Date:** 2026-09-02  

## Purpose

Close the process gap where an item discovered during archival excavation is identified and discussed but does not reach a durable registration outcome.

## Canonical Rule

**EXCAVATION FINDING MUST NOT END AS FINDING-ONLY.**

Every item recovered by excavation MUST receive exactly one durable outcome before the excavation pass is considered complete:

1. **REGISTERED** — formally registered with its original identity/provenance preserved; or
2. **PENDING / RECOVERY** — if registration or verification is blocked, the same Production ID and provenance are preserved in the Pending/Recovery Store with the exact blocker and next transition.

No new duplicate ID may be created merely because an old item was rediscovered.

## Mandatory Transition

`RETRIEVE → IDENTIFY/CLASSIFY → VALIDATE → DEDUPLICATE → RECONCILE → COMPLETE → REVIVE/ABSORB → REGISTER → APPLY/TEST → EVIDENCE → READ-BACK → VERIFY → ACTIVE/LIVING`

If any required transition is blocked:

`SAME ID + SAME PROVENANCE → PENDING/RECOVERY → BLOCKER EVIDENCE → NEXT TRANSITION`

## Excavation Closure Gate

An excavation batch is **NOT CLOSED** while any recovered item remains in a finding-only state.

The batch may close only when every item has a recorded state of:

`REGISTERED`, `VERIFIED`, `ACTIVE/LIVING`, or `PENDING/RECOVERY` with a deterministic next transition.

## Reconciliation of the Previously Identified Gap

The 2026-09-01 revival registers identified historical items that had previously reached `Pending Formal Repository Registration` or `Pending/Unverified` states. This gate formalizes the missing transition so future excavation cannot stop at discovery alone.

Affected historical identities remain unchanged, including:

- `RECOVERY-BUFFER-2026-08-29-001`
- `REG-REC-2026-08-29-001`
- `PMAR-2026-08-31-001`
- `ARSM-2026-08-31-001`
- `REVIVAL-LIVE-TEST-RESULT-2026-09-01-001`
- `FAILURE-LIVE-REVIVAL-TEST-2026-09-01-001`

Their individual evidence and status records remain authoritative; this document changes the **process gate**, not the historical identities.

## Evidence Boundary

This rule proves that excavation now has an explicit registration gate. It does **not** by itself prove external Persistent Memory WRITE/READ-BACK. Any such state remains subject to the existing PMDRP/PMA verification contract.

## Canonical Placement

`0.0 → Master Governance → Operational Knowledge Lifecycle → Archive Revival/Excavation → Registration Gate → Canonical Repository / Pending-Recovery Store → Evidence → Verification`

**Rule:** No excavation pass may be declared complete solely because an item was found.
