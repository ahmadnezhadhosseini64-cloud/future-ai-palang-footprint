# TIME-BINDING-EVT-0167 — Live Mirror Sync Recheck

- Stable ID: PALANG-TIME-BINDING-EVT-0167-2026-10-25
- Event: [EVT-0167](./EVT-0167-LIVE-MIRROR-SYNC-RECHECK-2026-10-25.md)
- Version: 1.0.0
- Rule: the actual last-change Git commit timestamp in UTC is canonical for a repository item; Asia/Tehran is derived from the same instant. No message time, tool response time, source commit time, Library metadata time, or unknown operation time may be substituted.

## Event registration time — canonical
- Event file last-change commit: `ca7e23d67b2d35cbc0e3f1109b22d8f98ccb603e`.
- UTC: `2026-10-25T06:04:46Z`.
- Asia/Tehran derived from the same instant: `2026-10-25T09:34:46+03:30`.
- Commit evidence: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/commit/ca7e23d67b2d35cbc0e3f1109b22d8f98ccb603e

## Distinct contextual times
- Canonical source last-changing commit `a2374d7da36a5af69b1bdf17f6dfd673bc03c97f`: UTC `2026-10-23T17:34:39Z`; Tehran `2026-10-23T21:04:39+03:30`.
- Library file metadata modified time: UTC `2026-10-24T04:45:28.479773Z`; Tehran `2026-10-24T08:15:28.479773+03:30`. This is metadata, not the read-back operation time.
- Exact Library read-back operation timestamp: UNKNOWN; the read tool did not return an independently usable operation timestamp.
- Main HEAD observed at audit start: `836161bf280783d247bad7cd945ea414710eaf9b`, commit UTC `2026-10-25T06:02:35Z`; Tehran `2026-10-25T09:32:35+03:30`. This is a starting observation, not the event registration timestamp.

## Comparison receipt
- Source blob: `de1b75f07241c9b313e476af5f1417177ff78c10`; 10,479 characters.
- Library snapshot: version `7`, file ID `file_00000000942881f8a4a3833110229fb7`, stable ID `libfile_7ac3c9a6ec14819198eb2751e204aa48`; 10,480 characters.
- Difference: one trailing newline; length delta 1; Levenshtein distance 1.
- Stable ID, Test ID, Version, next-action chain and destination status lines match.
- Decision: READ-BACK PASS / SEMANTIC MATCH PASS / no write required / no byte-for-byte identity claim.
- Scope: exact canonical source and exact Library mirror only. Buffer and Persistent Memory NOT VERIFIED; Dropbox OPEN / NOT VERIFIED; external end-to-end recovery NOT RUN.
