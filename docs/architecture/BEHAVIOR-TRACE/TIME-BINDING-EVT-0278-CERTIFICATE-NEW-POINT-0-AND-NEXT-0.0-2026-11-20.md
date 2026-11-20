# TIME-BINDING-EVT-0278 — New certificate Point 0 and next 0.0

- Event: [EVT-0278](./EVT-0278-CERTIFICATE-NEW-POINT-0-AND-NEXT-0.0-2026-11-20.md)
- Project event: `CERT-EVT-20261120-003`
- Stable root: `CERT-POINT-0-20261120-003`
- Next checkpoint: `CERT-POINT-0.0-20261120-003`
- Canonical timezone: Asia/Tehran; UTC is the permanent base.
- Processing-time reference: `2026-11-20T11:29:57+03:30`; UTC `2026-11-20T07:59:57Z`.
- The processing time is not the exact user-message receipt timestamp.
- The run-start main HEAD was `d8bac7ed09d7b4ea705354c39f389cf4b16cdc06`; its recorded committer time was `2026-11-20T07:27:46Z`.

## Git commit ledger
This table is completed only from actual GitHub commit metadata after each file write. Tehran is UTC +03:30.

| Artifact | Commit SHA | Git UTC | Asia/Tehran |
|---|---|---|---|
| CERT-IN-20261120-003 | `a6407413a55e2db3ea6edf1d910ac4b33ef811f6` | 2026-11-20T08:00:34Z | 2026-11-20T11:30:34+03:30 |
| CERT-OUT-20261120-003 initial | `6a304e9f5226d9cb32bd46d02ede79458b67616a` | 2026-11-20T08:00:38Z | 2026-11-20T11:30:38+03:30 |
| CERT-POINT-0-20261120-003 initial | `cd97fe7b1162311f5d44990fbbd91e3142031d9a` | 2026-11-20T08:00:43Z | 2026-11-20T11:30:43+03:30 |
| CERT-POINT-0.0-20261120-003 initial | `bb42b2563732e0fb689a490916ffc8857834cf35` | 2026-11-20T08:00:47Z | 2026-11-20T11:30:47+03:30 |
| EVT-0278 | `dcb5866b4432369c85e57b7014174dfc81116e54` | 2026-11-20T08:00:52Z | 2026-11-20T11:30:52+03:30 |
| Initial TIME-BINDING-EVT-0278 | `069d446152f1cf8635d6bd54709a5c37ddeb1647` | 2026-11-20T08:00:57Z | 2026-11-20T11:30:57+03:30 |
| CERT-EVT-20261120-003 | `72e9d2b26071264c75a7f57dba1af9668ebd90f9` | 2026-11-20T08:01:25Z | 2026-11-20T11:31:25+03:30 |
| CERT-OUT with event link | `5ea4e7e0f6c572b1c3b4f4b4337b73f7ff38e32b` | 2026-11-20T08:01:45Z | 2026-11-20T11:31:45+03:30 |
| Point 0 with event link | `5634c457abe55c49d46f0b35653cbc666df5f3fe` | 2026-11-20T08:01:50Z | 2026-11-20T11:31:50+03:30 |
| 0.0 with event/receipt links | `e4de3e874c013fb387c3edeb29d2f0a51b59e98c` | 2026-11-20T08:01:55Z | 2026-11-20T11:31:55+03:30 |
| Prior 0+ successor link | `871b3ca6da8e5692e6a53955c482a418cd9acb07` | 2026-11-20T08:02:01Z | 2026-11-20T11:32:01+03:30 |
| Prior 0.0 successor link | `7472e3f682e366d6a6a410e4cb581c64ac49fd0e` | 2026-11-20T08:02:07Z | 2026-11-20T11:32:07+03:30 |
| Point 0.1 continuity link | `6d135c5d73095e33ebcb2e1589ca388ed09b11e1` | 2026-11-20T08:02:12Z | 2026-11-20T11:32:12+03:30 |
| Certificate living master link | `a9da2eadcdf7ef7b74454dd5be001e8dcdbbd255` | 2026-11-20T08:02:18Z | 2026-11-20T11:32:18+03:30 |
| Certificate README link | `d4e000c5f39b72ff64c264ba51b29e86b4424955` | 2026-11-20T08:02:24Z | 2026-11-20T11:32:24+03:30 |
| Behavior Trace README link | `013110f718ed2e9d59ad80ec5a772d61446377c7` | 2026-11-20T08:02:29Z | 2026-11-20T11:32:29+03:30 |
| Reference Index child-branch link | `5ac7031339775c708269522d98fb750984a5f151` | 2026-11-20T08:02:37Z | 2026-11-20T11:32:37+03:30 |

## Integrity rules
- Never substitute processing time for user-message time.
- Never infer a commit timestamp from an adjacent commit.
- Record author/committer metadata from the exact commit for each artifact.
- Preserve the global root POINT-0/064 and CURRENT-115 / NEXT-051.
- Independent-host recovery is not proven by Git read-back or CI alone.
