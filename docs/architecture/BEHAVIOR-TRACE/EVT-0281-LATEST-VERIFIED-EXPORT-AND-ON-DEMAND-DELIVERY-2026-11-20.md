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
