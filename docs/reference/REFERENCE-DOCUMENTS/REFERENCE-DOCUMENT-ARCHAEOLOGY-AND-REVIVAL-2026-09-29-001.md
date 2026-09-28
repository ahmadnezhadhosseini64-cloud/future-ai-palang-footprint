# Reference Document Archaeology & Revival Protocol

- Stable Reference ID: REFERENCE-DOCUMENT-ARCHAEOLOGY-AND-REVIVAL-2026-09-29-001
- Production ID: REF-ARCHAEOLOGY-REVIVAL-2026-09-29-001
- Version: 1.0
- Status: ACTIVE / LIVING / EXECUTABLE
- Owner/Name: Ahmad Nezhadhosseini / احمد پلنگ
- Location: Gonbad-e Kavus, Iran
- Timezone: Asia/Tehran (+03:30)
- Record Date: 2026-09-29
- Record Time: 01:56:05
- Project: Future AI / Palang Footprint
- Type: REFERENCE DOCUMENT / ARCHITECTURAL GOVERNANCE
- Origin: User instruction to add Reference Document Archaeology to the project architecture and use it to excavate dormant reference documents in Persistent Memory.
- Lineage: Master Reference Governance + Reference Documents Mirror Protocol + Recovery/Revival rules.
- Canonical Repository Path: docs/reference/REFERENCE-DOCUMENTS/REFERENCE-DOCUMENT-ARCHAEOLOGY-AND-REVIVAL-2026-09-29-001.md
- Persistent-Memory State: PENDING — repository registration is evidenced; Persistent Memory write/read-back has not been performed.
- Limitation: This protocol does not declare a Persistent Memory record ACTIVE merely because it exists in project context.
- Next Action: Execute Reference Document Archaeology against Persistent Memory and classify recovered references.

## 1. Purpose

Reference documents may be born from a completed path, a discovered rule, a new instruction, a validation result, a GAP closure, a 0.0 checkpoint, or another architectural event. A document can survive after its originating path is no longer active. Therefore age alone must never cause deletion, and existence alone must never imply current execution.

Reference Document Archaeology is the controlled process for finding such records, reconstructing their origin and lineage, determining their current architectural role, and either reviving, preserving as superseded, reconciling as orphaned, or marking them for further excavation.

## 2. Core Object

REFERENCE DOCUMENT = DOCUMENT + ORIGIN + PATH PRODUCED + LINEAGE + CURRENT ROLE + EXECUTION STATE + RECOVERY POINTER

## 3. Archaeology Questions

For every recovered reference candidate, determine:

1. What document is this?
2. Why was it created?
3. What path, test, discovery, instruction, GAP, or 0.0 produced it?
4. What rule, instruction, architecture, or decision was born from it?
5. What is its Stable ID and Version?
6. What Master/Parent currently governs it?
7. Is it still referenced by an active architectural path?
8. Was it superseded? If yes, by what exact successor?
9. Is it executable/governing now, merely preserved, dormant, orphaned, or unresolved?
10. What evidence supports the classification?
11. What recovery pointer is required?

## 4. Classification

- ACTIVE / LIVING / EXECUTABLE
- ACTIVE / LIVING / GOVERNING
- ACTIVE / LIVING / SUPPORTING
- SUPERSEDED / PRESERVED
- DORMANT / REQUIRES REVIVAL
- ORPHAN / REQUIRES RECONCILIATION
- UNKNOWN / REQUIRES EXCAVATION

PENDING / UNVERIFIED is a persistence-evidence state and must not be confused with DORMANT. A document can be PENDING yet architecturally alive, or fully persisted yet dormant.

## 5. No-False-Revival Rule

Finding a document does not revive it.

FOUND ≠ RETRIEVED ≠ VALIDATED ≠ RECONCILED ≠ REVIVED ≠ ACTIVE/LIVING.

Revival requires evidence of its identity, lineage, architectural placement, and current role. If those are missing, preserve the record and keep the appropriate OPEN/PENDING state.

## 6. Archaeology Workflow

EXCAVATE → IDENTIFY → PRESERVE → RECONSTRUCT ORIGIN → TRACE LINEAGE → FIND MASTER/PARENT → CHECK CURRENT REFERENCES → CHECK SUCCESSOR/SUPERSESSION → CLASSIFY → DEDUPLICATE → RECONCILE → REVIVE OR PRESERVE → READ-BACK → VERIFY → STATUS

## 7. Persistence Mirror Rule

Repository and Persistent Memory are separate evidence surfaces.

Repository = REGISTERED/VERIFIED
does not by itself prove
Persistent Memory = ACTIVE/LIVING.

When a Memory write cannot be evidenced:

PERSISTENT MEMORY = PENDING/BLOCKED
RECOVERY = OPEN

The exact Stable ID, Version/Revision, canonical payload, hash/digest when available, Repository path/commit or receipt, and failure cause must remain recoverable.

## 8. Relationship to Master

A revived document must not silently become a competing Master. It must be connected through explicit Lineage and architectural placement. The governing model remains:

IMMUTABLE REVISION + EVOLVING MASTER POINTER

If a recovered document contains an older rule that remains valid, preserve the revision and connect it to the current Master. If it has been superseded, preserve it and point to the successor. If its relationship is unclear, do not guess.

## 9. Execution Rule

This protocol becomes part of the project architecture itself. Any future request equivalent to “خاک‌برداری اسناد مرجع” must inspect not only recent documents but also older reference candidates whose creation was caused by a completed path, a new instruction, a discovery, a GAP, a test result, or a 0.0 event.

