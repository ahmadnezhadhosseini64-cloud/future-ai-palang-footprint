# IN-097 — ورودی: درخواست ثبت پایدار نقطهٔ جاری در مخزن

- Stable ID: HAIF-IN-097-POINT-059-REPOSITORY-PERSISTENCE-REPAIR-20261028
- Point: [POINT-0/059](./GPT6-RAHM-USER-POINT-0-20261028-059-REPOSITORY-PERSISTENCE-REPAIR.md)
- Previous chain: [CURRENT-108](./PALANG-0.0-CURRENT-20261028-108-INDEPENDENT-HOST-RECOVERY.md)
- Output: [OUT-096](./PALANG-0.0-OUT-20261028-096-POINT-059-REPOSITORY-PERSISTENCE-REPAIR.md)
- Event: [EVT-0235](../../architecture/BEHAVIOR-TRACE/EVT-0235-POINT-059-REPOSITORY-PERSISTENCE-REPAIR-2026-10-28.md)
- Current: [CURRENT-109](./PALANG-0.0-CURRENT-20261028-109-REPOSITORY-PERSISTENCE-REPAIR.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Status: REGISTERED — user input transcribed from the current turn; user-message time UNKNOWN / UNVERIFIED.

## Input as operational requirement
The user explicitly asks to mark the current turn as point 0, continue the next work as 0.0, and attempt durable registration in the canonical GitHub repository.

## Constraints
- Do not claim repository persistence until the point, input, output, event, current checkpoint, and central navigation pointers have been written and independently read back.
- Preserve POINT-0/058 as the prior 0+ highlight.
- Preserve NEXT-051 as the sole active queue; do not create NEXT-052.
- Keep ZIP/master version mismatch and external-host acceptance OPEN until real evidence resolves them.
- Repository writes, Library mirror, Dropbox, Buffer/Persistent Memory, and independent-host acceptance are separate destinations and statuses.
