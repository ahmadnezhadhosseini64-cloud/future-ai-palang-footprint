# CURRENT-117 — Latest verified export and on-demand delivery

- Stable ID: HAIF-CURRENT-117-LATEST-VERIFIED-EXPORT-DELIVERY-20261120-001
- Parent context: POINT-0/065 → CURRENT-116
- Input: [IN-106](PALANG-0.0-IN-20261120-106-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Output: [OUT-105](PALANG-0.0-OUT-20261120-105-LATEST-VERIFIED-EXPORT-DELIVERY.md)
- Event: [EVT-0281](../../architecture/BEHAVIOR-TRACE/EVT-0281-LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-2026-11-20.md)
- Contract: [Latest verified export and on-demand delivery](../../portable/RAHM/LATEST-VERIFIED-EXPORT-AND-ON-DEMAND-DELIVERY-CONTRACT-2026-11-20-001.md)
- Sole active queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN — contract registered; durable latest delivery and exact-current-SHA package acceptance not yet proven

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
