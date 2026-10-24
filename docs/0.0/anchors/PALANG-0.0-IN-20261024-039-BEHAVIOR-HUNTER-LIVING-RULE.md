# IN-039 — قاعدهٔ زندهٔ شکارچی رفتار و چرخهٔ شواهد
- Stable ID: G6IP-RAHM-IN-039-20261024
- Production ID: G6IP-IN-039
- Version: 1.0.0
- Status: REGISTERED pending read-back
- Parent checkpoint: [CURRENT-046](./PALANG-0.0-CURRENT-20261024-046-CAPABILITY-FALLBACK.md)
- Requested outcome: make the current interaction the next preserved Point 0; connect it to prior anchors and living mothers; set the next execution checkpoint to 0.0; keep unverified tasks open and actionable; bind the rule to چشم پلنگ / Behavior Hunter.

## Captured user intent
The user asks whether the assistant has inferred from repeated interaction that they want a durable, evidence-backed workflow rather than a mere summary. The actionable rule is:
> هر موردی که پیاده‌سازی و بازخوانی آن اثبات شده، وضعیت متناسب می‌گیرد؛ هر موردی که فقط تعریف یا مستند شده، به‌عنوان قابلیت فعال جا زده نمی‌شود؛ و هر آزمون انجام‌نشده یا ناموفق با شناسه، دلیل و گام بازیابی باز باقی می‌ماند.

## Behavior-hunter observations (not hidden-thought claims)
- Observable preference: preserve prior points, create a new linked anchor, maintain a living mother, and set the next step explicitly.
- Observable quality constraint: implementation, read-back, validation, integration, and runtime activation are different evidence gates.
- Observable error lesson: task drift (e.g., pursuing Dropbox while the active target is architecture continuation) must be logged as a recoverable routing error, not hidden or rationalized.
- Inference boundary: this is an evidence-based inference from explicit repeated instructions and observed corrections; it does not prove access to hidden thoughts, continuous background monitoring, or automatic capture outside this interaction.

## Required processing
Preserve → classify → assign IDs/version → create IN/OUT/event/current/next links → update living mothers and index/queue → write → fetch read-back → match identifiers/links → run only feasible tests → leave all remaining tests OPEN / NOT RUN with recovery steps.

## Acceptance
The rule becomes repository-registered only after post-write read-back. The Behavior Hunter is an architecture/process rule, not an always-running autonomous service unless a deployed runtime independently proves that behavior.

## Read-back receipt — CURRENT-047 registration cycle
- The file was fetched again after creation/update; Stable ID and core rule were present in returned content.
- Living-mother, Reference Index and integration-queue updates were each fetched after write; CURRENT-047 and NEXT-045 links and rule marker matched.
- Repository write/read-back verification is limited to these named paths. It does not validate JSON Schema, SHA-256, runtime deployment, persistent memory, idle background execution, or cross-host behavior.
- Canonical repository commit for the final cross-link update: `49bfeb2a64b808238c73c742fca9959703ccb464`, UTC `2026-10-24T15:37:59Z`, Tehran `2026-10-24T19:07:59+03:30`. This is the commit time, not the exact user-message time.
- Remaining gates continue OPEN / NOT RUN; resume from NEXT-045.
