# CURRENT-108 — گام ۰.۰: بازیابی میزبان مستقل

- Stable ID: HAIF-CURRENT-108-INDEPENDENT-HOST-RECOVERY-20261028
- Production ID: G6IP-CURRENT-108
- Previous checkpoint: [CURRENT-107](./PALANG-0.0-CURRENT-20261028-107-PORTABLE-CONFORMANCE-REPAIR.md)
- 0+ marker: [POINT-0/058](./GPT6-RAHM-USER-POINT-0-20261028-058-0PLUS-INDEPENDENT-HOST-RECOVERY.md)
- Input: [IN-096](./PALANG-0.0-IN-20261028-096-POINT-058-INDEPENDENT-HOST-RECOVERY.md)
- Output: [OUT-095](./PALANG-0.0-OUT-20261028-095-POINT-058-INDEPENDENT-HOST-RECOVERY.md)
- Event: [EVT-0233](../../architecture/BEHAVIOR-TRACE/EVT-0233-POINT-058-INDEPENDENT-HOST-RECOVERY-2026-10-28.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Status: ACTIVE / LIVING / PROTOCOL PREPARED / EXTERNAL HOST ACCEPTANCE OPEN

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
