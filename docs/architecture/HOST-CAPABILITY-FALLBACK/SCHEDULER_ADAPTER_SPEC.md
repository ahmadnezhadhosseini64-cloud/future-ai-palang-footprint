# Scheduler / Background Execution Adapter Specification
Version: 1.0.0
Status: SPECIFICATION ONLY / NOT CONFIGURED

## Required interface
- schedule(job_id, schedule, bounded_task, input_checkpoint, permissions)
- status(job_id)
- fetch_logs(job_id)
- cancel(job_id)
- revoke_permissions(job_id or adapter_id)

## Mandatory controls
Explicit user/organization authorization; least-privilege credentials; bounded task and time budget; duplicate/idempotency key; retry cap; rate limit; audit log; UTC timestamps; output artifact path; stop/cancel; revoke; failure alert; and no promotion of candidate artifacts without human/master review.

## Background proof test BG-01
1. Record the exact scheduler/agent identity and version.
2. Schedule a harmless, bounded test with unique job ID and UTC due time.
3. Leave the interactive session inactive for the test window.
4. Fetch the execution log and durable output after the window.
5. Independently read back the output and compare the unique marker.
6. Cancel the next run and verify cancellation.
7. Record permissions, errors and evidence.
PASS applies only to the tested runtime and configuration. A schedule declaration without observed idle execution is NOT VERIFIED. If no authorized scheduler is available, report UNSUPPORTED/NOT VERIFIED and keep this gate open.
