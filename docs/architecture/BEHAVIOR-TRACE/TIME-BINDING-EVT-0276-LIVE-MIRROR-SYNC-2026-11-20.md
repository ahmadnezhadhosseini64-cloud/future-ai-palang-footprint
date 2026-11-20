# TIME-BINDING-EVT-0276 — Live Mirror Synchronization

- Event: [EVT-0276](./EVT-0276-LIVE-MIRROR-SYNC-RECHECK-2026-11-20.md)
- Stable ID: PALANG-TIME-BINDING-EVT-0276-2026-11-20
- Version: 1.0.0
- Canonical clock: actual last-change Git commit timestamp in UTC; Asia/Tehran is derived from that same instant.
- Run observation UTC `2026-11-20T06:32:08Z`; Tehran `2026-11-20T10:02:08+03:30`. Not a Git commit or Actions run time.

## Run-start anchors
- Main HEAD `2ea7e826931a42fb0a5957cdb58b698bb8f30e00`; commit UTC `2026-11-20T06:28:22Z`; Tehran `2026-11-20T09:58:22+03:30`.
- Main root POINT-0/064 / EVT-0257; separate certificate child root CERT-POINT-0.0-20261120-002 / EVT-0274.
- CURRENT-115 v1.0.8; NEXT-051 v1.0.44; NEXT-052 not created.
- Living mother v1.7.66; canonical continuation master v1.0.13; Behavior Trace Index v1.0.41; Reference Index last updated EVT-0275; Integration Queue v1.10.45; Observatory v1.0.27.
- Preserve POINT-0/016, /017, /018 / EVT-0180, EVT-0177, canonical EVT-0178, EVT-0179 and the quarantined duplicate draft. CURRENT-065/CURRENT-066 remains OPEN / AMBIGUOUS; no winner selected.

## Source / Library time boundary
- Source blob `de1b75f07241c9b313e476af5f1417177ff78c10`; 10,479 chars / 13,303 UTF-8 bytes.
- Library stable ID `libfile_7ac3c9a6ec14819198eb2751e204aa48`; file ID `file_00000000942881f8a4a3833110229fb7`; version 7; 10,480 chars / 13,304 decoded bytes.
- Normalized full text MATCH; exact equality FALSE by one additional terminal LF; edit distance 1.
- Library metadata modified UTC `2026-10-24T04:45:28.479773Z`; Tehran `2026-10-24T08:15:28.479773+03:30`.
- Library listing observation UTC `2026-11-20T06:32:22.866540Z`; Tehran `2026-11-20T10:02:22.866540+03:30`.
- Exact Library read operation time UNKNOWN. No source/Library write; no exported source snapshot for source_file_ref; no container_path.

## Actions exact-SHA bindings
| Workflow | Run ID | Tested SHA | Result |
|---|---:|---|---|
| Living Architecture Audit | 44688034068 | `2ea7e826931a42fb0a5957cdb58b698bb8f30e00` | SUCCESS |
| CPREL Runtime Transfer Harness | 44688034103 | `2ea7e826931a42fb0a5957cdb58b698bb8f30e00` | SUCCESS |
| CPREL Transfer Evidence | 44688034176 | `2ea7e826931a42fb0a5957cdb58b698bb8f30e00` | SUCCESS |
| Cross-Layer Integrity Gate | 44688034341 | `2ea7e826931a42fb0a5957cdb58b698bb8f30e00` | SUCCESS |
| Portable RAHM Conformance | 44687870952 | `bd44a799ce6296aede0ee6be64bdf26cd0af3383` | SUCCESS; prior SHA |

- Audit job 136126970847; CPREL jobs 136126940886 / 136126974174; RAHM job 136126415817 (23 tests, prior SHA).
- Exact-main Audit/CPREL PASS; exact-main RAHM NOT VERIFIED. CPREL is not a substitute for RAHM.

## Registration commit binding
- Initial event/index registration commit UTC: PENDING post-write Git metadata read-back; do not infer it from run observation time.
- Event file and time-binding file may have distinct final-change commits if this binding is revised after initial registration.
- This file's final-change timestamp is the actual committer timestamp of its final Git commit, independently read from Git metadata; no recursive self-timestamp is guessed.
- Library metadata time, listing observation time, exact read operation time, run observation time and Actions run times remain distinct. UNKNOWN is retained where not exposed.