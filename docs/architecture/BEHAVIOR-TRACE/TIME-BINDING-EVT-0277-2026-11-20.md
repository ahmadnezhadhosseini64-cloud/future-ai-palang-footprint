# TIME-BINDING-EVT-0277 — Certificate Introduction Baseline Anchor

- Event: [EVT-0277](./EVT-0277-CERTIFICATE-INTRO-REFERENCE-ANCHOR-2026-11-20.md)
- Stable ID: `PALANG-TIME-BINDING-EVT-0277-2026-11-20`
- Certificate anchor: `CERT-POINT-0PLUS-20261120-002`
- Baseline ID: `CERT-INTRO-BASELINE-20261120-001`
- Canonical timezone: `Asia/Tehran`; UTC is the permanent base.
- User-message time reference: `2026-11-20T10:51+03:30`; minute precision, seconds unknown.
- UTC equivalent: `2026-11-20T07:21Z`; minute precision, seconds unknown.
- These are message-time references, not Git commit timestamps.

## Actual Git commit timestamps
All Git timestamps below were retrieved from GitHub commit metadata after the corresponding writes. Tehran values are derived from the same UTC instant (+03:30).

| Artifact | Commit SHA | Git UTC | Asia/Tehran |
|---|---|---|---|
| CERT-IN-20261120-002 | `5aafae42d09c9d762eb0a11286ef36617634e1bd` | 2026-11-20T07:23:03Z | 2026-11-20T10:53:03+03:30 |
| CERT-OUT-20261120-002 | `7b3af621132a3eb47cccedae6c2167d6b2161ace` | 2026-11-20T07:23:07Z | 2026-11-20T10:53:07+03:30 |
| CERT-POINT-0PLUS-20261120-002 | `9b9dc79e8081a941f45a400cccbcf5e847b4c62d` | 2026-11-20T07:23:11Z | 2026-11-20T10:53:11+03:30 |
| EVT-0277 | `ae35d4f3194ee655e5bbf24b964439fb8943dfd2` | 2026-11-20T07:23:15Z | 2026-11-20T10:53:15+03:30 |
| Certificate living master | `c0fe74cf9682763003296984abc1054b4e69ad9e` | 2026-11-20T07:24:02Z | 2026-11-20T10:54:02+03:30 |
| Prior 0.0 checkpoint link | `26b82a9c07693420b97d9c3f8f6ebf84ba571c83` | 2026-11-20T07:24:07Z | 2026-11-20T10:54:07+03:30 |
| Point 0.1 continuity link | `df1fbd23553db8fb788c0533aeb87603df3045e8` | 2026-11-20T07:24:12Z | 2026-11-20T10:54:12+03:30 |
| Certificate README | `50303eab2984139164d3dfe1947b8fc16836eb0f` | 2026-11-20T07:24:17Z | 2026-11-20T10:54:17+03:30 |
| Behavior Trace README | `d977cc2dc208b60ce7968ffea73f3ae8730a3c51` | 2026-11-20T07:24:23Z | 2026-11-20T10:54:23+03:30 |
| Reference Index | `23b303fe0183c6862c0b45c7f0ee19bce3070c8d` | 2026-11-20T07:24:29Z | 2026-11-20T10:54:29+03:30 |

## Time integrity
- Message-time reference, Git author/committer time, tool execution time and readback time are distinct.
- The exact message receipt second is unavailable and remains unknown.
- The timestamp of this time-binding file and the final receipt must be read from their own Git commit metadata after creation.
- No timestamp is backfilled or inferred from an adjacent event.


## 7. Cross-link and finalization commits
| Artifact | Commit SHA | Git UTC | Asia/Tehran |
|---|---|---|---|
| Initial time-binding record | `651da803ea4d2707e2e0262532d7a1e228d87ac4` | 2026-11-20T07:25:28Z | 2026-11-20T10:55:28+03:30 |
| Point 0+ time/receipt links | `a42af3e68a140717da1a4558d763842dd865f129` | 2026-11-20T07:25:42Z | 2026-11-20T10:55:42+03:30 |
| EVT-0277 time-binding/receipt links | `1684c75ed376a3133bafbedf142483dcdee0c21a` | 2026-11-20T07:25:46Z | 2026-11-20T10:55:46+03:30 |
| CERT-OUT receipt/time-binding links | `324df29b8e876d4bb9d42b03eb30066bc27dbea2` | 2026-11-20T07:25:51Z | 2026-11-20T10:55:51+03:30 |
| Behavior Trace README final pointer | `ba34d9064bfc38347d7f60ea8bd6f4934325649d` | 2026-11-20T07:25:55Z | 2026-11-20T10:55:55+03:30 |
| Reference Index final pointer | `c5531db8fa561845ea4e80d223a0b81f8d75bca8` | 2026-11-20T07:26:00Z | 2026-11-20T10:56:00+03:30 |
| Certificate living master final pointer | `34bc72c2cbf0fa4d437a161bcc99010cac22904e` | 2026-11-20T07:26:06Z | 2026-11-20T10:56:06+03:30 |

- The final update commit for this time-binding file is recorded in the receipt after its metadata is read.
