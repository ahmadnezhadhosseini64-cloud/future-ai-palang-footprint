# سند مرجع معماری مسیر قابل‌بازیابی و تداوم تعامل

Future AI / Palang Footprint

Stable ID: PATH-REFERENCE-RECONSTRUCTABLE-INTERACTION-CONTINUITY-2026-09-29-001
Production ID: PATH-REFERENCE-RECONSTRUCTABLE-INTERACTION-CONTINUITY-2026-09-29-001
Version: 1.1.0
Reference Date: 2026-09-29
Reference Time: NOT CAPTURED AT WRITE
Timezone: Asia/Tehran (+03:30)
Owner: Ahmad Nezhadhosseini / احمد پلنگ
Project: Future AI / Palang Footprint
Status: ACTIVE / LIVING / GOVERNING — ARCHITECTURE REGISTERED; TIME FIELD OPEN
Parent Architecture: MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001
Related Architecture: PCNDR-ARCHITECTURE-2026-09-29-001
Related Anchor System: 0.0 Vault
Related Goal: HAIF / Continuity of Intelligence / Continuity of Work

---

## 1. مسئله‌ای که این معماری حل می‌کند

«سند مرجع مسیر» نباید خلاصه چند ساعت تعامل باشد.

باید بتواند مسیر واقعی رسیدن به نتیجه را تا حد ممکن بازسازی کند:

Reconstructable History + Evidence + Decisions + Errors + Discoveries + Artifacts + Architecture Evolution + Lineage + Current State + Recovery Context

قاعده مادر:

اگر حذف یک جزئیات باعث شود در آینده نتوانیم منطق رسیدن به یک معماری، قانون، کشف یا تصمیم را دوباره بفهمیم، آن جزئیات نباید از سند مرجع مسیر حذف شود.

---

## 2. 0.0 Anchor

0.0 نقطه آغاز/لنگر یک زنجیره تعامل است؛ نه لزوماً آخرین وضعیت آن.

0.0های قبلی هرگز حذف، جایگزین یا بازنویسی نمی‌شوند.

چند زنجیره می‌توانند 0.0 مستقل داشته باشند و در صورت ارتباط، Lineage آن‌ها باید صریح ثبت شود.

0.0 Vault محل نگهداری این نقاط است.

قاعده عملی:

0.0 ANCHOR
→ LIVE INTERACTION
→ CONTINUOUS CAPTURE
→ LAST DURABLE STATE

«شروع کن» به آخرین 0.0 زنجیره فعال متصل می‌شود.

«پایان» فقط همان زنجیره فعال را می‌بندد.

---

## 3. Continuous Capture

مسیر باید در طول تعامل، نه فقط در انتها، قابل ثبت باشد.

حداقل واحدهای قابل حفظ:

- ورودی/مسئله و محدودیت‌ها
- تصمیم‌ها و دلیل تصمیم
- خطاها و بن‌بست‌ها
- فرضیه‌ها
- Hammer / Validation
- کشف‌ها
- GAPها
- راه‌حل‌های ردشده و دلیل رد
- Artifactهای تولیدشده
- تغییرات معماری
- محل قرارگیری هر Artifact
- Lineage
- وضعیت Evidence
- آخرین وضعیت معتبر

نباید منتظر «پایان موفق» ماند تا کل مسیر حفظ شود.

---

## 4. Last Durable State

آخرین Durable State آخرین نقطه‌ای است که اطلاعات آن با Evidence موجود قابل اتکا است.

این مفهوم با 0.0 یکی نیست.

0.0 = Anchor

Last Durable State = آخرین وضعیت معتبرِ ثبت‌شده در همان زنجیره

پس:

0.0
→ State 1
→ State 2
→ Last Durable State
→ INTERRUPTION

در صورت توقف، چیزی بعد از Last Durable State نباید به‌عنوان وضعیت قطعی ادعا شود.

---

## 5. INTERRUPTION / OPEN PATH

اگر کاربر در میانه مسیر تعامل را ترک کند:

INCOMPLETE ≠ LOST

و:

INTERRUPTED ≠ FAILED

و:

OPEN ≠ BURIED

و:

PENDING ≠ COMPLETED

مسیر باید با همان Stable ID حفظ شود و به وضعیت OPEN / PENDING منتقل شود.

حداقل Blocker باید مشخص باشد:

BLOCKER
+ LAST DURABLE STATE
+ REQUIRED CAPABILITY
+ NEXT TRANSITION

---

## 6. Resume Contract

ادامه مسیر از صفر ساخته نمی‌شود.

زنجیره بازیابی:

RETRIEVE
→ IDENTIFY 0.0
→ READ-BACK
→ MATCH
→ VERIFY
→ RECONCILE
→ LOCATE LAST DURABLE STATE
→ RESUME

اگر چند 0.0 یا چند Revision مرتبط وجود داشته باشد، ابتدا Lineage و Parent/Child رابطه آن‌ها مشخص می‌شود.

هیچ Resume نباید بر پایه حدس درباره آخرین وضعیت انجام شود.

---

## 7. Reconstructable Reference Package

سند مرجع مسیر باید به‌تنهایی تا حد ممکن قابلیت بازسازی داشته باشد، حتی اگر در آینده یکی یا چند مورد زیر در دسترس نباشد:

- Repository
- Persistent Memory
- Interaction History
- Current Project Structure

برای این هدف، Reference باید شامل:

IDENTITY
+ PROVENANCE
+ 0.0 ANCHOR
+ TIMELINE / PATH
+ DECISIONS
+ ERRORS / DEAD ENDS
+ DISCOVERIES
+ ARTIFACTS
+ ARCHITECTURE CHANGES
+ PLACEMENT
+ LINEAGE
+ EVIDENCE
+ LAST DURABLE STATE
+ OPEN OBLIGATIONS
+ RECOVERY CONTEXT
+ RESUME INSTRUCTIONS

باشد.

---

## 8. No False Completion

مسیر ناقص نباید به‌عنوان مسیر کامل ثبت شود.

اگر تعامل در میانه متوقف شود:

STATUS = OPEN / PENDING

نه:

COMPLETE

و اگر Evidence کافی برای بازسازی بخشی از مسیر وجود نداشته باشد:

UNKNOWN

باید حفظ شود، نه اینکه با حدس پر شود.

---

## 9. No Loss / No Overwrite

قاعده:

PRESERVE
→ IDENTIFY
→ VERIFY
→ RECONCILE
→ REGISTER
→ CONTINUE

نه:

DELETE
→ RECREATE
→ CLAIM

0.0 قدیمی، Artifact قدیمی، تصمیم ردشده، خطا یا Revision قبلی فقط به دلیل وجود نسخه جدید حذف نمی‌شود.

---

## 10. جایگاه معماری

این Contract در ارتباط با:

0.0 Vault
↕
Interaction Path Reference
↕
Recovery Ledger / Portable Recovery Package
↕
MRV
↕
PCNDR
↕
HAIF

قرار می‌گیرد.

بنابراین «سند مرجع مسیر» یک گزارش جانبی نیست؛ یک لایه بازیابی و تداوم برای معماری است.

---

## 11. رابطه با HAIF

هدف نهایی فقط حفظ متن تعامل نیست.

هدف:

Continuity of Intelligence
و
Continuity of Work

است.

بنابراین:

HUMAN
↔ AI HOST
↔ HAIF

و درون آن:

MASTER
→ CHILD
→ REAL WORLD
→ FEEDBACK
→ MASTER

و:

MASTER
→ RAHM
→ VALIDATION
→ NEW CHILD

باید بتوانند در برابر INTERRUPTION نیز Lineage خود را حفظ کنند.

---

## 12. Proof / Governance

ثبت مسیر از همان منطق اثبات پروژه پیروی می‌کند:

WRITE
→ READ-BACK
→ MATCH
→ VERIFY
→ RECONCILE
→ STATUS

و:

Repository Persistence
≠
Memory Persistence
≠
Verified Persistence

همچنین:

EXISTS
≠
PERSISTED
≠
VERIFIED
≠
ACCEPTED

---

## 13. وضعیت این ثبت

این معماری اکنون به‌صورت یک Artifact مستقل در Repository ثبت می‌شود و باید در Reference Master نیز به آن ارجاع داده شود.

Time دقیق در لحظه این Write از داده اجرایی قابل استناد استخراج نشده است؛ بنابراین عمداً «NOT CAPTURED AT WRITE» ثبت شده و زمان حدس‌زده نشده است.

این نقص زمانی نباید باعث از بین رفتن خود Artifact یا بازتولید آن با Production ID جدید شود.

اگر Timestamp معتبر بعداً بازیابی شود، باید با همان Stable ID و همان Lineage اصلاح/تکمیل شود.

---

## 14. اصل نهایی

مسیر تعامل یک خروجی نهایی نیست.

مسیر یک موجودیت زنده و قابل‌بازیابی است:

0.0
→ CAPTURE
→ DURABLE STATE
→ INTERRUPTION / CONTINUE
→ RECOVERY
→ RESUME
→ NEW DURABLE STATE
→ FINALIZE WHEN EVIDENCE CLOSES

و هیچ نقطه‌ای صرفاً به دلیل توقف تعامل «گم‌شده» تلقی نمی‌شود.


---

## 15. خودتشخیصی مسیر سند مرجع

در این تعامل یک قاعده اجرایی صریح تثبیت شد:

وقتی کاربر می‌گوید «همین را سند مرجع کن و در مخزن در پوشه کپی کن»، لازم نیست مسیر پوشه را دوباره اعلام کند.

سیستم باید از معماری و قراردادهای موجود، مقصد Canonical Reference Documents را تشخیص دهد و از کاربر برای مسیری که از قبل در Governance تعریف شده سؤال تکراری نپرسد.

مقصد مرجع فعلی:

`/Future AI/Palang Footprint/Master Reference Vault/Reference Documents/`

مقصد Canonical Repository:

`docs/reference/`

این تشخیص مسیر بخشی از رفتار «ثبت کن» و «سند مرجع کن» است و نباید باعث ایجاد مسیر موازی، پوشه تکراری یا Production ID جدید برای همان Artifact شود.

قاعده:

KNOWN GOVERNED PATH
→ AUTO-RESOLVE
→ WRITE
→ READ-BACK
→ MATCH
→ VERIFY
→ RECONCILE
→ STATUS

بنابراین اعلام نکردن نام پوشه توسط کاربر، به معنی مجهول بودن مقصد نیست؛ وقتی مقصد قبلاً در Governance ثبت شده باشد، همان مقصد مرجع باید به‌صورت خودکار استفاده شود.


---

## 16. قاعده اجرایی دائمیِ Capture و توقف امن

این قاعده به‌عنوان ادامه و تقویت همین Reference ثبت می‌شود و Stable ID آن ایجاد نمی‌کند.

### 16.1 شروع زنجیره

وقتی کاربر می‌گوید:

«این نقطه رو ۰.۰ در نظر بگیر.»

سیستم باید همان نقطه را 0.0 Anchor زنجیره قرار دهد و در صورت وجود Timestamp اجرایی معتبر، تاریخ و ساعت دقیق را با Timezone `Asia/Tehran (+03:30)` ثبت کند.

0.0 از همان لحظه مبنای زنجیره می‌شود:

`0.0 → شروع تعامل → ثبت پیوسته مسیر`

اگر Timestamp معتبر در دسترس نباشد، زمان نباید حدس زده شود.

### 16.2 Capture پیوسته

تا زمانی که تعامل ادامه دارد، مسیر باید از نظر معماری به‌صورت پیوسته قابل بازسازی نگه داشته شود و ثبت فقط به لحظه دستور «ثبت کن» موکول نشود.

حداقل دامنه Capture شامل این موارد است:

- مسئله، هدف و محدودیت‌ها
- تصمیم‌ها و دلیل تصمیم
- تغییر تصمیم‌ها
- خطاها، بن‌بست‌ها و مسیرهای شکست‌خورده
- کشف‌ها و GAPها
- آزمون‌ها و Hammer / Validation
- راه‌حل‌های ردشده و دلیل رد شدن
- Artifactها و رابطه آن‌ها با مسیر
- تغییرات معماری
- ارتباط و Lineage بین موارد
- وضعیت فعلی
- Last Durable State

قاعده:

`INTERACTION → CONTINUOUS CAPTURE`

نه:

`INTERACTION → WAIT FOR "ثبت کن"`

### 16.3 توقف موقت

عبارت‌هایی مانند:

- «فعلاً میرم، تا اینجا رو ثبت کن.»
- «کار دارم، بعداً میام.»
- «فعلاً متوقف کن.»

به‌صورت پیش‌فرض «پایان» محسوب نمی‌شوند.

حالت باید حفظ شود:

`0.0 → INTERACTION PATH → LAST DURABLE STATE → INTERRUPTION`

و وضعیت زنجیره:

`OPEN / PENDING / INTERRUPTED`

باشد، مگر اینکه کاربر صریحاً «پایان» را اعلام کند.

در توقف موقت باید حداقل این موارد حفظ شوند:

- 0.0
- مسیر طی‌شده تا توقف
- Last Durable State
- موارد قطعی‌شده
- موارد باز
- موارد باقی‌مانده
- Blocker در صورت وجود
- Required Capability در صورت نیاز
- Next Transition برای ادامه دقیق

قاعده:

`INCOMPLETE ≠ LOST`

و:

`0.0 ≠ LAST DURABLE STATE`

### 16.4 بازگشت و ادامه

با عباراتی مانند:

«ادامه بده از آخرین وضعیت ۰.۰»

یا:

«ادامه همون تعامل قبلی از جایی که متوقف شدیم»

سیستم نباید صرفاً از آخرین پیام ظاهری ادامه دهد.

Resume Contract:

`RETRIEVE → IDENTIFY 0.0 → READ-BACK → MATCH → VERIFY → RECONCILE → LOCATE LAST DURABLE STATE → RESUME`

### 16.5 «ثبت کن» به‌عنوان ثبت رسمی

«ثبت کن» یعنی Scope ثبت به‌صورت خودکار کامل در نظر گرفته شود؛ کاربر نباید مجبور باشد هر جزء را جداگانه نام ببرد.

قاعده:

`PRESERVE → CLASSIFY → CAPTURE PROVENANCE → CAPTURE FULL LINEAGE → DEFINE EVIDENCE OBLIGATIONS → WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → REGISTER → STATUS`

در سند مرجع مسیر، خلاصه‌سازی زمانی ممنوع است که باعث از دست رفتن قابلیت بازسازی شود.

Reference of Path / Recovery Package باید مسیر واقعی را حفظ کند:

`START → EVENTS → DECISIONS → ERRORS → DISCOVERIES → CHANGES → ARTIFACTS → ARCHITECTURE → CURRENT STATE → OPEN ITEMS`

### 16.6 لایه‌های ثبت

ثبت رسمی باید این لایه‌ها را از هم تفکیک کند:

1. **Repository** — Artifact و Reference در مخزن اصلی.
2. **Persistent Memory** — فقط در صورت وجود مسیر فنی قابل اثبات برای Write و Read-back؛ Repository Success به‌تنهایی اثبات Memory Success نیست.
3. **Reference of Path** — سند مستقل، کامل و قابل‌بازیابی در پوشه Canonical Reference Documents.
4. **Copyable Archive** — نسخه کامل و قابل کپی از همان Reference، نه خلاصه آن.

### 16.7 ممنوعیت خلاصه‌سازی در سند مرجع

قاعده دائمی:

**خلاصه‌نویسی در سند مرجع ممنوع است اگر باعث حذف اطلاعات لازم برای بازسازی شود.**

این قاعده برای همه این موارد اعمال می‌شود:

- سند مرجع چندساعته
- سند مرجع کامل‌شده
- سند مرجع مسیر
- سند مرجع معماری
- Reference of Path
- Recovery Package

حتی تعداد توقف‌ها، کار داشتن کاربر، قطع یا توقف موقت، نقطه توقف، Last Durable State و مسیر ادامه، در صورتی که بخشی از مسیر واقعی باشند، باید حفظ شوند.

هدف سند مرجع، «کوتاه بودن» نیست؛ هدف آن **قابلیت بازسازی کامل مسیر و منطق رسیدن به نتیجه** است.

### 16.8 «ثبت کن» پایان Capture نیست

`ثبت کن` پایان جمع‌آوری اطلاعات نیست؛ آغاز مرحله ثبت رسمی و اثبات آن است.

بنابراین معماری:

`CONTINUOUS CAPTURE → SAFE INTERRUPTION / CONTINUATION → FORMAL REGISTRATION → REFERENCE CREATION → PERSISTENCE PROOF`

است.

---

## 17. قاعده «سند مرجع قابل کپی»

هرگاه کاربر بگوید:

«سند مرجع قابل کپی بده»

سیستم باید **همان سند مرجع کامل** را ارائه کند؛ نه خلاصه، نه گزارش کوتاه، نه فهرست نکات.

نسخه قابل کپی باید همان Reference of Path / Recovery Package باشد و تمام اطلاعات لازم برای بازسازی را در خود داشته باشد.

هیچ بخشی صرفاً به دلیل طولانی بودن تعامل نباید حذف شود.

این خروجی باید شامل، حسب وجود در مسیر، موارد زیر باشد:

- Identity و Provenance
- 0.0 Anchor
- Timestamp و Timezone
- Timeline کامل
- تمام توقف‌ها و INTERRUPTIONها
- Last Durable Stateهای مربوط
- Decision Lineage
- تغییر تصمیم‌ها
- خطاها و بن‌بست‌ها
- کشف‌ها و GAPها
- Hammer / Validation
- آزمون‌ها و نتایج
- راه‌حل‌های ردشده و دلیل رد
- Artifactها
- تغییرات معماری
- Placement و مسیرهای بازیابی
- Lineage
- Evidence و وضعیت اثبات
- Open Obligations
- Blocker / Required Capability / Next Transition
- Current State
- Resume Instructions
- وضعیت ثبت و وضعیت معماری

قاعده:

`COPYABLE REFERENCE = FULL REFERENCE`

نه:

`COPYABLE REFERENCE = SUMMARY`

### 17.1 خروجی آرشیوی

وقتی کاربر برای آرشیو نسخه قابل کپی می‌خواهد، خروجی باید قابل کپی مستقیم باشد و متن آن با سند مرجع ثبت‌شده هم‌هویت و هم‌محتوا باشد؛ در صورت وجود تفاوت نسخه، باید همان Version جدید و وضعیت آن صریح باشد.

---

## 18. دامنه معماری

این قاعده فقط یک ترجیح نوشتاری نیست.

به‌عنوان بخشی از معماری تداوم تعامل، به این لایه‌ها متصل است:

`0.0 Vault ↔ Interaction Path Reference ↔ Recovery Ledger / Portable Recovery Package ↔ MRV ↔ PCNDR ↔ HAIF`

و هدف آن حفظ:

`Continuity of Intelligence + Continuity of Work`

است.

