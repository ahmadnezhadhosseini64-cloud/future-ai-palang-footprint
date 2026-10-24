# دفتر زندهٔ درس‌های معماری — Living Architecture Lessons Registry

- Stable ID: PALANG-LIVING-ARCHITECTURE-LESSONS-REGISTRY-2026-10-23-001
- Production ID: LALR-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EVOLVABLE; repository READ-BACK VERIFIED; full lesson migration/runtime enforcement/rollback proof OPEN
- Owner: Future AI / Palang Footprint
- Governing master: [CMIND — ادامه از مدل اولیه، نه Dropbox](../../reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md)
- Governing architecture: [Living Evolutionary Architecture](../../../architecture/ARCH-2026-08-29-001-living-evolutionary-architecture.md)
- Intake: [Live Inbox](../LIVE-INBOX/README.md)
- Verification queue: [Architecture Integration Queue](../INTEGRATION-QUEUE/README.md)
- Current lesson: [LAL-20261023-001](./lessons/LAL-20261023-001-LIVING-APPEND-ONLY-VERIFY-RECOVER-CYCLE.md)
- Related event: [EVT-0107](../BEHAVIOR-TRACE/EVT-0107-LIVING-LESSON-CYCLE-AND-ROLLBACK-GOVERNANCE-2026-10-23.md)

## 1. Purpose
این پوشه مرجع مستقل و قابل بازیابی برای هر درس معماری است. درس نباید در متن گفتگو یا گزارش رویداد گم شود. هر درس شناسهٔ پایدار، منشأ، نسخه، قاعدهٔ عملیاتی، معیار آزمون، نتیجهٔ آزمون، دامنهٔ اعتبار، پیوند به اجزای متأثر و وضعیت جاری دارد.

## 2. Core guarantee and boundary
این دفتر و قراردادش در مخزن ثبت می‌شوند؛ اما ثبت سند به‌تنهایی تضمین نمی‌کند که هر میزبان AI همهٔ تعامل‌ها را خودکار شکار کند یا تمام قواعد را در هر اجرا به‌طور خودکار enforce کند. این توانایی فقط پس از پیاده‌سازی producer/runtime و آزمون مستقل آن قابل ادعاست. تا آن زمان، گردش‌کار ثبت باید هر بار با بازیابی منبع و بررسی قواعد مربوط اجرا شود و شکاف خودکارسازی OPEN بماند.

## 3. Required lifecycle
DISCOVERED → CAPTURED → CLASSIFIED → REGISTERED → READ-BACK VERIFIED → OPERATIONALIZED → TESTED → VALIDATED → INTEGRATED → ACTIVE / LIVING

- DISCOVERED: نشانهٔ اولیه شناسایی شده؛ هنوز درس قطعی نیست.
- CAPTURED: عبارت/منشأ و شواهد حفظ شده‌اند.
- CLASSIFIED: مشاهده، استنباط، فرضیه یا ناشناخته بودن جدا شده است.
- REGISTERED: پروندهٔ نسخه‌دار در مخزن commit شده است.
- READ-BACK VERIFIED: فایل پس از نوشتن مجدداً خوانده و شناسه/پیوند/محتوا تطبیق داده شده است.
- OPERATIONALIZED: درس به قاعده، کنترل، تصمیم یا گام اجرایی قابل‌استفاده تبدیل شده است.
- TESTED: آزمون مشخص با نسخه، ورودی، انتظار، نتیجه و شاهد اجرا شده است.
- VALIDATED: شواهد معیارهای پذیرش را برآورده کرده‌اند.
- INTEGRATED: سند مادر، دفتر درس‌ها، نمایه‌ها، صف، جزء متأثر و تست‌های مربوط هم‌تراز شده‌اند.
- ACTIVE / LIVING: قاعده در مسیر ادامه اعمال می‌شود و با شواهد تازه دوباره ارزیابی می‌گردد.

هیچ مرحله‌ای از روی وجود فایل یا وعدهٔ اجراشده فرض نمی‌شود.

## 4. Append-only, immutable history, and version promotion
1. پروندهٔ ثبت‌شده و نسخهٔ قبلی پاک یا بی‌صدا بازنویسی نمی‌شود.
2. اصلاح با addendum یا نسخهٔ جانشین جدید انجام می‌شود؛ علت، شواهد، آزمون و رابطهٔ supersedes/derived-from ثبت می‌گردد.
3. نسخهٔ جدید تنها پس از عبور از معیارهای پذیرش و ثبت شواهد به CURRENT/ACTIVE ارتقا می‌یابد.
4. نسخهٔ پیشین به‌عنوان تاریخی و قابل‌بازیابی حفظ می‌شود؛ جایگزین‌شدن به معنی حذف یا کپی‌کردن روی آن نیست.
5. هر نسخهٔ جاری به آخرین نسخهٔ پذیرفته‌شده وابسته است، ولی زنجیرهٔ نسخه‌ها و شواهد مستقل می‌مانند.
6. در شکست یا تناقض، آخرین baseline سالمِ اثبات‌شده انتخاب می‌شود؛ تغییر ناموفق حفظ می‌شود و ادامه از نسخهٔ سالم با یک شاخه/نسخهٔ اصلاحی انجام می‌شود. بازگشت باید ثبت شود، نه اینکه تاریخچه پاک شود.

## 5. Verification cadence and no-redundant-retest rule
- در زمان کشف درس: آزمون مستقیم یا شاهد موجود بررسی می‌شود.
- پس از تغییر قاعده، کد، schema، workflow، dependency یا مقصد: آزمون‌های مرتبط دوباره اجرا می‌شوند.
- پس از خطا، regression، تناقض شواهد یا بازیابی: آزمون هدفمند دوباره اجرا می‌شود.
- در checkpointهای چرخه‌ای: ممیزی ساختاری/پیوند/وضعیت اجرا می‌شود؛ این ممیزی جایگزین آزمون رفتاری نیست.
- اگر آزمون در همان نسخه موفق و شاهد معتبر آن ثبت شده باشد، بدون تغییر/نیاز/خطا/تناقض همان آزمون تکراری انجام نمی‌شود. قاعدهٔ NO-REDUNDANT-RETEST حفظ می‌شود.
- آزمون باید نسخهٔ مورد آزمون، پیش‌شرط، روش، نتیجه، شاهد قابل‌بازخوانی و محدودهٔ ادعا را ثبت کند.

## 6. Universal rule for every material artifact
هر درس، سند، کد، schema، آزمون، لنگر، صف، شاخص، اتصال، checkpoint و جزء معماری باید:
- ID پایدار و مسیر canonical داشته باشد؛
- منشأ و زنجیرهٔ parent/related را نگه دارد؛
- version و وضعیت جداگانه داشته باشد؛
- شاهد ثبت، بازخوانی و آزمون را از هم تفکیک کند؛
- به مالک/جزء/صف اقدام بعدی متصل باشد؛
- تاریخچهٔ نسخه‌ها و مسیر بازیابی را حفظ کند؛
- در برابر تغییرات مرتبط و شواهد متناقض دوباره ارزیابی شود.

## 7. Current lesson inventory (initial, not exhaustive)
| Lesson ID | Lesson | Operational rule | Current state |
|---|---|---|---|
| LAL-20261023-001 | درس معماری نباید فقط نوشته شود؛ باید عملیاتی، آزموده و به چرخهٔ نسخه‌پذیر وصل شود | هر درس → کنترل/آزمون/شاهد/بازخوانی/ارتباط/بازیابی | REGISTERED / READ-BACK VERIFIED / INTEGRATION PARTIAL |
| EVT-0103 | کشف رفتاری و برخورد شناسه باید آشکارا ثبت و اصلاح شود | طبقه‌بندی شواهد؛ یکتایی ID پیش از write؛ regression test | Existing event; runtime remains OPEN |
| EVT-0093 | تعامل پروژه‌محور واحد رشد است | IN/OUT/EVT → inbox → master → action → evidence | Existing event |
| NO-REDUNDANT-RETEST-2026-09-03-001 | آزمون بسته‌شده و معتبر بی‌دلیل تکرار نشود | retest on change, deployment, need, error, regression, conflicting evidence | Existing registered rule |
| EVT-0106 | لنگر تاریخی مقصد نباید مسیر جاری را منحرف کند | بازیابی آخرین 0.0/master/queue پیش از انتخاب اقدام | Existing event |

این جدول فقط فهرست آغازین است؛ ادعای شمارش کامل همهٔ درس‌های تاریخی نیست. مرحلهٔ بعد باید همهٔ درس‌های پراکنده را از event، inbox، master، registry و queue استخراج و با حفظ منشأ به این دفتر وصل کند.

## 8. Audit checklist
- [ ] هر درس کشف‌شده شناسهٔ مستقل دارد.
- [ ] هر درس به ورودی/رویداد/سند مادر و جزء متأثر پیوند دارد.
- [ ] قواعد عملیاتی با متن درس سازگارند.
- [ ] آزمون و معیار پذیرش مشخص‌اند.
- [ ] نتیجهٔ آزمون شاهد واقعی دارد یا صریحاً NOT RUN است.
- [ ] نسخهٔ پیشین حفظ و رابطهٔ نسخه‌ها ثبت شده است.
- [ ] نمایه، صف، master و پیوندهای داخلی read-back شده‌اند.
- [ ] وضعیت runtime/host/external از وضعیت repository جداست.
- [ ] شکست‌ها و علت‌های محتمل از علت‌های اثبات‌شده تفکیک شده‌اند.
- [ ] rollback/recovery از baseline سالم دارای آزمون و شاهد است.

## 9. Known open gaps
- Automatic capture of every host interaction and automatic lesson candidate extraction: OPEN / NOT PROVEN.
- Enforcing every lesson in every future host/runtime without a retrieval/invocation mechanism: OPEN / NOT PROVEN.
- Full repository-wide migration/count of all historical architecture lessons into this directory: OPEN.
- Tested rollback/recovery across every component and external destination: OPEN / NOT PROVEN.
- External persistence beyond the canonical repository: NOT ATTEMPTED in this registration.

## 10. Change rule
این README خودش نسخه‌پذیر است؛ اما تغییرات باید append-only و شاهددار باشند. هر به‌روزرسانی، نسخهٔ قبلی را از تاریخچه حذف نمی‌کند. این دفتر تا رسیدن به شاهد تازه ACTIVE / LIVING می‌ماند؛ هر بار که درس جدید، شکست، تناقض یا تغییر معماری کشف شود، دفتر و آزمون مربوط باید به‌روزرسانی شوند.


## Current interaction provenance
- User input: [IN-019](../../0.0/anchors/PALANG-0.0-IN-20261023-019-LIVING-LESSON-CYCLE.md).
- Assistant output: [OUT-019](../../0.0/anchors/PALANG-0.0-OUT-20261023-019-LIVING-LESSON-CYCLE.md).
- Behavior event: [EVT-0107](../BEHAVIOR-TRACE/EVT-0107-LIVING-LESSON-CYCLE-AND-ROLLBACK-GOVERNANCE-2026-10-23.md).
- Live inbox item: [INBOX-20261023-005](../LIVE-INBOX/entries/INBOX-20261023-005.md).


## Repository verification checkpoint — 2026-10-23
- Registry, lesson, event, IN-019, OUT-019, INBOX-20261023-005, CMIND, reference index (raw GitHub read), behavior-trace index, 0.0 registry, integration queue, live inbox and audit script were fetched/read back after writes.
- Expected IDs and principal links matched in the fetched surfaces.
- The first Living Architecture Audit run #1703 (run ID 39885773714) failed with two findings: the audit script used the wrong path docs/reference/REFERENCE_INDEX.md instead of docs/REFERENCE_INDEX.md, and the queue did not yet contain the new lesson ID at the commit tested. The path defect was corrected in commit 3703a9ec653b5c3574fb3f5d9c8aa6eef67eb50b. The queue now contains the lesson ID; a fresh audit on the corrected HEAD is required before marking structural audit PASS.
- Runtime lesson enforcement, complete historic lesson migration and real rollback/recovery remain OPEN.


## Verified structural audit — 2026-10-23
- Workflow: [Living Architecture Audit run 39885966380](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39885966380).
- Tested commit: 28a0977a0e4b6cc4c0122e86a5df79c562309282.
- Result: SUCCESS. Structural/link audit, historical 0.0 graph audit, repository timestamp inventory audit, historical graph manifest/edge validation, semantic UTC/Tehran timestamp-pair audit, compilation checks and durable host-adapter tests all completed successfully in this run.
- Workflow interval: 2026-10-23 01:47:19Z–01:47:35Z (UTC); Tehran equivalent 05:17:19–05:17:35 (+03:30).
- Scope boundary: this validates the tested repository commit and listed workflow checks; it does not prove automatic capture of all future ChatGPT messages, full historical lesson migration, or rollback across all external destinations.



## Execution successor — EVT-0108
- Current execution tracker: [EVT-0108](../BEHAVIOR-TRACE/EVT-0108-LIVING-ARCHITECTURE-EXECUTION-AND-EVIDENCE-CYCLE-2026-10-23.md).
- Independent interaction anchors: [IN-020](../../0.0/anchors/PALANG-0.0-IN-20261023-020-LIVING-ARCHITECTURE-EXECUTION-CYCLE.md) / [OUT-020](../../0.0/anchors/PALANG-0.0-OUT-20261023-020-LIVING-ARCHITECTURE-EXECUTION-CYCLE.md).
- Inbox: [INBOX-20261023-006](../LIVE-INBOX/entries/INBOX-20261023-006.md).
- Required next evolution: excavate historic lesson candidates with provenance, adjudicate duplicate IDs without merging uncertain records, turn confirmed rules into executable checks/manual gates, then run a fresh audit and bounded recovery test.
- Status: this is an append-only continuation; the inventory remains non-exhaustive and host-wide automation remains NOT PROVEN.



## Historic migration ledger
- First evidence-backed excavation batch: [HALML-2026-10-23-001](./HISTORIC-LESSON-MIGRATION-LEDGER-2026-10-23-001.md).
- Time provenance for the current interaction: [TIME-BINDING-INT-20261023-020](../BEHAVIOR-TRACE/TIME-BINDING-INT-20261023-020.md).
- The ledger is intentionally partial. Existing canonical sources remain the source of truth until provenance, semantic equivalence and acceptance gates are checked. No ambiguous IDs are merged.


## Verification evidence for current execution
- [VERIFY-INT-20261023-020](../BEHAVIOR-TRACE/VERIFICATION-CHECKPOINT-INT-20261023-020.md) records read-back and test scopes.
- [HALML-2026-10-23-001](./HISTORIC-LESSON-MIGRATION-LEDGER-2026-10-23-001.md) remains a partial inventory; migration completion is not inferred.



## Normalized source-linked lesson records — 2026-10-23
The following records were created as derivative, source-linked lessons. Canonical source documents remain authoritative; these records do not replace them.
- [LAL-20261023-002 — تعامل، واحد رشد معماری است](./lessons/LAL-20261023-002-INTERACTION-IS-ARCHITECTURE-GROWTH-UNIT.md) — source EVT-0093.
- [LAL-20261023-003 — شکارچی رفتار، منفی کاذب و یکتایی شناسه](./lessons/LAL-20261023-003-BEHAVIOR-HUNTER-FALSE-NEGATIVE-ID-COLLISION.md) — source EVT-0103; runtime remains OPEN.
- [LAL-20261023-004 — تداوم مسیر مدل اولیه، نه Dropbox](./lessons/LAL-20261023-004-CONTINUE-MODEL-INITIAL-NOT-DROPBOX.md) — source EVT-0106.
- [LAL-20261023-005 — عدم تکرار آزمون معتبر بدون محرک](./lessons/LAL-20261023-005-NO-REDUNDANT-RETEST.md) — source canonical NO-REDUNDANT-RETEST registration.
- [LAL-20261023-006 — بررسی منفی کاذب سامانهٔ ارزیابی](./lessons/LAL-20261023-006-AUTOMATED-FALSE-NEGATIVE-INVESTIGATION.md) — source EVT-0035 and Behavior Observatory test.
- [LAL-20261023-007 — بازگشت نسخه، رویداد تازه در تبار معماری است](./lessons/LAL-20261023-007-ROLLBACK-AS-NEW-LINEAGE-EVENT.md) — source persistence/recovery architecture.

State: six source-linked lesson files have been created and fetched back; this does not close complete historical migration or prove runtime enforcement. The next pass must validate local links, operationalize tests and avoid duplicate retests without a material trigger.


## Rollback test evidence — EVT-0109
- [EVT-0109](../BEHAVIOR-TRACE/EVT-0109-CONTROLLED-GIT-ROLLBACK-RECOVERY-TEST-2026-10-23.md) validates the bounded Git ref rollback path.
- [LAL-20261023-007 v1.0.2](./lessons/LAL-20261023-007-ROLLBACK-AS-NEW-LINEAGE-EVENT.md) now references the test. Do not generalize this result to runtime/global recovery.


## Universal component governance lesson — LAL-20261023-008
- [LAL-20261023-008](./lessons/LAL-20261023-008-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE.md) — each law/lesson/component has independent source/version/evidence and remains linked to the shared graph.
- Governing master: [ULCG](../../reference/REFERENCE-DOCUMENTS/UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-MASTER-REFERENCE-2026-10-23-001.md).
- Event and anchors: [EVT-0110](../BEHAVIOR-TRACE/EVT-0110-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE-2026-10-23.md), [IN-021](../../0.0/anchors/PALANG-0.0-IN-20261023-021-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE.md), [OUT-021](../../0.0/anchors/PALANG-0.0-OUT-20261023-021-UNIVERSAL-LIVING-COMPONENT-GOVERNANCE.md).


## Source-to-rule-component-test graph
- [SRCMAP-2026-10-23-001](./SOURCE-RULE-COMPONENT-TEST-MAP-2026-10-23-001.md) maps the first verified source batch to operational rules, components, test evidence and gaps.
- It is a partial source graph, not a claim of complete lesson census.


## Current point 0 lesson — LAL-20261023-010
- [LAL-20261023-010](./lessons/LAL-20261023-010-CURRENT-POINT-AND-NEXT-CHECKPOINT.md) — the current interaction becomes a recoverable point 0; NEXT-024 is the next 0.0; previous checkpoints and open work remain linked and open.
- Event: [EVT-0112](../BEHAVIOR-TRACE/EVT-0112-CURRENT-POINT-0-AND-NEXT-0.0-2026-10-23.md); anchors: [IN-023](../../0.0/anchors/PALANG-0.0-IN-20261023-023-REGISTER-CURRENT-POINT-0.md) / [OUT-023](../../0.0/anchors/PALANG-0.0-OUT-20261023-023-REGISTER-CURRENT-POINT-0.md).


## LAL-20261023-011 — visible continuation
- [LAL-20261023-011](./lessons/LAL-20261023-011-VISIBLE-CONTINUATION-AND-RESUMABLE-WORK.md) — visible milestones, resume from the queue, and do not imply silent background execution.
- Event: [EVT-0113](../BEHAVIOR-TRACE/EVT-0113-VISIBLE-CONTINUATION-AND-SOURCE-CLAUSE-EXCAVATION-2026-10-23.md); anchors IN-024 / OUT-024; next point [NEXT-025](../../0.0/anchors/PALANG-0.0-NEXT-20261023-025-SOURCE-RULE-TEST-CROSSWALK-AND-COLD-START.md).


## LAL-20261023-012 — visible status and resumable execution
- [LAL-20261023-012](./lessons/LAL-20261023-012-STATUS-TRANSPARENCY-AND-RESUMABLE-EXECUTION.md) / [EVT-0114](../BEHAVIOR-TRACE/EVT-0114-STATUS-TRANSPARENCY-AND-RESUMABLE-EXECUTION-2026-10-23.md); anchors IN-025 / OUT-025.
- NEXT-025 remains the next checkpoint. Work must report visible milestones and must not imply silent background execution.


## LAL-20261024-013 — current point 0 and living registration
- [Lesson](./lessons/LAL-20261024-013-CURRENT-POINT-ZERO-AND-LIVING-REGISTRATION.md) / [EVT-0134](../BEHAVIOR-TRACE/EVT-0134-CURRENT-POINT-ZERO-AND-LIVING-REGISTRATION-2026-10-24.md).
- Current point / next 0.0: [CURRENT-036](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-036-USER-REQUEST-AND-LIVING-REGISTRATION.md) / [NEXT-036](../../0.0/anchors/PALANG-0.0-NEXT-20261024-036-HISTORIC-SOURCE-CENSUS-AND-COLD-START.md).
- Rule: append-only point 0; separately anchored successor 0.0; prior work preserved; status claims require evidence.


## SCRTC-B3-2026-10-24-001 — source-clause crosswalk batch 3
- [Crosswalk batch 3](./SOURCE-CLAUSE-CROSSWALK-BATCH-3-2026-10-24-001.md): five full-source fetches and rule-family mapping for excavation gate, registration orchestrator, three-level command, every-input/output anchors, and every-interaction anchors.
- Connected master version: ULCG v1.2.5; current point CURRENT-036; next checkpoint NEXT-036.
- Status: provisional source-backed mapping; full census and runtime tests remain open.
