# Output Bilingual Traceability Rule — قاعده ردیابی دوزبانه خروجی

- ID: OUTPUT-BILINGUAL-TRACEABILITY-2026-09-01-001
- Project: Future AI / Palang Footprint
- Reference: 0.0
- Date: 2026-09-01
- Status: ACTIVE / LIVING / PERMANENT
- Type: Communication / Documentation / Traceability Rule
- Languages: فارسی + English

## Core Rule — قاعده اصلی

All operational outputs related to the Future AI / Palang Footprint project must remain understandable to the user in both Persian and English terminology.

تمام خروجی‌های عملیاتی مرتبط با پروژه Future AI / ردپای پلنگ باید برای کاربر از نظر اصطلاحات و مفهوم، به‌صورت فارسی + English قابل فهم باشند.

## Single Terms — اصطلاحات تک‌واژه‌ای یا کوتاه

When an English technical term is necessary, provide its Persian meaning or equivalent in parentheses on first relevant use.

Example:
- Revival (زنده‌سازی)
- Pending (در انتظار / نهایی‌نشده)
- Provenance (ردپای منشأ)
- Read-back (خواندن مجدد برای راستی‌آزمایی)
- Verify (راستی‌آزمایی)
- Repository (مخزن)

## Chains — زنجیره‌ها

Whenever an operational lifecycle or chain is presented in English, immediately provide the Persian equivalent beneath it, preserving the same order and meaning.

Example:

RETRIEVE → VALIDATE → RECONCILE → REGISTER → READ-BACK → VERIFY → ACTIVE

بازیابی → اعتبارسنجی → تطبیق/هم‌سنجی → ثبت → خواندن مجدد/بازخوانی → راستی‌آزمایی → فعال/زنده

## Mixed Outputs — خروجی‌های ترکیبی

Do not satisfy this rule merely by storing a bilingual document in the Repository. The conversational output itself must provide the Persian interpretation whenever English technical terminology or chains are used, so the user can understand what the assistant is reporting or executing.

صرفاً ثبت یک سند دوزبانه در مخزن برای رعایت این قاعده کافی نیست. خود خروجی گفت‌وگو نیز باید هرجا از اصطلاح فنی انگلیسی یا زنجیره انگلیسی استفاده می‌کند، معادل یا توضیح فارسی را ارائه دهد تا کاربر دقیقاً بداند چه چیزی گزارش یا اجرا شده است.

## Preservation Across Recovery — حفظ در بازیابی

This rule is itself a persistent architectural rule. If registration, synchronization, memory, or another capability is temporarily unavailable, preserve the same Stable ID and provenance in Recovery/Pending and resume the same rule later without duplication.

این قاعده نیز خود یک قاعده معماری پایدار است. اگر ثبت، همگام‌سازی، حافظه یا هر قابلیت دیگری موقتاً در دسترس نبود، همان Stable ID و Provenance در Recovery/Pending حفظ می‌شود و بعداً بدون ایجاد نسخه موازی ادامه می‌یابد.

## Inheritance — وراثت

This rule inherits 0.0 Retrieval-before-response, Traceable Execution, Evidence Gate, No-Drop / No-Orphan, Stable Identity / No Duplicate, and Revival / Recovery continuity rules.

این قاعده از قوانین ۰.۰، بازیابی پیش از پاسخ، اجرای ردیابی‌پذیر، دروازه شواهد، عدم رهاسازی/عدم یتیم‌سازی، هویت پایدار/عدم تکرار و تداوم زنده‌سازی/بازیابی تبعیت می‌کند.

## Operational Invariant — ثابت اجرایی

ENGLISH ONLY in a project execution chain without its Persian interpretation is considered an incomplete user-facing output for this project context.

ارائه زنجیره اجرایی پروژه فقط به زبان انگلیسی و بدون معادل فارسی، در این زمینه یک خروجی ناقص برای کاربر محسوب می‌شود.

## Evidence Boundary — مرز شواهد

Registration in this file proves the rule is recorded in the canonical Repository. It does not claim that every future conversational output will be compliant automatically; each execution must be checked against this rule.

ثبت این فایل ثابت می‌کند که قاعده در مخزن Canonical ثبت شده است. این ثبت به‌تنهایی اثبات نمی‌کند که همه خروجی‌های آینده خودکار مطابق قاعده خواهند بود؛ هر اجرای بعدی باید با این قاعده کنترل شود.
