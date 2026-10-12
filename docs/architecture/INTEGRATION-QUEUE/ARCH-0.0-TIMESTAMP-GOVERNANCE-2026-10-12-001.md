# پروندهٔ انتظار ادغام: حاکمیت زمان‌گذاری نقاط ۰.۰

## شناسنامه
- Stable ID: ARCH-0.0-TIMESTAMP-GOVERNANCE-2026-10-12-001
- Production ID: ARCH0TSG-2026-10-12-001
- Version: 1.0.0
- Date: 2026-10-12
- Exact Time: زمان دقیق ایجاد این پرونده مستقلاً ثبت نشده؛ حدس زده نمی‌شود.
- Timezone: Asia/Tehran (منطقهٔ زمانی پروژه؛ زمان دقیق اجرا ثبت نشده)
- Owner: Ahmad Nezhadhosseini / احمد پلنگ
- Project: Future AI / Palang Footprint
- Status: PENDING INTEGRATION — در انتظار اتصال به اسناد مرجع مادر؛ پس از نوشتن باید بازخوانی شود.
- Origin / Lineage: قرارداد «ثبت زمان نقاط ۰.۰» که در docs/0.0/README.md درج شده؛ اتصال به اسناد مرجع مادر و حاکم فرمان هنوز در این اجرا تأیید نشده است.
- Queue Index: docs/architecture/INTEGRATION-QUEUE/README.md

## 1. تغییر مورد انتظار
هر نقطهٔ ۰.۰ باید زمان‌های مستقل و منشأ هر زمان را نگه دارد:
- Anchor Created At — زمان ایجاد نقطه
- Repository Registered At — زمان ثبت در مخزن، ترجیحاً با مهر زمانی واقعی commit و شناسهٔ commit
- Last Modified At — زمان آخرین تغییر
- Last Verified At — زمان آخرین بازخوانی و تطبیق موفق
- Timezone — منطقهٔ زمانی صریح
- Time Provenance — منشأ/مدرک هر زمان

این زمان‌ها نباید با یکدیگر یکی فرض شوند. زمان ناموجود باید UNKNOWN / UNVERIFIED (نامعلوم / تأییدنشده) بماند؛ حدس زدن زمان ممنوع است.

## 2. شواهد موجود
- دفتر مرکزی نقاط ۰.۰، مسیر docs/0.0/README.md، شامل بخش «قرارداد ثبت زمان نقاط ۰.۰» بوده و پیش‌تر بازخوانی شده است.
- شناسهٔ blob ثبت‌شده برای آن بازخوانی: 5bcdc07d9fa3c1f51026a495153373046adff08f.
- فایل معماری docs/reference/REFERENCE-DOCUMENTS/MULTI-POINT-0.0-ANCHOR-REGISTRY-ARCHITECTURE-2026-10-12-001.md در زمان بررسی هنوز اتصال کامل قرارداد زمان‌گذاری به‌عنوان تغییر تازه را نداشت.
- اتصال به سند مرجع مادر و سند حاکم فرمان «ثبت کن» هنوز باید مستقل انجام و بازخوانی شود.

## 3. مقصدهای ادغام
1. docs/reference/REFERENCE-DOCUMENTS/MULTI-POINT-0.0-ANCHOR-REGISTRY-ARCHITECTURE-2026-10-12-001.md
2. docs/reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md
3. docs/reference/REFERENCE-DOCUMENTS/REGISTER-COMMAND-GOVERNING-BINDING-2026-10-12-001.md
4. docs/0.0/README.md — باید پیوند به این صف و این پرونده را نگه دارد.

## 4. اقدام بعدی
در اجرای «خاک‌برداری»، مقصدها را از نسخهٔ فعلی بازیابی کن، تغییرات هم‌زمان را حفظ کن، قرارداد زمان‌گذاری را در محل مناسب ادغام کن، سپس هر فایل را جداگانه بازخوانی و تطبیق بده. در صورت توقف ابزار/مجوز، این پرونده PENDING / BLOCKED باقی بماند.

## 5. وضعیت لایه‌ها
- Repository: در انتظار نوشتن و بازخوانی مستقل این پرونده.
- Buffer: NOT VERIFIED — تأیید نشده.
- Library: NOT VERIFIED — تأیید نشده.
- Persistent Memory: NOT VERIFIED — تأیید نشده.

## 6. قاعدهٔ نهایی
وجود این پرونده به معنی تکمیل ادغام نیست. فقط پس از ثبت مقصد، بازخوانی، تطبیق محتوا و پیوند دادن commit/نسخهٔ مقصد می‌توان آن را INTEGRATED / VERIFIED (یکپارچه‌شده / تأییدشده) کرد.
