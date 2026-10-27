# Time Binding — EVT-0213 / POINT-0/040 — 2026-10-27

- Stable ID: HAIF-TIME-BINDING-EVT-0213-POINT-0-040-20261027
- Production ID: HAIF-TB-EVT0213-P040-20261027
- Version: 1.0.0
- Status: REGISTERED / READ-BACK VERIFIED / OPEN
- Event: [EVT-0213](./EVT-0213-INITIAL-MODEL-NEW-HOST-HANDOFF-2026-10-27.md)
- Root: [POINT-0/040](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261027-040-INITIAL-MODEL-NEW-HOST-HANDOFF.md)
- Canonical rule: actual last-change repository commit time in UTC; Tehran derived from that same instant. Message time and operation time are separate and UNKNOWN unless captured by a trusted receipt.

## Source-backed repository commit timestamps

| Artifact | Commit SHA | Commit UTC | Asia/Tehran (+03:30) |
|---|---|---|---|
| POINT-0/040 | 300a142db9771767debd996b2e06d423978263e1 | 2026-10-27T07:49:34Z | 2026-10-27T11:19:34+03:30 |
| IN-077 | def8bcb0d63acc97d1bfbff91d332d0f1e6b00e1 | 2026-10-27T07:49:37Z | 2026-10-27T11:19:37+03:30 |
| OUT-076 | d8a8f9ab0f2a7984e06284258d3a6ff6e2324028 | 2026-10-27T07:49:40Z | 2026-10-27T11:19:40+03:30 |
| EVT-0213 | a74676f530861ed3646add527b0a60aca150e60a | 2026-10-27T07:50:13Z | 2026-10-27T11:20:13+03:30 |
| CURRENT-089 | c85fad6368429f8dc607d96b4f61329d007e89bf | 2026-10-27T07:50:16Z | 2026-10-27T11:20:16+03:30 |
| NEW-HOST-BOOTSTRAP | d85cbb4d7cecad7b280b3c747e9c353f1e9623e8 | 2026-10-27T07:50:18Z | 2026-10-27T11:20:18+03:30 |

## Distinct clocks

- User message timestamp: UNKNOWN / not supplied by a trusted message-time receipt in this record.
- Operation time for each GitHub API write/read: UNKNOWN unless exposed by a separate operation receipt.
- Workflow run timestamps and their tested SHA are recorded in the Actions evidence; they are not substituted for artifact commit timestamps.
- Library metadata time: UNKNOWN for this event; no Library write is claimed.
- Current main has moved through automated Evidence Gate commits after some tested workflow runs. Never treat an older tested SHA as proof of a later main HEAD.
