# فرمان حاکم و پیش‌فرض «ثبت کن» — Governing Register Command Binding

## شناسنامه
- **Stable ID:** `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001` (سند مرجع مادر؛ مرجع اصلی و حاکم)
- **Production ID:** `REGISTER-COMMAND-GOVERNING-BINDING-2026-10-12-001`
- **Version:** 1.0.0
- **Date:** 2026-10-12
- **Exact Time:** Not recorded by the execution system; intentionally not invented.
- **Timezone:** Asia/Tehran (project timezone; exact execution timestamp not independently captured)
- **Owner:** Ahmad Nezhadhosseini / احمد پلنگ
- **Project:** Future AI / Palang Footprint — آینده AI / ردپای پلنگ
- **Artifact Type:** Command Binding / Architectural Entry Point
- **Status:** REPOSITORY WRITE + READ-BACK + CONTENT MATCH VERIFIED for this file and the linked MRV master; other destinations remain unverified.
- **Canonical Parent:** `docs/reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md`

## 1. Binding decision
از این پس هرگاه کاربر بگوید **«ثبت کن»**، همین سند مرجع مادر با شناسه `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001` مبنای پیش‌فرض و حاکم اجرای فرمان است. کاربر لازم نیست هر بار قواعد را دوباره توضیح دهد یا این سند را مجدداً بفرستد، مشروط به اینکه مرجع از محل پایدار واقعاً قابل بازیابی باشد.

این سند کوتاه فقط نقطه ورود و اتصال معماری است؛ جایگزین سند مرجع مادر یا مجوز حذف جزئیات آن نیست.

## 2. Minimum required execution
برای هر فرمان «ثبت کن»، تا جایی که ابزارها و دسترسی‌های واقعی اجازه می‌دهند:
1. محتوای ارزشمند را حفظ و طبقه‌بندی کن؛ منشأ، زمینه، مسئله/پرسش، یافته‌ها، آزمون‌ها، شواهد، تصمیم‌ها، دلیل تصمیم و اثر معماری را ثبت کن.
2. شناسه پایدار و شناسه تولید را ایجاد یا با حفظ lineage قبلی ادامه بده؛ برای تلاش مجدد، بی‌دلیل شناسه جدید نساز.
3. اگر محتوا معماری‌محور یا قابل استفاده مجدد است، سند مرجع کامل را بساز یا به‌روزرسانی کن و تاریخچه/نسخه‌های قبلی را حفظ کن.
4. مقصدهای واقعی را جداگانه هدف بگیر: مخزن (Repository)، بافر (Buffer)، حافظه پایدار (Persistent Memory) و هر مخزن اسنادی متصل و در دسترس.
5. برای هر مقصد مستقل، چرخه `WRITE → READ-BACK → MATCH → VERIFY` را اجرا کن؛ موفقیت یک مقصد را به مقصد دیگر تعمیم نده.
6. جایگاه سند در معماری، وابستگی‌ها، نسخه، تعارض/جایگزینی، مسیر بازیابی، وضعیت و گام بعدی را ثبت کن.
7. فقط وضعیت پشتیبانی‌شده با شواهد را گزارش بده. اگر مرحله‌ای قابل اجرا نیست، آن را `OPEN/PENDING` یا «پودینگ» نگه دار و مانع، آخرین وضعیت پایدار، قابلیت موردنیاز، گام بعدی و اشاره‌گر بازیابی را بنویس.

## 3. Hard constraints
- قصد اجرا یا پاسخ موفق ابزار به‌تنهایی اثبات بازیابی و تطبیق نیست.
- وجود/خواندن فایل در مخزن، ثبت در بافر یا حافظه پایدار را اثبات نمی‌کند.
- هیچ ادعای `ACTIVE / VERIFIED / COMPLETE` بدون شواهد مخصوص همان مقصد مجاز نیست.
- اگر سند قابل بازیابی است، پیش از درخواست از کاربر برای ارسال دوباره، آن را بازیابی و بررسی کن.
- اگر در این محیط امکان نوشتن یا تأیید یک مقصد وجود ندارد، شفاف بگو؛ هرگز وضعیت را حدس نزن یا موفقیت را جعل نکن.
- «ثبت کن» به معنای ثبت کامل و حاکمیتی است، نه صرفاً پاسخ‌دادن، خلاصه‌کردن، یا گفتن «ذخیره شد».

## 4. Architecture placement and relationship
- **Reference Documents Vault:** `/Future AI/Palang Footprint/Master Reference Vault/Reference Documents/`
- **Canonical repository folder:** `docs/reference/REFERENCE-DOCUMENTS/`
- **Master governing reference:** `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001`
- **Related command contract:** `UNIVERSAL-REGISTER-COMMAND-EXECUTION-CONTRACT-2026-09-29-001` (باید هنگام بازیابی بررسی شود؛ وجود/نسخه فعلی آن در این عملیات مستقلاً بررسی نشده است)
- **Architecture relation:** This record is the command-to-governance binding entry point; the MRV master remains the detailed lifecycle and verification authority.

## 5. Current evidence and open obligations
- The existing MRV master was fetched from the canonical repository before modification.
- The MRV master was updated to bind the literal command «ثبت کن» to its full lifecycle.
- This companion record is being created in the canonical repository.
- Repository read-back completed for this file and the updated MRV master; expected binding text was found in both. README entry point was also read back and its links/headings were found.
- Library, Buffer, and Persistent Memory have **not** been independently written/read back in this operation; do not mark them complete.
- **Next action:** read back this file and the updated master from the repository, compare the expected binding text, then report only the verified scope. Continue other destinations only when their actual write capabilities are available.

## 6. No-loss recovery rule
If interrupted or blocked, preserve this same Production ID and Stable ID relationship; keep the work pending rather than dropping it. On return: retrieve → identify → validate → deduplicate → reconcile → register → read back → verify → continue. Do not ask the user to repeat retrievable material.
