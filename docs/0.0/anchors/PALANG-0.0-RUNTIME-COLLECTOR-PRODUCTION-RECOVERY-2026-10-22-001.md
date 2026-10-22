# لنگر مستقل ۰.۰ — گام بعدی: شکارچی runtime و بازیابی تولیدی

- Anchor ID: PALANG-0.0-RUNTIME-COLLECTOR-PRODUCTION-RECOVERY-2026-10-22-001
- Stable ID: PALANG-RUNTIME-COLLECTOR-PRODUCTION-RECOVERY-2026-10-22-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / NEXT

## هدف
پیاده‌سازی جمع‌آورندهٔ مجاز تعاملات (runtime collector) و دفتر پایدار؛ سپس اجرای آزمون cold-start واقعی و بازیابی مستقل از شناسه‌های INT/IN/OUT.

## ترتیب اجرا
1. بازخوانی issue #20 و قراردادهای دسترسی و حریم خصوصی.
2. تعیین دقیق داده‌های مجاز برای ثبت؛ ادعای ثبت خودکار تعاملات میزبان بدون اتصال و مجوز واقعی ممنوع.
3. پیاده‌سازی ثبت رویدادهای ورودی/خروجی، شناسه‌های هم‌ردیف، منشأ، نسخه، خطا و وضعیت.
4. ذخیرهٔ پایدار و idempotent؛ جلوگیری از رکورد تکراری هنگام retry.
5. آزمون schema، واحد، یکپارچه‌سازی و خطاهای رکورد گم‌شده/تکراری/خراب/زمان نامعلوم.
6. اجرای cold-start در محیط تازه از دادهٔ واقعاً ذخیره‌شده، نه صرفاً fixture ساختگی.
7. بازیابی جداگانه از INT و IN و OUT؛ تطبیق با شواهد، رویداد، نسخهٔ معماری و GAPها.
8. ثبت timestamp واقعی commit در UTC به‌عنوان زمان canonical مخزن و معادل تهران از همان instant؛ زمان اجرا/API جدا بماند.
9. ثبت نتیجه در رویداد جدید، سند مادر و پابند زمانی؛ الحاق افزایشی به معماری و نمایه‌ها.
10. WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS.

## معیار پذیرش
آزمون در محیط تازه و بدون حافظهٔ همان فرایند موفق شود؛ شناسه‌ها به دادهٔ پایدار و شواهد واقعی برسند؛ شکست‌ها و GAPها صریح ثبت شوند؛ هیچ ادعایی فراتر از مدرک مطرح نشود.

- مدرک پیشین: [EVT-0087](../../architecture/BEHAVIOR-TRACE/EVT-0087-INTERACTION-VALIDATION-RECOVERY-RESULT-2026-10-22.md)
- CI: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39750440075
- Issue #20: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20
- سند مادر: [LBAF](../../reference/REFERENCE-DOCUMENTS/LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-MASTER-REFERENCE-2026-10-22-001.md)

این لنگر خودِ پیاده‌سازی نیست؛ وضعیت runtime collector و cold-start تا اجرای مستقل OPEN / NOT VERIFIED است.
