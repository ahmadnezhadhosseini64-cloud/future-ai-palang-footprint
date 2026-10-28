# TIME-BINDING-EVT-0236 — Live mirror synchronization recheck

- Event: [EVT-0236](./EVT-0236-LIVE-MIRROR-SYNC-RECHECK-2026-10-28.md)
- Stable ID: PALANG-TIME-BINDING-EVT-0236-LIVE-MIRROR-SYNC-2026-10-28
- Version: 1.0.0
- Canonical registration clock: actual final-change Git commit timestamp in UTC; Tehran time is derived from that same instant (+03:30).
- Event registration commit SHA / UTC / Tehran: PENDING the first commit response and independent read-back; replace this provisional field with actual repository metadata before treating the binding as final.
- Main HEAD observed at comparison start: `11e69bb6b5e62a11186569b23312ba06e1d4e1c3`, commit UTC `2026-10-28T07:29:56Z`, Tehran `2026-10-28T10:59:56+03:30`. This is an observation anchor, not the event registration time.
- Comparison observation clock from the execution context: UTC `2026-10-28T07:35:16Z` / Tehran `2026-10-28T11:05:16+03:30`; not a repository commit timestamp.
- Canonical source blob: `de1b75f07241c9b313e476af5f1417177ff78c10`, 10,479 characters.
- Library stable ID: `libfile_7ac3c9a6ec14819198eb2751e204aa48`; version 7; 10,480 characters; metadata modified UTC `2026-10-24T04:45:28.479773Z`, Tehran `2026-10-24T08:15:28.479773+03:30`. Metadata time is distinct from comparison operation time.
- Comparison: normalized content MATCH; exact text/byte identity FALSE; Library has one additional trailing LF. No write was performed because a supported exported-snapshot/source_file_ref route was not available.
- Latest passing Living Architecture Audit and Portable RAHM Conformance runs were on SHA `8bbb7a535687357c77f66ab115232dd98d897f20`, not observed main `11e69bb6b5e62a11186569b23312ba06e1d4e1c3`; exact-current-main acceptance remains NOT VERIFIED. Exact run IDs and tested SHAs are recorded in EVT-0236.
- Status: PROVISIONAL until the actual event registration commit metadata is read back and this file is updated with the corresponding UTC/Tehran pair. No timestamp is inferred from schedule, user-message time, Library metadata or Actions run time.
