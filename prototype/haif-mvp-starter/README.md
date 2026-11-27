# HAIF MVP Host Starter 0.1.0

این بسته برای یک کار مشخص ساخته شده است: **یک پیام ورود + یک هستهٔ اجرایی کوچک + روش آزمون + مسیر تحویل خروجی**.

## محتویات
- `ONE_MESSAGE_HOST_ENTRY_FA.md`: پیام واحدی که برای میزبان تازه فرستاده می‌شود.
- `manifest.json`: هویت بسته، نسخه، فایل‌های اصلی و محدودیت‌ها.
- `../../scripts/haif-runtime/`: هستهٔ محلی MVP و آزمون‌های آن (در مخزن مرجع).
- `../../docs/architecture/HAIF-MVP-CANONICAL-IMPLEMENTATION-DECISION-2026-11-23.md`: تصمیم انتخاب یک هسته.
- `../../docs/architecture/HAIF-MVP-OPEN-WORK-CHECKLIST.md`: چک‌لیست زندهٔ کارها.

## شروع سریع برای میزبان
1. پیام `ONE_MESSAGE_HOST_ENTRY_FA.md` را کامل بخوان و اجرا کن.
2. ابتدا main و سپس شاخهٔ candidate را با SHA دقیق بازیابی کن.
3. اگر Python 3.10+ داری، در checkout مستقل اجرا کن:

```bash
python -m unittest discover -s scripts/haif-runtime/tests -v
python scripts/haif-runtime/haif_runtime.py --help
```

4. برای آزمون محلی مصنوعی، فقط در فضای خصوصی خودت:

```bash
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json init
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json record --input "synthetic input" --output "synthetic output"
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json verify
python scripts/haif-runtime/haif_runtime.py --state ./haif-state.json export
```

5. فایل وضعیت مصنوعی را به‌عنوان دادهٔ واقعی کاربر یا حافظهٔ خودکار معرفی نکن.

## محدودیت‌های فعلی
- این runtime فقط هستهٔ محلی است؛ اتصال مستقیم به رابط ChatGPT یا سایر میزبان‌ها پیاده‌سازی نشده.
- ثبت خودکار ورودی/خروجی، ذخیره‌سازی ابری، همگام‌سازی چندمیزبانی و بازیابی مستقل پس از restart باید جداگانه اثبات شوند.
- قبولی تست کد، اثبات اجرای میزبان مستقل نیست.
- بسته و این شاخه تا ادغام کنترل‌شده و read-back مالک، candidate هستند؛ main را تغییر نمی‌دهند.

## ساخت بستهٔ ZIP
Workflow با نام `HAIF MVP Host Starter Package` از همین شاخه اجرا می‌شود و ZIP را به‌عنوان GitHub Actions artifact منتشر می‌کند. artifact خروجی build است؛ release پایدار یا تأیید میزبان مستقل محسوب نمی‌شود.
