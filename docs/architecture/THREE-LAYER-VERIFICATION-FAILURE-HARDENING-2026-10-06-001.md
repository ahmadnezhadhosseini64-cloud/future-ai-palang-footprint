# سند اصلاح معماری — سخت‌سازی کنترل بررسی سه‌سطحی و جلوگیری از ادعای بدون شواهد

**Stable ID:** THREE-LAYER-VERIFICATION-FAILURE-HARDENING-2026-10-06-001  
**Production ID:** 3LR-HARDEN-2026-10-06-001  
**Version:** 1.1  
**Date:** 2026-10-06  
**Timezone:** Asia/Tehran (+03:30)  
**Owner:** Ahmad Nezhadhosseini / احمد پلنگ  
**Project:** Future AI / Palang Footprint  
**Type:** Architectural Amendment / Failure-Prevention Control  
**Status:** ACTIVE / LIVING / REGISTERED

## 1. Trigger
این Amendment در پی یک خطای واقعی در بررسی وضعیت سند مرجع معماری سه‌سطحی ایجاد شد. کاربر صریحاً درخواست بررسی مستقل سه مقصد را داده بود: Repository، Buffer و Persistent Memory؛ اما پاسخ اولیه بدون بررسی واقعی صادر شد، سپس وضعیت نادرست به مخزن/بافر تعمیم داده شد، و تنها پس از اجرای جست‌وجوی واقعی وضعیت صحیح مشخص شد.

## 2. Root Cause — ریشه خطا
1. **Intent Compression:** درخواست سه‌مقصدی به یک سؤال کلی درباره وجود سند تقلیل یافت.
2. **Premature Answering:** پاسخ قبل از اجرای ابزار/جست‌وجوی لازم تولید شد.
3. **Evidence Substitution:** وضعیت/متن خود سند به‌جای شواهد مقصد استفاده شد.
4. **Cross-Surface Leakage:** وضعیت یک سطح به سطح دیگر تعمیم داده شد.
5. **Failure to Reconcile Contradiction:** ادعای اولیه با درخواست بررسی واقعی reconcile نشد.
6. **No Destination Matrix:** ماتریس Repository/Buffer/Memory قبل از پاسخ ساخته نشد.
7. **No Claim Gate:** پاسخ قطعی بدون عبور از Evidence Gate صادر شد.

## 3. New Root-Cause Layer — لایه ریشه‌ای جدید: فهم درخواست → مسیر جست‌وجو → پاسخ
خطای اصلی فقط «نگشتن در مقصدها» نبود. خطا یک مرحله قبل‌تر رخ داد: درخواست دقیق کاربر در مرحله تبدیل پیام به Task / کار اجرایی، به‌درستی حفظ نشد.

### 3.1 What the user actually asked
در نمونه حادثه، ساختار واقعی درخواست این بود:
- **Target / هدف:** سند مرجع معماری سه‌سطحی
- **Action / عمل:** بررسی اینکه واقعاً ثبت/ذخیره شده است یا خیر
- **Destinations / مقصدها:** Repository + Buffer + Persistent Memory
- **Required Output / خروجی موردنیاز:** وضعیت مستقل هر مقصد بر پایه شاهد

### 3.2 Incorrect internal path
مسیر خطادار:
**USER MESSAGE → TOPIC RECOGNITION → ASSUMED QUESTION → ANSWER**

در این مسیر، «موضوع» حفظ شد اما «عمل مورد درخواست»، «مقصدها» و «معیار اثبات» در تفسیر فشرده شدند.

### 3.3 Required path
مسیر اجباری جدید:
**USER MESSAGE → REQUEST PRESERVATION → INTENT PARSE → TARGET/ACTION/DESTINATIONS/OUTPUT → TASK CLASSIFICATION → TOOL/SEARCH PLAN → EVIDENCE → RECONCILE → ANSWER**

معنی فارسی:
- **REQUEST PRESERVATION / حفظ درخواست:** متن و اجزای عملیاتی سؤال نباید در خلاصه‌سازی از بین بروند.
- **INTENT PARSE / تجزیه منظور:** مشخص شود کاربر دقیقاً چه کاری می‌خواهد، نه فقط درباره چه چیزی صحبت می‌کند.
- **TASK CLASSIFICATION / طبقه‌بندی کار:** تشخیص داده شود سؤال عادی است یا درخواست بررسی/بازیابی/راستی‌آزمایی.
- **TOOL/SEARCH PLAN / برنامه ابزار و جست‌وجو:** مسیر بررسی قبل از نتیجه‌گیری تعیین شود.

### 3.4 Mandatory Intent Preservation Gate
پیش از پاسخ به درخواست‌های بررسی، مدل باید حداقل این چهار جزء را حفظ کند:
**TARGET + ACTION + DESTINATIONS/CONDITIONS + REQUIRED OUTPUT**

اگر هرکدام حذف، مبهم یا با حدس جایگزین شده باشد:
**DO NOT ANSWER YET → RE-PARSE REQUEST**

این کنترل برای جلوگیری از تبدیل سؤال دقیق کاربر به یک سؤال ساده‌تر و اشتباه طراحی شده است.

### 3.5 Topic ≠ Task
اصل معماری جدید:
**Understanding the Topic ≠ Understanding the Task**

یعنی فهمیدن «موضوع» به معنی فهمیدن «کاری که کاربر خواسته» نیست.

بنابراین شناسایی صحیح سند، پروژه، فایل یا مفهوم به‌تنهایی مجوز پاسخ نیست؛ ابتدا باید عملیات درخواستی و شرایط اثبات آن استخراج شود.

## 4. New Mandatory Control — کنترل اجباری مقصدها
هر درخواست شامل «چک کن»، «بگرد»، «ذخیره شده؟»، «در مخزن هست؟»، «در بافر هست؟»، «در حافظه هست؟»، «کجا ثبت شده؟»، «Verify کن» یا «Read-back کن» یک Verification Query است، نه سؤال عادی.

### 4.1 Destination Matrix Gate
قبل از پاسخ باید سه سطح مستقل بررسی شوند:
- Repository / مخزن: آیا Artifact واقعاً در مقصد پیدا و قابل‌بازیابی است؟
- Buffer / بافر: آیا همان Production واقعاً در Buffer وجود دارد؟
- Persistent Memory / حافظه پایدار: آیا Provider-level Write و Read-back مستقل وجود دارد؟

هیچ خانه‌ای از ماتریس از خانه دیگر پر نمی‌شود.

## 5. Evidence Isolation — جداسازی شواهد
- Repository proof فقط Repository را اثبات می‌کند.
- Buffer proof فقط Buffer را اثبات می‌کند.
- Memory proof فقط با Provider-level independent Read-back می‌تواند Memory را اثبات کند.
- متن یک سند که می‌گوید در مقصدی ثبت شده، به‌تنهایی اثبات حضور فعلی در آن مقصد نیست.
- هیچ سطحی وضعیت VERIFIED سطح دیگر را به ارث نمی‌برد.

## 6. No-Answer-Before-Check Gate
اگر کاربر صریحاً «بررسی» خواست:
**REQUEST PRESERVATION → PARSE → IDENTIFY TARGET → ENUMERATE DESTINATIONS → SEARCH/READ-BACK → BUILD DESTINATION MATRIX → RECONCILE → ANSWER**

پاسخ پیش از SEARCH/READ-BACK ممنوع است؛ اگر ابزار در دسترس نباشد باید «قابل بررسی نیست» گفته شود، نه «وجود ندارد».

## 7. Search/Answer Separation — جداسازی جست‌وجو از تولید پاسخ
مدل نباید مسیر زیر را طی کند:
**Question → Guess/Memory Impression → Answer → Search afterward**

مسیر مجاز:
**Question → Structured Task → Search/Read-back → Evidence Assembly → Claim Gate → Answer**

یعنی جست‌وجو مرحله‌ای برای «تأیید پاسخ از قبل ساخته‌شده» نیست؛ جست‌وجو بخشی از ساخت پاسخ است.

## 8. Negative Claim Hardening — سخت‌سازی ادعای منفی
عبارت‌هایی مانند «ندارم»، «پیدا نشد»، «در مخزن نیست»، «در حافظه نیست» یا «ذخیره نشده» فقط با دامنه جست‌وجو و شاهد منفی مجازند.

**NO SEARCH → NO NEGATIVE CLAIM**  
**NO DESTINATION READ-BACK → NO DESTINATION ABSENCE CLAIM**

## 9. Contradiction / Reconciliation Gate
اگر نتیجه جدید با پاسخ قبلی ناسازگار بود:
1. پاسخ قبلی **SUPERSEDED / INCORRECT CLAIM** شود.
2. علت خطا ثبت شود.
3. نتیجه جدید فقط از شواهد معتبر ساخته شود.
4. سه مقصد جداگانه گزارش شوند.
5. اگر ریشه در مسیر فهم/جست‌وجو بوده، همان کنترل معماری نیز اصلاح شود.

## 10. Mandatory Three-Level Response Format
برای درخواست‌های سه‌سطحی:
- Repository: [state] — [evidence]
- Buffer: [state] — [evidence]
- Persistent Memory: [state] — [evidence/boundary]

سپس نتیجه کلی، بدون ادغام سه وضعیت.

## 11. Anti-Inference Rule
ممنوع است:
- «سند می‌گوید Buffer VERIFIED است» → «من الان Buffer را پیدا کردم».
- «Memory capability gap» → «Memory وجود ندارد».
- «Library artifact پیدا شد» → «Canonical Repository حتماً تأیید شده».
- «Report پیدا شد» → «خود مقصد حتماً وجود دارد» بدون بررسی رابطه و Evidence.

## 12. Acceptance Tests
- AT-3L-H01: هر سه مقصد نام‌برده جداگانه بررسی شوند.
- AT-3L-H02: پاسخ قبل از Search/Read-back صادر نشود.
- AT-3L-H03: نبود شواهد با نبود Artifact یکی نشود.
- AT-3L-H04: Repository به Buffer/Memory تعمیم داده نشود.
- AT-3L-H05: Buffer به Memory تعمیم داده نشود.
- AT-3L-H06: متن سند جای Evidence مقصد را نگیرد.
- AT-3L-H07: ادعای منفی دامنه و شاهد جست‌وجو داشته باشد.
- AT-3L-H08: تناقض با پاسخ قبلی reconcile شود.
- AT-3L-H09: Memory بدون Provider-level independent Read-back، NOT-VERIFIED / CAPABILITY-GAP بماند.
- AT-3L-H10: خروجی نهایی Destination Matrix داشته باشد.
- **AT-3L-H11:** Target/Action/Destinations/Required Output قبل از پاسخ استخراج و حفظ شوند.
- **AT-3L-H12:** Topic Recognition به‌تنهایی برای پاسخ کافی نباشد.
- **AT-3L-H13:** Search/Read-back قبل از Claim انجام شود، نه بعد از آن.
- **AT-3L-H14:** اگر Intent Compression رخ داد، پاسخ متوقف و Request Re-parse شود.
- **AT-3L-H15:** مسیر واقعی اجرای سؤال با ساختار درخواست کاربر قابل تطبیق باشد.

## 13. Architectural Decision
این خطا به‌عنوان **Architecture GAP / Execution-Control Failure** ثبت می‌شود، نه صرفاً خطای گفتاری.

اصل جدید:
**سه مقصد را جداگانه ببین؛ سه شاهد را جداگانه بسنج؛ سپس نتیجه را reconcile کن.**

اصل بنیادی‌تر:
**اول منظور و ساختار کاربر را حفظ کن؛ بعد مسیر جست‌وجو را بساز؛ سپس بر اساس شواهد پاسخ بده.**

اصل اجرایی:
**REQUEST PRESERVATION → INTENT PARSE → TASK CLASSIFICATION → TOOL-FIRST → DESTINATION-BY-DESTINATION → EVIDENCE ISOLATION → RECONCILE → CLAIM**

## 14. Failure-Prevention Scope
این کنترل فقط برای سه‌سطح Repository/Buffer/Memory نیست. هرجا کاربر سؤال مشخصی درباره وجود، وضعیت، بازیابی، ثبت، مقایسه، بررسی، یا صحت یک Artifact/State می‌پرسد، مدل باید ابتدا «کاری که کاربر خواسته» را از «موضوعی که درباره آن صحبت می‌کند» جدا کند.

هدف این کنترل:
**جلوگیری از تکرار مسیر خطادار «برداشت ناقص از سؤال → پاسخ زودهنگام → جست‌وجوی پس از پاسخ».**

## 15. Evidence Boundary
این Amendment به‌عنوان Artifact معماری در Repository ثبت شده است. وضعیت Library/Buffer و Persistent Memory فقط در صورت اجرای مستقل ابزار و دریافت شواهد مربوطه قابل ادعاست.

## 16. Lineage
Parent: THREE-LAYER-REGISTRATION-ARCHITECTURE-2026-10-06-001 / 3LR-REG-2026-10-06-001  
Related: 3LR-REPO-REPORT-2026-10-06-001, 3LR-BUFFER-REPORT-2026-10-06-001, 3LR-MEMORY-REPORT-2026-10-06-001  
Trigger Incident: incorrect premature answer to explicit three-destination verification request on 2026-10-06.  
Revision 1.1: اضافه‌شدن لایه «حفظ درخواست و تجزیه منظور پیش از طراحی جست‌وجو و پاسخ» بر اساس چکش ریشه‌ای خطا.
