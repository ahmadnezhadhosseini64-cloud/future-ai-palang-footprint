# Local/External Agent Runtime Contract
Version: 1.0.0
Status: SPECIFICATION ONLY / NOT INSTALLED
Purpose: define how a separately authorized agent can provide work continuity when an AI chat host lacks memory or background execution.

## Minimum runtime
1. A user-controlled or organization-authorized process host.
2. Durable versioned storage for package, checkpoints, jobs and receipts.
3. A scheduler or event loop with explicit start/stop controls.
4. A worker adapter for the chosen AI provider/API; credentials remain in a secret manager/environment and never in project documents.
5. Structured logs with UTC timestamps and a Tehran conversion when useful.
6. Job ledger with unique job ID, input checkpoint, output artifacts, status, retries, errors and evidence references.
7. Health check, permission scope, quotas, retry limits, cancellation and rollback.

## Execution protocol
LOAD CHECKPOINT → VERIFY MANIFEST → CHECK PERMISSIONS → CLAIM JOB WITH UNIQUE ID → RUN BOUNDED TASK → WRITE ARTIFACTS → READ BACK → MATCH EXPECTED STATE → RECORD RECEIPT → UPDATE CHECKPOINT → RELEASE JOB.
Retries must be idempotent or explicitly detect duplicates. Failed tasks remain OPEN/FAILED with retained logs; they must not silently mark the project ACTIVE.

## Boundaries
This document is not an executable agent, does not provision hosting, does not create credentials, and does not prove a scheduler exists. Installing and operating such a runtime requires an explicit deployment and authorization step. Never represent a chat response as an autonomous background run.
