# Time Binding — POINT-0/026 / IN-062 / OUT-061 / EVT-0192 / CURRENT-073

- **Stable ID:** HAIF-TIME-BINDING-POINT-0-026-20261026
- **Production ID:** HAIF-TB-026-20261026
- **Version:** 1.0.0
- **Status:** REPOSITORY COMMIT TIMES READ-BACK VERIFIED
- **Canonical rule:** Repository registration time is the actual commit timestamp in UTC; Asia/Tehran is derived from that same instant (+03:30 on the recorded date). These are file-registration commits, not claims about the exact user-message time.
- **Root:** [POINT-0/026](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-026-DUAL-PATH-HAIF-CONTINUATION.md)
- **IN:** [IN-062](../../0.0/anchors/PALANG-0.0-IN-20261026-062-DUAL-PATH-HAIF-CONTINUATION.md)
- **OUT:** [OUT-061](../../0.0/anchors/PALANG-0.0-OUT-20261026-061-DUAL-PATH-HAIF-CONTINUATION.md)
- **Event:** [EVT-0192](./EVT-0192-USER-REQUEST-POINT-0-DUAL-PATH-HAIF-CONTINUATION-2026-10-26.md)
- **Current checkpoint:** [CURRENT-073](../../0.0/anchors/PALANG-0.0-CURRENT-20261026-073-DUAL-PATH-HAIF-CONTINUATION.md)

| Item | Registration commit SHA | Canonical UTC commit time | Asia/Tehran derived time |
|---|---|---|---|
| POINT-0/026 | `04ce62b40fc011c27f3ae0809f86d8425e96eefc` | `2026-10-26T05:30:32Z` | `2026-10-26 09:00:32 +03:30` |
| IN-062 | `f1387a79eb57422d20cc8326228bd0bbb9a5cafb` | `2026-10-26T05:30:36Z` | `2026-10-26 09:00:36 +03:30` |
| OUT-061 | `09c54fcc9440a33d421140526f8ec8c0e0a8fe65` | `2026-10-26T05:30:40Z` | `2026-10-26 09:00:40 +03:30` |
| EVT-0192 | `38c466d53737ee9e2e7fdbb2b8968865a91594ba` | `2026-10-26T05:30:45Z` | `2026-10-26 09:00:45 +03:30` |
| CURRENT-073 | `14945996ceea0cfbbe5b1fb5bc9c7be9fe9aa65f` | `2026-10-26T05:30:48Z` | `2026-10-26 09:00:48 +03:30` |

## Evidence and boundary
Each commit timestamp was retrieved from GitHub commit metadata for the exact commit SHA listed above. The files were independently fetched after creation and their identifiers and cross-links were checked. This binding does not assert the exact time the user sent the message, and it does not verify any non-repository storage destination.
