# سند مرجع کامل — معماری ثبت همزمان سه‌سطحی و پایدار

**Stable ID:** THREE-LAYER-REGISTRATION-ARCHITECTURE-2026-10-06-001  
**Production ID:** 3LR-REG-2026-10-06-001  
**Version:** 1.0  
**Date:** 2026-10-06  
**Timezone:** Asia/Tehran (+03:30)  
**Owner:** Ahmad Nezhadhosseini / احمد پلنگ  
**Project:** Future AI / Palang Footprint  
**Type:** Living Reference / Core Registration Architecture  
**Status:** ACTIVE / LIVING / REGISTERED  
**Parent:** NLRDOA-2026-10-06-001; MPPA-PMVG-2026-10-06-001  
**Command:** «ثبت کن» / «ثبت و زنده»

> **ماهیت:** این سند «سند مرجع کامل» است، نه سند ردپا. این سند معماری جدیدی را تثبیت می‌کند که در آن هر تولید/کشف/دانش قابل‌حفظ از ابتدا یک هویت واحد دارد و ثبت آن به‌صورت سه‌سطحی دنبال می‌شود: مخزن اصلی + حافظه پایدار + بافر پایدار.

## 1. تصمیم معماری

مدل قبلی «مخزن اصلی + بافر اضطراری» به مدل زیر ارتقا یافت:

**ONE PRODUCTION ID → THREE REGISTRATION SURFACES**

1. **Canonical Repository** — مخزن اصلی و مرجع قابل‌اثبات پروژه.
2. **Persistent Memory** — حافظه پایدار برای استمرار زمینه/دانش، مشروط به وجود قابلیت واقعی Write و Read-back مستقل.
3. **Durable Registration Buffer** — بافر/صندوق پایدار برای نگهداری کامل و مستقل تولیدات و مسیر بازیابی؛ دیگر صرفاً محل اضطراری نیست.

این سه سطح سه تولید مستقل نیستند؛ سه سطح ثبت/نگهداری یک تولید واحد با هویت، نسخه و Lineage مشترک‌اند.

## 2. اصل مادر

**ONE PRODUCTION → ONE IDENTITY → THREE SURFACES → INDEPENDENT EVIDENCE**

محدودیت یک مقصد نباید باعث توقف تولید، از دست رفتن اطلاعات، یا ساخت هویت جدید شود.

**DESTINATION LIMIT ≠ REGISTRATION STOP ≠ DATA LOSS**

## 3. دامنه

این معماری برای هر مورد ارزشمند حاصل از تعامل اعمال می‌شود، از جمله:
- کشف جدید
- تولید جدید
- تصمیم معماری
- مسیر/ردپای قابل‌اهمیت تعامل، وقتی خود مسیر بخشی از ارزش تولید است
- دانش/قاعده/Gap/Valuable Idea
- سند مرجع کامل
- گزارش تولید
- نتیجه آزمون، Hammer، Validation یا Reconciliation
- هر Artifact قابل‌حفظ که تحت قواعد پروژه باید زنده بماند

## 4. مدل هویت واحد

هر تولید در نقطه پذیرش یک **Stable ID** و یک **Production ID** دریافت می‌کند.

همان هویت در هر سه سطح حفظ می‌شود:

`Repository[X] = Memory[X] = Buffer[X]`

تفاوت فقط در **Destination State** است؛ نه در هویت.

هیچ Retry نباید برای همان تولید هویت جدید بسازد. Version/Attempt در صورت نیاز جدا ثبت می‌شود.

## 5. ثبت همزمان سه‌سطحی

جریان استاندارد:

**CAPTURE → IDENTIFY → CLASSIFY → ASSIGN ONE ID → PRESERVE COMPLETE PAYLOAD → ATTEMPT/REGISTER REPOSITORY + MEMORY + BUFFER → RECORD THREE INDEPENDENT STATES → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS**

هدف معماری این است که هر سه سطح از ابتدا مقصد ثبت باشند، نه اینکه Buffer فقط پس از شکست فعال شود.

## 6. تفاوت نقش سه سطح

### 6.1 Canonical Repository — مخزن اصلی
مرجع اصلی ساختاری/نسخه‌ای پروژه، محل اسناد مرجع و تاریخچه قابل‌اثبات.

### 6.2 Persistent Memory — حافظه پایدار
سطح استمرار زمینه و دانش برای تعاملات آینده. **این سطح فقط با قابلیت واقعی سرویس حافظه و Read-back مستقل می‌تواند VERIFIED شود.** پاسخ مکالمه، Write acknowledgement، Repository یا Buffer جای Read-back مستقل را نمی‌گیرد.

### 6.3 Durable Registration Buffer — بافر پایدار
صندوق دائمی و قابل‌بازیابی برای نگهداری کامل Payload. Buffer همزمان یک سطح نگهداری است و در صورت محدودیت هر مقصد نیز نقش Recovery/Overflow را دارد.

**Trace-only کافی نیست؛ Complete Payload الزامی است.**

## 7. Complete Payload Contract — قرارداد بدنه کامل

هر سطحی که Payload را نگهداری می‌کند باید تا حد قابلیت خود این عناصر را حفظ کند:
- Stable ID / Production ID
- Version / Attempt
- Date / Time / Timezone وقتی ثبت شده
- Owner / Project / Origin
- متن کامل تولید یا سند مرجع
- Evidence / Provenance
- Lineage / Parent / Master / 0.0 links
- Destination States هر سه سطح
- Blocker / Capability Gap
- Recovery Pointer
- Integrity metadata در صورت وجود

## 8. استقلال وضعیت‌ها

وضعیت یک سطح هرگز از سطح دیگر استنتاج نمی‌شود. نمونه‌های معتبر:

`Repository = VERIFIED | Memory = CAPABILITY-GAP | Buffer = VERIFIED`

`Repository = VERIFIED | Memory = VERIFIED | Buffer = VERIFIED`

`Repository = BLOCKED | Memory = CAPABILITY-GAP | Buffer = VERIFIED`

حتی در حالت اول، تولید از نظر No-Loss حفظ شده است؛ اما ادعای Memory VERIFIED ممنوع است.

## 9. Verification Gate — دروازه تأیید

برای هر سطح:

**WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS**

`WRITE` به‌تنهایی تأیید نیست.

برای Persistent Memory، Read-back باید مستقل از پاسخ Write و از خود سطح حافظه باشد. تا وقتی این قابلیت در Runtime در دسترس نیست، وضعیت باید **NOT-VERIFIED / CAPABILITY-GAP** باقی بماند.

## 10. رفتار در محدودیت

اگر یکی از سه مقصد محدود/قطع/غیرقابل‌دسترس باشد:
1. تولید با همان ID حفظ می‌شود.
2. دو مقصد دیگر همچنان مستقل ثبت می‌شوند، در صورت دسترسی.
3. Buffer در صورت دسترسی Payload کامل را نگه می‌دارد.
4. مقصد محدودشده صریحاً BLOCKED / UNAVAILABLE / CAPABILITY-GAP ثبت می‌شود.
5. بعداً Recovery انجام می‌شود.
6. فقط پس از Read-back/Match/Verify/Reconcile مقصد بسته/Promote می‌شود.

**No destination failure may erase the production.**

## 11. Recovery / Excavation — بازیابی

**EXCAVATE → IDENTIFY → VALIDATE → DEDUPLICATE → RECOVER COMPLETE PAYLOAD → CHECK MASTER/PARENT → REGISTER MISSING DESTINATION → READ-BACK → MATCH → VERIFY → RECONCILE → UPDATE STATES → PROMOTE/CLOSE**

اصل: هویت قبلی حفظ می‌شود؛ تولید دوباره از صفر ساخته نمی‌شود مگر با نسخه/Revision صریح.

## 12. Reference Documents — اسناد مرجع

هر سند مرجع جدید باید از ابتدا به‌عنوان Artifact کامل در مسیر مرجع ثبت شود. اگر مقصدی محدود باشد، نسخه کامل آن در Buffer نیز نگهداری می‌شود. «سند ردپا» جایگزین سند مرجع کامل نیست.

## 13. گزارش سه‌سطحی

برای هر Production مهم، یک مجموعه گزارش سه‌سطحی هم‌هویت ایجاد می‌شود:

- **Repository Report** — گزارش وضعیت ثبت در مخزن اصلی.
- **Memory Report** — گزارش وضعیت ثبت/تلاش/محدودیت حافظه پایدار.
- **Buffer Report** — گزارش نگهداری کامل و وضعیت بافر.

این سه گزارش مستقل‌اند ولی یک Production ID مشترک دارند و برای Reconcile کنار هم خوانده می‌شوند.

## 14. ساختمان پروژه

ساختار منطقی جدید:

```text
/Future AI/Palang Footprint/
├── docs/reference/REFERENCE-DOCUMENTS/        ← Canonical Reference Documents
├── docs/architecture/                         ← Architecture Controls
├── docs/reports/THREE-LAYER/                  ← Three-Level Reports
├── registry/                                  ← Production/0.0 Registry
└── Registration Buffer/
    ├── سند مرجع/                              ← Complete Reference Artifacts
    └── reports/THREE-LAYER/                   ← Buffer-side Three-Level Reports
```

Persistent Memory نیز یک سطح منطقی مستقل است و باید با همان Stable/Production ID و نسخه متصل شود؛ وضعیت واقعی آن فقط با شواهد سرویس خودش تعیین می‌شود.

## 15. No-Loss Invariants — قواعد تغییرناپذیر

- یک تولید = یک هویت.
- سه سطح = سه مقصد مستقل برای همان تولید.
- Buffer فقط اضطراری نیست؛ یک سطح ثبت/نگهداری همزمان است.
- محدودیت مقصد = توقف ثبت آن مقصد، نه توقف تولید.
- Complete Payload بر Trace-only مقدم است.
- هیچ VERIFIED بدون Evidence Closure.
- هیچ Memory VERIFIED بدون Provider-level independent Read-back.
- هیچ نسخه جدید بدون Lineage.
- هیچ حذف نسخه قبلی برای جایگزینی بی‌ردپا.

## 16. وضعیت اجرای این نسخه

**Architecture Decision:** ACCEPTED / ACTIVE / LIVING

**Repository:** REGISTERED / READ-BACK / MATCH / VERIFIED

**Buffer:** REGISTERED / READ-BACK / MATCH / VERIFIED برای سطح Library Buffer

**Persistent Memory:** ATTEMPTED AS REQUIRED DESTINATION; NOT-VERIFIED / CAPABILITY-GAP چون Provider-level Write + independent Read-back در Runtime در دسترس نیست.

این وضعیت به‌معنای شکست معماری نیست؛ به‌معنای ثبت صادقانه مرز قابلیت است.

## 17. Hammer Closure — چکش

چکش این تغییر را به‌عنوان **Architectural Change** شناسایی کرد، نه تغییر نام Buffer. بنابراین از این نسخه، هر ثبت جدید باید با مدل سه‌سطحی ارزیابی شود.

آزمون‌های اجباری:
- **AT-3L-01:** یک Production ID در هر سه سطح یکسان بماند.
- **AT-3L-02:** شکست Memory باعث از بین رفتن Repository/Buffer نشود.
- **AT-3L-03:** شکست Repository باعث از بین رفتن Buffer نشود.
- **AT-3L-04:** Buffer Payload کامل داشته باشد، نه Trace.
- **AT-3L-05:** هیچ سطحی وضعیت VERIFIED سطح دیگر را به ارث نبرد.
- **AT-3L-06:** تغییر Version/Revision، Verification قبلی را بدون Revalidation معتبر نکند.
- **AT-3L-07:** Memory بدون independent provider Read-back هرگز VERIFIED نشود.

## 18. Continuity Rule

از این نسخه، فرمان «ثبت کن» به‌صورت پیش‌فرض به معنی:

**CAPTURE → ONE ID → COMPLETE PAYLOAD → THREE-SURFACE REGISTRATION → THREE-SURFACE STATE CAPTURE → READ-BACK/MATCH/VERIFY/RECONCILE → STATUS**

است؛ و در صورت محدودیت، همان تولید با همان هویت وارد مسیر Recovery می‌شود.

**NO CLAIM WITHOUT EVIDENCE.**
**PRESERVE → IDENTIFY → VERIFY → RECONCILE → REGISTER → PROMOTE.**