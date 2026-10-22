# رصدخانهٔ مستقل رفتار تعامل انسان و AI — مرجع زنده

- Stable ID: HUMAN-AI-INTERACTION-BEHAVIOR-OBSERVATORY-2026-10-22-001
- Production ID: HAIBO-HAIF-2026-10-22-001
- Version: 1.0.0
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Project: Future AI / Palang Footprint / HAIF
- Canonical path: `docs/architecture/BEHAVIOR-OBSERVATORY/README.md`
- Status: ACTIVE / LIVING in repository; full architecture-wide integration remains OPEN until linked indexes are updated and read back.
- Time rule: UTC is canonical; Asia/Tehran time is derived from the same UTC instant (+03:30 for this date). Unknown timestamps remain UNKNOWN, never guessed.
- Independent anchor: `PALANG-BEHAVIOR-OBSERVATION-AND-RECOVERY-TEST-2026-10-22-001`
- Related event: `EVT-0034`
- Parent rule: `HUMAN-AI-BEHAVIOR-RECOGNITION-RULE-2026-10-19-001`
- Related trace: `INTERACTION-BEHAVIOR-TRACE-2026-10-19-001`
- Related registration contract: `UNIFIED-OUTPUT-ANCHOR-REGISTRATION-LIVING-REFERENCE-2026-10-19-001`
- Previous anchor preserved: `PALANG-START-COMPLETE-REGISTRATION-UTC-ANCHOR-2026-10-22-001`

## 1. Purpose and architectural placement

This is a dedicated, independently retrievable folder for observing and improving human–AI interaction behavior over time. It does not replace the existing behavior rule or interaction trace; it gives them a dedicated observation workspace, evidence ledger, tests, and integration queue.

Placement: HAIF → Governance & Interaction → Behavior Observation → Evidence/Patterns → Controlled Proposal → Validation/Hammer → Owner Approval → Master integration (only after approval).

## 2. Observation scope

Capture observable interaction data: explicit user requests and constraints; assistant commitments and claims; tool actions actually attempted; results; read-back and verification; corrections, failures, recovery outcomes; repeated gaps; next action. Keep user-originated statements and AI-originated actions separate but linked by event IDs.

Do not claim hidden motives, personality diagnoses, or certainty about mental states. Record only observable behavior and clearly labeled interpretations. Do not store private chain-of-thought. Instead preserve a concise decision record: operational objective, evidence consulted, options considered at a high level, rule applied, action taken, result, limitation, and why the result passed or failed.

## 3. Per-interaction record schema

- Event ID, Stable ID, Production ID, Version
- independent anchor and parent/child links
- user input and assistant output (distinct fields)
- UTC event time and derived Tehran equivalent, with source and precision
- action/commit/read-back/verification timestamps as separate fields
- evidence refs, file paths, commit SHA/blob SHA when available
- observable user behavior, observable AI behavior, corrections and claims
- expected outcome, actual outcome, pass/fail/blocked/unknown
- destination-by-destination status (Repository, Buffer, Library, Persistent Memory, Dropbox)
- gap, risk, limitations, next action and recovery instructions
- retention/minimization note; avoid irrelevant sensitive personal inference

## 4. Observation loop

CAPTURE → ANCHOR → SEPARATE HUMAN/AI ACTIONS → CLASSIFY → LINK → TEST WHEN POSSIBLE → PRESERVE EVIDENCE → WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → QUEUE → REPORT → RESUME.

Meaning: capture → assign an anchor → separate human/AI actions → classify → link → test where possible → preserve evidence → write → read back → compare → verify → reconcile → queue → report → resume.

## 5. Pattern lifecycle and safeguards

1. Observation is not a validated pattern.
2. A repeated pattern is a hypothesis until evidence and counterexamples are reviewed.
3. A tested pattern becomes a candidate only when the test method, scope, outcome and limitations are documented.
4. Architectural promotion requires explicit owner approval; no automatic Child-to-Master promotion.
5. Keep failed and inconclusive tests. Do not rewrite a failure as success.
6. Use minimum necessary data. Avoid collecting unrelated sensitive personal details; do not infer psychological or medical traits.
7. Maintain versioned, append-only event records; corrections link to earlier versions.

## 6. Verification and recovery test gate

A standalone recovery test must retrieve only the independent reference document and determine whether a new session/operator can reconstruct: goal, governing rules, architecture placement, identifiers, evidence state, unresolved gaps, next actions, and destination limitations. The test result must be recorded separately from the reference being tested. Passing a text checklist is not proof that every external destination is persisted.

## 7. Current known state

- Existing behavior rule and interaction trace were found and linked.
- The independent recovery test was run; final result PASS 10/10 criteria.
- The standalone reference was fetched again; read-back blob SHA `363dbc6ed14118c5ae7cc5b14903cb644edf37d3`, retrieved length 5,675 characters.
- EVT-0035 records the C4 false-negative evaluator behavior and correction; companion reference is in `docs/reference/REFERENCE-DOCUMENTS/`.
- Repository file existence and content read-back are verified for the recorded files. Exact tool read-back timestamps were not returned and remain UNKNOWN / UNVERIFIED.
- Buffer, external Library, Persistent Memory and Dropbox are not verified by repository operations.

## 8. Mandatory open follow-up work

1. **Architecture/master-reference audit:** finish link/ID/anchor reconciliation across master reference, behavior rule/trace, 0.0 and integration queue; read back and verify.
2. **Dropbox failover:** establish the connection, write a test reference, retrieve it from Dropbox and compare content; keep OPEN until both write and retrieval evidence exist.
3. **External end-to-end recovery:** prove a copy exists outside the repository, then reconstruct in a separate test environment. Do not delete the production repository; simulate repository loss and document each result.

Continue collecting observable interaction and evaluator behavior as evidence-backed events, distinguishing observed facts from interpretation. Do not claim unverified destination persistence.


## 9. Current 0.0 continuation anchor
- [EVT-0036](../BEHAVIOR-TRACE/EVT-0036-CURRENT-0.0-ANCHOR-AND-NEXT-ACTION-2026-10-22.md)
- [Independent 0.0 anchor](../../0.0/anchors/PALANG-0.0-CONTINUATION-BEHAVIOR-REGISTRATION-NEXT-AUDIT-2026-10-22-001.md)
- [Complete living reference](../../reference/REFERENCE-DOCUMENTS/PALANG-0.0-CONTINUATION-BEHAVIOR-REGISTRATION-NEXT-AUDIT-2026-10-22-001.md)
- Next mandatory action: architecture/master-reference audit (BOART-FOLLOWUP-01); Dropbox failover and external end-to-end recovery remain open.


## 10. آزمون زندهٔ پایداری مقصدها — EVT-0037
- [پروندهٔ آزمون مستقل زنده](./LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001.md) — `LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001`.
- [رویداد EVT-0037](../BEHAVIOR-TRACE/EVT-0037-LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22.md).
- نتیجه: همخوانی پیوندهای مخزن PASS با محدودیت؛ آزمون محتوایی قبلی همچنان PASS 10/10 و بی‌دلیل تکرار نشده.
- مقصدهای Buffer، Library بیرونی، Persistent Memory و Dropbox: NOT VERIFIED؛ بازیابی سرتاسری: NOT RUN.
- ادامه: `BOART-FOLLOWUP-01` → `BOART-FOLLOWUP-02` → `BOART-FOLLOWUP-03`.

## 11. تفکیک وضعیت Library پس از بازخوانی مستقل — EVT-0037
- یک فایل مشخص، یعنی `LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001.md`، در مسیر Library مرجع پروژه ثبت و بازخوانی شد.
- وضعیت همان artifact: `REGISTERED / READ-BACK VERIFIED`.
- این شاهد فقط همان فایل/نسخه را پوشش می‌دهد؛ کل کتابخانه یا سایر اسناد به‌صورت جمعی تأیید نشده‌اند. Buffer و Persistent Memory همچنان NOT VERIFIED و Dropbox OPEN / NOT VERIFIED است.

## 12. همگام‌سازی زندهٔ آینه — EVT-0037
- آینهٔ Library برای پروندهٔ `LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001.md` به‌روزرسانی و از مسیر مستقل بازخوانی شد.
- نتیجهٔ همان فایل: `WRITE=PASS / READ-BACK=PASS / MATCH=PASS`.
- فرادادهٔ آخرین تغییر Library: UTC `2026-10-22T05:50:28.914450Z` = تهران `2026-10-22 09:20:28.914450`.
- این وضعیت فقط همین آینه را تأیید می‌کند؛ Buffer و Persistent Memory تأییدنشده، Dropbox باز/تأییدنشده، بازیابی بیرونی اجرا‌نشده است. همگام‌سازی خودکار پس‌زمینه ادعا نمی‌شود.

## 13. کنترل‌گر همگام‌سازی زندهٔ آینه — EVT-0038
- [کنترل‌گر آینه](./PALANG-MIRROR-SYNC-CONTROLLER-2026-10-22-001.md) — `PALANG-MIRROR-SYNC-CONTROLLER-2026-10-22-001`.
- [رویداد فعال‌سازی و بازخوانی](../BEHAVIOR-TRACE/EVT-0038-PALANG-MIRROR-SYNC-ACTIVATION-2026-10-22.md).
- اتوماسیون روزانه `Palang Mirror Sync` فعال است؛ هر اجرای آینده باید مقایسه و بازخوانی مستقل را ثبت کند.
- Library برای فایل آزمون مشخص بازخوانی شده است؛ Buffer و Persistent Memory تأییدنشده‌اند؛ Dropbox باز/تأییدنشده است.

## 12. همگام‌سازی آینهٔ زنده — EVT-0038
- [سیاست حاکم همگام‌سازی آینه](./MIRROR-SYNC-GOVERNANCE-AND-LIVE-REGISTRATION-2026-10-22-001.md) — Stable ID: PALANG-MIRROR-SYNC-GOVERNANCE-2026-10-22-001.
- [رویداد فعال‌سازی EVT-0038](../BEHAVIOR-TRACE/EVT-0038-LIVE-MIRROR-SYNC-ACTIVATION-2026-10-22.md).
- نسخهٔ مشخص سیاست در مخزن ثبت و بازخوانی شد؛ آینهٔ Library نیز در مسیر مرجع ثبت و بازخوانی شد. متن تا پایان محتوا تطبیق دارد؛ بازخوانی Library پایان‌خط نهایی را حذف می‌کند.
- دامنهٔ تأیید فقط همین فایل/نسخه است؛ این فرایند در حال حاضر دستی و مبتنی بر شواهد است، نه سرویس پس‌زمینهٔ خودکار.
- Buffer و Persistent Memory: NOT VERIFIED؛ Dropbox: OPEN / NOT VERIFIED؛ بازیابی سرتاسری: NOT RUN.

## 12. همگام‌سازی آینهٔ زنده — EVT-0038
- [سیاست حاکم همگام‌سازی آینه](./MIRROR-SYNC-GOVERNANCE-AND-LIVE-REGISTRATION-2026-10-22-001.md) — Stable ID: PALANG-MIRROR-SYNC-GOVERNANCE-2026-10-22-001.
- [رویداد فعال‌سازی EVT-0038](../BEHAVIOR-TRACE/EVT-0038-LIVE-MIRROR-SYNC-ACTIVATION-2026-10-22.md).
- نسخهٔ مشخص سیاست در مخزن ثبت و بازخوانی شد؛ آینهٔ Library نیز در مسیر مرجع ثبت و بازخوانی شد. متن تا پایان محتوا تطبیق دارد؛ بازخوانی Library پایان‌خط نهایی را حذف می‌کند.
- دامنهٔ تأیید فقط همین فایل/نسخه است؛ این فرایند در حال حاضر دستی و مبتنی بر شواهد است، نه سرویس پس‌زمینهٔ خودکار.
- Buffer و Persistent Memory: NOT VERIFIED؛ Dropbox: OPEN / NOT VERIFIED؛ بازیابی سرتاسری: NOT RUN.