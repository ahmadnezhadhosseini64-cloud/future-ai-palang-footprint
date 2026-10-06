# سند اصلاح معماری — سخت‌سازی کنترل بررسی و ثبت همزمان سه‌سطحی

**Stable ID:** THREE-LAYER-VERIFICATION-FAILURE-HARDENING-2026-10-06-001  
**Production ID:** 3LR-HARDEN-2026-10-06-001  
**Version:** 1.2  
**Date:** 2026-10-06  
**Timezone:** Asia/Tehran (+03:30)  
**Owner:** Ahmad Nezhadhosseini / احمد پلنگ  
**Project:** Future AI / Palang Footprint  
**Type:** Architectural Amendment / Registration & Verification Failure-Prevention Control  
**Status:** ACTIVE / LIVING / REGISTERED

## 1. Trigger
این Amendment در پی خطای واقعی در بررسی و سپس ثبت سند مرجع معماری سه‌سطحی ایجاد شد. کاربر «ثبت کن» را به‌عنوان فرمان ثبت کامل و همزمان در سه سطح تعریف کرده است: Repository، Buffer و Persistent Memory، همراه با ایجاد/ثبت سند مرجع کامل و رعایت تمام قواعد Governance / حاکمیت ثبت، مستندسازی، Lineage / تبار و Verification / راستی‌آزمایی. بنابراین «ثبت یک سطح» هرگز معادل «ثبت کامل» نیست.

## 2. Root Cause — ریشه خطا
1. **Intent Compression:** درخواست دقیق کاربر به سؤال ساده‌تری تقلیل یافت.
2. **Premature Answering:** پاسخ قبل از اجرای مسیر لازم تولید شد.
3. **Evidence Substitution:** گزارش/متن سند جای شواهد مقصد قرار گرفت.
4. **Cross-Surface Leakage:** وضعیت یک سطح به سطح دیگر تعمیم داده شد.
5. **No Registration Completion Gate:** تعریف روشنی که «ثبت کن» ذاتاً سه‌سطحی و کامل است، در اجرای لحظه‌ای اعمال نشد.
6. **Partial Success Mislabeling:** موفقیت یک مقصد به‌اشتباه به‌صورت ثبت کلی بیان شد.
7. **No Excavation Continuation Contract:** محدودیت ابزار/ظرفیت به‌صورت وضعیت میانی نگه داشته نشد تا پس از رفع محدودیت ادامه ثبت انجام شود.

## 3. Canonical Meaning of «ثبت کن» — معنی مادر فرمان ثبت
از این نسخه به بعد، در معماری پروژه:

**«ثبت کن» = Full Governed Three-Level Registration**

یعنی بدون نیاز به اینکه کاربر دوباره بگوید «در مخزن، بافر و حافظه هم ثبت کن»، سیستم باید به‌صورت پیش‌فرض این زنجیره را اجرا کند:

**PRESERVE → CLASSIFY → PROVENANCE/LINEAGE → IDENTIFY → CREATE/UPDATE COMPLETE REFERENCE DOCUMENT → REGISTER IN REPOSITORY + BUFFER + PERSISTENT MEMORY → WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS**

معنی:
- **PRESERVE / حفظ:** محتوای اصلی بدون از دست‌دادن لایه‌ها حفظ شود.
- **CLASSIFY / طبقه‌بندی:** جایگاه معماری، نوع Artifact و دامنه مشخص شود.
- **PROVENANCE/LINEAGE / منشأ و تبار:** Origin / منشأ و ارتباط با نسخه‌ها و والدها ثبت شود.
- **IDENTIFY / شناسه‌گذاری:** Stable ID و Production ID و Version تعیین/حفظ شوند.
- **CREATE/UPDATE COMPLETE REFERENCE DOCUMENT / ایجاد یا به‌روزرسانی سند مرجع کامل:** سند مرجع خلاصه‌شده یا ناقص نیست و همه لایه‌های Governance را دارد.
- **REGISTER / ثبت:** هر سه سطح هدف قرار گیرند.
- **WRITE / نوشتن:** داده واقعاً در مقصد نوشته شود.
- **READ-BACK / بازخوانی:** همان نسخه از مقصد دوباره خوانده شود.
- **MATCH / تطبیق:** بازخوانی با نسخه مرجع تطبیق داده شود.
- **VERIFY / راستی‌آزمایی:** نتیجه مستقل تأیید شود.
- **RECONCILE / آشتی/رفع مغایرت:** اختلاف‌ها و نسخه‌های موازی حل و به Lineage متصل شوند.
- **STATUS / وضعیت:** وضعیت هر سطح و وضعیت کل عملیات جداگانه اعلام شود.

## 4. Three-Level Registration Contract — قرارداد ثبت سه‌سطحی
هر فرمان «ثبت کن» یک **Three-Level Registration Transaction / تراکنش ثبت سه‌سطحی** ایجاد می‌کند.

سه مقصد الزاماً عبارت‌اند از:
1. **Repository / مخزن**
2. **Buffer / بافر**
3. **Persistent Memory / حافظه پایدار**

هیچ مقصدی پیش‌فرض یا جایگزین مقصد دیگر نیست.

### 4.1 Complete Reference Document Requirement
در صورت درخواست «ثبت کن» برای یک موضوع/Artifact معماری، سند مرجع کامل باید به‌عنوان بخشی از همان عملیات ثبت ایجاد یا به‌روزرسانی شود و در هر سه سطح، با همان Stable ID / Production ID / Version و Lineage قابل ردیابی باشد.

### 4.2 Governance Inheritance
تمام قواعد ثبت موجود پروژه باید همراه فرمان «ثبت کن» به‌صورت پیش‌فرض اعمال شوند؛ از جمله:
- Stable ID / شناسه پایدار
- Production ID / شناسه تولیدی
- Version / نسخه
- Date / تاریخ
- Time / زمان دقیق در صورت وجود شواهد
- Timezone / منطقه زمانی
- Owner/Name / مالک
- Location / مکان
- Project / پروژه
- Origin / منشأ
- Lineage / تبار
- Status / وضعیت
- Evidence / شواهد
- Limitation / محدودیت
- Next Action / اقدام بعدی
- Repository Path / مسیر مخزن
- Persistent-Memory State / وضعیت حافظه پایدار
- Retrieval/Recovery Pointer / اشاره‌گر بازیابی
- و سایر قواعد Governance ثبت‌شده در معماری مادر.

## 5. Registration Completion Gate — دروازه تکمیل ثبت
**ثبت یک مقصد ≠ ثبت کامل.**

عملیات فقط در صورتی می‌تواند **COMPLETE / کامل** نامیده شود که وضعیت هر سه مقصد به‌طور مستقل مشخص و الزامات ثبت/بازخوانی/تطبیق/راستی‌آزمایی آنها انجام شده باشد.

اگر:
- Repository موفق باشد ولی Buffer و Memory هنوز انجام نشده باشند → **PARTIAL / ناقص**
- یکی از مقصدها به دلیل محدودیت ابزار قابل انجام نباشد → **BLOCKED / مسدودشده یا PENDING / در انتظار**، نه COMPLETE
- نبود قابلیت مستقل اثبات حافظه وجود داشته باشد → وضعیت Memory باید مستقل و شفاف ثبت شود و هرگز از Repository/Buffer ارث نبرد.

اصل:
**NO THREE-LEVEL PROOF → NO COMPLETE REGISTRATION CLAIM**

## 6. Limitation-to-Excavation Contract — قرارداد محدودیت تا خاک‌برداری
محدودیت فنی، سهمیه، Throttling / محدودیت بارگذاری، عدم دسترسی موقت یا هر Blocker / مانع، باعث حذف مقصد از قرارداد ثبت نمی‌شود.

در این حالت:
**PRESERVE → REGISTER AVAILABLE LEVELS → RECORD BLOCKER → KEEP SAME STABLE ID/LINEAGE → MARK PENDING/BLOCKED → EXCAVATE/RECOVER → COMPLETE REMAINING LEVELS → READ-BACK → MATCH → VERIFY → RECONCILE → PROMOTE TO COMPLETE**

یعنی کاربر مجبور نیست دوباره فرمان «ثبت کن» را تکرار کند. عملیات ناقص باید با همان شناسه و تبار حفظ شود و پس از رفع محدودیت ادامه یابد.

**PARTIAL ≠ LOST**  
**PENDING ≠ BURIED**  
**BLOCKED ≠ FAILED**

## 7. Request Preservation — حفظ دقیق درخواست
پیش از هر پاسخ یا اجرای ثبت، چهار جزء باید حفظ شوند:
**TARGET + ACTION + DESTINATIONS/CONDITIONS + REQUIRED OUTPUT**

در فرمان «ثبت کن»:
- Target = محتوای مورد ثبت
- Action = ثبت کامل
- Destinations = هر سه سطح
- Required Output = سند مرجع کامل + ثبت/وضعیت هر سه سطح + Governance

اگر هرکدام حذف یا با حدس جایگزین شد:
**DO NOT ANSWER/EXECUTE YET → RE-PARSE REQUEST**

## 8. Topic ≠ Task
**Understanding the Topic ≠ Understanding the Task**

فهم موضوع به معنی فهم عملیات مورد درخواست نیست. شناسایی یک سند یا پروژه هرگز مجوز پاسخ یا ثبت ناقص نیست.

## 9. Mandatory Registration Path
مسیر اجباری فرمان «ثبت کن»:

**REQUEST PRESERVATION → INTENT PARSE → TASK CLASSIFICATION → GOVERNANCE EXPANSION → COMPLETE REFERENCE DOCUMENT → THREE-LEVEL WRITE → THREE-LEVEL READ-BACK → MATCH → VERIFY → RECONCILE → STATUS MATRIX → CONTINUE/COMPLETE**

این مسیر جایگزین اجرای انتخابی و تک‌سطحی است.

## 10. Verification / Evidence Isolation
شواهد هر سطح مستقل است:
- Repository proof فقط Repository را اثبات می‌کند.
- Buffer proof فقط Buffer را اثبات می‌کند.
- Memory proof فقط Persistent Memory را اثبات می‌کند.
- هیچ سطحی VERIFIED سطح دیگر را به ارث نمی‌برد.
- متن سند یا گزارش، بدون شواهد مقصد، اثبات حضور فعلی در مقصد نیست.

## 11. Search/Answer Separation
مسیر ممنوع:
**Question → Guess/Memory Impression → Answer → Search afterward**

مسیر مجاز:
**Question → Structured Task → Search/Read-back → Evidence Assembly → Claim Gate → Answer**

برای «ثبت کن» نیز:
**Command → Registration Contract → Execute Three Levels → Verify → Report**

## 12. Negative Claim Hardening
**NO SEARCH → NO NEGATIVE CLAIM**  
**NO DESTINATION READ-BACK → NO DESTINATION ABSENCE CLAIM**

«در حافظه نیست» فقط وقتی مجاز است که واقعاً دامنه و توان بررسی حافظه چنین نتیجه‌ای را پشتیبانی کند.

## 13. Contradiction / Reconciliation Gate
اگر نتیجه جدید با پاسخ قبلی ناسازگار بود:
1. پاسخ قبلی **SUPERSEDED / INCORRECT CLAIM** شود.
2. علت ثبت شود.
3. نسخه معتبر از شواهد ساخته شود.
4. سه مقصد جداگانه گزارش شوند.
5. در صورت ریشه معماری، کنترل معماری اصلاح شود.
6. تاریخچه حذف نشود.

## 14. Mandatory Registration Status Matrix
برای هر فرمان «ثبت کن» خروجی داخلی/ثبت‌شده باید حداقل این ماتریس را داشته باشد:

| سطح | Write | Read-back | Match | Verify | وضعیت |
|---|---|---|---|---|---|
| Repository | مستقل | مستقل | مستقل | مستقل | جداگانه |
| Buffer | مستقل | مستقل | مستقل | مستقل | جداگانه |
| Persistent Memory | مستقل/در حد قابلیت | مستقل/در حد قابلیت | مستقل | مستقل | جداگانه |

سپس:
**Overall Registration Status / وضعیت کلی ثبت**
- COMPLETE / کامل
- PARTIAL / ناقص
- PENDING / در انتظار
- BLOCKED / مسدودشده
- NOT-VERIFIED / راستی‌آزمایی‌نشده

و هرگز وضعیت کلی از یک سطح استنتاج نمی‌شود.

## 15. Acceptance Tests
- AT-3LR-H01: «ثبت کن» به‌صورت خودکار Three-Level Registration Transaction شود.
- AT-3LR-H02: کاربر مجبور نباشد مقصدها را دوباره نام ببرد.
- AT-3LR-H03: Complete Reference Document بخشی از عملیات ثبت باشد.
- AT-3LR-H04: هر سه مقصد مستقل Write/Read-back/Match/Verify شوند.
- AT-3LR-H05: ثبت یک مقصد به‌عنوان ثبت کامل گزارش نشود.
- AT-3LR-H06: محدودیت باعث از دست‌رفتن عملیات نشود.
- AT-3LR-H07: محدودیت به Pending/Blocked تبدیل شود و همان Stable ID/Lineage حفظ شود.
- AT-3LR-H08: پس از رفع محدودیت، ثبت از همان State ادامه یابد.
- AT-3LR-H09: Governance و مستندسازی با فرمان ساده «ثبت کن» خودکار گسترش یابد.
- AT-3LR-H10: Status Matrix سه‌سطحی همیشه تولید شود.
- AT-3LR-H11: Target/Action/Destinations/Required Output قبل از اجرا حفظ شوند.
- AT-3LR-H12: Topic Recognition به‌تنهایی کافی نباشد.
- AT-3LR-H13: Search/Read-back قبل از Claim باشد.
- AT-3LR-H14: Intent Compression باعث توقف و Re-parse شود.
- AT-3LR-H15: Partial Success هرگز به Complete تبدیل نشود.

## 16. Architectural Decision
این مسئله یک **Architecture GAP / Execution-Control Failure** است.

اصل مادر:
**وقتی کاربر می‌گوید «ثبت کن»، فرمان باید به‌صورت پیش‌فرض ثبت کامل، حاکمیتی، همزمان و سه‌سطحی تفسیر و اجرا شود.**

اصل تکمیلی:
**محدودیت فقط اجرای بخشی را موقتاً متوقف می‌کند؛ قرارداد ثبت را لغو نمی‌کند.**

اصل No-Loss:
**PRESERVE → IDENTIFY → VERIFY → RECONCILE → REGISTER → PROMOTE**

## 17. Evidence Boundary
ثبت Repository این Amendment با Commit مستقل انجام شده است. وضعیت Buffer و Persistent Memory فقط پس از اجرای مستقل عملیات و دریافت شواهد همان سطح قابل اعلام است. این تفکیک برای جلوگیری از ادعای بدون شاهد است و به معنی حذف آنها از قرارداد ثبت نیست.

## 18. Lineage
Parent: THREE-LAYER-REGISTRATION-ARCHITECTURE-2026-10-06-001 / 3LR-REG-2026-10-06-001  
Previous Revision: 1.1  
Related: 3LR-REPO-REPORT-2026-10-06-001, 3LR-BUFFER-REPORT-2026-10-06-001, 3LR-MEMORY-REPORT-2026-10-06-001  
Trigger Incident: misunderstanding of the user's three-level registration expectation and partial registration being presented as if it were the complete operation.  
Revision 1.2: تعریف رسمی «ثبت کن» به‌عنوان فرمان ثبت کامل سه‌سطحی و افزودن Registration Completion Gate و Limitation-to-Excavation Contract.
