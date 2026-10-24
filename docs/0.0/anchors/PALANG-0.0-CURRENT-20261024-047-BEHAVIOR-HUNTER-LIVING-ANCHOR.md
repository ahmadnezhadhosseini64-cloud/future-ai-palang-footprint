# CURRENT-047 — نقطهٔ جاری زنده: قاعدهٔ شکارچی رفتار و حاکمیت شواهد
- Stable ID: G6IP-RAHM-CURRENT-047-20261024
- Production ID: G6IP-CURRENT-047
- Version: 1.0.0
- Status: REGISTERED / READ-BACK VERIFIED only after read-back; runtime automation OPEN
- Parent: [CURRENT-046](./PALANG-0.0-CURRENT-20261024-046-CAPABILITY-FALLBACK.md)
- Input: [IN-039](./PALANG-0.0-IN-20261024-039-BEHAVIOR-HUNTER-LIVING-RULE.md)
- Output: [OUT-039](./PALANG-0.0-OUT-20261024-039-BEHAVIOR-HUNTER-LIVING-RULE.md)
- Event: [EVT-0147](../../architecture/BEHAVIOR-TRACE/EVT-0147-BEHAVIOR-HUNTER-LIVING-RULE-AND-CHECKPOINT-2026-10-24.md)
- Previous action queue: [NEXT-044](./PALANG-0.0-NEXT-20261024-044-FALLBACK-TEST-AND-INDEX-RECONCILIATION.md)
- Next 0.0 checkpoint: [NEXT-045](./PALANG-0.0-NEXT-20261024-045-BEHAVIOR-HUNTER-TEST-AND-OPEN-GATES.md)
- HAIF living mother: [سند مرجع مادر مدل اولیه هوش مصنوعی](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- GPT-6 living master: [GPT6 Interactive Project Living Master](../../reference/REFERENCE-DOCUMENTS/GPT6-INTERACTIVE-PROJECT-LIVING-MASTER-REFERENCE-2026-10-24-001.md)
- Inherited architecture master: [GPT6 New Project Inherited Architecture](../../reference/REFERENCE-DOCUMENTS/GPT6-NEW-PROJECT-INHERITED-ARCHITECTURE-LIVING-MASTER-2026-10-24-001.md)
- Behavior Hunter / چشم پلنگ: [EVT-0147](../../architecture/BEHAVIOR-TRACE/EVT-0147-BEHAVIOR-HUNTER-LIVING-RULE-AND-CHECKPOINT-2026-10-24.md)

## Current governing rule
هر موردی که پیاده‌سازی و بازخوانی آن اثبات شده، وضعیت متناسب می‌گیرد؛ هر موردی که فقط تعریف یا مستند شده، به‌عنوان قابلیت فعال جا زده نمی‌شود؛ و هر آزمون انجام‌نشده یا ناموفق با شناسه، دلیل و گام بازیابی باز باقی می‌ماند.

## Chain
CURRENT-045 → IN-038 → OUT-038 → EVT-0146 → CURRENT-046 → IN-039 → OUT-039 → EVT-0147 → CURRENT-047 → NEXT-045.

## Verified / open state
- Repository record creation and cross-links: verify by post-write fetch before calling READ-BACK VERIFIED.
- Behavior Hunter as a documented rule: pending artifact read-back.
- Automatic capture/continuous monitoring: NOT VERIFIED.
- Capability fallback deployment: OPEN / NOT RUN.
- JSON Schema positive/negative fixtures: OPEN / NOT RUN.
- SHA-256 exact-byte verification: OPEN / NOT RUN.
- Comprehensive link and duplicate-ID audit: OPEN / NOT RUN.
- Durable memory restart, idle background execution, clean-host and second-host tests: OPEN / NOT RUN.
- Earlier CURRENT-046/NEXT-044 and older anchors are preserved; no branch is overwritten.

## Canonical timestamp policy
Repository registration time is the actual Git commit timestamp in UTC, with Tehran equivalent derived from the same instant. Exact user-message time is not substituted with commit time. The actual commit timestamp will be attached after fetching the created commit metadata.

## Recovery
Resume from NEXT-045. If any write/read-back fails, preserve the failure, leave the gate OPEN, record the exact path and reason, and retry only after diagnosing the failure.

## Read-back result
- This checkpoint was fetched after creation; its Stable ID, CURRENT-046 parent, IN-039/OUT-039/EVT-0147 chain, mother links and NEXT-045 continuation link matched.
- The HAIF mother, both GPT-6 living masters, Reference Index and integration queue were updated and fetched after write; the CURRENT-047/NEXT-045 markers and links matched.
- Repository registration/read-back is verified for these named paths only. Runtime activation and all unrun test gates remain OPEN / NOT RUN.
- Latest cross-link commit observed: `49bfeb2a64b808238c73c742fca9959703ccb464`; UTC `2026-10-24T15:37:59Z`; Tehran `2026-10-24T19:07:59+03:30`. This is repository commit time, not the exact user-message time.
- Continue from NEXT-045; preserve earlier checkpoints.
