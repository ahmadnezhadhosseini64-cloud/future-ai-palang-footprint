# سند مرجع مادر — MRV / Master Reference Vault

## 0. شناسنامه و قفل هویت

- **Production ID / Stable ID:** `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001`
- **Artifact Type:** Architectural Control / Living Reference Vault / Recovery & Resume Contract
- **Project:** Future AI / Palang Footprint — آینده AI / ردپای پلنگ
- **Owner:** Ahmad Nezhadhosseini / احمد پلنگ
- **Origin:** معماری پروژه + چکش‌زدن چرخه کامل «ثبت کن» و «ثبت کن و سند مرجع زنده قرار بده»
- **Created Date:** `2026-09-15`
- **Created Time:** `03:17:24`
- **Timezone:** `Asia/Tehran (UTC+03:30)`
- **Current Evidence State at Creation:** `READY FOR LIBRARY WRITE → READ-BACK → MATCH → VERIFY`
- **Intended Status:** `ACTIVE / LIVING`
- **Destination:** `/Future AI/Palang Footprint/Master Reference Vault/`
- **Parent Architecture:** Future AI / Palang Footprint
- **Role:** Governing architectural reference for reference-document lifecycle, recovery, registration, verification, and automatic resume.

> این سند خودش «چرخه کامل ثبت» را تعریف می‌کند. وضعیت نهایی آن فقط از شواهد واقعی Persistence / Read-back / Match / Verify و Placement مشتق می‌شود؛ ادعای موفقیت بدون evidence مجاز نیست.

---

## 1. مسئله / GAP که این سند برای آن ایجاد شد

مسئله این بود که «سند مرجع» نباید یک متن موقت باشد که کاربر مجبور شود در هر خاک‌برداری دوباره ارسالش کند. یک سند مرجع باید:

1. هویت پایدار داشته باشد.
2. در معماری محل مشخص و قابل بازیابی داشته باشد.
3. نسخه، lineage و وضعیت آن حفظ شود.
4. هنگام «خاک‌برداری و زنده‌سازی» به‌عنوان منبع governing کشف و بازیابی شود.
5. در صورت ادامه کار، همان Stable ID و lineage حفظ شود.
6. در صورت failure یا unavailable capability، OPEN/PENDING بماند و گم نشود.
7. drift / conflict / supersession را تشخیص دهد.
8. بتواند بدون بازفرستادن کاربر، مبنای ادامه اجرای تعهدات باشد؛ مشروط به اینکه واقعاً persisted و قابل بازیابی باشد.

### Finding

**Reference Document باید از یک فایل آرشیوی به یک Architectural Living Control تبدیل شود.**

---

## 2. اصل مادر

**هیچ ارزش تولیدشده‌ای به علت محدودیت ابزار، interruption، failure، unavailable capability، ambiguity یا توقف نباید گم شود.**

اما «حفظ» با «انجام‌شدن» یکی نیست.

- Preservation ≠ Verification
- Retrieval ≠ Revival
- Registration ≠ Verification
- Library Read-back ≠ Canonical Repository Evidence
- Memory ≠ independently verified persistence
- Intended execution ≠ Executed transition

وضعیت باید از evidence مشتق شود، نه از ادعای مکالمه.

---

# 3. فرمان «ثبت کن» — Complete Registration Lifecycle

«ثبت کن» یک فرمان ساخت فایل نیست؛ یک چرخه کامل ثبت است.

## 3.1 قفل نوع رویداد / Artifact Classification

هر مورد باید قبل از promotion طبقه‌بندی شود. نمونه‌ها:

`QUESTION / PROBLEM / GAP / OBSERVATION / TEST / EXPERIMENT / FINDING / EVIDENCE / DECISION / RULE / SOLUTION / CORRECTION / ARCHITECTURAL CHANGE / REFERENCE / FAILURE / RECOVERY EVENT / PRODUCTION`

یک مورد می‌تواند چند برچسب داشته باشد، اما Primary Artifact Type باید مشخص باشد.

---

## 3.2 شناسنامه زمانی و هویتی کامل

هر ثبت باید تا حد امکان شامل:

- Production ID
- Stable ID
- Date
- Exact Time
- Timezone
- Owner
- Source / Origin
- Context
- Parent Production
- Related Productions
- Previous → Current → Next
- Version
- Attempt / Transition Identity
- Status
- Evidence State
- Repository / Persistence Surface
- Retrieval Path

**زمان تقریبی یا ساختگی ممنوع است.** اگر زمان دقیق قابل اثبات نیست، `UNKNOWN` یا `UNVERIFIED` ثبت می‌شود.

---

# 4. چرخه کامل محتوایی ثبت

هر ثبت مهم باید در صورت وجود این زنجیره را حفظ کند:

`ORIGIN`
→ `CONTEXT`
→ `QUESTION / PROBLEM / GAP`
→ `OBSERVATION`
→ `HYPOTHESIS / ASSUMPTIONS`
→ `TEST / EXPERIMENT`
→ `EVIDENCE`
→ `ANALYSIS / HAMMER`
→ `FINDING`
→ `ALTERNATIVES`
→ `REJECTED ALTERNATIVES + WHY`
→ `DECISION`
→ `RATIONALE`
→ `SOLUTION / RULE / CORRECTION`
→ `RESULT`
→ `CONSEQUENCE`
→ `ARCHITECTURAL IMPACT`
→ `REGISTRATION`
→ `READ-BACK`
→ `MATCH`
→ `VERIFY`
→ `RECONCILE`
→ `STATUS`

اگر یک مرحله وجود نداشته باشد، «ندارد / N/A» ثبت می‌شود؛ نباید بی‌صدا حذف شود.

---

# 5. Decision Lineage — مسیر تصمیم

هر تصمیم معماری باید علاوه بر Artifact Lineage، مسیر شکل‌گیری خود را نگه دارد:

`Question`
→ `Observation`
→ `Problem/GAP`
→ `Test`
→ `Evidence`
→ `Failure / Result`
→ `Hammer Analysis`
→ `New Insight`
→ `Architectural Idea`
→ `Alternatives`
→ `Decision`
→ `Reference`
→ `Architectural Integration`

هدف: بعداً فقط «چه تصمیمی گرفتیم؟» دیده نشود؛ بلکه «چرا به این تصمیم رسیدیم؟» نیز قابل بازیابی باشد.

---

# 6. Impact / Dependency Lineage

برای هر Reference / Rule / Architectural Change باید مشخص شود:

- چه GAPی را حل کرد؟
- چه Failureای را پیشگیری می‌کند؟
- چه Ruleی اضافه/اصلاح شد؟
- کدام بخش معماری ایجاد/تغییر کرد؟
- به کدام Productionها وابسته است؟
- کدام Productionها از آن ارث می‌برند؟
- اگر superseded شود چه چیزهایی باید revalidate شوند؟
- چه Acceptance Testهایی باید دوباره اجرا شوند؟

---

# 7. «ثبت کن و سند مرجع زنده قرار بده» — چرخه ویژه

این فرمان برابر است با:

**Complete Registration Lifecycle + Reference Lifecycle + Architectural Integration + Decision Lineage + Recovery Contract + Living Status Gates**

چرخه کامل:

`DISCOVER`
→ `CLASSIFY`
→ `CAPTURE ORIGIN`
→ `CAPTURE QUESTION/PROBLEM/GAP`
→ `CAPTURE OBSERVATIONS`
→ `CAPTURE TESTS/EXPERIMENTS`
→ `CAPTURE EVIDENCE`
→ `HAMMER / ANALYZE`
→ `EXTRACT FINDING`
→ `FORM ARCHITECTURAL PRINCIPLE`
→ `DEFINE SOLUTION / RULE / CONTRACT`
→ `CHECK ALTERNATIVES`
→ `DECIDE`
→ `CREATE/UPDATE REFERENCE`
→ `VERSION`
→ `REGISTER`
→ `PERSIST`
→ `READ-BACK`
→ `MATCH`
→ `VERIFY`
→ `RECONCILE`
→ `APPLY TO ARCHITECTURE`
→ `DEFINE RELATIONSHIPS`
→ `DOCUMENT ARCHITECTURAL CHANGE`
→ `DOCUMENT WHY / HOW`
→ `CONNECT LINEAGE`
→ `DEFINE RETRIEVAL PATH`
→ `CHECK DRIFT / CONFLICT / SUPERSESSION`
→ `CLOSE EVIDENCE GATES`
→ `ACTIVE / LIVING`

اگر هر gate بسته نشود، سند «LIVING» را به‌صورت اثبات‌شده دریافت نمی‌کند و همان Stable ID در OPEN/PENDING ادامه می‌یابد.

---

# 8. Master Reference Vault — MRV

## 8.1 نقش

MRV یک آرشیو صرف نیست. یک **لایه معماری governing** برای اسناد مرجع زنده است.

**Destination:**
`/Future AI/Palang Footprint/Master Reference Vault/`

## 8.2 هر Living Reference حداقل باید داشته باشد

- Stable ID
- Production ID
- Title
- Artifact Type
- Claim Class
- Owner
- Origin
- Exact Date/Time/Timezone
- Version
- Parent Architecture
- Scope
- Governing Scope
- Previous Version
- Supersedes / Superseded By
- Related IDs
- Decision Lineage
- Artifact Lineage
- Impact/Dependency Lineage
- Evidence Obligations
- Persistence Surface
- Read-back method/path
- Verification requirements
- Recovery path
- Open Obligations
- Drift conditions
- Conflict conditions
- Applicability conditions
- Status

---

# 9. Automatic Resume / خاک‌برداری و زنده‌سازی

هنگامی که کاربر می‌گوید:

**«خاک‌برداری و زنده‌سازی»**

ترتیب مادر باید چنین باشد:

`DISCOVER MRV`
→ `IDENTIFY GOVERNING REFERENCES`
→ `RETRIEVE CURRENT VERSION`
→ `READ-BACK`
→ `CHECK IDENTITY / VERSION / SCOPE`
→ `CHECK DRIFT / SUPERSESSION / CONFLICT`
→ `DISCOVER OPEN/PENDING OBLIGATIONS`
→ `SEARCH RECOVERY / PENDING`
→ `DEDUPLICATE`
→ `RECONCILE`
→ `CHECK CAPABILITY`
→ `EXECUTE POSSIBLE REMAINING STEPS`
→ `READ-BACK`
→ `MATCH`
→ `VERIFY`
→ `REGISTER / UPDATE`
→ `CONNECT`
→ `ACTIVATE / CLOSE`

MRV باید پیش از درخواست مجدد از کاربر برای ارسال همان سند persisted را جست‌وجو کند.

---

# 10. مرز «خودکار بودن»

Automatic Resume یعنی:

- کشف خودکار
- بازیابی خودکار
- تشخیص نسخه حاکم
- تشخیص obligationهای باز
- deduplication
- reconciliation
- routing به capability موجود
- اجرای مراحل واقعاً ممکن
- read-back و verification واقعی

Automatic Resume **به معنی جعل execution نیست**.

اگر capability موجود نباشد:

`OPEN/PENDING`

با حفظ:

- Same Stable ID
- Blocker
- Required Capability
- Last Durable State
- Last Attempt
- Next Transition
- Recovery Location

و در excavation بعدی دوباره قابل اجراست.

---

# 11. Same-ID Retry / No Duplicate

اگر یک Production نیمه‌کاره بماند:

**Retry = ادامه همان Production، نه Production جدید.**

پس:

`SAME STABLE ID`
+ `NEW ATTEMPT / TRANSITION RECORD`
+ `NEW EVIDENCE`
+ `RECONCILIATION`

اما:

`N EXCAVATIONS ≠ N PRODUCTIONS`

فقط وقتی Production ID جدید ایجاد می‌شود که یک یافته/تصمیم/رویداد واقعاً مستقل و جدید تولید شده باشد.

---

# 12. UNKNOWN Execution State

اگر معلوم نباشد یک transition واقعاً اجرا شده یا نه:

`UNKNOWN`

نه `SUCCESS` و نه `FAILED`.

سپس باید با surface واقعی بررسی شود.

**UNKNOWN → VERIFY**

نه:

**UNKNOWN → ASSUME SUCCESS**

---

# 13. Crash / Interruption Safety

چرخه:

`INTENT RECORDED`
→ `EXECUTION`
→ `RESULT RECORDED`
→ `READ-BACK`
→ `MATCH`
→ `VERIFY`
→ `CLOSE / OPEN`

اگر وسط کار قطع شد:

`UNKNOWN / INCOMPLETE`

و نه موفقیت فرضی.

---

# 14. Drift / Schema Change

اگر Rule، Schema، Claim Scope، Architecture، Content یا Evidence تغییر کرد:

`DETECT DRIFT`
→ `IDENTIFY AFFECTED OBLIGATIONS`
→ `REOPEN`
→ `REVALIDATE`
→ `RECONCILE`
→ `PROMOTE OR HOLD`

Evidence قدیمی بدون بررسی مجدد نباید برای نسخه جدید استفاده شود.

---

# 15. Conflict / Supersession

در تعارض:

`CONFLICT`
→ `HOLD`
→ `IDENTIFY CURRENT GOVERNING VERSION`
→ `COMPARE LINEAGE`
→ `RECONCILE`
→ `SUPERSEDE OR PRESERVE BOTH`
→ `REVALIDATE`
→ `ACTIVATE`

هرگز overwrite خاموش مجاز نیست.

---

# 16. Evidence Boundary

هر evidence فقط claim scope خودش را ثابت می‌کند.

مثال:

`Library Read-back` ثابت می‌کند که artifact در Library قابل بازیابی است.

اما به‌تنهایی ثابت نمی‌کند:

- Canonical Repository write
- Independent Runtime execution
- Persistent Memory verification

این لایه‌ها باید جداگانه evidence داشته باشند.

---

# 17. Registration Evidence Gate

ثبت نهایی زمانی قابل promotion است که، متناسب با Claim Class:

1. Artifact Type قفل شده باشد.
2. Stable ID مشخص باشد.
3. Metadata کامل یا صریحاً N/A/UNKNOWN باشد.
4. Required content captured باشد.
5. Evidence obligations ساخته شده باشند.
6. Persistence واقعاً انجام شده باشد، اگر لازم است.
7. Read-back انجام شده باشد.
8. Identity match شده باشد.
9. Content/version match شده باشد.
10. Lineage match شده باشد.
11. Architectural placement اثبات شده باشد.
12. Conflict/stale evidence باز نمانده باشد.
13. Recovery state مشخص باشد.
14. Required independent evidence موجود باشد.
15. Status از gate results مشتق شود.

---

# 18. Closure Receipt

هر Final / Verified / Active Reference باید یک Closure Receipt منطقی داشته باشد:

- Production ID
- Stable ID
- Artifact Type
- Claim Class
- Required Obligations
- Evidence Sources
- Persistence Surface
- Write Result
- Read-back Result
- Identity Match
- Content Match
- Version Match
- Lineage Match
- Architectural Placement
- Recovery State
- Conflict/Drift Check
- Verification Result
- Final Derived Status
- Remaining External Obligations

---

# 19. Multi-Axis Status Matrix

| Axis | States | معنی |
|---|---|---|
| Discovery | UNKNOWN / FOUND / RETRIEVED | آیا پیدا و بازیابی شده؟ |
| Identity | UNKNOWN / MATCHED / CONFLICTED | آیا هویت قطعی است؟ |
| Content | UNKNOWN / MATCHED / DRIFTED | آیا محتوا با مرجع منطبق است؟ |
| Persistence | NOT_WRITTEN / WRITTEN / READ_BACK | وضعیت ذخیره‌سازی |
| Evidence | OPEN / PARTIAL / CLOSED | وضعیت تعهدات evidence |
| Verification | UNVERIFIED / VERIFIED | آیا verify شده؟ |
| Architecture | UNPLACED / PLACED / RECONCILED | جایگاه معماری |
| Recovery | NONE / OPEN / PENDING / READY | وضعیت ادامه |
| Governance | CANDIDATE / GOVERNING / SUPERSEDED / CONFLICTED | وضعیت حاکمیت |
| Overall | INCOMPLETE / PENDING / ACTIVE / VERIFIED / FINAL | وضعیت مشتق‌شده |

**یک وضعیت کلی نباید وضعیت محورهای دیگر را پنهان کند.**

---

# 20. Standard Registration Form

```text
PRODUCTION ID:
STABLE ID:
ARTIFACT TYPE:
CLAIM CLASS:
TITLE:
OWNER:
ORIGIN:
CONTEXT:
DATE:
EXACT TIME:
TIMEZONE:
PARENT:
RELATED IDS:
VERSION:
ATTEMPT / TRANSITION ID:

QUESTION:
PROBLEM:
GAP:
OBSERVATION:
HYPOTHESIS:
TEST / EXPERIMENT:
EVIDENCE:
ANALYSIS / HAMMER:
FINDING:
ALTERNATIVES:
REJECTED ALTERNATIVES + WHY:
DECISION:
RATIONALE:
SOLUTION / RULE / CORRECTION:
RESULT:
CONSEQUENCE:
ARCHITECTURAL IMPACT:

ARTIFACT LINEAGE:
DECISION LINEAGE:
IMPACT / DEPENDENCY LINEAGE:

PERSISTENCE SURFACE:
WRITE RESULT:
READ-BACK RESULT:
IDENTITY MATCH:
CONTENT MATCH:
VERSION MATCH:
LINEAGE MATCH:
ARCHITECTURAL PLACEMENT:

OPEN OBLIGATIONS:
BLOCKER:
REQUIRED CAPABILITY:
LAST DURABLE STATE:
NEXT TRANSITION:
RECOVERY PATH:
DRIFT CHECK:
CONFLICT CHECK:
SUPERSESSION CHECK:

DERIVED STATUS:
CLOSURE RECEIPT:
``` 

---

# 21. Standard Living Reference Form

```text
REFERENCE ID / STABLE ID:
REFERENCE TITLE:
REFERENCE TYPE:
GOVERNING SCOPE:
OWNER:
ORIGIN:
DATE / EXACT TIME / TIMEZONE:
CURRENT VERSION:
PREVIOUS VERSION:
SUPERSEDES:
SUPERSEDED BY:
PARENT ARCHITECTURE:
DESTINATION:

PROBLEM / GAP SOLVED:
QUESTION:
OBSERVATIONS:
TESTS / EXPERIMENTS:
EVIDENCE:
HAMMER FINDING:
ARCHITECTURAL PRINCIPLE:
RULE / SOLUTION / CONTRACT:
DECISION + RATIONALE:
REJECTED ALTERNATIVES:

ARTIFACT LINEAGE:
DECISION LINEAGE:
IMPACT / DEPENDENCY LINEAGE:

APPLICABILITY:
INAPPLICABILITY CONDITIONS:
DRIFT CONDITIONS:
CONFLICT CONDITIONS:
EVIDENCE OBLIGATIONS:
RECOVERY CONTRACT:
RETRIEVAL PATH:

PERSISTENCE:
READ-BACK:
MATCH:
VERIFY:
ARCHITECTURAL PLACEMENT:
RECONCILIATION:

OPEN OBLIGATIONS:
BLOCKER:
NEXT TRANSITION:

DERIVED STATUS:
GOVERNING STATUS:
CLOSURE RECEIPT:
``` 

---

# 22. Command Contract — «ثبت کن»

وقتی کاربر می‌گوید:

**ثبت کن**

سیستم باید:

1. نوع artifact را تعیین کند.
2. provenance را ثبت کند.
3. تاریخ/زمان/timezone را ثبت کند.
4. question/problem/gap/observation/test/finding/evidence/decision و سایر موارد موجود را استخراج کند.
5. lineage را بسازد.
6. evidence obligations را تعیین کند.
7. persistence surface مناسب را انتخاب کند.
8. فقط مراحل واقعاً قابل اجرا را اجرا کند.
9. read-back بگیرد.
10. match کند.
11. verify کند.
12. reconcile کند.
13. architectural placement را در صورت نیاز انجام/ثبت کند.
14. open obligations را نگه دارد.
15. status را از evidence مشتق کند.
16. در failure همان Stable ID را حفظ کند.

---

# 23. Command Contract — «ثبت کن و سند مرجع زنده قرار بده»

این فرمان علاوه بر تمام موارد «ثبت کن» باید:

1. Reference Candidate را شناسایی کند.
2. Decision Lineage را حفظ کند.
3. دلیل ایجاد Reference را ثبت کند.
4. scope حاکمیتی را مشخص کند.
5. alternativeها و رد آن‌ها را نگه دارد.
6. rule/solution/contract را استخراج کند.
7. impact/dependency lineage را بسازد.
8. version و supersession chain را بسازد.
9. آن را در MRV قرار دهد.
10. retrieval path را تعریف کند.
11. drift/conflict conditions را ثبت کند.
12. recovery contract را ثبت کند.
13. read-back و match انجام دهد.
14. evidence gates را ببندد.
15. architectural relationship را ثبت کند.
16. فقط در صورت بسته‌شدن gateهای لازم، آن را `ACTIVE / LIVING / GOVERNING` اعلام کند.

---

# 24. Command Contract — «خاک‌برداری و زنده‌سازی»

اول MRV، سپس Recovery/Pending و سایر سطوح مرتبط بررسی می‌شوند.

قانون:

**کاربر نباید سند مرجع persisted را دوباره بفرستد، مگر اینکه بازیابی آن واقعاً ممکن نباشد یا نسخه/هویت آن unresolved باشد.**

ترتیب:

`MRV DISCOVERY`
→ `GOVERNING REFERENCE RETRIEVAL`
→ `READ-BACK`
→ `VERSION / DRIFT / CONFLICT CHECK`
→ `OPEN OBLIGATION DISCOVERY`
→ `RECOVERY / PENDING DISCOVERY`
→ `DEDUP`
→ `RECONCILE`
→ `CAPABILITY CHECK`
→ `EXECUTE`
→ `READ-BACK`
→ `VERIFY`
→ `ACTIVATE / CLOSE`

---

# 25. New Production Isolation

اگر در هنگام ثبت یا خاک‌برداری، واقعاً یک Finding / Decision / Architectural Change جدید کشف شود:

`NEW PRODUCTION ID`

اما اگر صرفاً ادامه همان مورد قبلی باشد:

`SAME STABLE ID`

این تفکیک باید قبل از ثبت نهایی انجام شود.

---

# 26. No-Loss / Pending Anti-Forgetting

هر OPEN/PENDING item باید حداقل داشته باشد:

- Stable ID
- Current State
- Blocker
- Source/Capability
- Last Attempt
- Last Durable State
- Next Transition
- Recovery Path
- Evidence already available
- Evidence still required

**OPEN بدون مسیر ادامه = ثبت ناقص.**

---

# 27. Architecture Placement Contract

ادعای «در معماری وارد شد» فقط وقتی معتبر است که این چهار مورد مشخص باشد:

`DESTINATION`
+ `PARENT ARCHITECTURE`
+ `RELATIONSHIP`
+ `RETRIEVAL PATH`

و placement evidence موجود باشد.

---

# 28. Invariants — اصول تغییرناپذیر

1. No loss.
2. No duplicate production from retry.
3. No false completion.
4. No false verification.
5. No silent overwrite.
6. No stale evidence reuse after material drift.
7. No evidence substitution across claim scopes.
8. No UNKNOWN → SUCCESS assumption.
9. No final status without required evidence closure.
10. No architectural placement claim without placement evidence.
11. No new Production ID without genuinely new production.
12. No open obligation without blocker/source/last attempt/next transition.
13. Same Stable ID across retry.
14. Status is derived from evidence.
15. User acceptance ≠ technical verification.
16. Library persistence ≠ Canonical Repository evidence.
17. Reference retrieval precedes asking user to resend a persisted reference.
18. Living/governing status requires its applicable gates to be closed.

---

# 29. Master Executable Rule

### For «ثبت کن»

`PRESERVE`
→ `CLASSIFY`
→ `CAPTURE PROVENANCE`
→ `CAPTURE FULL LINEAGE`
→ `DEFINE EVIDENCE OBLIGATIONS`
→ `EXECUTE AVAILABLE STEPS`
→ `READ-BACK`
→ `MATCH`
→ `VERIFY`
→ `RECONCILE`
→ `REGISTER / CONNECT`
→ `DERIVE STATUS`
→ `CLOSE OR KEEP OPEN`

### For «ثبت کن و سند مرجع زنده قرار بده»

`REGISTER`
→ `REFERENCE LIFECYCLE`
→ `DECISION LINEAGE`
→ `IMPACT LINEAGE`
→ `VERSION`
→ `MRV PERSISTENCE`
→ `READ-BACK`
→ `MATCH`
→ `VERIFY`
→ `ARCHITECTURAL PLACEMENT`
→ `DRIFT / CONFLICT / SUPERSESSION CHECK`
→ `RECOVERY CONTRACT`
→ `CLOSE EVIDENCE GATES`
→ `ACTIVE / LIVING / GOVERNING`

### If blocked

`KEEP SAME ID`
→ `PRESERVE LAST DURABLE STATE`
→ `RECORD BLOCKER`
→ `RECORD REQUIRED CAPABILITY`
→ `RECORD NEXT TRANSITION`
→ `OPEN / PENDING`
→ `RETRY ON NEXT EXCAVATION`

---

# 30. Final Architectural Decision

**MASTER REFERENCE VAULT (MRV) is a permanent architectural layer of Future AI / Palang Footprint.**

A Reference Document is no longer treated merely as a text to resend. When it is actually persisted and verified in MRV, it becomes a recoverable living governing artifact with:

`IDENTITY + PROVENANCE + TIME + CONTENT + DECISION LINEAGE + ARTIFACT LINEAGE + IMPACT LINEAGE + VERSION + SCOPE + EVIDENCE + RECOVERY + ARCHITECTURAL PLACEMENT + RETRIEVAL PATH + GOVERNING STATUS`

The next excavation must attempt retrieval from MRV before requesting the user to resend the same persisted reference.

---

# 31. Current Registration / Closure State

**This artifact is the master reference for the MRV architecture and the complete registration/living-reference lifecycle.**

Required evidence closure for this specific artifact:

`WRITE → READ-BACK → MATCH → VERIFY → ARCHITECTURAL PLACEMENT → ACTIVE/LIVING`

If any required operation cannot be performed, the correct status is:

`OPEN / PENDING`

with the same Stable ID and full recovery state.

---

# 32. Final Principle

> **ثبت کن = یک چرخه کامل و قابل‌بازیابی برای ثبت واقعیت، منشأ، زمان، سؤال، مسئله، شکاف، مشاهده، آزمون، شواهد، تحلیل، چکش، یافته، گزینه‌ها، تصمیم، دلیل تصمیم، راهکار، اصلاح، نتیجه، اثر، lineage، معماری، persistence، read-back، verification، reconciliation و recovery است.**
>
> **ثبت کن و سند مرجع زنده قرار بده = تمام چرخه بالا + تبدیل خروجی به یک Reference حاکم، نسخه‌دار، قابل‌بازیابی، دارای Decision/Impact Lineage، دارای قرارداد recovery، متصل به معماری و قابل استفاده در خاک‌برداری بعدی؛ اما فقط پس از evidence closure واقعی.**

**Governing rule:**

`NO GATE RESULT → NO PROMOTION`

`NO EVIDENCE CLOSURE → NO VERIFIED CLAIM`

`NO CAPABILITY → NO FALSE COMPLETION`

`SAME STABLE ID → SAME PRODUCTION ACROSS RETRY`

`MRV RETRIEVAL BEFORE USER RESEND`

---

## 33. Previous → Current → Next

`RECOVERY-HAMMER-REFERENCE-2026-09-15-001`
→ `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001`
→ **MRV PERSISTENCE / READ-BACK / MATCH / VERIFY**
→ **ARCHITECTURAL PLACEMENT**
→ **ACTIVE / LIVING / GOVERNING**
→ future `خاک‌برداری و زنده‌سازی`

---

## 34. Evidence Note

این سند در این لحظه به‌عنوان artifact تولیدشده آماده persistence است. «آماده بودن» با «ثبت‌شدن در Library» یکی نیست. وضعیت نهایی فقط پس از write واقعی، read-back واقعی، match و verification قابل ارتقا است.

---

# 35. Binding Rule — «ثبت کن» Uses This Master by Default

**Stable ID:** `MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001`  
**Rule ID:** `REGISTER-COMMAND-MASTER-BINDING-2026-10-12-001`  
**Version:** `1.0.0`  
**Project:** Future AI / Palang Footprint  
**Owner:** Ahmad Nezhadhosseini / احمد پلنگ  
**Effective intent:** Permanent default governing contract for every future user command `ثبت کن`, unless the user explicitly changes or supersedes this rule.

## 35.1 Default interpretation — no repeated explanation required

Whenever the user says **«ثبت کن»**, interpret it as the complete lifecycle in this master reference. The user is not required to repeat the rules, list the layers, or explain what registration means. Do not reduce the command to “remember this,” a short summary, a chat-only acknowledgment, or a file creation.

The default lifecycle is:

`PRESERVE → CLASSIFY → CAPTURE PROVENANCE → CAPTURE CONTEXT AND FULL AVAILABLE LINEAGE → ASSIGN/REUSE IDS → DEFINE EVIDENCE OBLIGATIONS → SELECT RELEVANT DESTINATIONS → WRITE/EXECUTE → READ-BACK → MATCH → VERIFY → RECONCILE → CONNECT TO ARCHITECTURE → DERIVE STATUS → CLOSE OR PRESERVE OPEN STATE`

When a living reference is appropriate, also apply the complete living-reference lifecycle in this document: versioning, MRV placement, governing scope, dependency/impact lineage, retrieval/recovery path, drift/conflict/supersession checks, and architectural integration.

## 35.2 Default persistence targets

The user’s intended full registration model has three distinct levels, to be attempted when the necessary capabilities are actually available:

1. **Canonical Repository (مخزن مرجع):** write the governing artifact to the correct repository path and read it back.
2. **Buffer / Recovery Queue (بافر/صف بازیابی):** preserve incomplete or blocked work with its identity, last durable state, blocker, required capability, next transition, and recovery pointer.
3. **Persistent Memory (حافظه پایدار):** preserve the compact governing instruction and retrieval pointer so later turns can apply the rule without asking the user to repeat it.

A write to one target is not evidence of a write to another. Do not report the three targets as complete unless each target has its own sufficient evidence. A conversational statement that something was “saved” is not a substitute for a target-specific write and read-back.

## 35.3 Governing behavior on every future use

- Retrieve and consult this master reference before asking the user to repeat its rules, when retrieval is available.
- Apply the full contract by default to each new «ثبت کن» request.
- Reuse the existing Stable ID when continuing this same governing contract; create a new Production ID only for a genuinely new production or transition record as defined in the contract.
- Never claim that a target was written, read back, matched, verified, activated, or made permanent unless the corresponding operation and evidence exist.
- Report Repository, Buffer, Persistent Memory, and architectural status separately.
- If a target is unavailable or blocked, preserve the obligation as OPEN/PENDING/UNKNOWN with the last durable state, blocker, required capability, next transition, and recovery pointer; continue the same identity rather than silently abandoning it.
- Do not imply that this repository file alone guarantees automatic behavior in every future model, session, or environment. The repository is the canonical specification; execution and memory availability remain capability- and evidence-dependent.
- This rule remains the default until an explicit, versioned, reconciled change supersedes it.

## 35.4 Architectural placement contract for this binding

- **Canonical destination:** `docs/reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md`
- **Parent architecture:** Future AI / Palang Footprint → Master Reference Vault (MRV)
- **Relationship:** Governing command contract for registration, persistence, recovery, verification, and living-reference handling.
- **Retrieval pointer:** repository path above and the Stable ID.
- **Next action:** verify the post-write repository read-back and match; separately complete Buffer and Persistent Memory only through actual supported operations.

## 35.5 Evidence-bounded state of this update

This section is an explicit binding of the user's intended command semantics to the existing master reference; it does not erase the evidence gates in sections 16–19 and 31–34.

The repository update must be followed by a fresh read-back and content check. Until that succeeds, repository write status is not verified. Buffer and Persistent Memory remain separate evidence obligations unless independently written and read back. Do not promote the overall three-level registration to fully complete based only on repository evidence.

**No repeated user explanation required. No unsupported permanence claim. No false three-level completion.**

---

## 34. Governing command binding — «ثبت کن» as the default execution contract

**Binding rule (added 2026-10-12):** Whenever Ahmad Nezhadhosseini / احمد پلنگ says «ثبت کن», this master reference is the governing contract by default. The user is not required to restate these requirements. This binding applies to new registration work and continuation/recovery of incomplete work.

**Final/Living designation (confirmed 2026-10-12):** This is the current final governing rule for the literal command «ثبت کن» in Future AI / Palang Footprint. It remains the default until a deliberate, versioned, evidence-backed change supersedes it; history must not be erased. On each available future turn, retrieve and apply this master and the companion entry point `REGISTER-COMMAND-GOVERNING-BINDING-2026-10-12-001` before interpreting «ثبت کن». This designation governs the specification, but it does not falsely guarantee automatic availability in every future environment or prove Buffer/Persistent Memory persistence.

The command MUST be interpreted as the full lifecycle defined in this document, not as “remember this in chat” or “write one file”. Execute all stages supported by the current environment: preserve; classify; capture provenance/context/evidence and lineage; assign or reuse stable and production identifiers; create/update the complete reference artifact when warranted; place it in the canonical repository and other genuinely available destinations; perform destination-specific write → read-back → match → verify; reconcile architecture and versions; and report the evidence-backed status and next action.

**No overclaim rule:** A repository commit does not prove Buffer or Persistent Memory writes. A successful write response alone does not prove read-back or match. Never report ACTIVE/VERIFIED for a destination unless its required evidence exists. For inaccessible destinations, keep the item OPEN/PENDING (or the project’s defined holding state “پودینگ”), with blocker, last durable state, required capability, next transition, and recovery pointer. Preserve prior history and continue with the same Stable ID for retries unless a genuine new artifact requires a new identity.

**Default retrieval rule:** When the user returns and says «ثبت کن», first retrieve and consult this governing reference and any applicable prior state available to the current environment; do not ask the user to repeat an already retrievable contract. If the reference cannot actually be retrieved, say so plainly and do not pretend it was consulted.

**Canonical command-binding record:** `REGISTER-COMMAND-GOVERNING-BINDING-2026-10-12-001`  
**Relationship:** This section binds the existing MRV master to the literal user command «ثبت کن». The companion record `docs/reference/REFERENCE-DOCUMENTS/REGISTER-COMMAND-GOVERNING-BINDING-2026-10-12-001.md` provides a concise entry point. It supplements rather than replaces this master and does not erase history.

**Evidence boundary at this update:** The repository update and its read-back can establish repository persistence only. They do not establish Library, Buffer, or Persistent Memory persistence. Those destinations remain independently unverified until separately written and read back.


---

## 31. Register Command — Repository Unavailable Fallback and Resume

**Related production record:** `REGISTER-REPOSITORY-UNAVAILABLE-FALLBACK-2026-10-12-001`  
**Canonical file:** `docs/reference/REFERENCE-DOCUMENTS/REGISTER-REPOSITORY-UNAVAILABLE-FALLBACK-2026-10-12-001.md`  
**Companion command binding:** `REGISTER-COMMAND-GOVERNING-BINDING-2026-10-12-001`

### Governing behavior

1. A successful write of a new repository file does not prove that edits to this master or its companion command-binding succeeded. Treat each file as an independent write/read-back/verification target.
2. If repository access, a write, or a verification step fails, state the exact known state and the failed step. Do not report the entire registration as complete.
3. Provide the user with the complete, copyable continuation/reference artifact when it is needed to preserve work outside the repository. The user may resend that same artifact when access returns.
4. On resumption, fetch the current master, command-binding, and fallback record; inspect current history and identities; validate provenance; deduplicate; reconcile conflicts and version lineage; then update the necessary files without replacing or erasing prior history.
5. For each updated file, fetch the current version first, use its current blob SHA for the write, then fetch the written version again and compare the content and returned SHA. A write receipt alone is not read-back proof.
6. Repository verification proves repository state only. It does not prove Library, Buffer, or Persistent Memory persistence. Those destinations remain unverified unless separately written and read back.

### Required status vocabulary

- `FALLBACK RECORD VERIFIED`: only when its repository content has been read back and matched.
- `MASTER INTEGRATION VERIFIED`: only when this section is present in the master after read-back and content match.
- `COMMAND BINDING INTEGRATION VERIFIED`: only when the companion binding contains the corresponding rule after read-back and content match.
- `PARTIAL / OPEN`: use when any required destination or integration remains incomplete.

**No-loss rule:** `PRESERVE → IDENTIFY → VALIDATE → DEDUPLICATE → RECONCILE → REGISTER → READ-BACK → MATCH → VERIFY → REPORT STATUS`.

This section supplements the master and preserves its existing content and history. It does not imply that the companion command-binding or any non-repository destination has been updated.
