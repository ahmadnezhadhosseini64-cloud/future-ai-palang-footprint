# PMAR Reminder

**ID:** PMAR-2026-08-31-001

When the owner later says: **«سند PMAR-2026-08-31-001 را اجرا کن»**:

1. Retrieve the PMAR reference and provenance record.
2. Preserve the same Production/Reference ID and payload.
3. If authorized Persistent Memory access is actually available, write the record.
4. Perform Memory read-back.
5. Verify the read-back.
6. Only then mark Memory VERIFIED and close the pending state.
7. If access is unavailable, retain PENDING/UNVERIFIED in the canonical Repository/Recovery source.

**Rule:** NO READ-BACK → NO VERIFIED CLAIM.

Reference: `docs/reference/PERSISTENT-MEMORY-AUTO-RECONCILIATION-REFERENCE-2026-08-31.md`
Protocol: `docs/protocols/PERSISTENT-MEMORY-DEFERRED-RECONCILIATION-PROTOCOL.md`
