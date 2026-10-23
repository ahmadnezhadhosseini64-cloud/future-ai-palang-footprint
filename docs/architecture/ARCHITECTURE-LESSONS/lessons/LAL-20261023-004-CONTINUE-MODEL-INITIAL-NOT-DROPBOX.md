# LAL-20261023-004 — تداوم مسیر مدل اولیه، نه Dropbox

- Stable ID: PALANG-ARCH-LESSON-CONTINUE-MODEL-INITIAL-NOT-DROPBOX-2026-10-23-004
- Production ID: LAL-20261023-004
- Version: 1.0.0
- Status: REGISTERED / ACTIVE ROUTING RULE / LIVING
- Source of truth: [EVT-0106](../../BEHAVIOR-TRACE/EVT-0106-RESUME-HAIF-EXECUTION-NOT-DROPBOX-2026-10-23.md)
- Governing master: [CMIND](../../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)

## Lesson
وجود یک مسیر تاریخی یا مقصد ذخیره‌سازی به‌تنهایی دلیل تغییر مسیر کار جاری نیست. ابتدا آخرین نقطهٔ 0.0، سند مادر، صف و شکاف فعال را بخوان؛ سپس از همان هدف ادامه بده.

## Operational rule
Before every continuation, verify the latest 0.0 return point, master reference, open queue and active execution target. Keep unrelated destinations such as the Dropbox failover branch separate unless the user explicitly reopens that branch.

## Acceptance criteria
- Chosen action is linked to the current return point and open queue.
- The reason for route selection is recorded.
- Historical paths are preserved but do not override the active goal.
- If path selection was wrong, record cause as observation/inference/hypothesis and add a regression check.

## Evidence boundary
EVT-0106 records the route correction. This lesson governs selection; it does not claim unrelated external destinations were tested.
