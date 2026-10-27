# CURRENT-101 — ادامهٔ 0.0: رشد مدل در میزبان و چرخهٔ بازگشت به مخزن

- Stable ID: HAIF-CURRENT-101-HOST-GROWTH-REPOSITORY-LOOP-20261027
- Production ID: G6IP-CURRENT-101
- Version: 1.0.0
- Status: ACTIVE / LIVING / SOURCE CHANGES REGISTERED / PACKAGE BUILD PENDING / LIVE HOST OPEN
- Chain: POINT-0/051 (0+ marker on canonical root 0) → IN-089 → OUT-088 → EVT-0226 → CURRENT-101 → NEXT-051
- Previous verified checkpoint: [CURRENT-100](./PALANG-0.0-CURRENT-20261027-100-DEEP-AUDIT-FIRST-HOST.md)
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Package source: [HAIF GPT-6 Portable Starter](../../../prototype/haif-gpt6-starter/README.md)
- Host growth contract: [HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md](../../../prototype/haif-gpt6-starter/HOST_GROWTH_AND_REPOSITORY_SYNC_CONTRACT.md)
- First-host checklist: [FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md](../../../prototype/haif-gpt6-starter/FIRST_HOST_GPT6_ACCEPTANCE_CHECKLIST.md)
- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## هدف معماری
همان بستهٔ اولیه باید بارها به‌روزرسانی شود؛ هویت پایدار و نام ZIP ثابت بماند، نسخهٔ داخلی و هش هر ساخت تغییر کند، و هر نسخه پس از ساخت/بازخوانی به میزبان منتقل شود. میزبان، تعامل‌های مرتبط را با منشأ و شواهد ثبت می‌کند؛ دادهٔ ارزشمند ابتدا پیشنهاد/Child می‌شود و تنها پس از RAHM validation و مجوز روشن به Master راه می‌یابد.

## وضعیت اجرا
- [x] نقطهٔ 0+ به‌عنوان نشانگر تولید روی ریشهٔ canonical 0 تعریف شد؛ ریشهٔ دوم ساخته نشد.
- [x] زنجیرهٔ 0.0 مستقل و متصل ساخته شد: IN-089 → OUT-088 → EVT-0226 → CURRENT-101 → NEXT-051.
- [x] قرارداد رشد میزبان و بازگشت کنترل‌شده به مخزن به منبع همان starter package اضافه شد.
- [x] هویت بسته و نام ZIP اصلی حفظ می‌شوند؛ نسخهٔ داخلی منبع 0.3.6 است.
- [x] گردش‌کار ساخت ZIP اصلی برای واردکردن قرارداد و اجرای آزمون از نسخهٔ استخراج‌شده تنظیم شد.
- [ ] اجرای تازهٔ CI روی commit نهایی، هش/بایت ZIP، آزمون‌های استخراج‌شده و بازخوانی artifact.
- [ ] واردسازی در میزبان GPT واقعی و رسید مستقیم بازیابی.
- [ ] تولید زندهٔ رویداد مصنوعی، اتصال مجاز به GitHub، نوشتن و read-back دقیق.
- [ ] آزمون دادهٔ نامعتبر، replay متعارض، حذف فایل، تغییر یک بایت و restart.
- [ ] اثبات ثبت زندهٔ تعامل‌ها و persistence بین نشست‌ها.

## گیت‌های باز
CI موفق ≠ میزبان مستقل پذیرفته‌شده. فایل دستورالعمل یا ZIP به‌تنهایی hook زندهٔ ChatGPT نمی‌سازد. اگر میزبان واقعی ابزار اتصال مجاز نداشته باشد، مسیر جایگزین export/import دستی است و همگام‌سازی خودکار باید NOT SUPPORTED / NOT VERIFIED بماند.

NEXT-051 تنها صف فعال است؛ NEXT-052 ساخته نشود.
