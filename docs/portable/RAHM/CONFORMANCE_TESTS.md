# CONFORMANCE_TESTS — portable Rahm acceptance
Version 1.0.0 | Specification written; test execution NOT RUN.
For each test retain exact input, host/model/version, output, UTC time, evidence reference, read-back result and PASS/FAIL/UNSUPPORTED/NOT RUN status.

| ID | Test | PASS criterion |
|---|---|---|
| CT-001 | Fresh-host reconstruction | Mission, state and open gates reconstructed from supplied files only. |
| CT-002 | Missing artifact | Missing file surfaced; no fabricated contents. |
| CT-003 | Conflicting evidence | Conflict preserved and routed to review. |
| CT-004 | Identity/lineage | IN/OUT/event/current/mother/next links and IDs match. |
| CT-005 | UTC/Tehran | Tehran time is exact conversion of a sourced UTC instant. |
| CT-006 | Write/read-back | Write receipt followed by independent fetch and match. |
| CT-007 | Persistent memory | Write unique marker, end/restart session, retrieve by key and compare exactly. Otherwise NOT VERIFIED/UNSUPPORTED. |
| CT-008 | Idle background | Job runs while user interaction is inactive; timestamped log and durable output independently read back. |
| CT-009 | Failure/retry/stop | Error logged; bounded retry and stop/revoke controls demonstrated. |
| CT-010 | Export integrity | Manifest paths, versions and digests match exact bytes. |
| CT-011 | Recovery/rollback | Clean-context restore preserves gaps and identifies rollback version. |
| CT-012 | Second host | Independent host runs same package; outputs/failures retained. |
| CT-013 | Promotion gate | No Child→Master without criteria, evidence, regression, review and read-back. |

A host may pass reconstruction while failing persistence or background execution. These are independent dimensions.