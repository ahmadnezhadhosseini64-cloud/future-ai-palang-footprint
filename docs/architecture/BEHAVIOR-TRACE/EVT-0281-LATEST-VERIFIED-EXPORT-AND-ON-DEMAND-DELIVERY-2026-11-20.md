# EVT-0281 — Latest verified export and on-demand delivery

- Stable ID: HAIF-EVT-0281-LATEST-VERIFIED-EXPORT-DELIVERY-20261120-001
- Input: [IN-106](../../0.0/anchors/PALANG-0.0-IN-20261120-106-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Output: [OUT-105](../../0.0/anchors/PALANG-0.0-OUT-20261120-105-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Contract: [LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT](../../portable/RAHM/LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT-2026-11-20-001.md)
- Parent context: POINT-0/065 → CURRENT-116 → NEXT-051
- Status: ACTIVE / LIVING / OPEN — implementation and acceptance pending

## Event

The user clarified that the architecture must continuously maintain a usable, extractable latest package and living mother reference, and must deliver the latest complete version immediately on request.

The repository inspection found an existing CI package builder with extraction and artifact round-trip checks, but no GitHub Release, no committed ZIP binary, stale package metadata, and no proof that the current main SHA has a current successful package receipt. The package's independent clean-host acceptance remains NOT RUN.

## Decision

Adopt OUT-105 and the linked delivery contract as the canonical behavior. Do not call a package latest, complete, verified or host-recovered beyond its actual evidence level. Deliver the same canonical ZIP identity plus the exact matching living mother and machine-readable receipt.

No historical root, queue, package identity or unresolved gate is replaced by this event. NEXT-051 remains the sole active queue; no NEXT-052 is created.

## Implementation progress — durable latest delivery

- Package builder succeeded on exact source SHA `e11234a6a4dac5d13938cfa0d19deae9da966b38` in [Run 44730867048](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44730867048).
- Internal package version `0.3.9`; canonical ZIP bytes `205839`; SHA-256 `b6bc06e6d50d1d3e6ec271d7f56dcde2e6981d272de3a6fed4c3c31cf428b115`; 14 files; ZIP CRC, source-byte read-back, extracted tests and downloaded-artifact round-trip PASS.
- Workflow artifact ID `14626341982`; outer artifact SHA-256 `8c7912510aab21e3aa494be56ea771d1e2a8bb0d992c8b3c9035f399b45111d9` (not the inner canonical ZIP digest).
- Durable-release publishing has been added to the workflow. It publishes ZIP + matching mother + receipt + checksum + latest pointer to stable tag `haif-latest-verified` only after all checks pass.
- A fresh run on the newer current HEAD and release read-back are still required. Independent-host acceptance remains NOT RUN.


## Final acceptance — permanent release and exact-current-main package

- [Portable RAHM Conformance Run 44734261656](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44734261656) completed SUCCESS on exact current main SHA `8859b3b8aa4017585540a0720687eed070fddda2`.
- Package: stable ID `HAIF-GPT6-PORTABLE-STARTER-20261025-004`; internal version `0.3.9`; canonical filename unchanged; 14 files; 206531 bytes; SHA-256 `a3df4951fbd03cc59845beee78bb0c7d3acedc815842a1cfcc30fd18fd525c99`.
- ZIP CRC, source-byte read-back, extracted package tests and downloaded artifact round-trip all PASS. The extracted package was independently rerun in the working environment: 24/24 tests PASS.
- Paired living mother: 627238 bytes; SHA-256 `8d3c0383cd460f68fa59d936b1206f31c536b9332c433872f8fab03f3214e102`; exact bytes match the packaged `LIVING_MASTER_REFERENCE.md`.
- Durable GitHub Release published and read back: [haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified), release ID `452647521`. Assets: canonical ZIP, `LIVING_MASTER_REFERENCE.md`, JSON receipt, latest pointer and SHA-256 file.
- Status: PACKAGE_VERIFIED for exact current main SHA. Independent clean-host import remains NOT RUN; therefore HOST_RECOVERED is not claimed.


## Latest superseding production receipt — 2026-11-20

- Successful workflow: [Run 44734731537](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44734731537); build source SHA `df6fef994b9c33edbc62612ff9b3db905fd666fb`.
- Current main at release publication: `1d28f83cbb427e90c36fdae75d865496dea03907`. The only post-build commit was the Evidence Gate receipt `evidence/evidence-gate-44734731110.txt`; compare confirmed no package source or living-mother changes. Workflow records `current_head_equivalence_verified=true` and the current main SHA in the release receipt/pointer.
- Package v0.3.9; 14 files; 207402 bytes; SHA-256 `36966dc71f951021a68defe72677a35b58c8fb5b25100b7e59e5d63c90109be2`; ZIP CRC/source-byte match/extracted tests/downloaded round-trip PASS; independent local extracted rerun 24/24 PASS.
- Paired living mother: 629579 bytes; SHA-256 `a6dd51f62f214476f17a40896b14c3e39a3ba4d713247297689f293af02702a9`.
- Stable release [haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified), ID `452647521`, refreshed at 2026-11-20T12:19:12Z. Five assets are present: ZIP, `LIVING_MASTER_REFERENCE.md`, receipt JSON, latest pointer JSON and checksum.
- This supersedes the previous v0.3.9 receipt for source SHA 8859b3b. Independent-host recovery remains NOT RUN.
