# TIME-BINDING-EVT-0319 — Owner continuation and exact-main audit

- Event: [EVT-0319](EVT-0319-OWNER-CONTINUATION-EXACT-MAIN-AUDIT-2026-11-22.md)
- Stable ID: PALANG-TIME-BINDING-EVT-0319-2026-11-22
- Version: 1.0.0
- Canonical clock: actual Git commit timestamp of event registration, UTC.
- Event registration commit: `64fd9a96c280570b9873c3571a78aaf87c4ea651`.
- Event registration commit UTC: `2026-11-22T08:22:08Z`.
- Asia/Tehran derived from the same instant: `2026-11-22T11:52:08+03:30`.
- Event file blob SHA at read-back: `201fa2ab97b7ad8367c196270b77ab30ec3769e6`.
- Owner-message timestamp: UNKNOWN / NOT PROVIDED AS A TRUSTWORTHY PLATFORM TIMESTAMP.
- Audit target main HEAD: `30d1d3b2de09078131fa3c8a0ff7c492a7ab0d7e`; its commit UTC `2026-11-22T07:38:58Z`; Tehran derived `2026-11-22T11:08:58+03:30`.
- Audit workflow observation window: GitHub Actions run records show runs created at `2026-11-22T07:39:01Z`; exact per-tool observation time is not inferred beyond recorded run metadata.

## Timing separation

Event registration time, target main commit time, Actions run time, and later file read-back time are separate facts. Unknown operation/message times remain UNKNOWN and are never derived from nearby timestamps.

- Initial time-binding file creation commit: `c8a63daf63764c8112b0fe87313c1f1e20c79be` (UTC `2026-11-22T08:22:17Z`; Tehran `2026-11-22T11:52:17+03:30`).
- Subsequent metadata-correction commit before Golden merge: `d60414337759efb90c6a6ce6d222bd9abb6c2f2d` (UTC `2026-11-22T08:24:29Z`; Tehran `2026-11-22T11:54:29+03:30`).
- The current file's final-change commit is read from Git metadata; no self-referential timestamp is embedded here.
