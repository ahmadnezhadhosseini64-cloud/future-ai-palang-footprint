# ورودی مستقل IN-019 — چرخهٔ زندهٔ درس‌ها و کل معماری

- Stable ID: PALANG-0.0-IN-20261023-019-LIVING-LESSON-CYCLE
- Production ID: IN-019
- Version: 1.0.0
- Date: 2026-10-23
- User input: درخواست چکش سخت؛ ساخت پوشهٔ درس‌های معماری؛ هر درس دائمی و عملیاتی باشد؛ تمام اجزای پروژه چرخهٔ پیوستهٔ رشد، آزمون، نسخه‌گذاری و بازیابی داشته باشند.
- Parent master: [CMIND](../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)
- Lesson registry: [ARCHITECTURE-LESSONS](../../architecture/ARCHITECTURE-LESSONS/README.md)
- Event: [EVT-0107](../../architecture/BEHAVIOR-TRACE/EVT-0107-LIVING-LESSON-CYCLE-AND-ROLLBACK-GOVERNANCE-2026-10-23.md)
- Status: REGISTERED; read-back pending.
- Exact user-message timestamp: NOT CAPTURED; commit time is not substituted for message time.

## Preserved intent
کاربر می‌خواهد هیچ درس یا تصمیم معماری فقط در گفتگو یا یک سند پراکنده نماند. هر درس باید به قاعدهٔ قابل‌اجرا، معیار آزمون، شاهد، وضعیت، اجزای متأثر و چرخهٔ بازنگری وصل شود. هر نسخهٔ تازه باید نسخهٔ قبلی را حفظ کند و در صورت شکست امکان بازگشت به آخرین baseline سالم وجود داشته باشد.

## Required architecture
DISCOVER → CAPTURE → CLASSIFY → REGISTER → READ-BACK → OPERATIONALIZE → TEST → VALIDATE → INTEGRATE → ACTIVATE → REASSESS → VERSION SUCCESSOR.
در شکست: حفظ نسخه و شواهد شکست → توقف ارتقا → انتخاب baseline سالم → بازیابی/شاخه‌سازی → آزمون‌های مرتبط → ثبت نتیجهٔ بازیابی.

## Limits
این ورودی، خواسته و معیار معماری را ثبت می‌کند؛ به‌تنهایی اثبات نمی‌کند که ثبت خودکار همهٔ پیام‌ها، اجرای خودکار همهٔ قواعد یا rollback سرتاسری پیاده‌سازی شده است.
