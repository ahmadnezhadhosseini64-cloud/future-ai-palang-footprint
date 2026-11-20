# TIME-BINDING-EVT-0281 — Latest verified export and on-demand delivery

- Event: [EVT-0281](./EVT-0281-LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-2026-11-20.md)
- Input: [IN-106](../../0.0/anchors/PALANG-0.0-IN-20261120-106-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Output: [OUT-105](../../0.0/anchors/PALANG-0.0-OUT-20261120-105-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Checkpoint: [CURRENT-117](../../0.0/anchors/PALANG-0.0-CURRENT-20261120-117-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Contract: [Latest verified export and on-demand delivery](../../portable/RAHM/LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT-2026-11-20-001.md)
- UTC is canonical; Asia/Tehran = UTC+03:30.
- Exact user-message receipt timestamp: UNKNOWN / UNVERIFIED.
- Assistant processing timestamp: NOT RELIABLY CAPTURED.
- Times below are actual Git commit timestamps and refer only to repository writes.

## Registration and integration ledger

| Artifact | Commit SHA | Git UTC | Asia/Tehran |
|---|---|---|---|
| IN-106 | `8314cbf0756afcb4332d1b3eab68c065229c8456` | 2026-11-20T11:40:35Z | 2026-11-20T15:10:35+03:30 |
| OUT-105 | `35b1053c65d4a6908ac1baaed3399f4ad16e0f07` | 2026-11-20T11:40:37Z | 2026-11-20T15:10:37+03:30 |
| EVT-0281 | `ce0c38bd0444e8073897b757748ad686eca3c0f5` | 2026-11-20T11:40:39Z | 2026-11-20T15:10:39+03:30 |
| CURRENT-117 | `89622eb6938272c584d82b49e2a8680dce101546` | 2026-11-20T11:40:42Z | 2026-11-20T15:10:42+03:30 |
| Delivery contract | `45562b1d8eeab214f40f9de39a9c5067e480ea3a` | 2026-11-20T11:41:05Z | 2026-11-20T15:11:05+03:30 |
| 0.0 register update | `1d754ad4dc617bbb24522f9a6fc1aaadb54b5289` | 2026-11-20T11:41:40Z | 2026-11-20T15:11:40+03:30 |
| Behavior Trace index update | `6de64629ddfe375105c10d8fce328bc537fd332f` | 2026-11-20T11:41:43Z | 2026-11-20T15:11:43+03:30 |
| Reference Index update | `a0009f98404e482fcd463f33ca59fb6540fcfcc4` | 2026-11-20T11:41:47Z | 2026-11-20T15:11:47+03:30 |
| Integration Queue index update | `deee87087e173f6f93c3be75301759339dc68226` | 2026-11-20T11:42:03Z | 2026-11-20T15:12:03+03:30 |
| Living mother update | `4a0acaf1eea14043b88900aa4a655b4dd193917a` | 2026-11-20T11:42:23Z | 2026-11-20T15:12:23+03:30 |
| NEXT-051 update | `a308dce4a4638e1d87dcdaf3796e839a73bb8cf8` | 2026-11-20T11:42:36Z | 2026-11-20T15:12:36+03:30 |

## Verification boundary

These commits establish registration and cross-index integration. They do not establish that the latest package has been rebuilt, that a permanent release pointer exists, or that clean-host recovery has passed. Those remain explicit acceptance gates under CURRENT-117 and NEXT-051.


## Final checkpoint link write

| Artifact | Commit SHA | Git UTC | Asia/Tehran |
|---|---|---|---|
| CURRENT-117 linked to TIME-BINDING-EVT-0281 | `f3018767e592a6a7e83df9e537d749709c55cf43` | 2026-11-20T11:43:15Z | 2026-11-20T15:13:15+03:30 |

Cross-file read-back fetched IN-106, OUT-105, EVT-0281, this time ledger, CURRENT-117, the delivery contract, 0.0 register, Behavior Trace index, Reference Index, Integration Queue index, living mother and NEXT-051. Their expected CURRENT-117 / EVT-0281 / contract references were present. This verifies registration and linking only; package build and delivery acceptance remain OPEN.


## Final exact-current-main build and durable release receipt

| Evidence | Value |
|---|---|
| Workflow run | [44734261656](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44734261656) — SUCCESS |
| Source/current main SHA | `8859b3b8aa4017585540a0720687eed070fddda2` |
| Run created | 2026-11-20T12:15:27Z / 2026-11-20T15:45:27+03:30 |
| Release updated | 2026-11-20T12:15:56Z / 2026-11-20T15:45:56+03:30 |
| Release ID / tag | `452647521` / `haif-latest-verified` |
| ZIP | 206531 bytes; SHA-256 `a3df4951fbd03cc59845beee78bb0c7d3acedc815842a1cfcc30fd18fd525c99` |
| Living mother | 627238 bytes; SHA-256 `8d3c0383cd460f68fa59d936b1206f31c536b9332c433872f8fab03f3214e102` |
| Workflow artifact ID | `14627118713`; outer artifact digest `sha256:9961cbc632fd1d8def6a08b4134a995f16090136af9e9332d3fa6fbb98cf495e` |
| Package checks | ZIP CRC PASS; source-byte match PASS; extracted tests PASS; downloaded round-trip PASS; local extracted rerun 24/24 PASS |

Release metadata read-back confirmed five assets: canonical ZIP, `LIVING_MASTER_REFERENCE.md`, receipt JSON, `latest-verified-export.json`, and SHA-256 checksum. The stable release locator is https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified.

This timestamp ledger records repository/workflow/release events only. It does not infer user-message receipt or assistant-processing time. Independent AI-host recovery remains NOT RUN.


## Latest superseding build and release ledger

| Field | Value |
|---|---|
| Workflow run | [44734731537](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44734731537) — SUCCESS |
| Build source SHA | `df6fef994b9c33edbc62612ff9b3db905fd666fb` |
| Current main SHA at release publication | `1d28f83cbb427e90c36fdae75d865496dea03907` |
| Post-build delta | `evidence/evidence-gate-44734731110.txt` only; compare confirms evidence-only addition |
| Current-head equivalence | `true`; recorded by workflow in receipt and latest pointer |
| Run created | 2026-11-20T12:18:51Z / 2026-11-20T15:48:51+03:30 |
| Release refreshed | 2026-11-20T12:19:12Z / 2026-11-20T15:49:12+03:30 |
| Release ID / tag | `452647521` / `haif-latest-verified` |
| ZIP | 207402 bytes; SHA-256 `36966dc71f951021a68defe72677a35b58c8fb5b25100b7e59e5d63c90109be2` |
| Living mother | 629579 bytes; SHA-256 `a6dd51f62f214476f17a40896b14c3e39a3ba4d713247297689f293af02702a9` |
| Workflow artifact ID | `14627472933`; outer artifact digest `sha256:34a3117e333a2920d26c8ed840d5ec128b7a9c9caf19ddec2accb9555525c751` |
| Package tests | CI extracted tests PASS; local extracted rerun 24/24 PASS |

Release assets read back: canonical ZIP, `LIVING_MASTER_REFERENCE.md`, receipt JSON, `latest-verified-export.json`, and SHA-256 checksum. The evidence-only equivalence is explicitly recorded; user-message receipt and assistant-processing timestamps remain unknown/unverified.


## Dynamic timestamp and receipt authority

The stable release [haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified) is the moving delivery pointer. Its latest JSON pointer and receipt provide the currently authoritative build source SHA, release-time main SHA, workflow run, exact package digest and paired mother digest. Prior run timestamps and hashes in this ledger are immutable historical observations, not a promise that they remain latest. Re-read the release metadata and pointer at every delivery. UTC remains canonical; Tehran is derived from the same sourced instant. User-message receipt and assistant-processing times remain unknown unless directly captured.
