# Pending Registration Queue

Status: ACTIVE_CONTRACT / DURABLE_REPOSITORY_QUEUE

This queue is the repository-side durable fallback for registration operations that cannot be completed at the destination at the time of request.

## Mandatory fields per pending item
- pending_id
- production_id
- trace_id
- production_type
- canonical_destination
- created_at
- reason
- payload_reference
- status
- retry_count
- last_attempt_at
- next_eligible_trigger
- evidence_reference

## Rules
- Never delete a pending item merely because an attempt failed.
- Never mark complete without execution and verification evidence.
- Every subsequent registration event and scheduled reconciliation must scan this queue.
- Successful reconciliation must be idempotent.
- Pending items remain independently traceable even when other items succeed.
- Human approval requirements must be preserved.
