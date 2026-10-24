# EVT-0157 — Test Harness Failure as Architecture Learning

- Stable ID: `G6IP-RAHM-EVT-0157-20261024`
- Production ID: `G6IP-EVT-0157`
- Version: 1.0.0
- Status: REGISTERED / LIVING; full host-transfer gates remain OPEN.
- Input: [IN-048](../../0.0/anchors/PALANG-0.0-IN-20261024-048-TEST-HARNESS-FAILURE-AND-LIVING-MASTER-READYNESS.md)
- Output: [OUT-047](../../0.0/anchors/PALANG-0.0-OUT-20261024-047-TEST-HARNESS-FAILURE-AND-LIVING-MASTER-READYNESS.md)
- Prior corrective event: [EVT-0156](./EVT-0156-FIRST-MASTER-HARNESS-CORRECTION-2026-10-24.md)
- Current: [CURRENT-055](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-055-FIRST-MASTER-READINESS.md)
- Next: [NEXT-049](../../0.0/anchors/PALANG-0.0-NEXT-20261024-049-REAL-HOST-TRANSFER-AND-GRAPH-AUDIT.md)

## Observation → cause → correction → retest
1. Observation: an earlier conformance workflow passed schema fixture validation, then stopped in digest-report generation because the script assumed every successful result object had a `status` field.
2. Cause: inconsistent result-object shape; successful results carried byte count and digest but no status, while missing-file results did carry status.
3. Correction: report logic was changed to use safe lookup and compare any non-pending expected SHA-256; the failed run was preserved and a rerun completed successfully. See [EVT-0156](./EVT-0156-FIRST-MASTER-HARNESS-CORRECTION-2026-10-24.md).
4. Latest receipt at registration: [Portable conformance run 40115178748](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40115178748) SUCCESS. This is evidence for the inventory and tests executed in that commit only.

## Permanent rule
A harness/reporting failure is itself an architecture event. Never delete or rewrite the failed history as success. Record the observed failure, likely cause, exact correction, retest run, raw evidence and residual gaps. A successful retest only closes the specific criterion it actually tests.

## Evidence boundaries
- Schema valid/invalid behavior: verified in CI.
- SHA-256 inventory comparison: verified for the exact inventory and commit of the referenced run.
- Limited IN/OUT checkpoint/link equivalence: verified; full graph/state reconstruction remains OPEN.
- Extractable archive construction: verified.
- Separate AI-host import, second-host import, runtime persistence, idle/background execution and automatic capture: OPEN / NOT VERIFIED.
