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