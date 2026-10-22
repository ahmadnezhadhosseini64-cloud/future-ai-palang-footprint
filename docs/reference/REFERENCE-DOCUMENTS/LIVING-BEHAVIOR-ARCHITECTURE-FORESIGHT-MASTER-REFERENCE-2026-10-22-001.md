# LBAF — سند مرجع مادر معماری رفتارشناسی زنده و آینده‌پژوهی

- Stable ID: PALANG-LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-GOVERNANCE-2026-10-22-001
- Production ID: HAIF-BEHAVIOR-FORESIGHT-GOVERNANCE-2026-10-22-001
- Master Reference ID: LBAF-MASTER-2026-10-22-001
- Version: 1.0.0
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Project: Future AI / Palang Footprint / HAIF
- Status: ACTIVE / LIVING / OPEN / EVOLVABLE / GOVERNING
- Policy: append-only; versioned growth; no silent replacement of the initial architecture.

## 1. هدف و دامنه
این سند مادر، پیوند رفتارشناسی تعامل، ثبت ورودی/خروجی، شواهد، اعتبارسنجی، بازیابی، آینده‌پژوهی و تکامل معماری را تعریف می‌کند. هر مدل/الگوی معماری جدید باید سند مادر مستقل، لنگر ۰.۰، رویداد، پابند زمانی و پیوند نسخه‌دار به این زنجیره داشته باشد.

## 2. نقطهٔ جاری و گام بعدی ۰.۰
- نقطهٔ جاری: [لنگر مستقل جاری](../../0.0/anchors/PALANG-0.0-CURRENT-LIVING-BEHAVIOR-ARCHITECTURE-2026-10-22-001.md).
- گام بعدی: [لنگر runtime collector و بازیابی تولیدی](../../0.0/anchors/PALANG-0.0-RUNTIME-COLLECTOR-PRODUCTION-RECOVERY-2026-10-22-001.md).
- رویداد حاکمیتی: [EVT-0088](../../architecture/BEHAVIOR-TRACE/EVT-0088-CURRENT-ANCHOR-LIVING-BEHAVIOR-ARCHITECTURE-AND-FUTURE-FORESIGHT-GOVERNANCE-2026-10-22.md).
- هیچ‌کدام لنگرهای قبلی را جایگزین نمی‌کنند.

## 3. اتصال معماری‌ها
- [FIOBAM — مدل رفتارشناسی اولین تعامل و نام‌گذاری ورودی/خروجی](./FIRST-INTERACTION-BEHAVIOR-ANALYSIS-AND-IO-NAMING-LIVING-REFERENCE-2026-10-22-001.md)
- [AOGM — رشد افزایشی و حاکمیت معماری](./APPEND-ONLY-ARCHITECTURE-GROWTH-MASTER-REFERENCE-2026-10-22-001.md)
- [ELVR — دفتر تعامل، schema و آزمون بازیابی](./EXECUTABLE-INTERACTION-LEDGER-VALIDATION-MASTER-REFERENCE-2026-10-22-001.md)
- [EVT-0087 — نتیجهٔ آزمون واقعی CI](../../architecture/BEHAVIOR-TRACE/EVT-0087-INTERACTION-VALIDATION-RECOVERY-RESULT-2026-10-22.md)
- [پابند زمانی ELVR](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-ELVR-2026-10-22-001.md)
- [معماری اولیهٔ رفتارشناسی](../../architecture/BEHAVIOR-SCIENCE-PALANG-FUTURE-AI/INTERACTIVE-BEHAVIOR-APP-ARCHITECTURE-INITIAL-2026-10-22-001.md)
- [CI run 39750440075](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39750440075)
- [Issue #20 — پیاده‌سازی runtime collector](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20)

## 4. چرخهٔ الزامی هر مدل جدید
OBSERVE → IDENTIFY → PRESERVE → CLASSIFY → PROVENANCE → MODEL → TEST → VALIDATE → RECONCILE → REGISTER → READ-BACK → VERIFY → CONNECT → RECOVER → LEARN → FORECAST → REVIEW → VERSIONED GROWTH.

هر مدل باید شناسهٔ پایدار، شناسهٔ تولید در صورت نیاز، نسخه، منشأ و دلیل ورود به معماری، شواهد، آزمون، وضعیت، محدودیت، GAP، زمان canonical، لنگر مستقل، سند مادر و پیوند به مدل‌های والد/هم‌خانواده داشته باشد.

## 5. نقشهٔ راه آینده‌پژوهی و آینده‌نگاری
این موارد نقشهٔ راه هستند و هنوز ادعای پیاده‌سازی‌شدن ندارند:
- پایش افق و پایش محیط؛
- روندها، پیشران‌ها، نشانه‌های ضعیف و مسائل نوظهور؛
- رخدادهای کم‌احتمال/پراثر؛
- سناریوهای پایه، جایگزین و گسست‌زا؛
- تحلیل علّی/ساختاری و حلقه‌های بازخورد؛
- پس‌نگری از آیندهٔ مطلوب، تحلیل پیامدها؛
- نشانه‌ها و شاخص‌های هشدار زودهنگام؛
- فرضیه‌های جایگزین، عدم‌قطعیت، کالیبراسیون و بازبینی پیش‌بینی.
هر پیش‌بینی باید فرض‌ها، بازهٔ زمانی، شواهد، عدم‌قطعیت و موعد بازبینی را جدا از واقعیت‌های مشاهده‌شده ثبت کند.

## 6. شواهد و وضعیت
- PASS: CI run 39750440075، اعتبارسنجی JSON Schema و بازیابی fixture ساختگی از IN و OUT در checkoutهای تازه.
- NOT PROVEN: جمع‌آورندهٔ runtime، cold-start سرویس تولیدی، ثبت خودکار همهٔ تعاملات و شکارچی دائماً فعال.
- GAP: اختلاف زمانی workflow بین updated_at=08:48:06Z و سابقهٔ قبلی 08:48:08Z؛ فیلد مستقل run_completed_at در پاسخ دریافت نشد.
- Library / Buffer / Persistent Memory / Dropbox: NOT VERIFIED.
- Gmail: NOT SENT / BLOCKED.

## 7. زمان و پذیرش
دستور کاربر در 2026-10-22 حدود 13:13 به وقت تهران مشاهده شد؛ دقت دقیقه‌ای و غیرهم‌ارز با زمان ثبت مخزن. زمان canonical باید از timestamp واقعی commit در UTC استخراج و زمان تهران از همان لحظه محاسبه شود. وضعیت پذیرش این ثبت تا بازخوانی و تطبیق فایل‌ها PENDING است.

## 8. گام اجرایی بعدی
از لنگر runtime collector و issue #20 ادامه بده؛ پیاده‌سازی مجاز و پایدار، آزمون خطا، cold-start واقعی، بازیابی از INT/IN/OUT، آشتی شواهد زمانی و سپس الحاق نسخه‌دار به معماری و این سند مادر. پس از هر نوشتن، READ-BACK → MATCH → VERIFY → RECONCILE → STATUS.

ACTIVE / LIVING / OPEN / EVOLVABLE / GOVERNING یعنی معماری و سند مادر قابل توسعه و بازیابی‌اند؛ نه اینکه عملیات پس‌زمینه یا مقصدهای خارجی بدون مدرک فعال باشند.


## پابند زمانی مادر
- [TIME-BINDING-LBAF-2026-10-22-001](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-LBAF-2026-10-22-001.md) — شواهد UTC/تهران برای commitهای این زنجیره.


## Universal per-interaction anchoring — UIOAM
- [UIOAM master reference](./UNIVERSAL-INPUT-OUTPUT-TEMPORAL-ANCHOR-MASTER-2026-10-22-001.md) — independent temporal and recovery anchors for every capturable input/output.
- [EVT-0089](../../architecture/BEHAVIOR-TRACE/EVT-0089-UNIVERSAL-INPUT-OUTPUT-ANCHORING-GOVERNANCE-2026-10-22.md).
- Current paired records: [IN-20261022-002](../../0.0/anchors/PALANG-0.0-IN-20261022-002-UNIVERSAL-IO-ANCHORING.md) and [OUT-20261022-002](../../0.0/anchors/PALANG-0.0-OUT-20261022-002-UNIVERSAL-IO-ANCHORING.md).
- [UIOAM timestamp binding](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-UIOAM-2026-10-22-001.md).
- Runtime capture is not considered active until implemented and independently tested.


## PIAL — پابند مستقل هر ورودی و خروجی
- [سند مرجع مادر PIAL](./PER-INTERACTION-IN-OUT-TEMPORAL-ANCHOR-LIVING-MASTER-REFERENCE-2026-10-22-001.md)
- [پابند زمانی PIAL](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-PIAL-2026-10-22-001.md)
- [EVT-0089](../../architecture/BEHAVIOR-TRACE/EVT-0089-EVERY-INTERACTION-IN-OUT-TEMPORAL-ANCHOR-AND-RECOVERY-GOVERNANCE-2026-10-22.md)


## Addendum v1.0.1 — Current continuation guard and model-initial path
- Continuation master: [CMIND](./CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md).
- Event: [EVT-0091](../../architecture/BEHAVIOR-TRACE/EVT-0091-CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-2026-10-22.md).
- Interaction pair: `INT-20261022-005`; anchors [IN](../../0.0/anchors/PALANG-0.0-IN-20261022-005-CONTINUE-MODEL-INITIAL.md) / [OUT](../../0.0/anchors/PALANG-0.0-OUT-20261022-005-CONTINUE-MODEL-INITIAL.md).
- Rule: classify each candidate continuation as ACTIVE TARGET, PARALLEL BACKLOG, or INDEPENDENT WAITING BRANCH before executing. An unresolved branch such as Dropbox must not displace the user-directed model-initial continuation.
- Current active implementation target remains Issue #20: authorized interaction-pair runtime, stable INT/IN/OUT lookup, durable local storage, idempotency, hash-verified read-back, and restart recovery tests.
- This addendum records governance and routing only; it does not claim runtime pair-ledger implementation or production automatic capture has been completed.


---

## Addendum v1.0.1 — دروازهٔ کشف رفتار و جلوگیری از منفی کاذب

- Trigger: user identified that the previous assistant outputs contained important architectural rules that were not fully harvested into evidence-backed candidates, open gaps and next actions.
- Canonical event: [EVT-0103](../../architecture/BEHAVIOR-TRACE/EVT-0103-BEHAVIOR-HUNTER-MISSED-DETECTION-AND-ID-COLLISION-CORRECTION-2026-10-22.md).
- Inbox: [INBOX-20261022-002](../../architecture/LIVE-INBOX/entries/INBOX-20261022-002.md).
- Runtime gap: [Issue #20](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20).

### New required behavior-hunter gate
Before finalizing a materially project-related response, inspect the visible user input and assistant output for: architectural rules, repeated patterns, user feedback, observed errors, contradictions, missing evidence, open gaps, new components and actionable next steps. Each candidate is labelled OBSERVATION, INFERENCE, HYPOTHESIS or UNKNOWN and linked to the exact visible evidence. Then perform identifier uniqueness checks, connect accepted findings to the living inbox, parent master, relevant component and implementation queue, and verify links by read-back.

### Dual-track architecture
- Track A — Interaction capture: INT/IN/OUT, provenance, UTC repository registration time and Tehran equivalent, EVT, inbox, parent master and read-back.
- Track B — Behavioral discovery: candidate extraction from both input and output, classification, evidence, review, model/gap/action linkage, and versioned growth.

### Failure evidence
The prior workflow missed architectural candidates and reused EVT-0093 despite a pre-existing EVT-0093 event. The collision is documented, not concealed; the legacy colliding file now points to canonical EVT-0103. This shows the uniqueness rule existed in architecture but was not enforced as an effective pre-write gate in that operation.

### Boundary
This is a workflow/control definition plus repository evidence, not proof of an always-on background hunter. Runtime collection, candidate extraction, permission boundary, durable storage and cold-start recovery remain OPEN / NOT PROVEN until implemented and independently tested under Issue #20.


---

## Addendum v1.0.1 — دروازهٔ کشف رفتار و جلوگیری از منفی کاذب

- Canonical event: [EVT-0103](../../architecture/BEHAVIOR-TRACE/EVT-0103-BEHAVIOR-HUNTER-MISSED-DETECTION-AND-ID-COLLISION-CORRECTION-2026-10-22.md).
- Inbox: [INBOX-20261022-002](../../architecture/LIVE-INBOX/entries/INBOX-20261022-002.md).
- Runtime gap: [Issue #20](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20).

### New required behavior-hunter gate
Before finalizing a materially project-related response, inspect the visible user input and assistant output for architectural rules, repeated patterns, user feedback, observed errors, contradictions, missing evidence, open gaps, new components and actionable next steps. Each candidate is labelled OBSERVATION, INFERENCE, HYPOTHESIS or UNKNOWN and linked to the exact visible evidence. Then perform identifier uniqueness checks, connect accepted findings to the living inbox, parent master, relevant component and implementation queue, and verify links by read-back.

### Dual-track architecture
- Track A — Interaction capture: INT/IN/OUT, provenance, UTC repository registration time and Tehran equivalent, EVT, inbox, parent master and read-back.
- Track B — Behavioral discovery: candidate extraction from both input and output, classification, evidence, review, model/gap/action linkage, and versioned growth.

### Failure evidence
The prior workflow missed architectural candidates and reused EVT-0093 despite a pre-existing EVT-0093 event. The collision is documented, not concealed; the legacy colliding file now points to canonical EVT-0103. This shows the uniqueness rule existed in architecture but was not enforced as an effective pre-write gate in that operation.

### Boundary
This is a workflow/control definition plus repository evidence, not proof of an always-on background hunter. Runtime collection, candidate extraction, permission boundary, durable storage and cold-start recovery remain OPEN / NOT PROVEN until implemented and independently tested under Issue #20.

- Time binding for this corrective interaction: [TIME-BINDING-INT-20261022-015](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-INT-20261022-015.md). Repository commit time is not the user-message timestamp.


## Addendum v1.0.2 — شش کاندید صریح و دروازهٔ شکارچی

- Event: [EVT-0104](../../architecture/BEHAVIOR-TRACE/EVT-0104-CANDIDATE-ARCHITECTURE-SIGNALS-AND-HUNTER-GATE-2026-10-22.md).
- Inbox: [INBOX-20261022-003](../../architecture/LIVE-INBOX/entries/INBOX-20261022-003.md).
- Anchors: [IN-016](../../0.0/anchors/PALANG-0.0-IN-20261022-016-EXPLICIT-CANDIDATE-SIGNALS.md) / [OUT-016](../../0.0/anchors/PALANG-0.0-OUT-20261022-016-EXPLICIT-CANDIDATE-SIGNALS.md).

### Required candidate gate
برای هر ورودی و خروجی قابل‌مشاهده، شکارچی باید کاندیدهای معماری را استخراج کند، شاهد دقیق را حفظ کند، OBSERVATION / INFERENCE / HYPOTHESIS / UNKNOWN را از هم جدا کند، یکتایی شناسه را پیش از نوشتن کنترل کند و یافته‌های پذیرفته‌شده را به صندوق زنده، سند مادر کل، سند جزء و صف اقدام وصل کند. پس از نوشتن، بازخوانی و تطبیق پیوندها لازم است.

شش کاندید جاری در EVT-0104 آمده‌اند. علت شکست قبلی فقط فرضیه است، نه علت ریشه‌ای اثبات‌شده. شکارچی خودکار، capture میزبان و بازیابی سرد همچنان OPEN / NOT PROVEN در Issue #20 هستند.
