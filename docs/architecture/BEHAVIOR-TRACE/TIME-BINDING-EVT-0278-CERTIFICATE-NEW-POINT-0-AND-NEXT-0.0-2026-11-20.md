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
| CERT-IN-20261120-003 | pending | pending | pending |
| CERT-OUT-20261120-003 | pending | pending | pending |
| CERT-POINT-0-20261120-003 | pending | pending | pending |
| CERT-POINT-0.0-20261120-003 | pending | pending | pending |
| EVT-0278 | pending | pending | pending |
| This time-binding file | pending | pending | pending |
| Cross-index updates | pending | pending | pending |
| Final receipt | pending | pending | pending |

## Integrity rules
- Never substitute processing time for user-message time.
- Never infer a commit timestamp from an adjacent commit.
- Record author/committer metadata from the exact commit for each artifact.
- Preserve the global root POINT-0/064 and CURRENT-115 / NEXT-051.
- Independent-host recovery is not proven by Git read-back or CI alone.
