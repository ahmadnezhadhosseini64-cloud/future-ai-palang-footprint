# EVT-0076 — زمان ثبت مخزن معیار واحد برای هر ثبت

- Stable ID / شناسهٔ پایدار: `EVT-0076-REPOSITORY-REGISTRATION-TIME-IS-CANONICAL-2026-10-21`
- Production ID / شناسهٔ تولید: `EVT-TS-CANON-2026-10-21-001`
- Version / نسخه: 1.0.0
- Project / پروژه: Future AI / Palang Footprint / HAIF
- Owner / مالک: احمد پلنگ
- Parent / والد: EVT-0075-ASSISTANT-OUTPUT-TIMESTAMP-SEMANTIC-AUDIT-AND-HOST-ADAPTER-2026-10-21
- Governing standard / استاندارد حاکم: ASSISTANT-TIMESTAMP-ANCHOR-STANDARD-2026-10-21-001
- Status / وضعیت: ACTIVE / LIVING / REPOSITORY-REGISTERED
- Event meaning / معنای رویداد: اصلاح قاعدهٔ زمان؛ هر فایل/رویداد ثبت‌شده در مخزن باید یک جفت زمان ثبت داشته باشد. UTC مرجع است و زمان تهران از همان UTC محاسبه می‌شود.

## درخواست و تصمیم کاربر
کاربر روشن کرد که چندین زمان برای هر ورودی/خروجی لازم نیست. معیار اصلی، زمان واقعی ثبت فایل/رویداد در مخزن است؛ همان ثبت باید UTC و زمان متناظر تهران داشته باشد. اگر محتوای تاریخی فقط زمان تهران داشته باشد UTC آن ساخته شود؛ اگر فقط UTC داشته باشد تهران ساخته شود؛ اگر زمان در محتوا نباشد، زمان آخرین commit تغییر‌دهندهٔ همان فایل از فرادادهٔ Git استفاده شود. زمان ثبت مخزن نباید به‌عنوان زمان پیام جا زده شود.

## قاعدهٔ پذیرفته‌شده
1. `repository_registration_utc` منبع canonical است.
2. `repository_registration_tehran` با `Asia/Tehran` از همان instant محاسبه می‌شود.
3. زمان‌های توکار/تاریخی جداگانه نرمال‌سازی می‌شوند؛ جفت صریح باید از نظر instant اختلاف صفر داشته باشد.
4. زمان بدون منطقه فقط در صورت برچسب روشن UTC یا تهران قابل تفسیر است؛ وگرنه UNKNOWN/REVIEW.
5. برای فایل فاقد زمان توکار، آخرین commit تغییر‌دهندهٔ فایل زمان ثبت مخزن است؛ تاریخچهٔ ناقص یا فرادادهٔ غایب باید به‌صراحت گزارش شود.
6. زمان پیام، شروع پردازش و read-back برای هر ثبت الزامی نیستند؛ زمان مستقل فقط در صورت داشتن منبع معتبر و نیاز ممیزی افزوده می‌شود.

## پیاده‌سازی مخزنی
- ممیزی نرمال‌سازی: `scripts/audit_timestamp_pairs_semantic.py`
- گردش‌کار: `.github/workflows/living-architecture-audit.yml` با `fetch-depth: 0` برای تاریخچهٔ کامل.
- استاندارد حاکم به نسخهٔ 1.2.0 اصلاح شد.
- سند مرجع مادر ممیزی زمان/میزبان اصلاح شد.

## چکش و حدود اثبات
- Repository write: ثبت این فایل و اصلاحیه‌ها از طریق GitHub Contents API انجام می‌شود.
- Read-back: پس از ثبت باید فایل‌ها دوباره از GitHub خوانده و شناسه‌ها/قاعده تطبیق داده شوند.
- Semantic audit execution: تا زمان خواندن خروجی تازهٔ workflow، نتیجهٔ کل مخزن OPEN است؛ کد و workflow به‌تنهایی اثبات اجرای موفق نیستند.
- Runtime live capture: این رویداد دربارهٔ قاعدهٔ زمان مخزن است و به‌تنهایی اتصال producer زندهٔ ChatGPT را ثابت نمی‌کند.
- No fabricated timestamps: زمان پیام کاربر یا تولید پاسخ از زمان commit استنتاج نمی‌شود.

## لنگر ثبت مخزن
- Initial registration commit: در فرادادهٔ GitHub برای همین فایل ثبت و بعد از ایجاد سند بازخوانی شود.
- UTC: از `commit.committer.date` همان commit.
- Tehran: تبدیل محاسباتی همان UTC به `Asia/Tehran`.
- Read-back: نتیجهٔ fetch فایل باید پس از ثبت موجود باشد؛ زمان دقیق fetch اگر در دسترس ابزار نباشد UNKNOWN می‌ماند.

## شاهد ثبت اولیه در مخزن
- Initial registration commit / زمان ثبت اولیه: `7831b4b79a30a61beae33fa5e2890a86e1fb0177`
- Repository registration UTC / زمان ثبت UTC: `2026-10-21T16:27:06Z`
- Repository registration Tehran / زمان ثبت تهران: `2026-10-21T19:57:06+03:30`
- Arithmetic check / چکش حسابی: UTC + 03:30 = Tehran؛ اختلاف instant برابر صفر ثانیه.
- Source / منبع: GitHub commit metadata؛ این زمان ثبت اولیهٔ فایل است، نه زمان پیام یا تولید پاسخ.
- Rule link / پیوند قاعده: [استاندارد حاکم زمان](../GOVERNANCE/ASSISTANT-TIMESTAMP-ANCHOR-STANDARD-2026-10-21-001.md) و [سند مرجع مادر](../../reference/REFERENCE-DOCUMENTS/SEMANTIC-TIMESTAMP-AUDIT-AND-HOST-CAPTURE-RECOVERY-MASTER-REFERENCE-2026-10-21-001.md).


## نتیجهٔ ممیزی کامل زمان مخزن
- Living Architecture Audit run: 39635817039 — SUCCESS.
- زمان اجرای ممیزی UTC: 2026-10-21T16:33:30Z.
- زمان متناظر تهران: 2026-10-21T20:03:30+03:30.
- فایل‌های ردیابی‌شده: 1,232؛ زمان‌های توکار: 632؛ جفت UTC/تهران نرمال‌شده: 632/632.
- ابهام/خطای تفسیر: 0؛ ناسازگاری تهران: 0؛ خطای UTC: 0؛ فایل فاقد زمان ثبت مخزن: 0.
- نتیجه: REPOSITORY_TIME_NORMALIZATION_PASS.
- این PASS فقط شکاف زمان ثبت فایل‌ها و نرمال‌سازی زمان‌های توکار در محدودهٔ مخزن را می‌بندد؛ اتصال پیام زنده و مقصدهای مستقل جداگانه‌اند.
