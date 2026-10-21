# لنگر مستقل ۰.۰ — اصلاح قاعدهٔ زمان ثبت مخزن

- Stable ID / شناسهٔ پایدار: `REPOSITORY-TIME-ANCHOR-SIMPLIFICATION-0.0-2026-10-21-001`
- Production ID / شناسهٔ تولید: `RTAS0-2026-10-21-001`
- Version / نسخه: 1.0.0
- Project: Future AI / Palang Footprint / HAIF
- Owner: احمد پلنگ
- Parent reference: [سند مرجع ساده‌سازی زمان](../reference/REFERENCE-DOCUMENTS/REPOSITORY-TIME-ANCHOR-SIMPLIFICATION-LIVING-REFERENCE-2026-10-21-001.md)
- Event: [EVT-0077](../architecture/BEHAVIOR-TRACE/EVT-0077-REPOSITORY-TIME-SIMPLIFICATION-2026-10-21.md)
- Status: ACTIVE / LIVING RECOVERY ANCHOR; repository write + read-back content match verified.

## Resume point / نقطهٔ ادامه
ادامه از این تصمیم قطعی است: **زمان ثبت در مخزن معیار زمانی ثبت‌هاست؛ UTC مرجع اصلی است و معادل تهران از همان UTC محاسبه می‌شود.** زمان‌های دیگر در صورت داشتن شاهد و معنای مستقل حفظ می‌شوند، اما معیارهای موازی نمی‌سازند و برای همهٔ رکوردها اجباری نیستند.

## Why / دلیل
ثبت چندین زمان به‌عنوان معیارهای هم‌سطح، معماری را بی‌جهت پیچیده کرده و هنگام بستن شکاف‌ها ابهام ساخته است. راه‌حل، حذف تاریخچه نیست؛ تعیین یک معیار ساده برای ثبت مخزن و نگه‌داشتن زمان‌های دیگر فقط در نقش شواهد زمینه‌ای است.

## شاهد وضعیت / Status evidence
سند مرجع، رویداد، این لنگر، استاندارد حاکم و شاخص مرجع از مخزن دوباره خوانده شدند؛ شناسه‌ها و پیوندهای اصلی تطبیق داشتند. زمان دقیق عملیات بازخوانی ابزار در دسترس نیست و حدس زده نمی‌شود. مقصدهای خارج از مخزن هنوز تأیید نشده‌اند.

## Next actions / گام‌های بعد
1. سند مرجع و رویداد را از مخزن بازخوانی و تطبیق بده.
2. استاندارد حاکم و شاخص‌ها را با همین قاعده هم‌راستا کن؛ تاریخچه را حذف نکن.
3. ممیزی سراسری جفت‌های UTC/تهران را با شواهد خروجی اجرا و خطاهای واقعی را جداگانه اصلاح کن.
4. زمان commit واقعی این لنگر را از GitHub بگیر؛ UTC اول و تهران محاسبه‌شده دوم.
5. وضعیت Repository، Buffer و Persistent Memory را جدا نگه دار؛ موفقیت یک مقصد، اثبات مقصد دیگر نیست.

## Time integrity / سلامت زمان
- Contextual interaction time available: `2026-10-21T17:22:00Z` UTC = `2026-10-21T20:52:00+03:30` Asia/Tehran.
- This is not the repository registration timestamp.
- Exact user-message timestamp: `UNAVAILABLE / NOT CAPTURED`.
- Repository registration UTC/Tehran: fill only from actual commit metadata after write; never infer it from the contextual time.


## اصلاحیهٔ ادامه — لنگر مشترک زنجیره

ایدهٔ کاربر پذیرفته شد با این قید: یک رویداد چندفایلی باید یک لنگر نهایی زنجیره با UTC مرجع و یک بازهٔ ثبت داشته باشد؛ زمان واقعی هر فایل و زمان اولیهٔ معتبرش نیز حفظ می‌شود. زمان مشترک برای مرتب‌سازی و بازیابی کل بسته است، نه جایگزین timestamp هر فایل.

### ادامه از این نقطه
1. ثبت نهایی زنجیره را با یک رویداد مستقل ببند.
2. زمان commit هر جزء را از فرادادهٔ واقعی بگیر و به UTC + معادل تهران بنویس.
3. زمان شروع بازه = نخستین commit واقعی جزءهای بسته؛ زمان پایان/لنگر نهایی = commit رویداد نهایی‌کننده.
4. بعد از ایجاد لنگر نهایی، هر تغییر جدید با رویداد/نسخهٔ تازه ثبت شود؛ زمان قبلی بازنویسی نشود.
5. ممیزی همهٔ زمان‌های قدیمی و تبدیل جفت‌های UTC/تهران همچنان باز است؛ تاریخچه حذف نشود.


- رویداد تکمیل بازهٔ زنجیره: [EVT-0078](../architecture/BEHAVIOR-TRACE/EVT-0078-CHAIN-REGISTRATION-WINDOW-AND-CANONICAL-ANCHOR-2026-10-21.md).
