# دروازه اجباری حاکمیت پیش از اجرا / Mandatory Pre-Execution Governance Gate

- Production ID / شناسه تولید: `MPGG-2026-09-01-001`
- Project / پروژه: Future AI / Palang Footprint
- Reference / مرجع: `0.0`
- Date / تاریخ: `2026-09-01`
- Exact Local Time / ساعت دقیق محلی: `17:24:00`
- IANA Timezone / منطقه زمانی IANA: `Asia/Tehran`
- Status / وضعیت: `FINAL / ACTIVE / LIVING`
- Authority / مرجع حاکم: `0.0 Master Reference`

## Final Decision / تصمیم نهایی

این سند، نقص معماری شناسایی‌شده را از یک توصیه به یک **دروازه اجباری پیش از اجرا** تبدیل می‌کند.

This document converts the identified regression from a recommendation into a **mandatory pre-execution gate**.

هیچ پاسخ، ثبت، آزمون، تصمیم یا اقدام معنادار نباید قبل از عبور از این دروازه تولید یا نهایی شود.

No meaningful response, registration, experiment, decision, or action may be finalized before this gate is resolved.

## Gate / دروازه

`0.0 LOCK`
→ `MASTER RETRIEVAL / بازیابی مرجع مادر`
→ `LATEST CHECKPOINT RETRIEVAL / بازیابی آخرین چک‌پوینت`
→ `APPLICABLE RULE RESOLUTION / حل قواعد قابل اعمال`
→ `BILINGUAL RULE RESOLUTION / حل قاعده فارسی + English`
→ `TIMESTAMP RESOLUTION / حل تاریخ + ساعت دقیق + Timezone`
→ `VALUE & NOVELTY DETECTION / تشخیص ارزش و تازگی`
→ `ACTION CLASSIFICATION / طبقه‌بندی اقدام`
→ `EXECUTE / اجرا`
→ `OUTPUT COMPLIANCE AUDIT / ممیزی انطباق خروجی`
→ `REGISTER OR PENDING / ثبت یا Pending`
→ `READ-BACK / بازخوانی`
→ `VERIFY / راستی‌آزمایی`
→ `CONTINUE / ادامه`

## Bilingual Invariant / اصل دوزبانگی

تمام موارد حاکمیتی، رکوردهای معماری، تولیدات، Checkpointها، Provenanceها، وضعیت‌ها و خروجی‌های رسمی باید در صورت تولید متنی، **فارسی + English** باشند.

All governance records, architecture records, productions, checkpoints, provenance records, statuses, and official textual outputs must be **Persian + English**.

این قاعده فقط برای Repository نیست؛ در مسیر پاسخ نهایی نیز اجباری است.

This rule applies not only to the Repository but also to the final-response path.

## Timestamp Invariant / اصل زمان‌مندی

هر اجرای رسمی باید Date / تاریخ، Exact Local Time / ساعت دقیق محلی و IANA Timezone / منطقه زمانی IANA را داشته باشد. اگر زمان دقیق معتبر در دسترس نیست، نباید زمان ساختگی تولید شود؛ وضعیت باید `TIME UNVERIFIED / زمان تأییدنشده` باشد.

## Automatic Valuable-Finding Recognition / تشخیص خودکار یافته ارزشمند

هر ورودی جدید باید پیش از عبور به اقدام اصلی از این آزمون عبور کند:

`NEWNESS / تازگی`
+ `VALUE POTENTIAL / ارزش بالقوه`
+ `TYPE / نوع`
+ `EVIDENCE STATE / وضعیت شواهد`

نوع‌ها شامل:
- `NEW FINDING / یافته جدید`
- `QUESTION / سؤال`
- `ANSWER / پاسخ`
- `EXPERIMENT / آزمون`
- `OPEN PROBLEM / مسئله باز`
- `RULE / قاعده`
- `ARCHITECTURE CHANGE / تغییر معماری`
- `RECOVERY ITEM / مورد بازیابی`
- `DUPLICATE / تکراری`
- `NO-VALUE / فاقد ارزش فعلی`

اصل مهم: **Potential Value must be preserved, not silently discarded. / ارزش بالقوه باید حفظ شود و بی‌صدا حذف نشود.**

اگر تازگی یا ارزش اثبات نشده باشد، مورد `CANDIDATE / PENDING` می‌شود، نه `VERIFIED` و نه `DISCARDED`.

## Output Compliance Gate / دروازه انطباق خروجی

پیش از ارسال هر خروجی رسمی، این موارد باید کنترل شوند:

1. Persian + English / فارسی + English
2. Date / تاریخ
3. Exact Local Time / ساعت دقیق
4. IANA Timezone / منطقه زمانی
5. Stable/Production ID / شناسه پایدار/تولید
6. `0.0` Reference / مرجع ۰.۰
7. Status / وضعیت
8. Evidence State / وضعیت شواهد
9. Provenance / منشأ و ردیابی

Failure of any mandatory field = `BLOCK / توقف` until corrected or explicitly marked `UNVERIFIED / تأییدنشده`.

## Anti-Drift Invariant / اصل ضد لغزش

`RULE EXISTS ≠ RULE RESOLVED ≠ RULE ENFORCED`

وجود قاعده به‌تنهایی کافی نیست. قاعده باید بازیابی، حل، اعمال و در خروجی ممیزی شود.

## 0.0 Protection / حفاظت از ۰.۰

هیچ اصلاحی نباید باعث از دست‌رفتن Continuation Anchor / لنگر ادامه شود.

`0.0 LOCK` همیشه پیش از اصلاح، آزمون یا تولید جدید اعمال می‌شود.

## Registration State / وضعیت ثبت

This is a **final architectural rule**, but implementation is considered fully proven only after a separate execution test demonstrates the gate blocks violations and automatically preserves a valuable novel finding.

این سند از نظر تصمیم معماری نهایی و زنده است؛ اما «اثبات اجرای کامل» فقط با آزمون اجرایی مستقل و Evidence معتبر قابل اعلام است.
