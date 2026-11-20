# TIME-BINDING-EVT-0275 — Live Mirror Synchronization

- Event: [EVT-0275](./EVT-0275-LIVE-MIRROR-SYNC-RECHECK-2026-11-20.md)
- Stable ID: PALANG-TIME-BINDING-EVT-0275-2026-11-20
- Version: 1.0.0
- Canonical clock: actual last-change Git commit timestamp in UTC; Asia/Tehran is derived from that same instant.
- Run observation time: UTC `2026-11-20T06:05:32Z`; Asia/Tehran `2026-11-20T09:35:32+03:30`. This is distinct from repository commit time, Actions run time, Library metadata time and Library listing time.

## 1. Run-start repository anchors

- Main HEAD: `0810674cb5340a62a4c3bcb547585c9b9263e1c2`; commit UTC `2026-11-19T20:45:41Z`; derived Tehran `2026-11-20T00:15:41+03:30`.
- Main 0.0 root: POINT-0/064 / latest main user-turn event EVT-0257.
- Separate certificate child root: CERT-POINT-0.0-20261120-002 / EVT-0274; it does not replace the main root.
- Execution checkpoint: CURRENT-115 v1.0.8; sole active queue: NEXT-051 v1.0.44; NEXT-052 not created.
- Living mother model v1.7.66; canonical continuation master v1.0.12.
- Behavior Trace Index v1.0.40; Reference Index last updated 2026-11-19; Integration Queue v1.10.44; Behavior Observatory v1.0.26.
- Prior mirror-only event: EVT-0271 / TIME-BINDING-EVT-0271. EVT-0274 is a child-branch event.
- Preserve POINT-0/016, POINT-0/017, POINT-0/018 / EVT-0180, EVT-0177, canonical EVT-0178, EVT-0179 and the quarantined duplicate-number artifact. CURRENT-065/CURRENT-066 remains OPEN / AMBIGUOUS; winner_selected=false.

## 2. Source and Library time boundary

- Canonical source blob: `de1b75f07241c9b313e476af5f1417177ff78c10`; 10,479 characters / 13,303 UTF-8 bytes.
- Library stable ID: `libfile_7ac3c9a6ec14819198eb2751e204aa48`; file ID `file_00000000942881f8a4a3833110229fb7`; version 7; 10,480 characters / 13,304 decoded UTF-8 bytes.
- Normalized full text MATCH; exact equality FALSE due solely to one extra terminal LF in Library; edit distance 1.
- Library metadata modified UTC `2026-10-24T04:45:28.479773Z`; derived Tehran `2026-10-24T08:15:28.479773+03:30`.
- Library listing response UTC `2026-11-20T06:05:58.614549Z`; derived Tehran `2026-11-20T09:35:58.614549+03:30`.
- Exact Library content-read operation time: UNKNOWN. No source or Library write occurred; no supported source_file_ref route was available; container_path was not used.

## 3. Actions run-time and exact tested-SHA bindings at run start

| Workflow | Run ID | Tested SHA | Result |
|---|---:|---|---|
| Living Architecture Audit | 44611950220 | `0810674cb5340a62a4c3bcb547585c9b9263e1c2` | SUCCESS |
| Portable RAHM Conformance | 44611586010 | `553efa493f6bca5c60385151961e56c46ca4430d` | SUCCESS; not current main |
| Evidence Gate - Independent Execution Test | 44611585687 | `553efa493f6bca5c60385151961e56c46ca4430d` | SUCCESS; not current main |
| Automatic Final Registration Proof | 44611950172 | `0810674cb5340a62a4c3bcb547585c9b9263e1c2` | SUCCESS |
| Production Detection Safety Net | 44666444747 | `0810674cb5340a62a4c3bcb547585c9b9263e1c2` | SUCCESS |
| Reconciliation Watchdog | 44665786914 | `0810674cb5340a62a4c3bcb547585c9b9263e1c2` | SUCCESS |
| Pending Registration Drain | 44648981452 | `0810674cb5340a62a4c3bcb547585c9b9263e1c2` | SUCCESS |

- Audit job 135870641523 logged `repository_commit=0810674cb5340a62a4c3bcb547585c9b9263e1c2`; 5,781 files scanned; zero timestamp parse/ambiguity errors; 17 missing local-link findings remain.
- RAHM job 135869312102 ran 23 tests; existing ZIP SHA-256 `79a0fe09eb2b8aa0d8a988aa129d4a9afca0267985f9840a7819b6d30c09bfa8`; uploaded artifact 14572916765 SHA-256 `4d4a22319674074f5e92cf2a7ae3d8a0c2cea6b44d3ae9278d0b73e0c20fec15`; downloaded digest matched and extracted tests PASS. Tested SHA is not run-start main.
- Exact-main Audit PASS; exact-main RAHM NOT VERIFIED at run start.

## 4. Registration commit boundary

- Initial event/index registration commit: pending Git metadata fetch after write; this file will be updated to version 1.0.1 only after independent read-back.
- Time-binding file final-change timestamp will be taken from its own Git commit metadata after its final update; it is not substituted with run-start time, Actions time or Library metadata time.
