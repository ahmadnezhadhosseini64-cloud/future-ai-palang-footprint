# Palang Persistent-Memory Recovery Hammer

**ID:** PMRH-2026-09-06-001  
**Status:** FINAL / ACTIVE / LIVING / PERMANENT  
**Project:** Future AI / Palang Footprint  
**Reference:** 0.0  
**Owner:** Ahmad Nezhadhosseini  
**Date:** 2026-09-06

## Purpose
Prevent valuable productions from becoming "only words" when ChatGPT Persistent Memory is unavailable, limited, or cannot be independently read back. Every approved production must have a durable recovery destination and a deterministic path back to live reconciliation.

## Hammered Contract
`PRODUCTION → UNIQUE ID → CLASSIFY/ROUTE → MEMORY WRITE+READ-BACK IF AVAILABLE → OTHERWISE DURABLE REPOSITORY/RECOVERY PENDING → MARK MEMORY PENDING/UNVERIFIED → EXCAVATION/RECOVERY → SAME ID → MEMORY WRITE → READ-BACK → VERIFY → RECONCILE → CLOSE`

## Non-Negotiable Invariants
1. **No Record → No Transition.**
2. **No durable destination → no success claim.**
3. Persistent Memory `VERIFIED` requires provider-level WRITE plus independent READ-BACK; repository presence alone cannot imply Memory success.
4. If Memory is unavailable/limited, the **same complete Production ID and payload** must be preserved in the canonical Repository / Recovery Pending Store.
5. A pending record is not dead data: it is an **excavatable live recovery item** discoverable by the Deep Excavation/Revival command/path.
6. Excavation never creates a replacement production; it retrieves the existing ID and revives/reconciles its lineage.
7. Reconciliation is idempotent: **same Production ID, no duplicate.**
8. `PENDING / UNVERIFIED` is an explicit operational state, never an implicit loss.
9. No READ-BACK → no VERIFIED; no evidence → no completion claim.
10. Repository-side success and ChatGPT Persistent Memory success are separate states.

## Routing Rule
For every `ثبت کن` / registration request, the system must determine the applicable destinations. At minimum:
- **Canonical Repository:** authoritative durable project record.
- **Recovery/Pending Store:** mandatory fallback when a required destination is unavailable.
- **Reference / Architecture / Registry / Evidence / Checkpoint:** added according to record type and architectural relevance.
- **Persistent Memory:** attempted only through an actually available authorized interface; marked `VERIFIED` only after independent read-back.

## Excavation Rule
A later `فرمان خاک‌برداری` must search pending/recovery records, validate lineage and integrity, inherit current 0.0/master rules, revive the original record, and continue reconciliation. It must not silently discard, rewrite, or duplicate the original production.

## Failure Rule
If any destination is unavailable:
`STOP → PRESERVE SAME ID → PENDING/UNVERIFIED → EVIDENCE → RETRY/EXCAVATION → RECONCILE → VERIFY`.

## Anti-False-Completion Test
A production fails this control if:
- it exists only in assistant text with no durable record;
- Memory is claimed `VERIFIED` without provider read-back;
- repository persistence is treated as equivalent to Memory persistence;
- pending data has no discoverable recovery route;
- excavation produces a duplicate ID;
- a retry silently creates a new production instead of reconciling the original.

## Relationship to Existing Controls
- `PMDRP-2026-08-31-001` — Persistent Memory Deferred Reconciliation Protocol
- `PMA-2026-09-01-001` — Persistent Memory Adapter Specification
- `GEN-EXEC-GOV-2026-09-06-001` — Generation & Execution Governance
- `PEFH-2026-09-06-001` — Palang Execution Fidelity Hammer
- `MPGG-2026-09-01-001` — Persistent Memory evidence boundary
- `0.0` — STOP → RECORD → VERIFY → THEN CONTINUE/GOODBYE

## Completion Criterion
This hammer is complete only when the rule is documented, routed into the governance layer, linked to the existing PMDRP/PMA controls, registered in the Production Registry, and independently read back from the canonical Repository. Provider-level Persistent Memory remains `UNVERIFIED` unless an actual Memory interface supplies WRITE + READ-BACK evidence.
