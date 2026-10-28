# TIME-BINDING-EVT-0234 — Live Mirror Sync Recheck and EVT-0233 Collision

- Event: [EVT-0234](./EVT-0234-LIVE-MIRROR-SYNC-RECHECK-AND-EVT0233-COLLISION-2026-10-28.md)
- Stable ID: PALANG-TIME-BINDING-EVT-0234-LIVE-MIRROR-SYNC-2026-10-28
- Version: 1.0.0
- Canonical clock: actual last-change Git commit timestamp in UTC; Asia/Tehran is derived from the same instant.
- EVT-0234 final last-change commit at initial registration: `3a13cdd9dda73bbfebe9803eb468ce1167152e93`.
- EVT-0234 registration UTC: `2026-10-28T06:26:30Z`.
- Derived Asia/Tehran time: `2026-10-28T09:56:30+03:30`.
- Pre-registration main observation: `36dead156b7e4f7a0fca41687d5d98b4620c82ee`, UTC `2026-10-28T06:25:13Z), Tehran `2026-10-28T09:55:13+03:30`. Later writes are not covered by that head observation.
- Canonical source blob: `de1b75f07241c9b313e476af5f1417177ff78c10`; source length 10,479 characters.
- Library snapshot file ID `file_00000000942881f8a4a3833110229fb7`; stable Library ID `libfile_7ac3c9a6ec14819198eb2751e204aa48`; version 7; content length 10,480 characters. After trimming trailing line feeds, source and Library content are exactly equal; the only difference is one extra trailing newline in Library.
- Library metadata UTC `2026-10-24T04:45:28.479773Z`; derived Tehran `2026-10-24T08:15:28.479773+03:30`. Exact Library read operation time is UNKNOWN.
- Collision: two distinct files used EVT-0233. The POINT-0/058 event is explicitly linked by POINT-0/058 and CURRENT-108; the mirror-sync EVT-0233 artifact is preserved and quarantined. Its pre-quarantine final commit was `b9bc6a550538c42e9d547aa680b301e8b6a50cdf` at UTC `2026-10-28T06:22:43Z`; its quarantine update commit is `70f04277fc57f8123167a27a253f3ba4e5e45063` at UTC `2026-10-28T06:26:53Z`, Tehran `2026-10-28T09:56:53+03:30`.
- Prior EVT-0233 time-binding artifact update commit: `4f68b209cbe9dcc4cb069289b84b772a03fa889b`, UTC `2026-10-28T06:27:12Z`, Tehran `2026-10-28T09:57:12+03:30`.
- Current root/checkpoint: POINT-0/058 (0+) → CURRENT-108 → NEXT-051. Preserve POINT-0/016, POINT-0/017, POINT-0/018, POINT-0/057 and all intervening records. Do not create NEXT-052.
- NEXT-051 path content remains OPEN / SOURCE-BACKED RECOVERY REQUIRED: its path currently resolves to a stale queue-like Version 1.10.3 body rather than a task-specific NEXT document. Preserve it pending path-specific Git history recovery.
- Latest previously observed successful Living Architecture Audit run 40639681454 and Portable RAHM Conformance run 40639681489 both tested SHA `764b9173c4a802669b9e13bc370a3922db0cbb3a`; Evidence Gate follow-up commit `0250a487aa4af58a0d0a4c39be0a6a130f28c7c0` and later commits are outside those runs' tested SHA.
- Buffer and Persistent Memory: NOT VERIFIED. Dropbox: OPEN / NOT VERIFIED. External-host/end-to-end recovery: NOT RUN unless separate raw evidence is supplied.
- Workflow timestamps, repository commit timestamps, Library metadata timestamps and exact read-operation timestamps are distinct. Unknown operation time remains UNKNOWN.
