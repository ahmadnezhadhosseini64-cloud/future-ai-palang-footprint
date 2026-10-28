# CURRENT-108 — گام ۰.۰: بازیابی میزبان مستقل

- Stable ID: HAIF-CURRENT-108-INDEPENDENT-HOST-RECOVERY-20261028
- Production ID: G6IP-CURRENT-108
- Previous checkpoint: [CURRENT-107](./PALANG-0.0-CURRENT-20261028-107-PORTABLE-CONFORMANCE-REPAIR.md)
- 0+ marker: [POINT-0/058](./GPT6-RAHM-USER-POINT-0-20261028-058-0PLUS-INDEPENDENT-HOST-RECOVERY.md)
- Input: [IN-096](./PALANG-0.0-IN-20261028-096-POINT-058-INDEPENDENT-HOST-RECOVERY.md)
- Output: [OUT-095](./PALANG-0.0-OUT-20261028-095-POINT-058-INDEPENDENT-HOST-RECOVERY.md)
- Event: [EVT-0233](../../architecture/BEHAVIOR-TRACE/EVT-0233-POINT-058-INDEPENDENT-HOST-RECOVERY-2026-10-28.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Status: ACTIVE / LIVING / PROTOCOL PREPARED / EXTERNAL HOST ACCEPTANCE OPEN / NOT RUN / NOT VERIFIED

## Canonical chain
`POINT-0/058 (0+) → IN-096 → OUT-095 → EVT-0233 → CURRENT-108 → NEXT-051`

## Completed in this checkpoint
- Defined an independent-host acceptance matrix with explicit positive/negative tests.
- Required exact identity and chain read-back from the transferred ZIP and living master.
- Required raw host receipt preservation, actual SHA-256, independent read-back and fresh-session/restart testing.
- Preserved the earlier POINT-0/057 and CURRENT-107 chain without overwriting it.
- Kept NEXT-051 as the only active queue; no NEXT-052 created.

## Still open
No independent host has supplied a raw response in this context. Therefore external import, acceptance, second-host recovery, restart persistence, automatic live capture, authorized GitHub write-back, unattended/background execution, and historical graph reconciliation remain OPEN / NOT PROVEN.

## Exact package receipt — Portable Conformance run 40644355767

- Source commit for this build: `a0361dda721418604b923f48cf22162186deb2d4`.
- Canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
- Internal package version: `0.3.8`; Stable ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`.
- Size: `101556` bytes; SHA-256: `330f6aab2f2b98959f1155099d20d344b20448cbdceaf2b765dce5a25f842177`.
- Inventory: 13 files, including `LIVING_MASTER_REFERENCE.md` and `INDEPENDENT_HOST_ACCEPTANCE_PROMPT_FA.md`.
- ZIP integrity: PASS; source-byte read-back: PASS; extracted package tests: 23/23 PASS. The downloaded canonical ZIP was independently extracted and hashed; the digest and byte count matched the workflow receipt.
- Portable Conformance: [run 40644355767](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40644355767) — SUCCESS.
- Living Architecture Audit: [run 40644355892](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40644355892) — SUCCESS.
- Cross-layer integrity: [run 40644355836](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40644355836) — SUCCESS.
- External independent-host acceptance: NOT RUN. This receipt is package/repository evidence only.
