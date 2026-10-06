# سند اصلاح معماری — سخت‌سازی کنترل بررسی سه‌سطحی و جلوگیری از ادعای بدون شواهد

**Stable ID:** THREE-LAYER-VERIFICATION-FAILURE-HARDENING-2026-10-06-001  
**Production ID:** 3LR-HARDEN-2026-10-06-001  
**Version:** 1.0  
**Date:** 2026-10-06  
**Timezone:** Asia/Tehran (+03:30)  
**Owner:** Ahmad Nezhadhosseini / احمد پلنگ  
**Project:** Future AI / Palang Footprint  
**Type:** Architectural Amendment / Failure-Prevention Control  
**Status:** ACTIVE / LIVING / REGISTERED

## 1. Trigger
این Amendment در پی یک خطای واقعی در بررسی وضعیت سند مرجع معماری سه‌سطحی ایجاد شد. کاربر صریحاً درخواست بررسی مستقل سه مقصد را داده بود: Repository، Buffer و Persistent Memory؛ اما پاسخ اولیه بدون بررسی واقعی صادر شد، سپس وضعیت نادرست به مخزن/بافر تعمیم داده شد، و تنها پس از اجرای جست‌وجوی واقعی وضعیت صحیح مشخص شد.

## 2. Root Cause — ریشه خطا
1. Intent Compression: درخواست سه‌مقصدی به یک سؤال کلی درباره وجود سند تقلیل یافت.
2. Premature Answering: پاسخ قبل از اجرای ابزار/جست‌وجوی لازم تولید شد.
3. Evidence Substitution: وضعیت/متن خود سند به‌جای شواهد مقصد استفاده شد.
4. Cross-Surface Leakage: وضعیت یک سطح به سطح دیگر تعمیم داده شد.
5. Failure to Reconcile Contradiction: ادعای اولیه با درخواست بررسی واقعی reconcile نشد.
6. No Destination Matrix: ماتریس Repository/Buffer/Memory قبل از پاسخ ساخته نشد.
7. No Claim Gate: پاسخ قطعی بدون عبور از Evidence Gate صادر شد.

## 3. New Mandatory Control — کنترل اجباری جدید
هر درخواست شامل «چک کن»، «بگرد»، «ذخیره شده؟»، «در مخزن هست؟»، «در بافر هست؟»، «در حافظه هست؟»، «کجا ثبت شده؟»، «Verify کن» یا «Read-back کن» یک Verification Query است، نه سؤال عادی.

### 3.1 Destination Matrix Gate
قبل از پاسخ باید سه سطح مستقل بررسی شوند:
- Repository / مخزن: آیا Artifact واقعاً در مقصد پیدا و قابل‌بازیابی است؟
- Buffer / بافر: آیا همان Production واقعاً در Buffer وجود دارد؟
- Persistent Memory / حافظه پایدار: آیا Provider-level Write و Read-back مستقل وجود دارد؟

هیچ خانه‌ای از ماتریس از خانه دیگر پر نمی‌شود.

## 4. Evidence Isolation — جداسازی شواهد
- Repository proof فقط Repository را اثبات می‌کند.
- Buffer proof فقط Buffer را اثبات می‌کند.
- Memory proof فقط با Provider-level independent Read-back می‌تواند Memory را اثبات کند.
- متن یک سند که می‌گوید در مقصدی ثبت شده، به‌تنهایی اثبات حضور فعلی در آن مقصد نیست.
- هیچ سطحی وضعیت VERIFIED سطح دیگر را به ارث نمی‌برد.

## 5. No-Answer-Before-Check Gate
اگر کاربر صریحاً «بررسی» خواست:
PARSE → IDENTIFY TARGET → ENUMERATE DESTINATIONS → SEARCH/READ-BACK → BUILD DESTINATION MATRIX → RECONCILE → ANSWER

پاسخ پیش از SEARCH/READ-BACK ممنوع است؛ اگر ابزار در دسترس نباشد باید «قابل بررسی نیست» گفته شود، نه «وجود ندارد».

## 6. Negative Claim Hardening — سخت‌سازی ادعای منفی
عبارت‌هایی مانند «ندارم»، «پیدا نشد»، «در مخزن نیست»، «در حافظه نیست» یا «ذخیره نشده» فقط با دامنه جست‌وجو و شاهد منفی مجازند.

NO SEARCH → NO NEGATIVE CLAIM  
NO DESTINATION READ-BACK → NO DESTINATION ABSENCE CLAIM

## 7. Contradiction / Reconciliation Gate
اگر نتیجه جدید با پاسخ قبلی ناسازگار بود:
1. پاسخ قبلی SUPERSEDED / INCORRECT CLAIM شود.
2. علت خطا ثبت شود.
3. نتیجه جدید فقط از شواهد معتبر ساخته شود.
4. سه مقصد جداگانه گزارش شوند.
5. خطای معماری به این کنترل افزوده شود.

## 8. Mandatory Three-Level Response Format
برای درخواست‌های سه‌سطحی:
- Repository: [state] — [evidence]
- Buffer: [state] — [evidence]
- Persistent Memory: [state] — [evidence/boundary]

سپس نتیجه کلی، بدون ادغام سه وضعیت.

## 9. Anti-Inference Rule
ممنوع است:
- «سند می‌گوید Buffer VERIFIED است» → «من الان Buffer را پیدا کردم».
- «Memory capability gap» → «Memory وجود ندارد».
- «Library artifact پیدا شد» → «Canonical Repository حتماً تأیید شده».
- «Report پیدا شد» → «خود مقصد حتماً وجود دارد» بدون بررسی رابطه و Evidence.

## 10. Acceptance Tests
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

## 11. Architectural Decision
این خطا به‌عنوان Architecture GAP / Execution-Control Failure ثبت می‌شود، نه صرفاً خطای گفتاری.

اصل جدید:
سه مقصد را جداگانه ببین؛ سه شاهد را جداگانه بسنج؛ سپس نتیجه را reconcile کن.

اصل اجرایی:
CHECK REQUEST → TOOL-FIRST → DESTINATION-BY-DESTINATION → EVIDENCE ISOLATION → RECONCILE → CLAIM

## 12. Evidence Boundary
این Amendment به‌عنوان Artifact معماری در Library و Repository ثبت می‌شود. Persistent Memory همچنان مشمول محدودیت Provider-level independent Read-back است؛ بنابراین هیچ Memory VERIFIED از این Amendment نتیجه‌گیری نمی‌شود.

## 13. Lineage
Parent: THREE-LAYER-REGISTRATION-ARCHITECTURE-2026-10-06-001 / 3LR-REG-2026-10-06-001  
Related: 3LR-REPO-REPORT-2026-10-06-001, 3LR-BUFFER-REPORT-2026-10-06-001, 3LR-MEMORY-REPORT-2026-10-06-001  
Trigger Incident: incorrect premature answer to explicit three-destination verification request on 2026-10-06.
