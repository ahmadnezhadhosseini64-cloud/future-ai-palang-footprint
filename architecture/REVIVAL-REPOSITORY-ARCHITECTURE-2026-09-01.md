# مخزن زنده‌سازی — Revival Repository

- Production ID: `REVIVAL-REPOSITORY-ARCHITECTURE-2026-09-01-001`
- Reference: `0.0`
- Status: `ACTIVE / LIVING / ARCHITECTURAL`
- Language: `فارسی + English`
- Type: `Architecture / Continuity / Historical Lineage`

## فارسی

### هدف
«مخزن زنده‌سازی» جایگاه معماری دائمی برای هر یافته یا تولید ارزشمندی است که در خاک‌برداری پیدا می‌شود اما به هر دلیل هنوز نهایی و زنده نشده است. هدف آن جلوگیری از Loss, Orphaning و دفن شدن داده و تبدیل یافته تاریخی به یک رکورد قابل ادامه است.

### قاعده اصلی
هر یافته پس از کشف باید ارزیابی شود:

- اگر کامل، نهایی، ثبت، اعمال و Verify شد: وارد `ACTIVE / LIVING` می‌شود و از صف Pending خارج می‌شود.
- اگر به هر دلیل کامل نشد: صرفاً گزارش نمی‌شود و حذف یا دفن نمی‌شود؛ با همان `Stable ID / Production ID`، `Provenance`، محتوای یافته، وضعیت، علت توقف، Evidence و `Next Transition` در `Revival Repository / Pending Queue` قرار می‌گیرد.
- زنده‌سازی بعدی باید همان رکورد را Retrieve کند و از آخرین نقطه معتبر ادامه دهد؛ نه اینکه فقط دوباره همان یافته را کشف یا گزارش کند.

### چرخه اجرایی
`RETRIEVE → IDENTIFY/CLASSIFY → VALIDATE → DEDUPLICATE → RECONCILE → COMPLETE → REVIVE/ABSORB → ARCHITECTURAL PLACEMENT → REGISTER → READ-BACK → VERIFY → ACTIVE/LIVING`

اگر گیت باقی بماند:

`SAME ID + SAME PROVENANCE → PENDING/RECOVERY → NEXT TRANSITION → LATER REVIVAL → RESUME FROM LAST VALID POINT`

### اصل عدم دفن
`FOUND ≠ REPORT ONLY`

`INCOMPLETE ≠ LOST`

`PENDING ≠ BURIED`

`PENDING = PRESERVED + TRACEABLE + RESUMABLE`

هیچ محدودیت ابزار، اتصال، Memory، ثبت، Verification یا خطای اجرایی به‌تنهایی مجوز حذف یافته از lineage نیست.

### ارزش تاریخی و معماری
هر یافته ارزشمند باید بتواند در حد شواهد موجود نشان دهد:

`IDEA/FINDING → WHY IT MATTERED → WHAT WAS PRESERVED → ARCHITECTURAL DECISION → WHERE IT ENTERED THE PROJECT`

بنابراین Revival Repository فقط صف خطا نیست؛ یک لایه برای `Historical Lineage / Architectural Evolution Trace` نیز هست.

### خروجی گفت‌وگو
گزارش‌های مرتبط با این جریان باید اصطلاحات کلیدی را برای فهم بهتر کاربر به صورت دوزبانه ارائه کنند؛ نمونه:

- مخزن زنده‌سازی — `Revival Repository`
- صف انتظار — `Pending Queue`
- زنده‌سازی — `Revival`
- منشأ و ردپا — `Provenance`
- جایگاه معماری — `Architectural Placement`
- مسیر ادامه — `Next Transition`

### Evidence Gate
Pending می‌تواند زنده و قابل ادامه باشد، اما تا زمانی که Evidence، Registration، Read-back و Verification لازم تکمیل نشده‌اند، نباید `ACTIVE / VERIFIED` به‌صورت ادعایی اعلام شود.

## English

### Purpose
The `Revival Repository` is a permanent architectural home for every valuable finding or production discovered during excavation but not yet finalized and revived for any reason. Its purpose is to prevent loss, orphaning, and burial, and to turn historical findings into resumable records.

### Core Rule
After discovery, every finding is evaluated:

- If it is complete, finalized, registered, applied, and verified, it becomes `ACTIVE / LIVING` and leaves the Pending queue.
- If it cannot be completed for any reason, it is not merely reported, deleted, or buried. The same `Stable ID / Production ID`, `Provenance`, finding content, state, stop reason, Evidence status, and `Next Transition` remain in the `Revival Repository / Pending Queue`.
- Later revival must Retrieve the same record and resume from its last valid point, not merely rediscover or re-report it.

### Execution Cycle
`RETRIEVE → IDENTIFY/CLASSIFY → VALIDATE → DEDUPLICATE → RECONCILE → COMPLETE → REVIVE/ABSORB → ARCHITECTURAL PLACEMENT → REGISTER → READ-BACK → VERIFY → ACTIVE/LIVING`

If a gate remains blocked:

`SAME ID + SAME PROVENANCE → PENDING/RECOVERY → NEXT TRANSITION → LATER REVIVAL → RESUME FROM LAST VALID POINT`

### No-Burial Principle
`FOUND ≠ REPORT ONLY`

`INCOMPLETE ≠ LOST`

`PENDING ≠ BURIED`

`PENDING = PRESERVED + TRACEABLE + RESUMABLE`

No tool, connection, Memory, registration, verification, or execution limitation by itself authorizes removal of a finding from lineage.

### Historical and Architectural Value
Every valuable finding should preserve, to the extent supported by evidence:

`IDEA/FINDING → WHY IT MATTERED → WHAT WAS PRESERVED → ARCHITECTURAL DECISION → WHERE IT ENTERED THE PROJECT`

Therefore the Revival Repository is not merely an error queue; it is also a layer for `Historical Lineage / Architectural Evolution Trace`.

### Conversation Output
Outputs in this flow should present key concepts bilingually for clarity, e.g.:

- مخزن زنده‌سازی — `Revival Repository`
- صف انتظار — `Pending Queue`
- زنده‌سازی — `Revival`
- منشأ و ردپا — `Provenance`
- جایگاه معماری — `Architectural Placement`
- مسیر ادامه — `Next Transition`

### Evidence Gate
Pending may be alive and resumable, but it must not be falsely declared `ACTIVE / VERIFIED` until the required Evidence, Registration, Read-back, and Verification are complete.

## Inheritance from 0.0 / Master
This architecture inherits the current 0.0/Master constraints: No-Drop / No-Orphan, Stable Identity / No Duplicate, Traceable Execution, Evidence Gate, Registration Continuity, Recovery Preservation, Retrieval-before-response, and bilingual Persian + English operational clarity.
