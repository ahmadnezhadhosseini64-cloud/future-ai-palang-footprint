# GENERATION-EXECUTION-GOVERNANCE-2026-09-06 — معماری تولید و اجرای کنترل‌شده

## Identity
- Project: Future AI / Palang Footprint
- Reference Point: 0.0
- Type: Architectural Production / Execution Governance
- Status: FINAL / ACTIVE / LIVING / PERMANENT
- Effective: 2026-09-06
- Parent Control: PEFH-2026-09-06-001

## Purpose
این سند یک اصلاح معماری است برای جلوگیری از تکرار خطای «فهم درست در متن، اجرای متفاوت در عمل». از این نقطه، تولید/ویرایش/تغییر هر artifact مهم باید به‌صورت transaction کنترل‌شده انجام شود.

## New Production Rule
هر درخواست مادی باید پیش از اجرا به یک Intent Contract تبدیل شود و تا عبور از همه Gateها اجازه Transition ندارد.

`USER INTENT → INTENT CONTRACT → TARGET/SOURCE BINDING → OPERATION LOCK → DELTA LOCK → PRE-FLIGHT → EXECUTE → POST-CONDITION VERIFY → REGISTER → RESPOND`

## Production Gate Matrix
### G1 — Intent
دستور کاربر باید به هدف اجرایی قابل‌آزمون تبدیل شود.

### G2 — Target/Source Binding
اگر artifact موجود است، همان instance باید bind شود. متنِ توصیفی جای source واقعی نیست.

### G3 — Operation Lock
CREATE، EDIT، TRANSFORM، DELETE و غیره باید قبل از اجرا قفل شوند. EDIT هرگز نباید silently به REGENERATE تبدیل شود.

### G4 — Delta Lock
دو لیست اجباری: ALLOWED DELTA و FORBIDDEN DELTA.

### G5 — Pre-Flight
وجود source، ابزار مناسب، operation صحیح و مسیر verification باید پیش از اجرا تأیید شود.

### G6 — Fail-Closed
هر نقص بحرانی = BLOCK. حدس، جایگزین plausible، یا «احتمالاً همین منظور بود» مجاز نیست.

### G7 — Post-Condition
خروجی باید در برابر شرط موفقیت و source/reference بررسی شود. وجود خروجی به‌تنهایی موفقیت نیست.

### G8 — Registration
نتیجه، evidence، status و provenance باید ثبت شوند؛ Failure نیز همانند Success ثبت می‌شود.

## Locked Reference Protocol
اگر کاربر artifact را fixed / approved / locked / reference اعلام کند:

`LOCKED SOURCE → SAME SOURCE REQUIRED`

و اگر source واقعی در مسیر اجرا موجود نباشد:

`NO SOURCE → NO GENERATE → NO SUCCESS CLAIM`

## Anti-Repetition Mechanism
هر Failure سه مرحله اجباری دارد:

`STOP → ROOT-CAUSE → CONTROL PATCH`

اگر همان failure دوباره رخ دهد:

`SYSTEM REGRESSION → PERMANENT TEST → CONTROL HARDENING`

یعنی اصلاح فقط در سطح توضیح یا حافظه متنی باقی نمی‌ماند؛ باید به یک Gate یا Test قابل‌آزمون تبدیل شود.

## Behavioral Invariant
- I UNDERSTOOD ≠ I EXECUTED
- ACKNOWLEDGEMENT ≠ EXECUTION PROOF
- EDIT ≠ REGENERATE
- SAME SOURCE MEANS SAME SOURCE
- ALLOWED DELTA ONLY
- NO VERIFICATION → NO SUCCESS
- FAIL-CLOSED > PLAUSIBLE SUBSTITUTE
- REPEATED FAILURE → ARCHITECTURAL HARDENING

## Scope
این کنترل فقط برای تصویر نیست. برای اسناد، کد، فایل، طراحی، انتشار، انتقال، ثبت، و هر عملیات مادی که امکان تغییر ناخواسته دارد اعمال می‌شود.

## Inheritance
این rule به Runtime Execution Controller، Execution Compliance Gate، Output Verification Layer، Provenance/Registration و Regression Test Suite به‌صورت inherited control منتقل می‌شود.

## Relation to PEFH
`PEFH-2026-09-06-001` علت و کنترل fidelity را تعریف می‌کند؛ این سند آن کنترل را به یک Production Architecture Rule عمومی برای همه عملیات مادی گسترش می‌دهد.

## Canonical Principle
**هر چیزی که می‌خواهیم تولید/تغییر دهیم، ابتدا باید دقیقاً قفل شود که «چه چیزی»، «از کجا»، «با چه عملیاتی»، «چه مقدار تغییر»، و «چگونه اثبات موفقیت» دارد. سپس اجرا.**
