# Automatic Pending Finalization Queue

Status: ACTIVE / MACHINE-READABLE PENDING LANE

A pending production may be placed here when it is already human-approved for durable registration but final registration is blocked by temporary capability unavailability.

## Required record format
Each pending production is one `.md` file containing these fields before `---PAYLOAD---`:

- `production_id:` stable ID
- `trace_id:` trace ID
- `approval:` APPROVED
- `status:` ELIGIBLE
- `auto_finalize:` true
- `canonical_destination:` path under `docs/`
- `created_at:` timestamp
- `reason:` blocking reason

Everything after `---PAYLOAD---` is the exact canonical payload to register.

## Automatic rule
The scheduled/push drain scans this directory automatically. If the destination is available and the record satisfies the eligibility gate, it reconciles by `production_id`, writes only when the destination is absent, reads the result back, verifies identity/content, and then marks the pending record `RECONCILED`.

If any gate fails, the record remains pending/unverified and is never deleted or falsely finalized.

Human approval remains mandatory. This lane is not an approval bypass.
