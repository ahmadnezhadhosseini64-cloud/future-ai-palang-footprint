# اصول بنیادین معماری برای همهٔ پروژه‌های جدید — سند مادر زنده

- Stable ID / شناسهٔ پایدار: `NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001`
- Production ID / شناسهٔ تولید: `NPFAP-20261024-001`
- Version / نسخه: 1.0.2
- Status / وضعیت: REGISTERED / READ-BACK VERIFIED / IDENTIFIERS MATCHED / ACTIVE / LIVING / EVOLVABLE / EXTRACTABLE / RECOVERY-ORIENTED
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
- [x] Exact file read-back after creation; Stable ID, Production ID, source anchor, contract and index links matched.
- [x] Governing contract updated to v1.3.0 and read back.
- [x] Reference index and project entry point updated and read back.
- [ ] Fresh-project adoption test executed.
- [ ] Export package and cold-start recovery test executed.

## 7. Status semantics / معنای وضعیت

This is a cross-project foundational specification. It becomes repository READ-BACK VERIFIED only after the exact file is fetched again and the expected identifiers, contents and links match. It becomes validated for a specific new project only after that project's own adoption evidence and acceptance tests exist.


## Repository read-back receipt — 2026-10-24
The exact foundational-principles file was fetched again after creation. Stable ID, Production ID, source architecture-zero link, governing contract v1.3.0, reference-index entry and repository README entry were confirmed. The governing contract, index, README and inherited architecture master were also fetched and their updates confirmed. This is repository-level read-back only; a fresh-project adoption test, export package test and cold-start recovery test remain open.


## Living activation and independent 0.0 anchor — 2026-10-24
This foundational mother is now linked to the independent living checkpoint [CURRENT-041](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-041-FOUNDATIONAL-ARCHITECTURE-MOTHER-ACTIVATION.md), parent [CURRENT-040](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-040-GPT6-POINT-0.0-RECOVERY-CHECKPOINT.md), interaction [IN-033](../../0.0/anchors/PALANG-0.0-IN-20261024-033-ACTIVATE-FOUNDATIONAL-ARCHITECTURE-MOTHER.md) ↔ [OUT-033](../../0.0/anchors/PALANG-0.0-OUT-20261024-033-ACTIVATE-FOUNDATIONAL-ARCHITECTURE-MOTHER.md), and event [EVT-0141](../../architecture/BEHAVIOR-TRACE/EVT-0141-FOUNDATIONAL-ARCHITECTURE-MOTHER-ACTIVATION-2026-10-24.md). The multi-point 0.0 registry and reference index carry the same links. Previous anchors remain preserved.

Living status means versioned, evidence-gated, recoverable, and open to controlled growth; it does not imply global automatic background capture. Fresh-project adoption and export/cold-start recovery tests remain OPEN / NOT RUN until evidence is recorded.


## Hard-audit amendment — v1.0.1 — 2026-10-24
The cross-project principles are now governed alongside the hard-audit mother [HA-001](./NEW-PROJECT-ARCHITECTURE-HARD-AUDIT-2026-10-24-001.md) and current checkpoint [CURRENT-042](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-042-NEW-PROJECT-ARCHITECTURE-HARD-AUDIT.md). The previous CURRENT-041 node remains preserved as historical lineage. The active handoff is [NEXT-040 — fresh-project adoption test](../../0.0/anchors/PALANG-0.0-NEXT-20261024-040-FRESH-PROJECT-ADOPTION-TEST.md). This version corrects the document version ledger and does not claim that the adoption test, prototype or cold-start recovery has passed.


## 8. Completeness and verifiability contract — v1.0.2

**Hard rule:** no architectural claim may remain as an unbounded slogan. Every principle, capability, status, link, test, and open task must have a defined verification method, an evidence location, an owner/next action, and a truthful state. If something cannot currently be verified, it must be explicitly marked UNKNOWN, NOT RUN, NOT BUILT, NOT VERIFIED, or BLOCKED; it must not be silently treated as complete.

### 8.1 Mandatory evidence row for each material claim

Each material claim in every project must be traceable to:
1. **Claim/requirement ID** — unique and stable.
2. **Expected result** — observable acceptance criteria, not subjective wording alone.
3. **Verification method** — exact file/path, test, command, workflow, review, or repeatable procedure.
4. **Evidence reference** — commit, artifact, test output, read-back result, or dated observation.
5. **Observed result** — what actually happened, including failure and uncertainty.
6. **Status** — NOT STARTED / OPEN / BLOCKED / NOT RUN / PASS / FAIL / INCONCLUSIVE / NOT VERIFIED.
7. **Next action and closure condition** — one concrete action and what evidence permits closure.
8. **Time provenance** — repository last-change commit in UTC and its Tehran equivalent; message/event time separate and UNKNOWN when not evidenced.

A document's existence is evidence of document presence only. It is not evidence that the described product, runtime, automation, integration, or recovery works.

### 8.2 Mandatory link and identity integrity

For every material node, verify both directions where applicable:
- IN ↔ OUT ↔ EVT ↔ CURRENT/0.0 ↔ living mother ↔ NEXT.
- Stable ID, Production ID, version, path, parent and successor must match across the node, index, registry and relevant masters.
- All relative links must resolve to an existing repository path; report missing links explicitly.
- A historical checkpoint may refer to the state current at its own time, but every active entry point must identify the latest current checkpoint and preserve predecessor links.
- A version change must update the file header and its change note; index/status changes must be read back. Do not infer versions from commit messages.

### 8.3 Mandatory principle-to-test matrix

Every new project must create a matrix with at least one observable acceptance criterion for each inherited principle:
- lineage and preservation → predecessor and history links exist; no prior anchor silently deleted;
- Point 0 and independent 0.0 → both root and resumable checkpoint are uniquely identified;
- living master → version, change log, current state, open gaps and next action exist;
- behavior trace → material interaction has IN/OUT/EVT and explicit evidence boundaries;
- identity/provenance → IDs, origin and version agree across linked records;
- evidence-gated promotion → no Child is promoted through Rahm to Master without recorded criteria and evidence;
- UTC-first time → actual repository commit timestamp is recorded in UTC and Tehran is derived from the same instant;
- recoverability/export → a clean-session recovery attempt reconstructs the current state from the export bundle;
- error/drift learning → detected mismatch has a finding, correction or justified open status, and a regression check;
- status boundaries → no status is stronger than its evidence;
- destination separation → each storage/runtime destination has its own write and read-back evidence;
- next-action continuity → CURRENT points to an executable NEXT with closure criteria;
- host portability → a second host or documented neutral reader can interpret the exported bundle;
- no premature closure → every PASS points to observable evidence; all other gates stay open.

### 8.4 Audit closure rules

- “REGISTERED” means the write succeeded.
- “READ-BACK VERIFIED” means the exact stored file was fetched after the write and expected content matched.
- “LINKS VERIFIED” means all declared local links were checked against repository paths.
- “VALIDATED” means acceptance criteria were exercised and passed with evidence.
- “INTEGRATED” means the change is linked into the active index/registry/master and read back.
- “ACTIVE / LIVING” means the record has a current owner/next action and versioned continuation path; it does not prove automatic execution.
- “RECOVERABLE” may describe the design until cold-start testing passes; actual recovery capability must separately be labelled TESTED / PASS.
- If any criterion is unknown, the overall result cannot be unconditional PASS. Use PARTIAL / INCONCLUSIVE and list the unknown criteria.

### 8.5 Required end-of-change reconciliation

After every material architecture update:
1. fetch each changed file after write;
2. match IDs, versions, status and cross-links;
3. resolve active-current and index discrepancies;
4. inspect broken/missing relative links;
5. compare requirements against observed evidence;
6. preserve unresolved findings with a concrete next action;
7. update the current checkpoint, living mother and registry;
8. state exactly which layers are verified and which are not.

### 8.6 Current truth boundary

At this version, repository document presence and read-back can be verified through the linked GitHub files. The fresh-project adoption test remains OPEN / NOT RUN; prototype remains NOT BUILT; cold-start recovery remains NOT RUN; any external destination remains NOT VERIFIED unless separately evidenced. These limits are explicit architecture state, not footnotes to omit.

### 8.7 Versioned continuity

v1.0.2 turns the principle “nothing should be impossible to fully examine” into a testable governance contract. It preserves v1.0.0/v1.0.1 history, links the hard-audit mother [HA-001](./NEW-PROJECT-ARCHITECTURE-HARD-AUDIT-2026-10-24-001.md), current checkpoint [CURRENT-042](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-042-NEW-PROJECT-ARCHITECTURE-HARD-AUDIT.md), interaction [IN-034](../../0.0/anchors/PALANG-0.0-IN-20261024-034-HARD-AUDIT-NEW-PROJECT-ARCHITECTURE.md) ↔ [OUT-034](../../0.0/anchors/PALANG-0.0-OUT-20261024-034-HARD-AUDIT-NEW-PROJECT-ARCHITECTURE.md), event [EVT-0142](../../architecture/BEHAVIOR-TRACE/EVT-0142-NEW-PROJECT-ARCHITECTURE-HARD-AUDIT-2026-10-24.md), and active adoption task [NEXT-040](../../0.0/anchors/PALANG-0.0-NEXT-20261024-040-FRESH-PROJECT-ADOPTION-TEST.md).
