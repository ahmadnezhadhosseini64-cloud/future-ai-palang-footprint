# سند مرجع کامل — فرمان «ثبت کن» به‌عنوان ثبت کامل سه‌سطحی و حاکمیتی

**Stable ID:** THREE-LEVEL-GOVERNED-REGISTRATION-COMMAND-2026-10-06-001  
**Production ID:** 3LR-GOVREG-CMD-2026-10-06-001  
**Version:** 1.1.3  
**Date:** 2026-10-12  
**Timezone:** Asia/Tehran (+03:30)  
**Owner:** Ahmad Nezhadhosseini / احمد پلنگ  
**Location:** Gonbad-e Kavus, Iran  
**Project:** Future AI / Palang Footprint  
**Type:** Master Reference / Architectural Contract  
**Status:** ACTIVE / LIVING as governing specification; runtime automation and three-level completion are separately evidence-gated.  
**Origin:** نتیجه چکش ریشه‌ای خطای فهم سؤال، مسیر جست‌وجو و ثبت ناقص در معماری سه‌سطحی  
**Parent Architecture:** THREE-LAYER-REGISTRATION-ARCHITECTURE-2026-10-06-001 / 3LR-REG-2026-10-06-001  
**Related Amendment:** THREE-LAYER-VERIFICATION-FAILURE-HARDENING-2026-10-06-001 / 3LR-HARDEN-2026-10-06-001  
**Repository Path:** docs/reference/REFERENCE-DOCUMENTS/THREE-LEVEL-GOVERNED-REGISTRATION-COMMAND-2026-10-06-001.md  
**Library Path:** /Future AI/Palang Footprint/Master Reference Vault/Reference Documents/  
**Persistent-Memory State:** باید مستقل و با Provider-level Read-back اثبات شود؛ از سطح دیگری ارث نمی‌برد.

---

## 1. تعریف مادر

از این پس در معماری Future AI / Palang Footprint:

**«ثبت کن» = Full Governed Three-Level Registration**

یعنی وقتی احمد پلنگ فقط می‌گوید:

**«ثبت کن»**

نیازی نیست دوباره بگوید:

- در مخزن ثبت کن
- در بافر ثبت کن
- در حافظه ثبت کن
- سند مرجع بساز
- مستندسازی کن
- شناسه بده
- Lineage ثبت کن
- Read-back کن
- Verify کن

همه این‌ها جزو معنی پیش‌فرض فرمان «ثبت کن» هستند.

---

## 2. سه سطح اجباری ثبت

هر فرمان «ثبت کن» به‌صورت پیش‌فرض یک **Three-Level Registration Transaction / تراکنش ثبت سه‌سطحی** ایجاد می‌کند:

1. **Repository / مخزن**
2. **Buffer / بافر**
3. **Persistent Memory / حافظه پایدار**

هیچ‌کدام جایگزین دیگری نیست.

ثبت یک سطح، ثبت کامل محسوب نمی‌شود.

---

## 3. سند مرجع کامل جزو خود عملیات ثبت است

وقتی محتوای معماری، کشف، قانون، GAP، تصمیم یا Artifact مهمی با فرمان «ثبت کن» ثبت می‌شود، ایجاد/به‌روزرسانی **Complete Reference Document / سند مرجع کامل** بخشی از همان عملیات است.

سند مرجع نباید فقط خلاصه باشد.

باید تا حد لازم شامل لایه‌های:

- Stable ID / شناسه پایدار
- Production ID / شناسه تولیدی
- Version / نسخه
- Date / تاریخ
- Time / زمان دقیق در صورت ثبت‌شدن
- Timezone / منطقه زمانی
- Owner / مالک
- Location / مکان
- Project / پروژه
- Origin / منشأ
- Lineage / تبار
- Status / وضعیت
- Evidence / شواهد
- Limitation / محدودیت
- Next Action / اقدام بعدی
- Repository Path / مسیر مخزن
- Library Path / مسیر کتابخانه
- Persistent-Memory State / وضعیت حافظه پایدار
- Retrieval/Recovery Pointer / اشاره‌گر بازیابی
- و سایر قواعد Governance / حاکمیت ثبت پروژه باشد.

---

## 4. زنجیره اجرایی «ثبت کن»

فرمان باید در این مسیر اجرا شود:

**REQUEST PRESERVATION → INTENT PARSE → GOVERNANCE EXPANSION → COMPLETE REFERENCE DOCUMENT → THREE-LEVEL WRITE → THREE-LEVEL READ-BACK → MATCH → VERIFY → RECONCILE → STATUS**

معنی:

**حفظ درخواست → فهم دقیق منظور → فعال‌کردن تمام قواعد حاکمیتی → ایجاد سند مرجع کامل → نوشتن در سه سطح → بازخوانی از سه سطح → تطبیق → راستی‌آزمایی → رفع مغایرت → ثبت وضعیت**

---

## 5. حفظ منظور کاربر

خطای اصلی کشف‌شده فقط «نگشتن» نبود.

مسیر خطا این بود:

**USER MESSAGE → TOPIC RECOGNITION → ASSUMED QUESTION → ANSWER**

یعنی موضوع درست تشخیص داده شد، اما کاری که کاربر خواسته بود از بین رفت.

اصل جدید:

**Understanding the Topic ≠ Understanding the Task**

فهم موضوع ≠ فهم کار درخواستی.

بنابراین قبل از اجرا باید این چهار جزء حفظ شوند:

**TARGET + ACTION + DESTINATIONS/CONDITIONS + REQUIRED OUTPUT**

در فرمان «ثبت کن»:

- **TARGET:** محتوای مورد ثبت
- **ACTION:** ثبت کامل
- **DESTINATIONS:** هر سه سطح
- **REQUIRED OUTPUT:** سند مرجع کامل + ثبت سه‌سطحی + Verification + Governance

اگر یکی از این اجزا حذف یا با حدس جایگزین شود:

**DO NOT ANSWER/EXECUTE YET → RE-PARSE REQUEST**

---

## 6. ثبت کامل با ثبت یک سطح یکی نیست

اصل:

**ONE LEVEL REGISTERED ≠ THREE-LEVEL REGISTRATION COMPLETE**

مثلاً:

Repository = VERIFIED  
Buffer = BLOCKED  
Memory = NOT-VERIFIED

نتیجه کلی:

**PARTIAL / ناقص**

نه:

**COMPLETE / کامل**

هیچ سطحی اجازه ندارد وضعیت خود را به کل عملیات تعمیم دهد.

---

## 7. دروازه تکمیل ثبت

**Registration Completion Gate / دروازه تکمیل ثبت**

عملیات فقط وقتی COMPLETE اعلام می‌شود که وضعیت هر سه مقصد مستقل مشخص و الزامات ثبت، بازخوانی، تطبیق و راستی‌آزمایی انجام شده باشد.

اصل:

**NO THREE-LEVEL PROOF → NO COMPLETE REGISTRATION CLAIM**

بدون اثبات سه‌سطحی، ادعای ثبت کامل ممنوع است.

---

## 8. محدودیت فنی، فرمان ثبت را لغو نمی‌کند

اگر یکی از سطوح به دلیل:

- Throttling / محدودیت بارگذاری
- سهمیه
- عدم دسترسی موقت
- محدودیت ابزار
- Blocker / مانع فنی
- یا هر محدودیت دیگر

قابل ثبت نباشد، آن مقصد از قرارداد حذف نمی‌شود.

مسیر صحیح:

**PRESERVE → REGISTER AVAILABLE LEVELS → RECORD BLOCKER → KEEP SAME STABLE ID/LINEAGE → MARK PENDING/BLOCKED → EXCAVATE/RECOVER → COMPLETE REMAINING LEVELS → READ-BACK → MATCH → VERIFY → RECONCILE → PROMOTE**

یعنی:

**حفظ → ثبت سطوح قابل‌اجرا → ثبت مانع → حفظ همان شناسه و تبار → وضعیت در انتظار/مسدود → خاک‌برداری/بازیابی → تکمیل سطوح باقی‌مانده → بازخوانی → تطبیق → راستی‌آزمایی → رفع مغایرت → ارتقا به کامل**

کاربر نباید مجبور شود فرمان «ثبت کن» را دوباره صادر کند.

---

## 9. محدودیت به معنی فقدان نیست

**PARTIAL ≠ LOST**  
**PENDING ≠ BURIED**  
**BLOCKED ≠ FAILED**  
**INTERRUPTED ≠ FAILED**

محدودیت باید State / وضعیت را حفظ کند، نه اینکه Artifact یا قرارداد ثبت را نابود کند.

---

## 10. قواعد Governance به‌صورت خودکار فعال می‌شوند

«ثبت کن» باید تمام قواعد ثبت پروژه را فعال کند، از جمله:

**PRESERVE → IDENTIFY → VERIFY → RECONCILE → REGISTER → PROMOTE**

همچنین:

- هیچ ادعایی بدون Evidence / شاهد
- هیچ Verification بدون Independence / استقلال
- هیچ Runtime Claim بدون Implementation / پیاده‌سازی
- هیچ Tested Claim بدون Acceptance / پذیرش
- هیچ Current Version بدون Lineage / تبار
- هیچ Replacement بدون Preserved History / تاریخچه حفظ‌شده
- هیچ Recovery بدون Preserved State / وضعیت حفظ‌شده
- هیچ Persistence Proof بدون Representation / نمایش تعریف‌شده
- هیچ Byte Match بدون Canonical Serialization / سریال‌سازی استاندارد
- هیچ Commit Claim بدون Revision Binding / اتصال به نسخه/بازبینی
- هیچ Safe Check بدون Version Awareness / آگاهی از نسخه

---

## 11. جداسازی شواهد سه سطح

شاهد هر سطح فقط همان سطح را اثبات می‌کند.

**Repository proof → فقط مخزن**

**Buffer proof → فقط بافر**

**Memory proof → فقط حافظه پایدار**

هیچ سطحی وضعیت VERIFIED سطح دیگر را به ارث نمی‌برد.

متن یک سند که می‌گوید «در بافر ثبت شده» به‌تنهایی اثبات حضور فعلی آن در بافر نیست.

گزارش نیز جای خود مقصد را نمی‌گیرد.

---

## 12. مسیر صحیح جست‌وجو و پاسخ

مسیر ممنوع:

**Question → Guess/Memory Impression → Answer → Search afterward**

مسیر صحیح:

**Question → Structured Task → Search/Read-back → Evidence Assembly → Claim Gate → Answer**

جست‌وجو نباید بعد از جواب برای پیدا کردن تأیید جواب انجام شود.

جست‌وجو بخشی از ساخت جواب است.

---

## 13. برای فرمان «ثبت کن» پاسخ پیش از اجرا ممنوع است

نباید قبل از اجرای عملیات گفته شود:

«ثبت شد.»

مگر اینکه شواهد متناسب با سطح مورد ادعا وجود داشته باشد.

اگر عملیات کامل نشده:

**PARTIAL / ناقص**

یا

**PENDING / در انتظار**

یا

**BLOCKED / مسدود**

یا

**NOT-VERIFIED / راستی‌آزمایی‌نشده**

باید اعلام شود.

---

## 14. ماتریس وضعیت اجباری

برای هر ثبت:

| سطح | Write | Read-back | Match | Verify | وضعیت |
|---|---|---|---|---|---|
| Repository / مخزن | مستقل | مستقل | مستقل | مستقل | مستقل |
| Buffer / بافر | مستقل | مستقل | مستقل | مستقل | مستقل |
| Persistent Memory / حافظه پایدار | مستقل/در حد قابلیت | مستقل/در حد قابلیت | مستقل | مستقل | مستقل |

سپس:

**Overall Registration Status / وضعیت کلی ثبت**

یکی از:

- COMPLETE / کامل
- PARTIAL / ناقص
- PENDING / در انتظار
- BLOCKED / مسدود
- NOT-VERIFIED / راستی‌آزمایی‌نشده

باشد.

---

## 15. Recovery / بازیابی و خاک‌برداری

اگر بخشی از ثبت در لحظه اجرا به علت محدودیت انجام نشد:

**EXCAVATE → IDENTIFY → VALIDATE → DEDUPLICATE → CONNECT/RECONCILE → REGISTER → REVIVE/ABSORB → INHERIT 0.0/MASTER → DOCUMENT → READ-BACK → VERIFY → CONTINUE**

و نباید تاریخچه قبلی حذف یا با ثبت تازه جایگزین شود.

---

## 16. تست‌های پذیرش

### AT-GR-01
فرمان «ثبت کن» باید خودکار به ثبت سه‌سطحی تبدیل شود.

### AT-GR-02
کاربر نباید مجبور باشد سه مقصد را دوباره نام ببرد.

### AT-GR-03
سند مرجع کامل بخشی از ثبت باشد.

### AT-GR-04
هر سه سطح مستقل Write/Read-back/Match/Verify داشته باشند.

### AT-GR-05
ثبت یک سطح هرگز Complete اعلام نشود.

### AT-GR-06
محدودیت باعث Lost شدن عملیات نشود.

### AT-GR-07
Stable ID و Lineage در وضعیت Pending/Blocked حفظ شوند.

### AT-GR-08
پس از رفع محدودیت، عملیات از همان State ادامه یابد.

### AT-GR-09
تمام قواعد Governance با فرمان ساده «ثبت کن» فعال شوند.

### AT-GR-10
Status Matrix سه‌سطحی تولید شود.

### AT-GR-11
Target/Action/Destinations/Required Output قبل از اجرا حفظ شوند.

### AT-GR-12
Topic Recognition به‌تنهایی برای پاسخ کافی نباشد.

### AT-GR-13
Search/Read-back قبل از Claim باشد.

### AT-GR-14
Intent Compression باعث توقف و Re-parse شود.

### AT-GR-15
Partial Success هرگز به Complete تبدیل نشود.

---

## 17. اصل مادر نهایی

**وقتی احمد پلنگ می‌گوید «ثبت کن»، فرمان باید به‌صورت پیش‌فرض به‌عنوان ثبت کامل، حاکمیتی، همزمان و سه‌سطحی تفسیر و اجرا شود.**

نه:

«هر سطحی که ابزار اجازه داد ثبت کن.»

بلکه:

**«هر سه سطح مقصد قطعی عملیات هستند؛ اگر محدودیت مانع یکی شد، آن سطح Pending/Blocked می‌ماند تا با همان Lineage و همان Stable ID تکمیل شود.»**

---

## 18. اصل ضدتکرار خطا

برای جلوگیری از تکرار خطای مورد بحث:

**اول منظور کاربر را حفظ کن.  
بعد Task را بساز.  
بعد مسیر جست‌وجو/ثبت را تعیین کن.  
بعد اجرا کن.  
بعد شواهد را جمع کن.  
بعد تطبیق و راستی‌آزمایی کن.  
بعد ادعا کن.**

و برای «ثبت کن»:

**REQUEST → GOVERNANCE EXPANSION → COMPLETE REFERENCE → 3-LEVEL WRITE → 3-LEVEL READ-BACK → MATCH → VERIFY → RECONCILE → STATUS**

---

## 19. Evidence Boundary / مرز شواهد

ثبت هر سطح فقط زمانی VERIFIED اعلام می‌شود که شواهد مستقل همان سطح موجود باشد.

اگر محدودیت مانع اثبات یک سطح شد، وضعیت آن سطح باید صریحاً NOT-VERIFIED / PENDING / BLOCKED باقی بماند.

هیچ سطحی نباید با شواهد سطح دیگر «پر» شود.

---

## 20. Lineage / تبار

**Parent:** THREE-LAYER-REGISTRATION-ARCHITECTURE-2026-10-06-001 / 3LR-REG-2026-10-06-001

**Related Amendment:** THREE-LAYER-VERIFICATION-FAILURE-HARDENING-2026-10-06-001 / 3LR-HARDEN-2026-10-06-001

**Trigger:** خطای واقعی در فهم درخواست، جست‌وجوی نادرست و تبدیل ثبت ناقص به برداشت ثبت کامل.

**Purpose:** جلوگیری معماری از تکرار این کلاس خطا در آینده.

---

## 21. Status

**ACTIVE / LIVING**

این سند یک قرارداد معماری زنده است و در صورت کشف GAP / شکاف جدید، با حفظ Lineage و History / تاریخچه قابل تکامل است.



---

## 22. Revision 1.1.0 — Live Registration State and Command Binding

**Revision Date:** 2026-10-12  
**Exact Time:** Not independently captured; intentionally not invented.  
**State Record ID:** `3LR-STATE-2026-10-12-001`  
**Related State Record:** `THREE-LEVEL-GOVERNED-REGISTRATION-STATE-2026-10-12-001.md`  
**Revision Purpose:** Reaffirm that the literal user command **«ثبت کن»** invokes this entire contract by default, and preserve the actual evidence boundary for all three registration surfaces.

### 22.1 Command binding

The command is complete by definition. Unless the user explicitly narrows or overrides it, **«ثبت کن»** automatically means:

- preserve the complete discovery, rule, architecture, decision, GAP, test, or artifact and its context;
- classify it and preserve provenance, lineage, prior versions, and related IDs;
- create or update the complete reference document when the content warrants a reference artifact;
- register the same production identity across Repository, Registration Buffer, and Persistent Memory;
- independently record the result for each destination;
- read back each destination where its actual interface permits, compare the returned representation with the intended payload, verify it, reconcile differences, and record evidence;
- preserve unresolved work in a recoverable `PENDING` / `BLOCKED` / `UNVERIFIED` holding state and continue it when a valid opportunity becomes available, without asking the user to repeat the same command;
- never report overall completion based only on a write acknowledgement, an in-chat statement, or evidence from another destination.

No extra prompt is required to ask whether the user also wants a reference document, repository, buffer, memory, lineage, or verification: these are default obligations of this command.

### 22.2 Destination-specific live state as of this revision

| Destination | State supported by current evidence | Evidence boundary |
|---|---|---|
| Repository / مخزن | `PRESENT — HISTORICAL FILE FOUND`; latest revision requires commit/read-back verification | The canonical command file was fetched from the repository before this revision. The revision must be committed and fetched again before the new version is called verified. |
| Buffer / بافر | Existing state record was found in the Library; this master reference must be uploaded to the Buffer and independently read back before calling this revision verified there | A state record is not a substitute for the full master reference. |
| Persistent Memory / حافظه پایدار | `WRITE-ACCEPTED / NOT-INDEPENDENTLY-VERIFIED` | The memory update can retain continuity facts, but there is no independent provider-level read-back evidence in this operation. Do not mark the full document as byte-for-byte persisted in memory. |

**Overall status after Repository and Buffer read-back:** `PARTIAL / MEMORY NOT-INDEPENDENTLY-VERIFIED`. Repository and Buffer are verified for revision 1.1.0; Persistent Memory remains unverified and therefore the three-level operation is not complete.

This status is not a declaration of loss. It preserves the known state and identifies exactly what remains unproven.

### 22.3 Memory representation boundary

Persistent Memory is a continuity layer, not automatically a byte-exact document vault. A memory update may preserve the operative rule, identifiers, lineage, current state, and recovery pointer, but that does not prove the full 21-section document is stored verbatim. Exact-document persistence requires an independently retrievable representation and matching evidence. Until such retrieval exists, the correct state is `WRITE-ACCEPTED / NOT-INDEPENDENTLY-VERIFIED`.

### 22.4 Mandatory per-destination evidence record

For every execution of «ثبت کن», record at minimum:

- destination name and exact path/provider;
- intended Stable ID, Production ID, version, and lineage;
- write result/receipt when available;
- independent read-back result or explicit reason it is unavailable;
- canonical representation/serialization used for comparison;
- byte length and cryptographic digest where a byte-exact comparison is technically supported;
- content match result, verification method, and version/revision binding;
- blockers, pending recovery pointer, next action, and timestamp only when actually captured;
- per-destination status and overall status.

A digest alone is not a read-back. A read-back without a defined representation is not a byte match. A repository commit does not prove Buffer or Memory. A Library Buffer file does not prove Repository or Memory.

### 22.5 Deferred registration and recovery

When any destination cannot be completed, preserve the same Stable ID, Production ID, version lineage, payload/reference pointer, blocker, and pending state. Retry safely without creating duplicate logical records. At the next valid opportunity, reconcile the pending record against the canonical version, finish the missing destination, read back, match, verify, and only then promote the overall status. Do not require a second user command to keep the recovery obligation alive.

### 22.6 Activation and acceptance

This contract is **ACTIVE / LIVING as the governing rule**. That design status must not be confused with proof that every destination or every automatic runtime mechanism is operational. Acceptance requires all of the following to be demonstrated independently:

1. A plain «ثبت کن» invokes the full contract without prompting the user to restate its layers.
2. The complete reference document and identifiers are preserved with lineage.
3. Repository, Buffer, and Memory each receive destination-specific state and evidence.
4. Every available destination supports independent read-back and comparison; unavailable ones remain explicitly pending/unverified.
5. A partial result never becomes `COMPLETE` by inference.
6. Pending records remain recoverable and can be reconciled without loss or duplicate logical registration.
7. The response reports only what the evidence proves.

### 22.7 Revision lineage

This revision extends, and does not replace, the prior 2026-10-06 Version 1.0 reference. Existing history and IDs remain valid. New changes must continue from this revision with explicit lineage; do not overwrite prior history or reinterpret historic evidence as fresh verification.

---

## 23. Historical operational declaration from revision 1.1.0

**Historical snapshot only — not the latest state.** At that time, command semantics were marked `ACTIVE / LIVING`; Repository and Buffer were reported as revision 1.1.0; Persistent Memory was `WRITE-ACCEPTED / NOT-INDEPENDENTLY-VERIFIED`. The current audit state is recorded in Section 24 below.


---

## 24. Revision 1.1.2 — Hammer Audit of Actual Registration Evidence

**Audit Date:** 2026-10-12  
**Exact Time:** Not independently captured; intentionally not invented.  
**Audit Trigger:** User requested a hammer-level audit to distinguish actual execution from an unsupported success report.  
**Audit Method:** Independently fetch the canonical repository file; read back the exact Buffer and Reference Vault files; compare the complete returned text representations; inspect the universal registration contract.  
**Related contract:** UNIVERSAL-REGISTER-COMMAND-EXECUTION-CONTRACT-2026-09-29-001.

### 24.1 Findings before this revision

1. The canonical repository copy, Buffer copy, and Reference Documents Vault copy all existed and were independently retrieved.
2. The complete returned text for repository, Buffer, and Reference Vault was identical at the time of audit (17,475 characters per returned text representation; Library metadata reported 21,963 bytes for each stored file). This verifies equality of those retrieved representations for revision 1.1.1.
3. The previous revision contained a governance/documentation defect: the header identified Version 1.1.1, while the operational declaration still called the current state revision 1.1.0. That mismatch is corrected by this revision; the older declaration is retained explicitly as historical.
4. The Persistent Memory layer was not independently retrieved or read back. Its write acceptance, if any, is not proof of exact document persistence, recall in a future conversation, or independent verification.
5. A reference contract and a saved state record do not by themselves prove an autonomous background retry/runtime mechanism. The recovery obligation is documented and must be resumed when a valid execution opportunity exists; no unobserved background process is claimed.

### 24.2 Evidence matrix for the audit

| Destination | Evidence established | Current state |
|---|---|---|
| Canonical Repository | The repository file was fetched; its full text was the comparison baseline. This revision must be fetched again after commit. | Pending verification of revision 1.1.2 until post-write read-back |
| Registration Buffer | Full stored file independently read; it matched the repository baseline for revision 1.1.1. This revision must be uploaded and read back. | Pending verification of revision 1.1.2 until post-write read-back |
| Reference Documents Vault | Full stored file independently read; it matched the repository baseline for revision 1.1.1. This revision must be uploaded and read back. | Pending verification of revision 1.1.2 until post-write read-back |
| Persistent Memory | No provider-level independent read-back was available in this audit. | NOT-INDEPENDENTLY-VERIFIED / PENDING |

### 24.3 Full-contract interpretation

The governing command is not limited to creating this reference document. A plain «ثبت کن» invokes the applicable rules from this master reference and the Universal Register Command Execution Contract, including:

- preserve the user's actual target, requested action, destinations/conditions, and required output before acting;
- preserve the full valuable artifact/context, classify it, retain provenance, lineage, previous versions, stable/production identity, architectural placement, and recovery pointers;
- assess whether a complete reference document is required and create/update it in the canonical reference location when applicable;
- attempt each required destination independently: Repository, Buffer/Library, and Persistent Memory;
- record write evidence, then independently read back each destination where supported, compare the retrieved representation, verify against the correct version/revision, reconcile differences, and report each layer's real state;
- preserve every unfinished layer with the same identity and lineage, explicit blocker, pending state, and next recovery action; do not call it lost, silently replace it, or create duplicate logical records;
- on a later valid recovery opportunity, excavate the pending state, identify, validate, deduplicate, connect/reconcile, finish the missing destination, read back, match, verify, and only then promote the overall status;
- do not claim implementation, automatic runtime execution, future-session recall, exact byte persistence, or completion without evidence that specifically supports that claim;
- explain English IDs/statuses/technical terms in Persian responses.

### 24.4 Current completion gate

**The three-level transaction is not complete unless Repository, Buffer, and Persistent Memory each have their own destination-specific evidence sufficient for the claim being made.** Evidence from the Reference Vault is useful Library evidence, but it does not substitute for the canonical Repository or Persistent Memory.

**Overall status before post-write verification of this revision:** PARTIAL / PENDING.  
**Persistent Memory:** NOT-INDEPENDENTLY-VERIFIED / PENDING.  
**Contract semantics:** ACTIVE / LIVING as the governing specification; actual runtime automation remains unproven unless separately tested.

This revision adds an audit layer without deleting the prior history or reclassifying historical evidence as current proof.

---

## 25. Amendment — دائمی‌بودن فرمان مادر «ثبت کن» و الزام اجرای کامل

**Amendment ID:** 3LR-GOVREG-ALWAYS-ON-2026-10-12-001  
**Date:** 2026-10-12  
**Exact Time:** NOT CAPTURED / ثبت نشده؛ زمان ساخته یا حدس زده نشود.  
**Status:** ACTIVE / LIVING as a governing rule; destination persistence and runtime automation remain evidence-gated.

### 25.1 فرمان کوتاه، معنای کامل

کاربر نباید بعد از هر بار گفتن «ثبت کن»، دوباره قواعد، مراحل یا مقصدها را فهرست کند. عبارت کوتاه **«ثبت کن» به‌تنهایی فرمان کامل مادر** است و تمام الزامات این سند و قراردادهای مادرِ مرتبط را فعال می‌کند. این قاعده برای محتوای ارزشمندِ قابل ثبت، از جمله کشف، تصمیم، قانون، معماری، GAP، آزمون، شواهد، اصلاح خطا و خودِ قراردادهای ثبت، اعمال می‌شود.

### 25.2 چرخهٔ اجرایی اجباری

1. حفظ محتوای اصلی و شواهد مرتبط، بدون حذف تاریخچهٔ لازم.
2. تشخیص اینکه چه چیزی باید ثبت شود؛ طبقه‌بندی و پیوند آن با منشأ، نسخه‌ها، سوابق و معماری موجود.
3. استفاده از شناسهٔ پایدار/تولیدی موجود برای ادامهٔ همان رکورد؛ شناسهٔ تازه فقط وقتی ساخته شود که واقعاً یک موجودیت مستقل باشد.
4. ساخت یا به‌روزرسانی سند مرجع کامل، در صورت کاربرد، با فراداده، شواهد، محدودیت‌ها و مسیر بازیابی.
5. اقدام مستقل برای ثبت در مخزن، بافر و حافظهٔ پایدار، و نیز جای‌گذاری سند در خزانهٔ اسناد مرجع در صورت کاربرد.
6. ثبت شواهد نوشتن، سپس بازخوانی مستقل هر مقصدِ در دسترس، تطبیق نسخه و محتوا، راستی‌آزمایی و رفع ناسازگاری‌ها.
7. تعیین وضعیت هر مقصد جداگانه و وضعیت کلی؛ ثبت موفقیت یک مقصد هرگز جایگزین اثبات مقصد دیگر نیست.
8. اگر بخشی مسدود یا ناممکن بود، حفظ همان رکورد با وضعیت PENDING / در انتظار، شرح مانع، آنچه واقعاً انجام شده، آنچه اثبات نشده و اقدام بعدیِ بازیابی. شکست یک مرحله نباید باعث حذف بی‌صدا یا ادعای تکمیل شود.
9. در فرصت معتبر بعدی، اجرای خاک‌برداری و تکمیلِ مرحلهٔ جامانده با همان شناسه و تبار؛ سپس بازخوانی و تأیید مجدد پیش از ارتقای وضعیت.
10. گزارش نهایی کوتاه اما دقیق: چه انجام شد، برای هر سطح چه شواهدی موجود است، چه چیزی معلق است و چه ادعایی هنوز مجاز نیست.

### 25.3 تفاوت الزام قراردادی با توانایی واقعی

این سند به‌تنهایی ابزار نوشتن، دسترسی، حافظهٔ بین‌گفتگویی یا اجرای خودکار پس‌زمینه ایجاد نمی‌کند. بنابراین:
- «ACTIVE / LIVING» یعنی قاعده در قرارداد فعال است؛ به‌تنهایی اثبات‌کنندهٔ اجرای خودکار یا موفقیت در همهٔ مقصدها نیست.
- اگر قابلیت نوشتن یا بازخوانیِ حافظهٔ پایدار در دسترس نباشد، وضعیت آن باید **NOT-INDEPENDENTLY-VERIFIED / مستقل تأییدنشده** یا **PENDING / در انتظار** گزارش شود؛ هرگز به‌دروغ REGISTERED / ثبت‌شده اعلام نشود.
- هیچ تضمینی دربارهٔ تلاش خودکار در آینده داده نمی‌شود، مگر اینکه زمان‌بندی، اجرا و نتیجه با شواهد واقعی آزموده شده باشند.
- کاربر لازم نیست این محدودیت‌ها یا قواعد را هر بار یادآوری کند؛ مسئولیت اجرای موجود، بررسی ابزارهای در دسترس و بیان دقیق محدودیت‌ها بر عهدهٔ دستیار است.

### 25.4 درخواست فعلی و وضعیت سه‌سطحی

درخواست 2026-10-12 این است که همین قاعده به‌صورت سند مرجع کامل، با حفظ شناسه و تبار فعلی، در تمام سطوح ثبت شود.

- Repository / مخزن: باید نسخهٔ جدید نوشته و از مخزن دوباره خوانده شود.
- Buffer / بافر: باید همین نسخهٔ دقیق دریافت و مستقل بازخوانی شود.
- Reference Documents Vault / خزانهٔ اسناد مرجع: باید همین نسخهٔ دقیق دریافت و مستقل بازخوانی شود.
- Persistent Memory / حافظهٔ پایدار: فقط در صورت وجود ابزار واقعی نوشتن و بازخوانی مستقل می‌توان وضعیت ثبت‌شده را اعلام کرد؛ در غیر این صورت معلق و مستقل‌تأییدنشده باقی می‌ماند.

**Overall completion gate / شرط تکمیل کلی:** PARTIAL / PENDING تا زمانی که برای هر سه سطح اصلی (مخزن، بافر و حافظهٔ پایدار) شواهد مقصد-ویژه وجود نداشته باشد. بازخوانی خزانهٔ اسناد مرجع، به‌تنهایی جایگزین اثبات حافظهٔ پایدار نیست.
