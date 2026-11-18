# TIME-BINDING-EVT-0270 — Live Mirror Synchronization

- Event: [EVT-0270](./EVT-0270-LIVE-MIRROR-SYNC-RECHECK-2026-11-18.md)
- Stable ID: PALANG-TIME-BINDING-EVT-0270-2026-11-18
- Version: 1.0.0 (initial registration; exact commit metadata addendum pending)
- Canonical clock: actual last-change Git commit timestamp in UTC; Asia/Tehran is derived from that same instant.

## 1. Run-start repository anchors

- Main HEAD: `f8bb694b4f11790585171b73439b246e90e148a9`; commit UTC `2026-11-17T14:16:27Z`; derived Tehran `2026-11-17T17:46:27+03:30`.
- Main 0.0 root: POINT-0/064 / EVT-0257; checkpoint CURRENT-115 v1.0.8; sole active queue NEXT-051 v1.0.44.
- Parallel fisheries project POINT-0+: commit `7845397ea018d445b6a6dd62fba8c3e82da69df6`; UTC `2026-11-17T14:07:48Z`; Tehran `2026-11-17T17:37:48+03:30`. This is not a replacement for the main 0.0 root.
- Prior mirror event EVT-0269 registration commit `e18f1c2cdc28a386892cc6e61a260944f6c5f9b8`; the prior time-binding update commit is `5b2e5f3d4a3c5527977fc633857833892474e28d`.

## 2. Actions run-time and tested-SHA bindings

| Workflow | Run ID | Tested SHA | Result |
|---|---:|---|---|
| Living Architecture Audit | 44101311777 | `f8bb694b4f11790585171b73439b246e90e148a9` | SUCCESS |
| Portable RAHM Conformance and Digest Evidence | 44031392845 | `5b2e5f3d4a3c5527977fc633857833892474e28d` | SUCCESS |
| Evidence Gate - Independent Execution Test | 44090659918 | `93d39b8570afc7f8e5052702b6015256e750a5d9` | SUCCESS |
| Production Detection Safety Net | 44236703587 | `f8bb694b4f11790585171b73439b246e90e148a9` | SUCCESS |

- Audit job 134101731492 explicitly logged `repository_commit=f8bb694b4f11790585171b73439b246e90e148a9`.
- RAHM job 133863937304 uploaded artifact 14304862944, downloaded it again, verified SHA-256 `8d2ffe4708f9518e5499c57758ceee3e00c262dcda1e37ea1014dec40b0e5f2f`, and reported extracted ZIP tests PASS. This tested SHA is not the run-start main SHA.
- Evidence Gate job 134064605857 pushed follow-up `860aca6` from tested SHA `93d39b8...`; that follow-up was later superseded by subsequent main commits.
- Exact-main Audit is PASS; exact-main Portable RAHM remains NOT VERIFIED.

## 3. Library and comparison time boundary

- Canonical source blob: `de1b75f07241c9b313e476af5f1417177ff78c10`; 10,479 characters / 13,303 UTF-8 bytes.
- Library stable ID: `libfile_7ac3c9a6ec14819198eb2751e204aa48`; version 7; 10,480 extracted characters / 13,304 UTF-8 bytes; one additional terminal LF.
- Library metadata modified UTC `2026-10-24T04:45:28.479773Z`; derived Tehran `2026-10-24T08:15:28.479773+03:30`.
- Library listing response timestamp UTC `2026-11-18T06:57:53.720756Z`; derived Tehran `2026-11-18T10:27:53.720756+03:30`. This is a listing observation, not the exact content-read operation time.
- Exact Library content-read operation time: UNKNOWN. No Library write occurred.

## 4. Registration commit boundary

- EVT-0270 and this initial time-binding file are registered in the same initial repository commit. The exact registration commit SHA and UTC/Tehran pair will be added in version 1.0.1 after independent Git metadata read-back.
- Do not substitute workflow run time, tool-response time, Library metadata time or operation time for the canonical Git commit time.
