# MEMORY PERSISTENCE PROOF ARCHITECTURE
Reference ID: MPPA-2026-09-28-001
Project: Future AI / Palang Footprint
Type: Architectural Guardrail / Regression Prevention / Living Reference
Date: 2026-09-28
Timezone: Asia/Tehran (+03:30)
Parent Architecture: PMA-2026-09-01-001

## 1. Purpose
This architecture prevents the permanent mixing of two proof levels:
WRITE-ACCEPTED = the memory provider accepted the write request.
MEMORY-VERIFIED = the stored record was independently read back, integrity-checked, matched against the exact expected canonical payload, and verified.

Canonical rule:
Memory Write Acceptance must never imply Memory Verification.

This is an amendment/hardening layer for PMA-2026-09-01-001.

## 2. Required Proof Chain
IDENTIFY
→ CANONICALIZE + SCHEMA PIN
→ HASH + LENGTH
→ WRITE
→ PROVIDER RECEIPT
→ INDEPENDENT READ-BACK BY ID + REVISION
→ CANONICALIZE
→ HASH + LENGTH MATCH
→ INTEGRITY / REVISION / TOMBSTONE CHECK
→ VERIFY
→ STATUS

## 3. Independent Proof Levels
Level 1 — WRITE-ACCEPTED:
Write request was sent and provider accepted it. This does not prove retrieval, payload equality, revision equality, completeness, absence of later mutation, or final verification.

Level 2 — MEMORY-VERIFIED:
The stored record was independently retrieved; correct ID and intended revision were targeted; full payload was obtained; canonical serialization/schema matched; hash and length matched; no truncation/tombstone/conflicting revision existed; verification succeeded.

WRITE-ACCEPTED ≠ MEMORY-VERIFIED

## 4. Canonicalization and Byte-Level Definition
“Byte-for-byte” must have a defined representation.

Before write:
PAYLOAD → CANONICAL SERIALIZATION → BYTES → HASH A

The canonicalization contract must pin:
- schema version
- field ordering
- encoding
- newline convention
- Unicode normalization where applicable
- whitespace rules where applicable
- serialization format/version
- hash algorithm/version

After independent read-back:
READ-BACK PAYLOAD → SAME CANONICALIZATION → BYTES → HASH B

Required:
HASH A == HASH B
and matching payload length.

## 5. Provider Receipt and Revision Binding
A provider receipt proves the write operation, not content verification.
Where supported it must identify/bind:
- provider
- Stable/Record ID
- revision/version/commit
- write timestamp
- operation identifier

Read-back must target the intended revision.
A newer revision must not verify an older write.

## 6. TOCTOU / Concurrent Mutation Protection
The architecture must prevent:
Write version A → another process changes record → Read version B → false verification.

Where revisioning exists:
EXPECTED REVISION == READ-BACK REVISION

If revision identity cannot be established, full revision-safe verification must not be claimed.

## 7. Independent Read-back
Independent Read-back must be a real retrieval operation.
It cannot be:
- the original write response
- a success acknowledgement
- the locally held input
- a cached write result
- reconstructed conversation context

The persistence surface itself must be read.

## 8. Integrity and Completeness
Verification checks:
- canonical payload
- hash
- payload length
- schema/version
- record identity
- revision/commit
- tombstone/deletion state
- completeness of retrieved content

Any failed required integrity check means NOT-VERIFIED.

## 9. Truncation / Partial Read Protection
A successful tool/API response is not automatically a complete payload.
The system must establish complete retrieval and valid serialization.
Unknown completeness means READ-BACK-UNVERIFIED, not VERIFIED.

## 10. Deletion / Tombstone Protection
Missing record, deletion marker, tombstone, or deleted state must never be interpreted as a successful empty record.

Only PRESENT plus successful integrity verification can progress toward MEMORY-VERIFIED.

## 11. Mutation Invalidates Prior Verification
Verification belongs to a specific content revision.

MEMORY-VERIFIED(version A) does not automatically prove version B.

MUTATION → INVALIDATE PRIOR CONTENT VERIFICATION → REVERIFY

## 12. Concurrency and Conflict
If competing writes exist:
HOLD → IDENTIFY CONFLICT → PRESERVE BOTH → RECONCILE → EXPLICIT SUPERSESSION → VERIFY

No silent overwrite.
No duplicate production.
No assumption that the latest record is automatically correct.

## 13. Proof Matrix
Every memory operation should expose:
Write Status
Provider Receipt Status
Read-back Status
Revision Match Status
Payload Completeness Status
Hash Status
Length Status
Tombstone Status
Verification Status
Repository Status
Overall Status

Overall Status must never become VERIFIED merely because Write = ACCEPTED.

## 14. Fail-Closed Rule
Missing evidence means NOT-VERIFIED.
Never infer:
UNKNOWN → SUCCESS
or
WRITE-ACCEPTED → VERIFIED

## 15. Required Backend Capability
A backend capable of Full Independent Memory Verification should expose:
write(record_id, payload, provenance)
read(record_id, revision)
get_version(record_id)
verify(record_id, expected_hash_or_payload)
reconcile(record_id)
status(record_id)

Preferably:
immutable audit trail
provider receipt
revision/commit ID
content length
canonical payload retrieval

## 16. State Machine
Normal:
UNKNOWN → WRITE-SENT → WRITE-ACCEPTED → READ-BACK-AVAILABLE → REVISION-MATCH → PAYLOAD-COMPLETE → HASH-MATCH → INTEGRITY-CHECK-PASS → VERIFIED → ACTIVE/LIVING

Capability-limited:
WRITE-ACCEPTED → READ-BACK-UNAVAILABLE → NOT-VERIFIED → PENDING/OPEN

Mismatch:
WRITE-ACCEPTED → READ-BACK → MISMATCH / REVISION-MISMATCH / PARTIAL / TOMBSTONED → NOT-VERIFIED → RECOVERY/RECONCILIATION

## 17. Recovery Integration
RETRIEVE/EXCAVATE
→ IDENTIFY
→ VALIDATE
→ DEDUPLICATE
→ RECONCILE
→ REGISTER
→ INDEPENDENT READ-BACK
→ MATCH
→ VERIFY
→ REVIVE/ABSORB
→ ACTIVE/LIVING

REGISTERED ≠ VERIFIED
VERIFIED ≠ ACTIVE/LIVING unless the relevant additional gates are satisfied.

## 18. No-Drop
No Repository Access → No Loss.

If verification capability is unavailable:
- preserve the same Stable/Production ID
- preserve payload/provenance
- mark PENDING/OPEN/NOT-VERIFIED
- record blocker/capability gap
- do not create duplicate production
- retry only after actual capability exists

## 19. Master / Child / Rahm
Master: governs Proof Contract and status semantics.
Child: experiments with providers, adapters, canonicalization and verification methods.
Rahm: validates new methods before promotion to Master.

## 20. PEH / Hammer
Problem type: Evidence / Reality / Contradiction / Confidence
Subtype: PEH — Palang Evidence Hammer

Hammer must challenge the operation itself:
Was Write accepted?
Was the stored record independently retrieved?
Was the correct revision retrieved?
Was the full payload retrieved?
Did integrity checks pass?
Did the expected payload match?
Did mutation occur?
Is evidence from the persistence surface or merely conversation context?

## 21. Mandatory Negative Acceptance Tests
1. altered expected payload → verification MUST fail
2. unavailable provider → PENDING/RECOVERY
3. mismatched revision → verification MUST fail
4. truncated payload → verification MUST fail or remain NOT-VERIFIED
5. stale cached acknowledgement → MUST NOT count as Read-back
6. mutation after verification → prior verification invalidated for new revision
7. deletion/tombstone → MUST NOT verify
8. conflicting concurrent writes → preserve/reconcile, no silent overwrite
9. schema/canonicalization mismatch → verification MUST fail
10. missing receipt/revision evidence → downgrade status, never infer success

## 22. Regression Prevention
Search Result ≠ Excavation
Excavation ≠ Revival
Report ≠ Truth
User Claim ≠ Evidence
Memory ≠ Repository
Generated ≠ Project Artifact
Description ≠ Artifact
Write Acceptance ≠ Memory Verification
Registration ≠ Verification
Verification of revision A ≠ Verification of revision B
Architecture Description ≠ Runtime Proof
Provider acknowledgement ≠ independent content proof

## 23. Relationship to PMA-2026-09-01-001
This architecture hardens the existing Persistent Memory Adapter Specification.
The existing lifecycle remains:
IDENTIFY → CLASSIFY → VALIDATE → DEDUPLICATE → WRITE → READ-BACK → MATCH → VERIFY → CLOSE

This amendment adds:
- canonical serialization
- explicit hash/version
- provider receipt
- revision pinning
- TOCTOU protection
- completeness checks
- tombstone checks
- mutation invalidation
- concurrency handling
- negative acceptance tests
- fail-closed semantics

## 24. Final Guardrails
NO VERIFIED WITHOUT INDEPENDENT READ-BACK + MATCH
NO OVERALL SUCCESS FROM WRITE ACCEPTANCE ALONE
NO READ-BACK → NO MEMORY VERIFICATION
NO MATCH → NO VERIFIED
NO REVISION MATCH → NO REVISION-SAFE VERIFICATION
NO COMPLETE PAYLOAD → NO VERIFIED
MUTATION → REVERIFY
NO EVIDENCE → NO FALSE SUCCESS

## 25. Recovery Instruction
If this reference is supplied again:
1. retrieve it fully
2. reconcile with PMA-2026-09-01-001 and canonical architecture
3. deduplicate
4. preserve Stable IDs and lineage
5. identify which proof layers actually have evidence
6. never infer Read-back from Write Acceptance
7. never infer Verification from Read-back alone
8. require Match and integrity checks
9. keep NOT-VERIFIED when evidence is unavailable
10. reopen verification after mutation/revision change

## 26. Final Architecture Contract
WRITE
→ ACCEPTANCE
→ INDEPENDENT READ-BACK
→ REVISION MATCH
→ COMPLETE PAYLOAD
→ CANONICALIZATION
→ HASH/LENGTH MATCH
→ INTEGRITY CHECK
→ VERIFY
→ STATUS

Core principle:
Acceptance proves acceptance.
Read-back proves retrieval.
Match proves content correspondence.
Verification proves the defined integrity contract.
Status must reflect the highest level actually supported by evidence.

END OF REFERENCE


---

## Supersession Notice — 2026-09-29
This reference is retained as historical lineage. The current integrated hardened architectural reference is:
`MPPA-2026-09-29-002`
Path: `architecture/memory/MEMORY-PERSISTENCE-PROOF-ARCHITECTURE-2026-09-29.md`

The 2026-09-29 reference adds explicit Independence Status, Implementation Capability Status, Acceptance Status, a self-acceptance matrix, independent-read evidence requirements, and integrated Hammer findings. Do not interpret this historical reference as the current standalone architectural baseline.
