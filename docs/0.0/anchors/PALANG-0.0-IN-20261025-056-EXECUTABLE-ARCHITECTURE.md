# IN-056 — Executable Architecture Input

- Stable ID: G6IP-IN-056-20261025
- Production ID: G6IP-IN-056
- Version: 1.0.0
- Parent: [POINT-0/012](./GPT6-RAHM-USER-POINT-0-20261025-012-EXECUTABLE-ARCHITECTURE.md)
- Previous checkpoint: [CURRENT-062](./PALANG-0.0-CURRENT-20261025-062-OPEN-GAPS-AND-CONTINUITY.md)
- User requirement: Stop substituting reports/documents for implementation. Make the new-project architecture practical, executable and recoverable; connect the current point to the living mother and keep defects/next steps as 0.0 work.
- Execution decision: build a small runnable local core first, validate its behavior, then integrate clean-host adoption and global historical graph reconciliation without claiming untested capabilities.
- Implemented source: [HAIF runtime](../../../../scripts/haif-runtime/haif_runtime.py), [tests](../../../../scripts/haif-runtime/tests/test_runtime.py), [runbook](../../../../scripts/haif-runtime/README.md).
- Open gates: current CI result, local clean-environment execution, clean independent-host import, second-host test, restart persistence, automatic capture/background execution and full semantic graph adjudication.
- Status: REGISTERED; implementation is linked; test outcome remains NOT VERIFIED until an actual run is inspected.
