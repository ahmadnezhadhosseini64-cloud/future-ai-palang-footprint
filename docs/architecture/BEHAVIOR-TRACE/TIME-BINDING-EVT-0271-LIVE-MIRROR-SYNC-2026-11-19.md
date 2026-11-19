# TIME-BINDING-EVT-0271 — Live Mirror Synchronization

- Event: [EVT-0271](./EVT-0271-LIVE-MIRROR-SYNC-RECHECK-2026-11-19.md)
- Stable ID: PALANG-TIME-BINDING-EVT-0271-2026-11-19
- Version: 1.0.0 (initial registration; exact commit metadata addendum pending)
- Canonical clock: actual last-change Git commit timestamp in UTC; Asia/Tehran is derived from that same instant.

## 1. Run-start repository anchors

- Main HEAD: `a06a4c3a24ae768bdab00f98511c1f1dc7b6d3f8`; commit UTC `2026-11-19T06:30:07Z`; derived Tehran `2026-11-19T10:00:07+03:30`.
- Main 0.0 root: POINT-0/064 / latest user-turn event EVT-0257.
- Execution checkpoint: CURRENT-115 v1.0.8.
- Sole active queue: NEXT-051 v1.0.44; NEXT-052 not created.
- Living mother model v1.7.66; canonical continuation master v1.0.11.
- Behavior Trace Index v1.0.39; Reference Index last updated 2026-11-18; Integration Queue v1.10.43; Behavior Observatory v1.0.25.
- Prior mirror event EVT-0270 / TIME-BINDING-EVT-0270; registration commit `47894652fbd5b4ab47cbd9fecc84464bcebe9041` at UTC `2026-11-18T07:14:40Z` / Tehran `2026-11-18T10:44:40+03:30`.
- Separate fisheries POINT-0+ under `صیادی/` remains an additive branch.

## 2. Actions run-time and exact tested-SHA bindings

| Workflow | Run ID | Tested SHA | Result |
|---|---:|---|---|
| Living Architecture Audit | 44472618022 | `a06a4c3a24ae768bdab00f98511c1f1dc7b6d3f8` | SUCCESS |
| Portable RAHM Conformance and Digest Evidence | 44257358104 | `47894652fbd5b4ab47cbd9fecc84464bcebe9041` | SUCCESS; not current main |
| Evidence Gate - Independent Execution Test | 44257358290 | `47894652fbd5b4ab47cbd9fecc84464bcebe9041` | SUCCESS; created prior main |
| Production Detection Safety Net | 44472617950 | `a06a4c3a24ae768bdab00f98511c1f1dc7b6d3f8` | SUCCESS |
| Reconciliation Watchdog | 44472618027 | `a06a4c3a24ae768bdab00f98511c1f1dc7b6d3f8` | SUCCESS |
| Pending Registration Drain | 44472618103 | `a06a4c3a24ae768bdab00f98511c1f1dc7b6d3f8` | SUCCESS |

- Audit job 135385505016 explicitly logged `repository_commit=a06a4c3a24ae768bdab00f98511c1f1dc7b6d3f8`; artifact ID 14505086636.
- RAHM job 134642143596 uploaded/downloaded artifact 14406556599 and verified SHA-256 `e9019a8b3ea6b37c529747f65d068e3fb3a6e1cee3b601e7e9c41b966b284f1b`; artifact round-trip and extracted tests PASS. This tested SHA is not run-start main.
- Evidence Gate job 134642144191 succeeded on its parent SHA and created `ae42d2b851cccb0425b61074a698384d0860f985`; a later independent certificate-documents commit moved main to the run-start HEAD.
- Exact-main Audit is PASS; exact-main Portable RAHM remains NOT VERIFIED.

## 3. Library and comparison time boundary

- Canonical source blob: `de1b75f07241c9b313e476af5f1417177ff78c10`; 10,479 characters / 13,303 UTF-8 bytes.
- Library stable ID: `libfile_7ac3c9a6ec14819198eb2751e204aa48`; file ID `file_00000000942881f8a4a3833110229fb7`; exact version 7; 10,480 characters / 13,304 decoded UTF-8 bytes; one additional terminal LF.
- Library metadata modified UTC `2026-10-24T04:45:28.479773Z`; derived Tehran `2026-10-24T08:15:28.479773+03:30`.
- Library listing response UTC `2026-11-19T06:24:11.132794Z`; derived Tehran `2026-11-19T09:54:11.132794+03:30`. This is not the exact content-read operation time.
- Exact Library content-read operation time: UNKNOWN. No Library write occurred.
- Exact ChatGPT automation invocation / task-run timestamp is not present in the GitHub or Library evidence used here; it is kept separate from Git commit, Actions run and Library metadata times.

## 4. Registration commit boundary

- EVT-0271 and this time-binding file are initially registered together. The exact registration commit SHA and UTC/Tehran pair will be added in version 1.0.1 after independent Git metadata read-back.
- Do not substitute GitHub Actions run time, Library metadata time, listing response time or content-read operation time for the canonical Git commit time.
