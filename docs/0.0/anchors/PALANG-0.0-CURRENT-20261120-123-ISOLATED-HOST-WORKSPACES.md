# CURRENT-123 — محیط‌های کاری مستقل و محصور میزبان‌ها

- Status: ACTIVE / LIVING / GOVERNANCE DESIGN REGISTERED / IMPLEMENTATION PARTIAL
- Parent checkpoint: CURRENT-122
- Previous point: POINT-0/069
- Current point: POINT-0/070 (0+)
- Input/output: IN-113 → OUT-112
- Event/time: EVT-0288 → TIME-BINDING-EVT-0288
- Living master: سند مرجع مادر مدل اولیه هوش مصنوعی, version 1.7.75
- Governing multi-host architecture: version 1.1.0
- Workspace model: docs/architecture/HOST-WORKSPACES/
- Host Registry: intentionally empty until a real host passes identity and acceptance
- Sole execution queue: NEXT-051
- Repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## ثبت و نتیجه
- POINT-0/070، IN-113، OUT-112 و EVT-0288 در مخزن ثبت شدند.
- ساختار مستقل workspace، الگوی منشور میزبان و پروتکل جداسازی/ارتقا ثبت شدند.
- سند مادر به 1.7.75 و معماری چندمیزبانی به 1.1.0 append-only ارتقا یافت.
- هر میزبان در صورت پذیرش واقعی باید Host ID، Workspace ID و Session ID مستعار داشته باشد و فقط در محدوده اختصاصی خود کار کند.
- میزبان‌ها فقط snapshot نسخه‌پین‌شدهٔ MASTER را می‌خوانند؛ پیشنهادها از broker احراز هویت‌شده به قرنطینه می‌روند.
- فقط نتیجهٔ معتبر، قابل بازتولید و مفید پس از RAHM و تأیید صریح مالک به سند مادر و همان ZIP canonical افزوده می‌شود.
- مسیر و لینک‌های معماری workspace در README مخزن ثبت شدند.

## زنجیره
POINT-0/066 → CURRENT-119 → POINT-0/067 → IN-110 → OUT-109 → EVT-0285 → TIME-BINDING-EVT-0285 → CURRENT-120 → POINT-0/068 → IN-111 → OUT-110 → EVT-0286 → TIME-BINDING-EVT-0286 → CURRENT-121 → POINT-0/069 → IN-112 → OUT-111 → EVT-0287 → TIME-BINDING-EVT-0287 → CURRENT-122 → POINT-0/070 → IN-113 → OUT-112 → EVT-0288 → TIME-BINDING-EVT-0288 → CURRENT-123 → NEXT-051.

## وضعیت اثبات
- Workspace architecture/templates: REGISTERED.
- Actual host identity/registration/provisioning: NOT RUN / NO ACTIVE HOST.
- Broker deployment and authenticated host-scoped path allowlist: OPEN.
- GitHub least-privilege credential isolation and branch protection: OPEN / NOT VERIFIED.
- Negative cross-workspace and MASTER access tests: OPEN / NOT RUN.
- Live host IN/OUT read-back receipt: OPEN / NOT RUN.
- Clean independent-host recovery: OPEN / NOT RUN.
- ZIP refresh for this exact main revision: PENDING workflow and release read-back.

## مرز امنیتی
پوشه‌بندی در GitHub به‌تنهایی مرز امنیتی نیست؛ میزبان نباید credential نوشتن مستقیم مخزن بگیرد. تا استقرار broker، allowlist مسیر، credential حداقلی، branch protection و آزمون منفی جداسازی، اتصال نوشتنی میزبان واقعی مجاز نیست. اگر این مرز در یک مخزن قابل تضمین نباشد، از repo/sandbox جدا استفاده می‌شود.

## لنگر زمانی
- CURRENT-123 creation commit SHA: `32b86a9f05e7508a5a2c6672958780bbbc07ced3`
- Commit UTC: `2026-11-20T18:14:17Z`
- Tehran: `2026-11-20T21:44:17+03:30`
- Timestamp source: GitHub commit metadata read-back; user-message time remains UNKNOWN / UNVERIFIED
- Exact user message timestamp: UNKNOWN / UNVERIFIED

NEXT-051 remains the sole active execution queue. No parallel root or queue is created.
