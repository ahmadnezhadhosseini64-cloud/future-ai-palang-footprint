# اصول بنیادین معماری برای همهٔ پروژه‌های جدید — سند مادر زنده

- Stable ID / شناسهٔ پایدار: `NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001`
- Production ID / شناسهٔ تولید: `NPFAP-20261024-001`
- Version / نسخه: 1.0.0
- Status / وضعیت اولیه: REGISTERED / ACTIVE / LIVING / EVOLVABLE / EXTRACTABLE / RECOVERY-ORIENTED / READ-BACK PENDING
- Scope / دامنه: الگوی پایه برای هر پروژهٔ جدید در خانوادهٔ Future AI / Palang Footprint / HAIF و شاخه‌های محصول/میزبان آن؛ با سازگارسازی مستند برای پروژه‌های دیگر
- Source anchor / منشأ: [G6IP-ARCH-ZERO-20261024-001](../../0.0/anchors/PALANG-0.0-ARCHITECTURE-ZERO-20261024-001-NEW-PROJECT-ARCHITECTURE-ROOT.md)
- Governing contract / قرارداد حاکم: [UIALAC-2026-10-20-001](./UNIVERSAL-INTERACTION-ANCHOR-AND-LIVING-ARCHITECTURE-CONTRACT-2026-10-20-001.md)
- HAIF parent / والد معماری: [GPT-6 inherited architecture master](./GPT6-NEW-PROJECT-INHERITED-ARCHITECTURE-LIVING-MASTER-2026-10-24-001.md)
- Repository: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`

## 1. Foundational decision / تصمیم بنیادین

The practices validated during creation of the new GPT-6 project architecture are adopted as the default foundational architecture pattern for new projects: preserve lineage, anchor state, maintain a living master, track behavior with evidence, make the project extractable and recoverable, and promote changes only through verification. A new project is not an isolated architecture that erases its parent, and a “living” label is not evidence of automatic background operation.

روش‌هایی که در ساخت معماری پروژهٔ جدید GPT-6 به‌کار رفتند، از این پس الگوی پایه برای پروژه‌های جدید هستند: حفظ تبار، لنگرگذاری وضعیت، نگهداری سند مادر زنده، رفتارشناسی مبتنی بر شواهد، قابلیت استخراج و بازیابی، و ارتقای تغییرات فقط پس از اعتبارسنجی. پروژهٔ جدید معماری جداافتاده‌ای نیست که والد و تاریخچه را حذف کند؛ «زنده» بودن نیز به‌خودی‌خود اثبات ضبط خودکار در پس‌زمینه نیست.

## 2. Mandatory principles / اصول الزامی

1. **Preserve lineage / حفظ تبار:** identify parent architecture, origin, initial Point 0, later checkpoints and current state. Never silently replace or erase prior anchors.
2. **Point 0 + independent checkpoints / نقطهٔ صفر و ایستگاه‌های مستقل:** establish a uniquely identified initial root; create later 0.0/current anchors as independent additions with explicit parent/child links.
3. **Living mother document / سند مادر زنده:** keep one canonical, versioned governing master for the project branch, linked to its parent architecture and current checkpoint. Changes must be appended/versioned, not silently overwritten.
4. **IN/OUT and event chain / زنجیرهٔ ورودی، خروجی و رویداد:** for each material interaction preserve user input, assistant output, observable actions/results, feedback, errors/corrections, event ID and next action. Do not fabricate hidden reasoning.
5. **Palang + AI behaviorology / رفتارشناسی پلنگ و AI:** track task alignment, context continuity, drift, evidence quality, failure and correction. Treat interpretations as hypotheses until supported; use two tracks: continuity/recovery/growth and drift/evidence/error prevention.
6. **Stable identity and provenance / هویت و منشأ:** assign stable ID, production ID, version, source/provenance, status, timestamps and links appropriate to the artifact.
7. **Evidence-gated lifecycle / چرخهٔ مبتنی بر شاهد:** PRESERVE → CLASSIFY → PROVENANCE → ID/VERSION → ANCHOR → DOCUMENT/LINK → WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS.
8. **UTC-first repository time / زمان مخزن با مرجع UTC:** canonical repository registration time comes only from the actual Git commit metadata in UTC; show Tehran equivalent from that same instant (+03:30). Preserve message/event/test times separately; never substitute commit time for message time.
9. **Recoverability and extraction / بازیابی و استخراج:** package the master, current checkpoint, Point 0/0.0 anchors, IN/OUT, events, evidence, time ledger, open gaps and next action. Preserve IDs and relative links; test recovery on a fresh start before calling it verified.
10. **Child → Rahm → Master / دروازهٔ رشد معماری:** new ideas begin as hypotheses/Child; Rahm validates against acceptance criteria and evidence; only verified changes are promoted to Master. Keep failed tests and unresolved gaps visible.
11. **Error and drift learning / یادگیری از خطا:** record observed mismatch and corrective rule, including wrong branch/task selection; distinguish observation from inferred cause.
12. **Explicit status boundaries / مرزبندی وضعیت:** distinguish REGISTERED, READ-BACK VERIFIED, VALIDATED, INTEGRATED, ACTIVE, LIVING, PENDING, NOT BUILT, NOT RUN and NOT VERIFIED. A write is not a read-back; a read-back is not a runtime test.
13. **Destination separation / تفکیک مقصدها:** repository, persistent memory, library, buffer, Dropbox, deployed app and automation are separate destinations; each needs its own evidence. Never claim universal sync or always-on capture from a repository commit.
14. **Next-action continuity / تداوم گام بعدی:** every current anchor must point to one concrete next executable step, acceptance criteria and open gates.
15. **Host portability / استقلال از میزبان:** architecture rules and recovery bundle must be understandable and exportable to another AI host or runtime; the host provides capabilities but does not silently override project governance.
16. **No premature closure / منع اعلام تکمیل زودرس:** do not mark a prototype, recovery test, integration or automation complete until the corresponding artifact and result are inspectable.

## 3. Required minimum bundle for every new project / بستهٔ حداقلی هر پروژهٔ جدید

- Project identity, purpose, owner/authority and scope.
- Parent architecture and provenance.
- Point 0 root anchor and initial state.
- Living master reference and version policy.
- Current/recovery checkpoint and next-action record.
- IN/OUT/event behavior-trace structure.
- Stable/production IDs and UTC-first timestamp ledger.
- Evidence and verification checklist.
- Open issues, failed checks, external destinations and unverified capabilities.
- Export/recovery instructions and a cold-start acceptance test plan.

## 4. Lifecycle and governance / چرخهٔ حاکمیت

`NEW PROJECT → POINT 0 → LIVING MASTER → IN/OUT + EVENT → EVIDENCE GATE (RAHM) → CURRENT CHECKPOINT → NEXT ACTION → READ-BACK / TEST → VERSIONED MASTER UPDATE`

A project may use a different folder structure or tools, but it must retain these responsibilities and document any exception. Do not copy GPT-6-specific IDs into another project; mint unique IDs and preserve lineage.

## 5. Adoption record / ثبت پذیرش

This document adopts the architecture lessons from the new GPT-6 project’s architecture-zero work as a cross-project foundational rule. It is linked to the universal interaction/living architecture contract and the inherited HAIF master. It does not claim that all future projects are automatically instrumented; each project must instantiate these records and verify them.

## 6. Verification gates / دروازه‌های اعتبارسنجی

- [x] Unique stable ID and production ID defined.
- [x] Parent source architecture and governing contract linked.
- [x] Foundational principles and minimum project bundle documented.
- [ ] Exact file read-back after creation.
- [ ] Governing contract updated and read back.
- [ ] Reference index and project entry point updated and read back.
- [ ] Fresh-project adoption test executed.
- [ ] Export package and cold-start recovery test executed.

## 7. Status semantics / معنای وضعیت

This is a cross-project foundational specification. It becomes repository READ-BACK VERIFIED only after the exact file is fetched again and the expected identifiers, contents and links match. It becomes validated for a specific new project only after that project's own adoption evidence and acceptance tests exist.
