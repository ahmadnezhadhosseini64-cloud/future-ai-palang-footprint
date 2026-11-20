# CURRENT-117 — Latest verified export and on-demand delivery

- Stable ID: HAIF-CURRENT-117-LATEST-VERIFIED-EXPORT-DELIVERY-20261120-001
- Parent context: POINT-0/065 → CURRENT-116
- Input: [IN-106](PALANG-0.0-IN-20261120-106-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Output: [OUT-105](PALANG-0.0-OUT-20261120-105-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Event: [EVT-0281](../../architecture/BEHAVIOR-TRACE/EVT-0281-LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-2026-11-20.md)
- Time binding: [TIME-BINDING-EVT-0281](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0281-LATEST-VERIFIED-EXPORT-DELIVERY-2026-11-20.md)
- Contract: [Latest verified export and on-demand delivery](../../portable/RAHM/LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT-2026-11-20-001.md)
- Sole active queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Version: 1.0.0
- Status: ACTIVE / LIVING / PACKAGE_VERIFIED — exact-current-main package and durable release verified; independent-host recovery OPEN

## Current truth

- The repository contains a CI workflow that rebuilds the canonical starter ZIP, synchronizes the living mother into its source, runs extracted-package tests and uploads the ZIP plus receipt.
- The current repository tree contains no committed ZIP binary and the Releases collection is empty.
- Existing package metadata is stale relative to the current point/event chain and says a fresh exact-head artifact receipt is not proven.
- Clean independent AI-host import, restart recovery, persistent memory and background capture remain separate unverified capabilities.

## Required final behavior

When the user asks for the latest complete version:
1. Resolve current main SHA and current living mother.
2. Find the newest successful package build and confirm it tested that exact SHA.
3. Retrieve the canonical ZIP and its receipt; validate actual digest, inventory and extracted test status.
4. Deliver ZIP + matching living mother + receipt/checksum.
5. If the current SHA has no passing package receipt, rebuild/test from current source where possible; otherwise disclose the blocker and never silently deliver a stale build.

## Next action

Continue NEXT-051 while implementing a durable latest-artifact pointer/manual rebuild path and synchronizing the package manifests. Do not create NEXT-052.

## Latest delivery implementation state — 2026-11-20

- Package source version 0.3.9 passed exact-SHA build in Run 44730867048 on `e11234a6a4dac5d13938cfa0d19deae9da966b38`: ZIP 205839 bytes; SHA-256 `b6bc06e6d50d1d3e6ec271d7f56dcde2e6981d272de3a6fed4c3c31cf428b115`; 14 files; CRC, source-byte match, extracted tests and artifact round-trip PASS.
- Workflow includes success-gated stable-release publishing. Stable locator: [haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified).
- Status: ACTIVE / LIVING / OPEN — package verified on the cited SHA; a fresh run on current main and release read-back remain pending.
- On request, resolve current HEAD first; if receipt SHA differs, rebuild rather than deliver stale bytes.
- Clean independent AI-host import, restart/persistence, automatic live capture and idle/background execution remain NOT RUN / NOT VERIFIED.


## Verified current delivery state — 2026-11-20

- Current main HEAD at acceptance: `8859b3b8aa4017585540a0720687eed070fddda2`.
- Successful exact-HEAD workflow: [44734261656](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44734261656).
- Canonical ZIP internal version 0.3.9; 206531 bytes; SHA-256 `a3df4951fbd03cc59845beee78bb0c7d3acedc815842a1cfcc30fd18fd525c99`; 14 files; ZIP CRC, source-byte match, extracted tests and artifact round-trip PASS; local extracted test rerun 24/24 PASS.
- Matching living mother 627238 bytes; SHA-256 `8d3c0383cd460f68fa59d936b1206f31c536b9332c433872f8fab03f3214e102`.
- Durable release ID `452647521`: [haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified). ZIP, mother, receipt, pointer and checksum assets are published.
- On-demand command «آخرین نسخه کامل را بده» now resolves this stable release, rechecks current HEAD and receipt, and delivers ZIP + living mother + receipt + checksum.
- HOST_RECOVERED remains NOT CLAIMED: independent AI-host import, restart persistence, automatic live capture and idle/background execution remain OPEN / NOT RUN / NOT VERIFIED.


## Latest superseding current delivery pointer — 2026-11-20

- Build workflow [44734731537](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44734731537): SUCCESS.
- Build source SHA: `df6fef994b9c33edbc62612ff9b3db905fd666fb`.
- Current main at release publication: `1d28f83cbb427e90c36fdae75d865496dea03907`; the sole post-build change is the Evidence Gate record `evidence/evidence-gate-44734731110.txt`. The release receipt/pointer confirms `current_head_equivalence_verified=true`; no package or mother bytes changed after build.
- ZIP v0.3.9: 207402 bytes; SHA-256 `36966dc71f951021a68defe72677a35b58c8fb5b25100b7e59e5d63c90109be2`; 14 files; CRC, byte match, extracted tests and round-trip PASS; local extracted tests 24/24 PASS.
- Mother: 629579 bytes; SHA-256 `a6dd51f62f214476f17a40896b14c3e39a3ba4d713247297689f293af02702a9`.
- Stable release ID 452647521 updated with five assets. On-demand delivery must compare receipt `current_main_head_sha` with current main and honor the evidence-only equivalence list.
- Independent host import/recovery remains NOT RUN; do not claim HOST_RECOVERED.


## مرجع زندهٔ نهایی برای هر درخواست تحویل

- منبع حقیقت متغیر: [انتشار پایدار haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified) و دارایی `latest-verified-export.json`.
- در هر درخواست «آخرین نسخه کامل را بده»، مقدارهای current main SHA، build source SHA، نسخه، digest، byte count، run ID و inventory باید از pointer و receipt همان انتشار دوباره خوانده شوند؛ snapshotهای عددی قبلی در این checkpoint تاریخچه‌اند.
- شرط تحویل: pointer.current_main_head_sha باید با HEAD جاری برابر باشد؛ اگر build_source_commit_sha متفاوت است، current_head_equivalence_verified باید true باشد و deltaها فقط Evidence Gate receipt باشند. هر تغییر دیگر نیازمند build تازه است.
- بسته، سند مادر هم‌نسخه، receipt، pointer و checksum با هم تحویل می‌شوند.
- وضعیت بسته PACKAGE_VERIFIED است؛ HOST_RECOVERED تا زمان دریافت رسید واقعی میزبان مستقل اعلام نمی‌شود.
