# OUT-105 — Latest verified export delivery architecture

- Stable ID: HAIF-OUT-105-LATEST-VERIFIED-EXPORT-20261120-001
- Input: [IN-106](PALANG-0.0-IN-20261120-106-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Parent context: POINT-0/065 → CURRENT-116 → NEXT-051
- Status: IMPLEMENTED / PACKAGE_VERIFIED / DURABLE RELEASE PUBLISHED; INDEPENDENT HOST RECOVERY OPEN

## Repository findings

- The Portable RAHM Conformance workflow already contains a canonical starter ZIP build, extraction tests, source-byte comparison, uploaded artifact and downloaded-artifact round-trip checks.
- The workflow synchronizes the living mother into the starter package source before rebuilding.
- The canonical filename and stable package identity are defined in the existing package contract.
- The repository currently has no GitHub Releases and no committed ZIP binary.
- The portable starter manifest still identifies version 0.3.8 and explicitly says that a fresh exact-head artifact receipt and real independent-host acceptance are not proven.
- The separate GPT6 HAIF Boot Package manifest says portable_archive_created=false, export pending and clean-host import NOT RUN.

## Delivery model

1. Canonical source: latest default-branch main SHA.
2. Package source sync: copy the exact current living mother reference into the starter package source.
3. Build: rebuild the existing canonical ZIP filename; retain stable package/production IDs and update internal version only through a reviewed version change.
4. Verify: required inventory, ZIP CRC, exact source-to-extracted byte comparison, tests executed from the extracted archive, SHA-256, byte count and downloaded-artifact round trip.
5. Receipt: record source main SHA, workflow run, package identity/version, canonical filename, inventory, bytes, SHA-256, tests and explicit host-acceptance status.
6. Delivery: provide the ZIP, the matching living mother reference and the receipt/checksum together.
7. Freshness: package is "latest verified" only when its source SHA equals the current main SHA, or the exact difference is disclosed. A later main commit invalidates the "latest exact-head verified" label until rebuilt and retested.

## Readiness levels

- SOURCE_CURRENT: current source and living mother are present; no package claim.
- PACKAGE_BUILT: ZIP created; integrity/test evidence may still be incomplete.
- PACKAGE_VERIFIED: exact source SHA, inventory, CRC, extracted tests, SHA-256 and artifact round-trip pass.
- HOST_RECOVERED: a genuinely independent clean AI host imports and reconstructs the state with direct evidence.

PACKAGE_VERIFIED is sufficient to deliver an extractable portable package, but it must never be described as HOST_RECOVERED.

## On-demand command

When the user says "آخرین نسخه کامل را بده", resolve current main SHA, inspect the newest successful package workflow run and its exact tested SHA, retrieve its artifact and receipt, verify freshness and digest, and deliver the ZIP + living mother + receipt. If no fresh successful artifact exists, rebuild and verify from the current source before delivery where the available execution route permits. If that cannot be done, state the exact blocker and do not substitute an older artifact silently.

## Open implementation items

- Establish a durable, clearly discoverable latest-artifact pointer or release endpoint; the current workflow artifact alone is temporary.
- Ensure the package build runs on every relevant source/mother change and supports a deliberate manual rebuild.
- Update stale package lineage and export manifests from source evidence, without inventing hashes.
- Run package build and strict conformance against the exact current main SHA.
- Keep clean-host recovery, persistence, background capture and external destination acceptance as separate OPEN gates until directly tested.

## Implementation update — exact build and durable-release automation

- Successful exact-SHA package build: [Run 44730867048](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44730867048), source SHA `e11234a6a4dac5d13938cfa0d19deae9da966b38`.
- Canonical ZIP: 205839 bytes; SHA-256 `b6bc06e6d50d1d3e6ec271d7f56dcde2e6981d272de3a6fed4c3c31cf428b115`; 14 files; CRC/source-byte match/extracted tests/downloaded round-trip PASS.
- Durable release publishing is implemented in the workflow at [haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified). It uploads ZIP, paired living mother, JSON receipt, checksum and latest pointer only after successful package verification.
- The workflow and runbook commits are newer than the cited receipt. A fresh run on current main and release read-back remain pending; do not label the stable release published until verified.
- Package identity and canonical filename remain unchanged. Independent clean-host recovery remains NOT RUN.


## Final implementation acceptance — 2026-11-20

- Exact current main SHA: `8859b3b8aa4017585540a0720687eed070fddda2`.
- Successful workflow: [Run 44734261656](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44734261656).
- Canonical ZIP internal version 0.3.9; 206531 bytes; SHA-256 `a3df4951fbd03cc59845beee78bb0c7d3acedc815842a1cfcc30fd18fd525c99`; 14 files; CRC, source-byte read-back, extracted tests and artifact round-trip PASS. Local extracted rerun: 24/24 PASS.
- Matching living mother: 627238 bytes; SHA-256 `8d3c0383cd460f68fa59d936b1206f31c536b9332c433872f8fab03f3214e102`.
- Permanent release: [haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified), release ID `452647521`; five assets read back in release metadata.
- Delivery set is now available at the stable release locator. Exact source SHA is the current main HEAD at acceptance.
- Remaining separate gate: genuine independent AI-host import/reconstruction and returned receipt remain NOT RUN. Package verification is not host recovery.
