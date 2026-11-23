# پیاده‌سازی RAHM WOMB و اتصال به مدل واقعی

- شناسه: RAHM-WOMB-MODEL-ENGINE-2026-11-24-001
- ریشه: POINT-0/GOLDEN
- صف: NEXT-051
- مالک: احمد نژادحسینی
- وضعیت: CODE-IMPLEMENTED / CI-TESTS-PASSED / LIVE-MODEL-NOT-CONFIGURED

## تفکیک اجزا
1. RAHM WOMB: چرخهٔ استدلال و اعتبارسنجی مدل‌یار؛ کد در scripts/rahm-womb/.
2. RAHM Evidence Ledger: دفتر قطعی ثبت رویداد و digest در scripts/rahm-runtime/؛ مدل زبانی نیست.
3. Model Provider: آداپتور قابل‌تعویض برای API سازگار با OpenAI Chat Completions. این کد وزن‌های یک مدل را آموزش یا ایجاد نمی‌کند؛ مدل واقعی از سرویس‌دهندهٔ انتخابی فراخوانی می‌شود.

## چرخه
OWNER-CURATED TASK + SAFE CONTEXT → RAHM WOMB → CONFIGURED MODEL → STRUCTURED RESULT → OWNER REVIEW → INDEPENDENT VALIDATION → EVIDENCE LEDGER

موتور فقط متن صریحاً تحویلی را می‌بیند؛ به مخزن، فایل‌های دیگر، shell، Git، وب یا ابزار عملیاتی دسترسی ندارد. خروجی مدل اجرا نمی‌شود و مسیر نوشتن به MASTER وجود ندارد.

## تنظیم اتصال
متغیرهای محیطی:
- RAHM_MODEL_BASE_URL: نشانی پایهٔ API سازگار با Chat Completions
- RAHM_MODEL_API_KEY: کلید؛ فقط در محیط اجرا یا secret store، هرگز در Git
- RAHM_MODEL_NAME: شناسهٔ مدل در سرویس انتخابی

نمونه:
```bash
export RAHM_MODEL_BASE_URL="https://provider.example/v1"
export RAHM_MODEL_API_KEY="(set outside the repository)"
export RAHM_MODEL_NAME="(provider model identifier)"
python scripts/rahm-womb/rahm_womb.py --task "Audit the supplied proposal"
```

هیچ endpoint، مدل، کلید یا حسابی از طرف مالک پیکربندی نشده است؛ بنابراین inference زنده در این تغییر ادعا نمی‌شود. آزمون HTTP محلی فقط قرارداد درخواست و پاسخ را بررسی می‌کند، نه توان استدلال مدل واقعی.

## حفاظ‌ها
- پیکربندی ناقص، درخواست را متوقف می‌کند.
- HTTP غیررمزگذاری‌شده فقط برای localhost مجاز است.
- هیچ ابزار یا function calling به مدل داده نمی‌شود.
- سقف task برابر ۱۲هزار و context برابر ۴۰هزار نویسه است.
- خروجی باید JSON معتبر با schema ثابت باشد.
- هر نتیجه OWNER_REVIEW_REQUIRED و master_written=false است.
- ورودی‌ها دادهٔ غیرقابل‌اعتمادند؛ خروجی مدل هرگز خودکار اجرا یا ادغام نمی‌شود.

## معیار LIVE-MODEL-VERIFIED
مالک باید endpoint و مدل واقعی را انتخاب و secret را خارج از مخزن تنظیم کند؛ سپس اجرای بی‌خطر واقعی، ثبت نام مدل و digest بدون secret، اعتبارسنجی ساختار پاسخ و read-back مستقل باید موفق باشد. تا آن زمان وضعیت LIVE-MODEL-NOT-CONFIGURED باقی می‌ماند.

## اصل نظارتی Palang Control
در هر نشست مجاز، Palang Control مرجع طلایی و مخزن را بازیابی می‌کند، ادعا را از شاهد جدا می‌کند، میزبان را از هسته دور نگه می‌دارد، خروجی را قرنطینه و ممیزی می‌کند، تست و read-back می‌خواهد و بدون دو تأیید مستقل مالک هیچ تغییری را در CHILD پذیرفته‌شده یا MASTER نهایی نمی‌کند. این تعهد، نگهبانی ۲۴ساعته یا پس‌زمینه نیست؛ برای آن سرویس مستقل و آزموده‌شده لازم است.


## شواهد CI در شاخهٔ پیشنهادی
- Commit آزموده‌شده: `b2bc69087635fbfa6538990557855ee905ff25ac`
- اجرای RAHM Runtime Tests: `45270680392` — `completed / success`
- اجرای Living Architecture Audit: `45270680320` — `completed / success`
- در اجرای RAHM Runtime Tests، گام‌های HAIF Runtime، RAHM Runtime، RAHM WOMB و Host Bridge همگی `success` شدند.
- این شواهد، آزمون کد و قرارداد HTTP محلی را اثبات می‌کند؛ اجرای inference با مدل واقعی را اثبات نمی‌کند.
