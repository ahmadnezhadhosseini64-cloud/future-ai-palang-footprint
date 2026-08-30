# سند مرجع — اصل حفظ مسیر تداوم و بازیابی

**Reference ID:** REF-CPP-2026-08-30-001  
**Principle ID:** CPPP-2026-08-30-001  
**Project:** Future AI / Palang Footprint  
**Type:** Reference Document / Permanent Principle  
**Version:** 1.0  
**Date:** 2026-08-30  
**Status:** ACTIVE / CANONICAL REFERENCE  
**Approval:** User-approved for implementation  
**Canonical companion:** `docs/protocols/CONNECTION-CHAIN-PROTOCOL.md`  

## 1. اصل

**اصل حفظ مسیر تداوم و بازیابی (Continuation Path Preservation & Recovery Principle)**

هیچ شروع گپ، بازگشت از `00`، تغییر موقت زمینه، محدودیت ابزار، یا پیام آغازین مانند «درود و مهر» نباید به‌خودی‌خود مسیر پروژه را تغییر دهد، بازنشانی کند یا با یک موضوع مشابه جایگزین کند.

هر نقطه توقف قابل ادامه، به‌ویژه `0.0`، باید یک **Continuation Anchor** داشته باشد که مسیر واقعی کار را قابل بازیابی کند.

## 2. حداقل اطلاعات اجباری Anchor

- Checkpoint ID
- Project / branch / path identity
- Exact goal at stop
- Work status: `UNFINISHED`, `COMPLETED — CONTINUE`, `PAUSED`, `CLOSED`
- Last verified action
- Last verified artifact/evidence
- Exact unfinished task(s)
- Exact next intended action
- Governing decisions/rules
- Active `00` detour and return target
- Open reconciliation records
- Proven/verified items
- Unverified items
- Dependencies/blockers
- Recovery source(s)
- Version/date/time/timezone

## 3. قاعده ادامه

> **No Explicit New Target → Resume the Last Valid Continuation Anchor**

اگر وضعیت `UNFINISHED` باشد، ابتدا همان کار ناتمام ادامه می‌یابد.

اگر وضعیت `COMPLETED — CONTINUE` باشد، کار تمام‌شده دوباره ناتمام فرض نمی‌شود؛ ادامه از هدف رشد/تکمیل ثبت‌شده انجام می‌شود.

## 4. قاعده Greeting

«درود و مهر» و پیام‌های آغازین مشابه، **Connection Event** هستند و Project Command محسوب نمی‌شوند؛ بنابراین حق تغییر مسیر پروژه را ندارند.

## 5. قاعده عدم حدس

اگر Anchor دقیق یا مسیر قبلی قابل بازیابی نباشد:

`RECOVERY REQUIRED / NO GUESS`

در این وضعیت، جایگزین‌کردن یک موضوع مشابه، ساختن مسیر فرضی، یا ادامه‌دادن از حافظه ناقص ممنوع است.

## 6. ارتباط با ثبت و مستندسازی

این اصل بخشی از Connection Chain است و با Production Registry، Dual Durable Registration، Deferred Reconciliation، Evidence Integrity و Checkpoint/0.0 یکپارچه اجرا می‌شود.

تولید رسمی فقط زمانی `COMPLETED` تلقی می‌شود که وضعیت هر مقصد لازم، Evidence، Verification و Reconciliation آن مشخص باشد.

## 7. وضعیت لایه‌های ثبت این اصل

| مقصد | وضعیت در این ثبت |
|---|---|
| تعریف و تصویب کاربر | **APPROVED** |
| Canonical Reference Document | **COMPLETED / VERIFIED** پس از بازیابی فایل از مخزن |
| Architecture placement | **COMPLETED / VERIFIED** |
| Connection Chain integration | **COMPLETED / VERIFIED** |
| Persistent Memory | **PENDING / UNAVAILABLE IN THIS SESSION** |
| Independent memory verification | **PENDING** |

## 8. الزام جلوگیری از تکرار

هر تولید رسمی جدید باید پیش از اعلام نهایی از یک Finalization/Registration Gate عبور کند که این موارد را بررسی کند:

1. Identity / unique ID
2. Classification
3. Architecture placement
4. Reference-document placement
5. Runtime/playground placement when applicable
6. Production Registry record
7. Persistent Memory state when applicable
8. Canonical Repository state
9. Evidence
10. Verification
11. Reconciliation status
12. Recovery/Continuation Anchor when the production affects continuity

هیچ مقصد ناموفق نباید باعث حذف موفقیت مقصد دیگر شود و هیچ مقصد موفقی نباید به‌جای مقصد دیگر تلقی شود.

## 9. حقیقت اجرایی

این سند تضمین نمی‌کند که هیچ خطای آینده‌ای ممکن نیست. تضمین اجرایی قابل قبول این است که **خطا باید قابل تشخیص، قابل ثبت، قابل بازیابی و قابل reconciliation باشد و نباید مسیر پروژه را به‌صورت خاموش تغییر دهد.**

## 10. Canonical Rule

این سند به‌عنوان سند مرجع اصل فوق در شاخه `docs/reference/` نگهداری می‌شود. هر تغییر آینده باید با Version/ID جدید یا ارتقای کنترل‌شده همین سند و با Evidence ثبت شود.
