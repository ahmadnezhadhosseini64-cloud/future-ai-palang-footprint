# اصل تکمیل و زنده‌سازی یافته‌های ناقص — Archive Revival Completion & Living Principle

Production ID: ARCLP-2026-09-01-001
Reference: 0.0
Status: ACTIVE / LIVING / PERMANENT
Language: فارسی + English

## فارسی

### اصل
هر artifact، rule، command، protocol، architecture، checkpoint، production، recovery record یا discovery که در هر خاک‌برداری تاریخی پیدا شده اما به‌علت محدودیت ابزار، خطا، قطع دسترسی، شکست Verify/Read-back، کمبود Evidence، محدودیت Memory یا هر مانع دیگری نهایی نشده باشد، «گمشده» یا صرفاً «بازیابی‌شده» محسوب نمی‌شود. برای آن باید در معماری یک جایگاه پایدار در Pending / Recovery / Candidate Path / Provenance ایجاد یا حفظ شود تا در خاک‌برداری و زنده‌سازی بعدی مستقیماً از همان یافته، همان Stable ID و همان Provenance وارد مرحله تکمیل و زنده‌سازی واقعی شود.

### قاعده عدم تکرار خاک‌برداری
اگر یافته قبلاً شناسایی شده و رکورد/Provenance آن موجود است، عملیات بعدی نباید صرفاً همان مورد را دوباره کشف کند. باید ابتدا آن یافته را Retrieve کرده و از آخرین نقطه ناتمام ادامه دهد:

RETRIEVE → IDENTIFY/CLASSIFY → RECONCILE WITH PRIOR ATTEMPT → COMPLETE MISSING PARTS → REVIVE/ABSORB → INHERIT 0.0/MASTER → REGISTER → APPLY/TEST → EVIDENCE → READ-BACK → VERIFY → CLOSE

اگر تکمیل دوباره شکست خورد، همان Production ID حفظ می‌شود و فقط وضعیت و علت شکست به‌روزرسانی می‌شود؛ مورد به Pending/Recovery برمی‌گردد و برای چرخه بعدی آماده می‌ماند. ID جدید برای همان مورد ساخته نمی‌شود مگر اینکه واقعاً artifact مستقلی باشد.

### اصل «FOUND ≠ REVIVED»
پیدا شدن یک مورد به معنی زنده‌شدن آن نیست. زنده‌سازی واقعی فقط وقتی اعلام می‌شود که محتوای قابل استفاده آن بازیابی، با وضعیت فعلی reconcile، قوانین مادر 0.0/MASTER بر آن اعمال، ثبت Canonical انجام و Read-back/Verify موفق شده باشد؛ در غیر این صورت وضعیت باید صادقانه Pending/Unverified باقی بماند.

### زبان
هر artifact احیاشونده‌ای که به‌عنوان سند معماری/قاعده رسمی ثبت می‌شود باید در صورت امکان نسخه فارسی و English آن را همراه داشته باشد. حذف یا ناقص‌کردن یکی از دو زبان نباید به‌عنوان تکمیل نهایی گزارش شود.

### No-Drop
هیچ مورد ناقص به‌دلیل محدودیت نباید گم شود. حداقل رکورد لازم: Stable/Production ID، Provenance، آخرین مرحله موفق، مرحله شکست‌خورده/ناقص، علت یا Evidence موجود، وضعیت Pending/Recovery، و Next Transition.

## English

### Principle
Any artifact, rule, command, protocol, architecture, checkpoint, production, recovery record, or discovery found during a historical excavation but not finalized because of tool limitations, errors, unavailable access, failed verification/read-back, insufficient evidence, memory limitations, or any other blocker MUST NOT be treated as lost or merely recovered. It MUST retain or receive a durable architectural position in Pending / Recovery / Candidate Path / Provenance so that a future excavation-and-revival cycle can continue directly from the existing finding, the same Stable ID, and the same provenance toward actual completion and revival.

### No-Redig Rule
When a finding has already been identified and its record/provenance exists, a later cycle MUST NOT merely rediscover it. It MUST first retrieve the existing finding and continue from its last incomplete point:

RETRIEVE → IDENTIFY/CLASSIFY → RECONCILE WITH PRIOR ATTEMPT → COMPLETE MISSING PARTS → REVIVE/ABSORB → INHERIT 0.0/MASTER → REGISTER → APPLY/TEST → EVIDENCE → READ-BACK → VERIFY → CLOSE

If completion fails again, preserve the same Production ID and update only the state and failure evidence. Return it to Pending/Recovery for the next cycle. Do not create a duplicate ID unless it is genuinely an independent artifact.

### FOUND ≠ REVIVED
Discovery does not equal revival. Actual revival may be declared only when the usable content has been recovered, reconciled with the current state, inherited the 0.0/MASTER rules, canonically registered, and successfully read back and verified. Otherwise the state remains honestly Pending/Unverified.

### Bilingual Requirement
Any revived artifact that becomes a formal architectural rule/document should, where applicable, retain both Persian and English versions. Missing one language must not be represented as final completion.

### No-Drop
No incomplete item may be lost because of a limitation. At minimum preserve: Stable/Production ID, provenance, last successful stage, failed/incomplete stage, known cause/evidence, Pending/Recovery state, and next transition.

## Integration
This principle inherits the existing Archive Revival Search Method (ARSM-2026-08-31-001), the 0.0 reference chain, the No-Drop rule, Pending/Recovery continuity, and the distinction between FOUND, VALIDATED, REVIVED, and VERIFIED.

## Evidence Boundary
This file records the rule canonically. Its operational application to each historical item requires separate retrieval and verification evidence; this rule does not itself claim that every historical item has already been revived.
