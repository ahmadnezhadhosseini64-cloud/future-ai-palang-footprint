# EVT-0201 — MASTER / RAHM / CHILD و آزمون محیط تعاملی

- Event ID: EVT-0201
- Stable ID: `HAIF-EVT-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION-20261026-0201`
- Production ID: `EVT-0201`
- Version: 1.0.0
- Status: REGISTERED / READ-BACK REQUIRED / OPEN
- Root: [POINT-0/032](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261026-032-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION.md)
- IN: [IN-067](../../0.0/anchors/PALANG-0.0-IN-20261026-067-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION.md)
- OUT: [OUT-066](../../0.0/anchors/PALANG-0.0-OUT-20261026-066-MASTER-RAHM-CHILD-INTERACTIVE-VERIFICATION.md)
- Previous event: [EVT-0200](./EVT-0200-REVERSIBLE-GRAPH-GAP-COVERS-AND-BEHAVIOR-HUNTER-2026-10-26.md)
- Active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## مشاهده
کاربر نقش پروژهٔ اصلی را MASTER، مدل اولیه/پروژهٔ جدید را RAHM و نسخهٔ آزموده را CHILD تعریف کرد. هدف برقرارکردن رابطهٔ قابل‌آزمون بین معماری و محیط تعاملی است، نه صرفاً تولید سند.

## اقدام
مدل اولیه و بستهٔ RAHM موجود از مخزن بازخوانی شدند. قرارداد پذیرش و معیارهای آزمون مستقل به POINT-0/032 افزوده شدند. گیت‌های گراف تاریخی و میزبان مستقل OPEN می‌مانند. این رویداد به معنی اجرای آزمون در رابط پروژهٔ تعاملی نیست.

## شواهد و محدودیت
مخزن `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`، شاخهٔ `main`. پیش از زنجیرهٔ جدید، HEAD مشاهده‌شده `2e5cf4bf4a881fed2509acf3c3f15ce685c1cb40` با زمان `2026-10-26T08:15:44Z` بود. فایل‌های مدل اولیه، صف آن، RAHM_BOOT، manifest و سند مادر قابل‌خواندن بودند. ممیزی دقیق SHA نهایی، واردسازی مستقل، بازیابی پس از restart و مقصدهای بیرونی تا رسید مستقیم NOT VERIFIED هستند.

هر واگرایی در شناسه‌ها، یال‌های والد، تاریخچه، hash شواهد، شکاف‌های باز یا اقدام بعدی باید شکاف مربوط را باز نگه دارد. ادغام گروهی یا انتخاب والد بر اساس حدس مجاز نیست.

> **CONFLICTED EVENT-NUMBER COLLISION / NON-CANONICAL.** A competing EVT-0201 exists at [EVT-0201 Master–Rahm–Child bridge](./EVT-0201-MASTER-RAHM-CHILD-BRIDGE-AND-INITIAL-MODEL-VALIDATION-2026-10-26.md), linked by the canonical POINT-0/032 chain. Preserve both event files until lineage and inbound/outbound references are audited. Do not infer equivalence or delete either file.