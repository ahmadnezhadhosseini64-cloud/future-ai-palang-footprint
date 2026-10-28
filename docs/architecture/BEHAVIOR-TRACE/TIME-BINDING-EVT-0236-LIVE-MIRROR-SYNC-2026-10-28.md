# TIME-BINDING-EVT-0236 — Live mirror synchronization recheck

- Event: [EVT-0236](./EVT-0236-LIVE-MIRROR-SYNC-RECHECK-2026-10-28.md)
- Stable ID: PALANG-TIME-BINDING-EVT-0236-LIVE-MIRROR-SYNC-2026-10-28
- Version: 1.0.0
- Status: FINAL / REGISTERED / READ-BACK VERIFIED for the event's repository registration time. This binding does not imply current-main audit, external-host, or destination acceptance.
- Canonical registration clock: actual final-change Git commit timestamp in UTC; Tehran time is derived from that same instant (+03:30).
- Event final-change / registration commit: `921d7079b48d895b53569599f327231db64eb566`.
- Event commit UTC: `2026-10-28T07:45:34Z`.
- Tehran equivalent derived from that exact commit instant: `2026-10-28T11:15:34+03:30`.
- Event file independently read back at exact path: blob `e5fad3aba9bf5971385757284f19d18cccfa4147`, 8,217 characters. Event file was not modified by this binding-finalization commit; the event's final-change commit remains `921d7079b48d895b53569599f327231db64eb566`.
- Main HEAD observed before event registration: `11e69bb6b5e62a11186569b23312ba06e1d4e1c3`, UTC `2026-10-28T07:29:56Z`, Tehran `2026-10-28T10:59:56+03:30`.
- Comparison operation clock from the execution context: UTC `2026-10-28T07:35:16Z` / Tehran `2026-10-28T11:05:16+03:30`. This is distinct from the event commit, workflow run metadata and Library metadata timestamps.

## Post-write Actions evidence on the event-registration commit

All run IDs below tested the exact event-registration commit `921d7079b48d895b53569599f327231db64eb566`; run metadata UTC is distinct from the repository commit time.

- Living Architecture Audit run [40652153671](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153671): SUCCESS; metadata updated UTC `2026-10-28T07:46:03Z`; Tehran `2026-10-28T11:16:03+03:30`.
- Portable RAHM Conformance and Digest Evidence run [40652153690](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153690): SUCCESS; metadata updated UTC `2026-10-28T07:45:58Z`; Tehran `2026-10-28T11:15:58+03:30`.
- Evidence Gate — Independent Execution Test run [40652153748](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153748): SUCCESS; metadata updated UTC `2026-10-28T07:45:50Z`; Tehran `2026-10-28T11:15:50+03:30`. It produced the follow-up evidence commit `f0b0c45ca881af074979882837180c281e7bdf0c`, whose actual commit UTC is `2026-10-28T07:45:44Z` / Tehran `2026-10-28T11:15:44+03:30`.
- Cross-Layer Integrity Gate run [40652153876](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153876): SUCCESS; metadata UTC `2026-10-28T07:45:49Z` / Tehran `2026-10-28T11:15:49+03:30`.
- Reconciliation Acceptance Test run [40652153763](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153763): SUCCESS; metadata UTC `2026-10-28T07:45:51Z` / Tehran `2026-10-28T11:15:51+03:30`.
- CPREL Independent Runtime Transfer Harness run [40652153653](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153653): SUCCESS; metadata UTC `2026-10-28T07:45:55Z` / Tehran `2026-10-28T11:15:55+03:30`.
- CPREL Independent Transfer Evidence run [40652154102](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652154102): SUCCESS; metadata UTC `2026-10-28T07:45:54Z` / Tehran `2026-10-28T11:15:54+03:30`.
- Palang Behavior Hunter — Candidate Test Generation run [40652153621](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153621): SUCCESS; metadata UTC `2026-10-28T07:45:52Z` / Tehran `2026-10-28T11:15:52+03:30`.
- Automatic Final Registration Proof run [40652153650](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153650): SUCCESS; metadata UTC `2026-10-28T07:45:53Z` / Tehran `2026-10-28T11:15:53+03:30`.
- Pending Registration Drain run [40652153669](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153669): SUCCESS; metadata UTC `2026-10-28T07:45:48Z` / Tehran `2026-10-28T11:15:48+03:30`.
- Reconciliation Watchdog run [40652153658](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40652153658): SUCCESS; metadata UTC `2026-10-28T07:45:49Z` / Tehran `2026-10-28T11:15:49+03:30`.

## Current-head boundary

- After the successful event-commit audit/conformance pair, the Evidence Gate moved `main` to `f0b0c45ca881af074979882837180c281e7bdf0c`. Exact-SHA Actions query for that head returned 0 run(s).
- Therefore the event-registration commit `921d7079b48d895b53569599f327231db64eb566` is audited/conformant, but the newer main HEAD `f0b0c45ca881af074979882837180c281e7bdf0c` remains NOT VERIFIED until both Living Architecture Audit and Portable RAHM Conformance test that exact SHA. Do not promote the parent-commit PASS to the newer head.
- Canonical source blob remains `de1b75f07241c9b313e476af5f1417177ff78c10` (10,479 characters). Library stable ID `libfile_7ac3c9a6ec14819198eb2751e204aa48`, version 7, 10,480 characters; normalized content MATCH, exact text/byte identity FALSE, one additional trailing LF in Library. No Library write was performed because no supported exported-snapshot/source_file_ref route was available.
- Root label POINT-0/059 remains ambiguous between two candidate files. EVT-0235 collision remains preserved. CURRENT-109 remains the observed checkpoint; NEXT-051 remains the sole active queue label with path/body mismatch OPEN. CURRENT-065/CURRENT-066 and Issues #20/#21 remain OPEN.
- Buffer and Persistent Memory: NOT VERIFIED. Dropbox: OPEN / NOT VERIFIED. External independent-host recovery: NOT RUN. Paired ZIP/master release readiness: NOT VERIFIED.

The final-change commit for this time-binding file is intentionally not self-referenced here; read it from Git metadata. Do not use this file's own creation time as the event's registration time.
