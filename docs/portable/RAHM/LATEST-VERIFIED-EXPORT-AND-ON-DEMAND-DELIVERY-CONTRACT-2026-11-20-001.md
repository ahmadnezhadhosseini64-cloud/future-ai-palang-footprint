# Latest Verified Export and On-Demand Delivery Contract

- Stable ID: HAIF-LATEST-VERIFIED-EXPORT-DELIVERY-CONTRACT-2026-11-20-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN — design registered; implementation pending
- Parent context: POINT-0/065 → CURRENT-116 → EVT-0281 → CURRENT-117
- Sole active queue: NEXT-051

## 1. Purpose

Maintain one continuously evolving, operational, extractable package and its matching living mother reference. On the user's request, deliver the newest package that has passed its stated acceptance checks, without relying on hidden conversation history and without presenting stale or unverified bytes as current.

## 2. Stable identity and outputs

- Preserve the established package stable ID and production ID.
- Preserve the canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
- Version the package internally; do not create competing version-named ZIP identities.
- Synchronize the current living mother into the package as `LIVING_MASTER_REFERENCE.md`.
- Deliver as a matched set: canonical ZIP, exact matching living mother Markdown, machine-readable receipt JSON, and SHA-256 checksum.
- Preserve previous receipts as historical evidence; never reuse an old digest for new bytes.

## 3. Build and acceptance pipeline

For each relevant main change and on deliberate manual rebuild:
1. Checkout an exact main commit SHA.
2. Synchronize the living mother reference from that same checkout.
3. Validate required package inventory, stable IDs, manifest schema and parent/current/queue references.
4. Build the canonical ZIP from exact source bytes.
5. Verify CRC, inventory, byte count and SHA-256.
6. Extract to a clean temporary directory and compare every packaged file byte-for-byte with source.
7. Run tests from the extracted archive, not only from the repository source.
8. Download the uploaded artifact and verify its bytes, digest, inventory and tests again.
9. Emit a receipt containing source SHA, run ID/URL, package IDs/version, filename, inventory, byte count, SHA-256, test results and host acceptance state.
10. Mark PACKAGE_VERIFIED only if every package-level criterion passes on the exact current main SHA.

A new main commit after the build means the package is no longer exact-current-head verified until a new build succeeds.

## 4. Readiness labels

- SOURCE_CURRENT: sources are current; no archive verification implied.
- PACKAGE_BUILT: archive exists; integrity or tests may be pending.
- PACKAGE_VERIFIED: exact-SHA build, inventory, CRC, source-byte match, extracted tests and downloaded-artifact round-trip all pass.
- HOST_RECOVERED: a genuinely independent clean AI host imports the package and reconstructs state with direct read-back evidence.

Never use PACKAGE_VERIFIED and HOST_RECOVERED interchangeably.

## 5. On-demand delivery procedure

On "آخرین نسخه کامل را بده":
- Resolve the current main SHA and latest living mother bytes.
- Retrieve the newest successful canonical-package workflow run and its uploaded archive/receipt.
- Confirm the receipt's source SHA equals current main; confirm the canonical filename and stable identity; independently recalculate SHA-256 and inspect ZIP inventory/CRC.
- Confirm extracted tests passed and the paired living mother matches the same source SHA.
- Deliver the ZIP, matching mother document and receipt/checksum together.
- If no exact-current-head artifact exists, start a fresh build/test from current source when an authorized execution route is available. If not, state that no exact-current verified artifact is currently deliverable; never silently fall back to a stale artifact.

## 6. Durable latest locator

The CI artifact is temporary and is not a permanent release URL. Implementation must provide a discoverable latest-successful artifact pointer or a stable release endpoint that is updated only after PACKAGE_VERIFIED. The pointer must identify the exact tested commit, workflow run, artifact ID, filename, digest and build receipt. It must never point to a failed, stale or unverified build.

## 7. Separate unresolved capabilities

Package build and extraction do not prove clean independent AI-host import, restart/new-session recovery, persistent memory or cross-device continuity, idle/background capture, live ChatGPT producer or authorized repository write-back, or Dropbox/other external persistence. These remain separate OPEN / NOT RUN / NOT VERIFIED gates until direct evidence exists.

## 8. Current baseline finding — 2026-11-20

Repository inspection at main tree SHA `c4b8fd21eafbdc9a22121af36705d19201bbbf15` found:
- no GitHub Releases;
- no committed ZIP binary in the 6,168-entry repository tree;
- an existing Portable RAHM Conformance workflow that builds and uploads the canonical starter ZIP and receipt, tests extracted contents and verifies a downloaded artifact round trip;
- starter source manifest version 0.3.8 with explicit not-proven entries for a fresh exact-head ZIP receipt and real independent-host acceptance;
- GPT6 HAIF Boot Package manifest with `portable_archive_created=false`, export pending and clean-host import NOT RUN.

Therefore the current state is not yet PACKAGE_VERIFIED for the exact latest main SHA. This contract does not upgrade any gate by declaration.

## 9. Implemented stable release publication — 2026-11-20

The Portable RAHM Conformance workflow now has a success-gated publishing step. Only after package construction, ZIP CRC, source-byte read-back, extracted tests, downloaded-artifact receipt/digest verification and paired living-master byte match succeed does it create or refresh the stable GitHub Release tag `haif-latest-verified`.

Stable locator: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified

Direct canonical ZIP asset: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/download/haif-latest-verified/haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip

The release contains the canonical ZIP, exact paired living mother, JSON receipt, SHA-256 checksum and `latest-verified-export.json`. The receipt identifies the exact tested source SHA; the stable tag is a locator, not a claim that its original tag target equals every later source commit.

A successful package run exists for SHA `e11234a6a4dac5d13938cfa0d19deae9da966b38` (Run 44730867048), internal version 0.3.9, 205839 ZIP bytes, SHA-256 `b6bc06e6d50d1d3e6ec271d7f56dcde2e6981d272de3a6fed4c3c31cf428b115`, 14 files, package checks PASS. This is evidence for that SHA only. A fresh successful run and release read-back on current main are required after release automation changes.

See [Latest Verified Export Delivery Runbook](./LATEST-VERIFIED-EXPORT-DELIVERY-RUNBOOK.md).
