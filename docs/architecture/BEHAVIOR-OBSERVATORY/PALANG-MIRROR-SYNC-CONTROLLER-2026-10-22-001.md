# کنترل‌گر همگام‌سازی زندهٔ آینه — Future AI / Palang Footprint

## شناسنامه
- Stable ID: PALANG-MIRROR-SYNC-CONTROLLER-2026-10-22-001
- Production ID: PMS-HAIF-2026-10-22-001
- Version: 1.0.0
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Project: Future AI / Palang Footprint / HAIF
- Project anchor location: گنبد کاووس، ایران
- Status: ACTIVE / LIVING — همگام‌سازی روزانه زمان‌بندی شده است؛ هر اجرا باید شواهد مستقل تولید کند.
- Canonical source: `docs/architecture/BEHAVIOR-OBSERVATORY/LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001.md`
- Mirror: `/Future AI/Palang Footprint/Master Reference Vault/Reference Documents/LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001.md`
- Daily automation ID: `6ad9a407b9d481919c7145fbe4638dec`
- Automation title: `Palang Mirror Sync`
- Schedule: daily, flexible timing, timezone `Asia/Tehran`; enabled state confirmed at creation.
- Time rule: repository commit UTC is canonical; Tehran time must be derived from that same instant. Do not invent execution/read-back timestamps.

## هدف و دامنه
این کنترل‌گر آینهٔ مشخصِ آزمون پایداری مقصدها را با سند مرجع مخزن همگام نگه می‌دارد. مخزن GitHub منبع مرجع اصلی است. کتابخانه یک آینهٔ مستقل است، نه جایگزین مخزن. فعال بودن زمان‌بندی به معنی موفقیت خودکار همهٔ مقصدها نیست؛ هر اجرا باید نوشتن، بازخوانی، تطبیق و نتیجه را جداگانه ثبت کند.

## گردش‌کار هر اجرا
1. PRESERVE: نسخهٔ قبلی و لنگرهای ۰.۰ را حفظ کن؛ هیچ لنگر قدیمی را بازنویسی یا حذف نکن.
2. READ SOURCE: فایل مرجع را از مسیر canonical بخوان و SHA/نسخه/شناسه‌اش را ثبت کن.
3. READ MIRROR: آینهٔ Library را از مسیر دقیق بخوان.
4. COMPARE: Stable ID، Version، بخش‌های مقصدها، گام بعدی، و محتوای کامل را مقایسه کن.
5. WRITE IF NEEDED: اگر متفاوت است، آینه را از نسخهٔ فعلی مرجع به‌روزرسانی کن؛ اگر برابر است، عدم نیاز به نوشتن را ثبت کن.
6. READ-BACK: آینه را پس از نوشتن دوباره بخوان.
7. MATCH / VERIFY: برابری محتوا یا تفاوت‌های مجاز و دقیق را ثبت کن. فقط اگر شواهد موجود است PASS بده.
8. REGISTER EVENT: رویداد مستقل در `docs/architecture/BEHAVIOR-TRACE/` ثبت کن؛ زمان commit واقعی UTC و تبدیل تهران را درج کن.
9. RECONCILE INDEX: نمایهٔ رصدخانه و صف یکپارچه‌سازی را به رویداد جدید پیوند بده.
10. STATUS: وضعیت هر مقصد را جداگانه نگه دار. موفقیت Repository یا Library، Buffer/Persistent Memory/Dropbox را تأیید نمی‌کند.

## وضعیت فعلی مقصدها
- Repository: ثبت و بازخوانی برای آزمون و کنترل‌گر، باید پس از هر commit با read-back تأیید شود.
- Library mirror: یک فایل آزمون مشخص در مسیر بالا بازنویسی شد؛ read-back مستقل پس از این آخرین بازنویسی باید تأیید شود.
- Buffer: NOT VERIFIED.
- Persistent Memory: NOT VERIFIED.
- Dropbox: OPEN / NOT VERIFIED؛ اتصال، نوشتن و بازیابی واقعی هنوز انجام نشده.
- External end-to-end recovery: NOT RUN.

## معیارهای پذیرش
- M1: منبع مرجع خوانده شده — PASS فقط با شاهد ابزار.
- M2: آینهٔ Library خوانده شده — PASS فقط با شاهد ابزار.
- M3: اختلاف‌ها تطبیق و در صورت نیاز اصلاح شده — PASS فقط با read-back.
- M4: Stable ID / Version / next action / destination status مطابق‌اند — PASS فقط پس از مقایسه.
- M5: رویداد و زمان commit واقعی ثبت شده — PASS فقط پس از خواندن commit.
- M6: سایر مقصدها مستقلاً آزموده شده‌اند — OPEN تا زمانی که آزمون مستقل هر مقصد موفق شود.

## قواعد عدم ادعای کاذب
- `WRITE ≠ READ-BACK`; نوشتن به‌تنهایی اثبات بازیابی نیست.
- `FOUND ≠ RETRIEVED ≠ VALIDATED ≠ REVIVED ≠ VERIFIED ≠ ACTIVE`.
- `ACTIVE / LIVING` یعنی پیگیری و کنترل‌گر فعال‌اند؛ به معنی تأیید همهٔ مقصدها نیست.
- اگر ابزار یا مجوز مانع شد، مانع دقیق را ثبت کن و مقصد را `NOT VERIFIED` نگه دار.
- زمان اجرای اتوماسیون تا وقتی خروجی واقعی ندهد، زمان‌بندی‌شده است، نه اجراشده.
