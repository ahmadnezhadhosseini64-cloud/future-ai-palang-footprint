# Latest Verified Export — Permanent Delivery Runbook

- Stable ID: HAIF-LATEST-VERIFIED-EXPORT-RUNBOOK-2026-11-20-001
- Version: 1.0.0
- Status: ACTIVE / LIVING
- Canonical package ID: HAIF-GPT6-PORTABLE-STARTER-20261025-004
- Production ID: HAIF-G6PS-20261025-004
- Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`
- Internal package version is read from the matching build receipt and may advance without changing the stable package identity or canonical ZIP filename.
- Stable latest-release locator: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified
- Direct ZIP asset URL: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/download/haif-latest-verified/haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip

## User command

The user phrase **«آخرین نسخه کامل را بده»** is a delivery command. It means resolve and deliver the latest exact-current-main package that has passed the package acceptance pipeline, not merely describe it.

## Permanent release contents

The stable GitHub Release is refreshed only after the workflow completes all package checks. It contains:
1. The canonical ZIP.
2. The exact matching living mother Markdown copied from the same checkout.
3. The machine-readable package receipt.
4. A SHA-256 checksum file for the ZIP.
5. `latest-verified-export.json`, the machine-readable latest pointer containing source SHA, workflow run, package ID/version, ZIP digest, inventory and host-acceptance boundary.

The release tag is a stable locator. The JSON pointer and receipt, not the tag's original target commit, identify the exact source SHA used for the latest asset bytes.

## Exact delivery verification

On every user request:
1. Fetch current main HEAD and the current living mother.
2. Fetch the stable release and its latest assets.
3. Read `latest-verified-export.json` and the receipt.
4. Require `source_commit_sha == current main HEAD`; if not, trigger a manual rebuild through Actions when available and wait for a successful run. Never silently deliver an older artifact.
5. Download the ZIP and independently verify SHA-256, byte count, ZIP CRC, inventory and receipt agreement.
6. Verify the paired living mother matches the current repository master bytes.
7. Deliver the ZIP, living mother, receipt and checksum together.

If a newer commit exists after the last passing build, label the release STALE / REBUILD REQUIRED until a new exact-SHA workflow succeeds.

## Readiness levels

- SOURCE_CURRENT: current repository source identified; no archive proof.
- PACKAGE_BUILT: ZIP exists; one or more package checks remain incomplete.
- PACKAGE_VERIFIED: exact source SHA, inventory, CRC, source-byte read-back, extracted tests, artifact round-trip and durable release publication all pass.
- HOST_RECOVERED: a genuinely independent clean AI host imports the package and reconstructs the project with a direct receipt.

Never treat PACKAGE_VERIFIED as HOST_RECOVERED.

## Automation

Workflow: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/workflows/rahm-portable-conformance.yml

The workflow runs for relevant main-source changes and supports manual dispatch. It publishes or refreshes the stable release only on a successful package verification path. If release publication fails, the job fails and the previous release remains the last verified delivery; freshness must still be checked against current main.

## Unclosed capabilities

Independent AI-host import, cold-start/restart recovery, persistent memory, automatic capture of every live conversation, idle/background execution, automatic external host refresh, and cross-device/external storage remain separate OPEN / NOT RUN / NOT VERIFIED gates until direct evidence exists.


## Verified baseline — 2026-11-20

- Current main SHA: `8859b3b8aa4017585540a0720687eed070fddda2`.
- Successful exact-SHA run: [44734261656](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44734261656).
- Stable release: [haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified), ID `452647521`.
- Canonical ZIP v0.3.9, 206531 bytes, SHA-256 `a3df4951fbd03cc59845beee78bb0c7d3acedc815842a1cfcc30fd18fd525c99`.
- Matching living mother 627238 bytes, SHA-256 `8d3c0383cd460f68fa59d936b1206f31c536b9332c433872f8fab03f3214e102`.
- Five release assets read back. Package tests pass 24/24 locally. Independent-host import remains NOT RUN.
