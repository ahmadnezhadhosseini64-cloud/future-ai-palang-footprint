# ضربه چکش پلنگ / Palang Hammer — Regression Analysis

- Production ID / شناسه تولید: `REGRESSION-HAMMER-2026-09-01-172130`
- Project / پروژه: Future AI / Palang Footprint
- Reference / مرجع: `0.0`
- Date / تاریخ: `2026-09-01`
- Exact Local Time / ساعت دقیق محلی: `17:21:30`
- IANA Timezone / منطقه زمانی IANA: `Asia/Tehran`
- UTC Offset / اختلاف UTC: `+03:30`
- Location / مکان: Iran / Gonbad-e Kavus (user-context; not GPS-verified)
- Status / وضعیت: `ACTIVE / INVESTIGATING / REGRESSION`

## هدف / Objective

تشخیص علت تکرار خطاهایی که مانع تشخیص مستقل ارزشمندبودن یافته جدید، آزمون، سؤال، پاسخ یا مسئله باز می‌شوند.

Identify why repeated execution drift occurs and why the system fails to consistently recognize a new valuable finding, experiment, question, answer, or open problem without an explicit user instruction.

## ضربه 1 — Rule Resolution Drift / لغزش در حل قواعد

The current 0.0 master reference explicitly requires retrieval of the master reference, latest checkpoint, and all applicable governing rules before continuation. It also requires Date, Exact Local Time, IANA timezone, location/status, previous reference, current state, Continuation Anchor, rule-resolution status, and verification status for every 0.0 record.

مرجع فعلی ۰.۰ این الزامات را صریحاً دارد. با این حال، در اجرای اخیر، پاسخ‌های آغازین بدون Timestamp کامل و بدون گزارش صریح Rule Resolution تولید شدند. این یعنی مشکل اصلی «نبودن قانون» نیست؛ مشکل، **عدم اجرای Gate قبل از تولید پاسخ** است.

## ضربه 2 — Bilingual Rule Not Resolved / قاعده دوزبانگی حل نشده

A repository search for explicit bilingual markers (`English`, `فارسی`, `دو زبانه`, `Date`, `Exact Local Time`) returned no matching governing record in the current repository search.

نتیجه: قاعده‌ای که کاربر آن را قبلاً به‌عنوان قاعده لازم برای همه ساختارهای ثبت و خروجی تعیین کرده، در مسیر فعلی به‌عنوان یک **Mandatory Governing Rule** قابل بازیابی نبود. بنابراین execution از آن عبور کرد.

این یک **Rule-Index / Rule-Resolution failure** است، نه صرفاً خطای نگارشی.

## ضربه 3 — Output Compliance Gate Missing / نبود دروازه انطباق خروجی

The system currently has persistence and verification rules, but the final-response path lacks a mandatory pre-send compliance gate that checks:

1. Persian + English presence / وجود فارسی + انگلیسی
2. Date / تاریخ
3. Exact Local Time / ساعت دقیق
4. IANA timezone / منطقه زمانی
5. Production/Stable ID / شناسه تولید/پایدار
6. 0.0 reference / مرجع ۰.۰
7. status / وضعیت
8. evidence state / وضعیت شواهد

Without this gate, a correct rule can exist while the produced response still violates it.

## ضربه 4 — Valuable Finding Recognition Gap / شکاف تشخیص ارزش

The architecture already contains Valuable Finding Recognition and Adaptive Discovery, but the trigger condition is not yet sufficiently operationalized as an automatic classifier.

The required behavior is:

ورودی جدید → تشخیص نوع → مقایسه با دانش/آرشیو موجود → تشخیص تازگی → تشخیص ارزش بالقوه → تشخیص آزمون/سؤال/پاسخ/مسئله باز → تعیین Candidate/Pending/Verified → ایجاد Provenance → ادامه چرخه بدون انتظار برای فرمان «ثبت کن».

A finding must not become VERIFIED merely because it is interesting; however, potentially valuable novelty must never be silently discarded.

## ضربه 5 — 0.0 Protection Failure Risk / خطر گم‌شدن ۰.۰

The user's concern is valid: chasing formatting or execution regressions can itself cause loss of the continuation anchor.

Therefore the first invariant must be:

`0.0 LOCK → RETRIEVE → RULE RESOLUTION → EXECUTION → COMPLIANCE AUDIT → REGISTER/RECOVER`

نه:

`EXECUTE → remember 0.0 later`.

## Root Cause / علت ریشه‌ای

The repeated errors are best classified as **pre-execution governance failures**:

`Rules exist → retrieval is partial → rule resolution is incomplete → execution begins → output is generated → compliance is discovered too late.`

The architecture therefore needs a **Mandatory Pre-Execution Governance Gate** that blocks execution until the applicable rules and continuation anchor are resolved.

## Required Next Architecture / معماری لازم برای گام بعد

Create a single mandatory gate before every meaningful response/action:

`0.0 LOCK`
→ `MASTER RETRIEVAL`
→ `LATEST CHECKPOINT RETRIEVAL`
→ `APPLICABLE RULE RESOLUTION`
→ `BILINGUAL COMPLIANCE RESOLUTION`
→ `TIMESTAMP COMPLIANCE RESOLUTION`
→ `VALUE/NEWNESS DETECTION`
→ `ACTION CLASSIFICATION`
→ `EXECUTE`
→ `OUTPUT COMPLIANCE AUDIT`
→ `REGISTER / PENDING`
→ `READ-BACK / VERIFY`
→ `CONTINUE`

## Non-Drop Rule / قاعده عدم ریزش

If the system detects a potentially valuable but unresolved finding, it must preserve it as Candidate/Pending with the same Stable ID and Provenance rather than discarding it.

اگر ارزش یا تازگی هنوز قطعی نیست، مورد نباید حذف شود و نباید بی‌دلیل VERIFIED شود؛ باید با Stable ID و Provenance در Candidate/Pending بماند.

## Evidence Boundary / مرز شواهد

This record proves the regression diagnosis and the existence of the stated 0.0 requirements. It does not by itself prove that the new automatic value-recognition gate has been implemented. Implementation requires a separate execution/evidence test.
