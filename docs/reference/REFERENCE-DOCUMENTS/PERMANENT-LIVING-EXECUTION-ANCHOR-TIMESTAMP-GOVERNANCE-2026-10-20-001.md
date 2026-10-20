# سند مرجع حاکم — قواعد اجرایی ثبت، لنگر و زمان‌گذاری

- Stable ID: PERMANENT-LIVING-EXECUTION-ANCHOR-TIMESTAMP-GOVERNANCE-2026-10-20-001
- Production ID: PLEATG-HAIF-2026-10-20-001
- Version: 1.0.0
- Owner: Ahmad Nezhadhosseini / احمد پلنگ
- Project: Future AI / Palang Footprint
- Record date: 2026-10-20
- Exact request time: UNKNOWN / UNVERIFIED
- Timezone: Asia/Tehran (UTC+03:30)
- Status target: ACTIVE / LIVING IN REPOSITORY, only after write/read-back/match
- Origin: explicit request to make registration, complete reference documentation, timestamping and anchor rules ongoing and operational.

## 1. Purpose
This is the canonical reference for applying the user's registration and traceability rules to future project work. "Ongoing" means the rule is to be applied in subsequent work when context and tools permit; it does not imply automatic storage in every destination or guaranteed platform memory.

## 2. Required lifecycle
PRESERVE → IDENTIFY → CLASSIFY → PROVENANCE/LINEAGE → STABLE ID + PRODUCTION ID + VERSION → ANCHOR → COMPLETE REFERENCE → ARCHITECTURE LINK → TIMESTAMP EVIDENCE → WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS BY DESTINATION → NEXT ACTION → RESUME.

معنی: حفظ → شناسایی → طبقه‌بندی → منشأ و تبار → شناسهٔ پایدار/تولید/نسخه → لنگر → سند مرجع کامل → پیوند معماری → شواهد زمانی → نوشتن → بازخوانی → تطبیق → تأیید → رفع مغایرت → وضعیت هر مقصد → اقدام بعدی → ادامه.

«ثبت کن» یعنی اجرای این چرخه تا جایی که ابزار و دسترسی واقعی اجازه می‌دهد؛ نه ساخت گزارش کوتاه. اگر مقصدی در دسترس نیست، وضعیت آن باز می‌ماند و بستهٔ کامل قابل‌بازیابی باید ارائه شود.

## 3. Anchor rule
هر خروجی مهم که تصمیم، قاعده، اقدام، خطا، اصلاح، معماری، وضعیت پروژه یا تعهد ادامه را تغییر می‌دهد، به لنگر خروجی یا رویداد دارای شناسهٔ دقیق وصل شود. لنگر شامل منشأ، تصمیم و دلیل، Stable ID، Production ID، Version، مسیر سند مرجع، پیوندهای معماری، شواهد زمانی، وضعیت هر مقصد، محدودیت‌ها و اقدام بعدی است. ۰.۰ فقط با تعیین صریح کاربر ساخته می‌شود؛ نقاط قبلی بی‌صدا حذف یا ادغام نمی‌شوند.

ثبت صرف در صف به معنی ادغام معماری نیست. جایگاه و پیوندها باید در پرونده و نمایهٔ معماری منعکس شوند؛ سپس فایل‌های مقصد بازخوانی و تطبیق شوند.

## 4. Timestamp rule
این زمان‌ها جدا ثبت شوند:
- Request/Interaction At — زمان پیام/درخواست؛ فقط با شاهد معتبر.
- Action At — زمان اقدام ابزار؛ فقط اگر ابزار آن را ارائه کند.
- Commit At — زمان ثبت مخزن، همراه commit ID و منطقهٔ زمانی.
- Last Modified At — آخرین تغییر از منبع مشخص.
- Read-back At — زمان بازخوانی واقعی، اگر ثبت شده باشد.
- Verified At — زمان تأیید پس از بازخوانی و تطبیق موفق، اگر شاهد زمانی موجود باشد.
- Timezone and provenance — منطقهٔ زمانی و منشأ هر مقدار زمانی.

زمان نامعلوم باید UNKNOWN / UNVERIFIED بماند. زمان commit را جای زمان پیام یا بازخوانی نگذار و زمان را حدس نزن.

## 5. Destination independence
Repository / مخزن، Buffer / بافر، Persistent Memory / حافظهٔ پایدار، Library / کتابخانه و Dropbox / دراپ‌باکس مقصدهای جدا هستند. برای هر مقصد، نوشتن، بازخوانی، تطبیق و وضعیت مستقل ثبت شود. WRITE ≠ VERIFIED (نوشتن مساوی تأیید نیست). اثبات یک مقصد، اثبات مقصد دیگر نیست.

## 6. State vocabulary
FOUND ≠ RETRIEVED ≠ VALIDATED ≠ REVIVED ≠ VERIFIED ≠ ACTIVE.
INCOMPLETE ≠ LOST; PENDING ≠ BURIED; INTERRUPTED ≠ FAILED.
یعنی پیدا شدن، بازیابی، اعتبارسنجی، احیا، تأیید و فعال بودن مراحل متفاوت‌اند؛ ناقص گم‌شده نیست؛ در انتظار مدفون نیست؛ توقف موقت شکست نیست.

## 7. Architecture links
- Living governing reference: [Unified Output Anchor Registration](./UNIFIED-OUTPUT-ANCHOR-REGISTRATION-LIVING-REFERENCE-2026-10-19-001.md)
- Complete path: [0.0 complete path reference](./PALANG-0.0-COMPLETE-PATH-AND-GOVERNING-ADDENDUM-2026-10-20-001.md)
- Architecture queue index: [Integration Queue](../../architecture/INTEGRATION-QUEUE/README.md)
- Queue case: [0.0 architecture case](../../architecture/INTEGRATION-QUEUE/PALANG-0.0-COMPLETE-PATH-GOVERNING-ADDENDUM-2026-10-20-001.md)
- Event: [EVT-0015](../../architecture/BEHAVIOR-TRACE/EVT-0015-0.0-GOVERNING-ADDENDUM-ARCHITECTURE-INTEGRATION-2026-10-20.md)
- Behavior trace: [Interaction Behavior Trace](../../architecture/BEHAVIOR-TRACE/INTERACTION-BEHAVIOR-TRACE-2026-10-19-001.md)
- 0.0 registry: [0.0 README](../../0.0/README.md)
- Current anchor: [Current 0.0 anchor](../../../checkpoints/PALANG-0.0-CURRENT-2026-10-20-001.md)

## 8. Current destination status and resume
- Repository: target ACTIVE / LIVING only after actual write, read-back and match.
- Buffer: NOT VERIFIED until independently evidenced.
- Persistent Memory: NOT VERIFIED until independently evidenced.
- Library: NOT VERIFIED until independently evidenced.
- Dropbox: OPEN / WAITING until connection, test write, read-back and match succeed.
- Exact request time: UNKNOWN / UNVERIFIED.
- Exact read-back time: UNKNOWN / UNVERIFIED unless valid tool metadata exists.
- After creation: fetch this exact path, compare Stable ID, version, rules and links, then update the living governing reference and architecture queue/trace as applicable; read back each changed file. Do not create duplicates or claim unverified destinations are complete.


## 9. Temporal bracketing rule — ثبت محصور بین دو لنگر زمانی
When an event's exact timestamp is unavailable, do not immediately leave its temporal placement wholly unspecified if reliable neighboring timestamped records can bound it. Register the event between a preceding and a following known timestamped anchor.

### Required fields
- **Event ID / شناسهٔ رویداد**
- **Previous temporal anchor / لنگر زمانی قبل:** ID, timestamp, timezone, evidence and source.
- **Following temporal anchor / لنگر زمانی بعد:** ID, timestamp, timezone, evidence and source.
- **Bounded interval / بازهٔ محصور:** after the previous anchor and before the following anchor, or inclusive/exclusive bounds if the evidence establishes them.
- **Ordering evidence / شاهد ترتیب:** conversation order, repository history, event sequence or other actual evidence.
- **Exact event time:** UNKNOWN / UNVERIFIED unless independently evidenced.
- **Confidence / اطمینان:** bounded, partial, or unbounded, with reason.
- **Method and limitations / روش و محدودیت:** explain why this event belongs within the interval; do not infer more precision than the evidence supports.

### Rules
1. Use only actual, independently supported timestamps. A commit time, message time, modification time and read-back time are different event types and must not be substituted for one another.
2. A temporal interval is not an exact timestamp. Never invent a midpoint or assign a made-up hour/minute.
3. If only one reliable anchor exists, record a one-sided bound and state the limitation; do not pretend that there are two anchors.
4. If two anchors exist but event ordering cannot be proven, record the candidate interval as uncertain rather than asserting it as verified.
5. Preserve the original unknown exact time alongside the bounded interval; never overwrite uncertainty with false precision.
6. When later evidence supplies an exact time, append the new evidence and revise the temporal assessment with provenance; preserve the prior state/history.
7. Link the event to both anchor records and to the relevant reference, behavior trace, queue and current continuation point as applicable.
8. Read back the new entry and verify the anchor IDs, timestamps, timezone, interval and links.

**Persian interpretation:** اگر ساعت دقیق رویداد معلوم نیست، اما دو ثبت معتبرِ زمان‌دار پیش و پس از آن وجود دارند و ترتیب رویداد با شواهد قابل اثبات است، رویداد را در بازهٔ میان آن دو ثبت کن. زمان دقیق را همچنان نامعلوم اعلام کن. زمان میانی نساز؛ زمان commit را جای زمان پیام نگذار؛ و اگر مرزها یا ترتیب اثبات نشده‌اند، عدم‌قطعیت را آشکار نگه دار.

**Acceptance criterion / معیار پذیرش:** رویداد دارای شناسه، دو لنگر زمان‌دار با منبع و منطقهٔ زمانی، بازهٔ محدودشده، شاهد ترتیب، وضعیت دقت، پیوندهای بازیابی و بازخوانیِ تطبیق‌شده باشد؛ در غیر این صورت وضعیت باید صریحاً ناقص یا تأییدنشده بماند.

### 9.1 Registered implementation event and recovery links
- Event ID: EVT-0018-TEMPORAL-BRACKETING-RULE-2026-10-20
- Complete event record: [EVT-0018 — ثبت محصور بین دو لنگر زمانی](../../architecture/BEHAVIOR-TRACE/EVT-0018-TEMPORAL-BRACKETING-RULE-2026-10-20.md)
- Behavior trace: [Interaction Behavior Trace](../../../architecture/BEHAVIOR-TRACE/INTERACTION-BEHAVIOR-TRACE-2026-10-19-001.md)
- Architecture integration queue: [Queue index, section 22](../../../architecture/INTEGRATION-QUEUE/README.md)
- Central 0.0 registry: [0.0 registry](../../../0.0/README.md)
- Current continuation anchor: [PALANG-0.0-CURRENT-2026-10-20-001](../../../../checkpoints/PALANG-0.0-CURRENT-2026-10-20-001.md)
- Living implementation reference: [Unified Output Anchor Registration](./UNIFIED-OUTPUT-ANCHOR-REGISTRATION-LIVING-REFERENCE-2026-10-19-001.md)
- Request timestamp for the temporal rule: UNKNOWN / UNVERIFIED. Do not infer it from commit metadata.
- Verification rule: each linked file must be fetched after its latest write and matched independently. The repository chain does not prove Buffer, Persistent Memory, Library or Dropbox persistence.
