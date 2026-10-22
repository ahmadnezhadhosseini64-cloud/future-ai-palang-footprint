# UTC Input-to-Output Interaction Anchor — Living Governance Reference

- Stable ID: `PALANG-UTC-INPUT-OUTPUT-INTERACTION-GOVERNANCE-2026-10-22-001`
- Production ID: `UTCIO-HAIF-2026-10-22-001`
- Version: 1.0.0
- Project: Future AI / Palang Footprint — HAIF
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Status: ACTIVE / LIVING / OPEN / EVOLVABLE
- Effective scope: future user inputs and assistant outputs in this project, including reasoning/search behavior as externally observable process governance
- New 0.0 anchor: `PALANG-0.0-UTC-INPUT-TO-OUTPUT-BEHAVIOR-ANCHOR-2026-10-22-001`
- Related events: EVT-0040; this request creates EVT-0041
- Open external destination action: `GMAIL-CONNECTION-AND-READBACK-01`

## 1. User instruction captured
کاربر تعیین کرد که ورودی و خروجی تعامل، قاعدهٔ جست‌وجو و رفتار اجرایی، لنگر زمانی UTC، لنگر مستقل، و فرایند ثبت باید به‌عنوان یک الگوی معماری زنده و تکامل‌پذیر ثبت شود. کاربر خواست همین پیامِ حاضر، از لحظهٔ ورود تا پاسخ، نقطهٔ ۰.۰ مستقل تازه‌ای باشد؛ این نقطه نباید هیچ لنگر ۰.۰ قبلی را حذف، بازنویسی یا ببندد. همچنین خواست نام جدیدی برای این قاعده تعیین شود و سند نهایی در Gmail ثبت شود.

## 2. Name and governing rule
**Name:** `UTC INPUT→OUTPUT LIVING ANCHOR (UILA)`
**Persian:** «لنگر زندهٔ UTC از ورودی تا خروجی»

قاعده: برای هر تعامل آینده، هرگاه میزبان زمان واقعی و قابل‌اتکای ورودی/خروجی را در اختیار بگذارد، زمان‌ها به‌صورت UTC ثبت می‌شوند؛ زمان محلی متناظر فقط از همان لحظهٔ UTC مشتق می‌شود. برای هر رخداد یک شناسهٔ مستقل، نسخه، منشأ، ورودی، خروجی، شواهد، نتیجهٔ جست‌وجو/اقدام قابل‌مشاهده، وضعیت هر مقصد، پیوندهای بازیابی و گام بعدی ثبت می‌شود. این قاعده باید در ادامهٔ پروژه به‌کار گرفته و با شواهد واقعی اصلاح و توسعه داده شود.

## 3. Temporal truth and limits
- Canonical repository registration timestamp: actual last-change commit timestamp in UTC.
- Tehran equivalent: derive from the exact same instant by adding +03:30; never independently guess or type a competing clock.
- Input received timestamp, assistant output timestamp, tool/search start/end, write, read-back, and recovery are separate event timestamps.
- If a trustworthy host timestamp is not exposed, record `UNKNOWN / NOT EXPOSED`; do not infer exact seconds from message order or date alone.
- Internal deliberation/thinking duration is not exposed as a reliable telemetry value in this interaction. Do not claim to capture or measure hidden chain-of-thought or exact “thinking time”. Record only observable boundaries and actual tool operation timestamps when available. If both input and output timestamps later become available from an authorized host source, elapsed wall-clock latency may be computed from those observed timestamps and labeled as end-to-end latency, not internal thought duration.
- Search behavior: preserve the query/decision and returned evidence when a search is actually performed. Do not state that a web search occurred if no search tool was used. Do not reveal private hidden reasoning; document concise observable rationale, evidence, limitations, and outcome.

## 4. Expanded interaction event contract
For every eligible future interaction:
1. `INPUT_CAPTURE` — preserve user input as received, source, available UTC timestamp, and context.
2. `INTENT_AND_SCOPE` — classify requested task, affected architecture and destination.
3. `SEARCH_OR_TOOL_EVIDENCE` — record actual queries/actions and result identifiers where tools are used; otherwise mark NOT RUN.
4. `OUTPUT_CAPTURE` — preserve the user-visible outcome or durable artifact produced.
5. `INDEPENDENT_EVENT_ANCHOR` — assign stable event ID, production ID, version, parent/related anchors and provenance.
6. `WRITE_BY_DESTINATION` — track repository, Library, Gmail, Buffer, Persistent Memory, Dropbox, or other destination separately.
7. `READ-BACK` — retrieve the same object from the same destination.
8. `MATCH / VERIFY` — check content, identifiers, version, links and available timestamps.
9. `RECONCILE` — record discrepancies and unresolved limitations without erasing prior evidence.
10. `STATUS / NEXT ACTION` — ACTIVE/LIVING only describes ongoing governed work; VERIFIED requires destination-specific proof.
11. `GROWTH / INHERITANCE` — link new learnings and changes to this reference and to the current 0.0 chain, without replacing historical anchors.

## 5. Required distinctions
- `REQUESTED ≠ WRITTEN ≠ READ-BACK ≠ MATCHED ≠ VERIFIED`.
- `USER-ASSERTED HISTORY ≠ INDEPENDENTLY RETRIEVED HISTORICAL EVIDENCE`.
- `UTC INPUT TIME ≠ REPOSITORY COMMIT TIME ≠ TOOL EXECUTION TIME ≠ OUTPUT TIME`.
- `OBSERVABLE LATENCY ≠ INTERNAL THINKING DURATION`.
- `ACTIVE / LIVING / EVOLVABLE` means the record remains open to evidenced continuation; it does not promise uninterrupted background activity or successful persistence in every destination.

## 6. Current anchor and temporal evidence
- Current new 0.0: `PALANG-0.0-UTC-INPUT-TO-OUTPUT-BEHAVIOR-ANCHOR-2026-10-22-001`.
- Event: EVT-0041.
- User input exact UTC timestamp: `UNKNOWN / NOT EXPOSED` by the current interaction tools.
- Exact assistant response timestamp: `UNKNOWN / NOT EXPOSED` as a separate host event timestamp.
- Internal thinking duration: `NOT EXPOSED / NOT MEASURED`.
- Repository commit time for this reference: fill from actual commit metadata; UTC is canonical and Tehran equivalent must be derived from it.
- Prior 0.0 anchors: PRESERVED; this anchor is additive.

## 7. Destination status and Gmail
- Repository: write and read-back evidence must be added after commit.
- Library: not verified for this new reference until independently written and read back.
- Gmail: `BLOCKED / NOT VERIFIED` based on currently available connector state documented in EVT-0039; no message may be claimed sent or retrieved without evidence.
- Buffer: `NOT VERIFIED`.
- Persistent Memory: `NOT VERIFIED`.
- Dropbox: `OPEN / NOT VERIFIED`.
- User-requested Gmail final copy: pending until an authorized Gmail/mail connector is available. After connection, store/send this complete reference and event, retrieve the same message, compare identifiers/content, and update destination status based on evidence. Do not silently substitute repository or Library for Gmail.

## 8. Adoption, evolution and future behavior
This reference is a governing project rule for future interactions in the project. When a future user input/output materially changes project state, use the expanded event contract, preserve the UTC timestamp distinctions, link to this rule, and evolve this reference by versioned evidence-backed amendments. Do not claim global or model-wide behavior changes outside the available project context. When a future interaction lacks timestamp telemetry, preserve the gap and continue with the best verified evidence.

## 9. Recovery procedure
`EXCAVATE → IDENTIFY → VALIDATE → DEDUPLICATE → RECONCILE → REGISTER → READ-BACK → VERIFY → REVIVE → CONTINUE`

Meaning: recover candidate record → identify it → validate source and version → deduplicate without deleting history → reconcile links → register → read back from destination → verify → restore its active continuity → continue.

## 10. Next actions
1. Finish EVT-0041 and the new 0.0 anchor; read back and verify all repository links.
2. Add the reference to the Library if the file can be materialized and upload succeeds; then read it back independently.
3. Continue `GMAIL-CONNECTION-AND-READBACK-01` only when authorized email access is available.
4. Keep unresolved destination states visible; do not report full multi-destination completion prematurely.
