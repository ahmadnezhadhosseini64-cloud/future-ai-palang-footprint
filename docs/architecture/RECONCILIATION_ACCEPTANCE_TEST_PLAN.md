# Reconciliation Acceptance Test Plan

**Project:** Future AI / Palang Footprint  
**Date:** 2026-08-30  
**Status:** REQUIRED BEFORE PROVEN

## Purpose
Prove the living reconciliation mechanism rather than inferring capability from specifications or workflow existence.

## Required tests
1. **Production detection:** create an intentionally material production candidate and verify a unique production/trace ID.
2. **Unavailable destination:** make the repository destination unavailable and verify a durable Pending record with owner, reason, destination, and retry metadata.
3. **Recovery:** restore write capability and verify automatic discovery of Pending without a manual reminder.
4. **Pending drain:** verify old Pending items are processed alongside a new registration opportunity.
5. **Idempotency:** repeat reconciliation and verify no duplicate canonical production.
6. **Verification:** require read-back/identity/content evidence before marking complete.
7. **Interruption:** interrupt a multi-step operation and verify resumable/partial state survives.
8. **Detection safety net:** introduce an intentionally unregistered production-bearing repository change and verify DETECTION_GAP/UNCLASSIFIED evidence.
9. **Watchdog:** verify stale, failed, and degraded control-plane conditions are surfaced.
10. **Memory bridge:** if and only if a real capability exists, test Memory↔Repository reconciliation end-to-end. Otherwise record the bridge as NOT AVAILABLE, never as proven.

## Pass rule
The system is PROVEN only if every applicable test has independently reviewable evidence. A specification, successful static-file check, or intended workflow is not sufficient evidence.
