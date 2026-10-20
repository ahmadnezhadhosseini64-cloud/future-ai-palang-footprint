# Reference Index

**Project:** Future AI / Palang Footprint  
**Reference Point:** 0.0  
**Status:** ACTIVE  
**Last Updated:** 2026-10-20 — LIARC-2026-10-20-001 and ABV-2026-10-20-001 linked; historical verification dates remain historical.

## Canonical References

| PGGR-2026-10-20-001 | `docs/reference/REFERENCE-DOCUMENTS/PROJECT-GOAL-AND-GAP-RECONCILIATION-2026-10-20-001.md` | سند هدف نهایی پروژه و تطبیق شکاف‌ها با وضعیت مبتنی بر شواهد | Repository write completed; independent read-back and architecture reconciliation pending |

| ID | Document | Role | Status |
|---|---|---|---|
| LIARC-2026-10-20-001 | `docs/reference/REFERENCE-DOCUMENTS/LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001.md` | قرارداد اجرای خودکار، لنگرگذاری، ممیزی معماری و تطبیق مقصدها | Repository structural audit EXECUTED / VERIFIED in run 39447083005; external integrations remain OPEN / NOT PROVEN |
| CEASR-2026-10-20-001 | `docs/reference/REFERENCE-DOCUMENTS/COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001.md` | سند مرجع خاک‌برداری جامع؛ لنگرها، معماری، شکاف‌های اتصال و مسیر بازیابی | Repository read-back verified; destination reconciliation and external layers remain open |
| EXCAVATION-ROUTINE-EXECUTION-CONTRACT-2026-10-20-001 | `docs/architecture/INTEGRATION-QUEUE/EXCAVATION-ROUTINE-EXECUTION-CONTRACT-2026-10-20-001.md` | قرارداد حاکم اجرای روتین خاک‌برداری؛ تکمیل کارهای باز و آزمون مقصدها | REPOSITORY WRITE + READ-BACK VERIFIED; external destinations and full routine execution remain unverified |
| EVT30-2026-10-20-001 | `docs/architecture/BEHAVIOR-TRACE/EVT-0030-CURRENT-0.0-AND-GAP-AUDIT-2026-10-20.md` | ممیزی نقطهٔ ۰.۰، نیاز به چهارتایی‌کردن، و شکاف‌های باز | Repository file read-back matched; cross-index reconciliation pending |
| F0CBG-2026-10-20-001 | `docs/reference/REFERENCE-DOCUMENTS/FOUR-LINKED-0.0-CHAIN-AND-BEHAVIORAL-DISCOVERY-GATE-2026-10-20-001.md` | زنجیرهٔ مرجع چهارتایی نقاط ۰.۰ و دروازهٔ کشف/اعتبارسنجی رفتاری پیش از ارتقای معماری | Repository write and read-back verified; 0.0 registry, behavior trace, and queue linked; full historical reconciliation pending |
| UIALAC-2026-10-20-001 | `docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-INTERACTION-ANCHOR-AND-LIVING-ARCHITECTURE-CONTRACT-2026-10-20-001.md` | قرارداد جامع لنگرگذاری، ثبت، مستندسازی، سه سطح ماندگاری و تداوم زنده | REPOSITORY WRITE + READ-BACK VERIFIED; architecture index linked; Buffer/Persistent Memory and automatic execution unverified |
| UIAWR-2026-10-20-001 | `docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-INTERACTION-ANCHOR-AND-WORKFLOW-RECOVERY-2026-10-20-001.md` | سند مرجع جامع لنگر تعامل، حاکمیت ثبت/زمان و مسیر واقعی بازیابی دو گردش کاری | ACTIVE / LIVING; workflow fixes committed; latest fresh runs 39454598933 and 39454598935 PASS / SUCCESS; artifacts and durable evidence read-back verified |
| SRC-2026-08-29-001 | `docs/STABLE_RETRIEVAL_CORE.md` | Stable external retrieval contract | VERIFIED / ACTIVE |
| RRT-2026-08-29-001 | `docs/RETRIEVAL_RUNTIME.md` | Operational retrieval sequence | VERIFIED / ACTIVE |
| EGE-2026-08-29-001 | `docs/EVIDENCE_GATE.md` | Independent execution evidence contract | PROVEN / ACTIVE / CLOSED / PASS |
| CHK-2026-08-29-001 | `docs/CHECKPOINT.md` | Current verified checkpoint | VERIFIED / ACTIVE |
| REF-GITHUB-2026-08-29-001 | Repository access reference | GitHub connection and repository access | VERIFIED / ACTIVE |
| URIG-2026-08-31-001 | `docs/protocols/RULE-INHERITANCE-AND-INVOCATION-GATE.md` | Universal rule inheritance and real-invocation verification | ACTIVE / LIVING / PERMANENT |
| TEST-0.0-TIMESTAMP-2026-08-31-001 | `evidence/tests/0.0-TIMESTAMP-INVOCATION-TEST-2026-08-31-001.md` | Real 0.0 timestamp inheritance invocation evidence | PASS / VERIFIED |

## Evidence Gate Proof

The Evidence Gate requirement E2 + E3 + E4 is verified by successful `Evidence Gate - Independent Execution Test` workflow execution. The latest verified run is **Run #7**, triggered by push to `main` at commit `c557be1cbfb518eb7066d0b15b4bf52fed2de5e9`. The run completed with `success` and produced an inspectable GitHub Actions trace.

## Consistency State

The canonical recovery documents are synchronized to the current verified state:

- Stable Retrieval Core = **VERIFIED / ACTIVE**.
- Retrieval Runtime = **VERIFIED / ACTIVE**.
- Evidence Gate = **PROVEN / ACTIVE / CLOSED / PASS**.
- Checkpoint = **VERIFIED / ACTIVE**.
- Universal Rule Inheritance & Invocation Gate = **ACTIVE / LIVING / PERMANENT**.
- 0.0 timestamp inheritance invocation test = **PASS / VERIFIED**.
- The obsolete `NOT YET PROVEN` Evidence Gate state is no longer canonical.
- The obsolete `actions/checkout@v4` warning is historical evidence only; the active workflow uses `actions/checkout@v5`.

## Rule

This index is a navigation layer, not a substitute for the referenced evidence. Each status must be supported by the underlying repository artifact or an explicit verification result.

## 0.0

At `0.0`, retrieval precedes response: retrieve the canonical source, verify its state, reconcile contradictions, resolve inherited rules, create the required timestamped connection/checkpoint record, verify the required fields by read-back, report evidence boundaries, then continue.


## Architecture verification record — 2026-10-20

- `ARCHITECTURE-BUILD-VERIFICATION-2026-10-20-001` / `ABV-2026-10-20-001`: [EVT-0024 — بازبینی ورود قرارداد به ساختمان پروژه](architecture/BEHAVIOR-TRACE/EVT-0024-ARCHITECTURE-BUILD-VERIFICATION-2026-10-20.md).
- نتیجه: اجرای ممیزی ساختاری GitHub Actions با شناسه `39447416772` به `success` رسید. این نتیجه فقط ساختمان داخلی مخزن را پوشش می‌دهد؛ capture سراسری گفتگو و مقصدهای بیرونی باز/اثبات‌نشده‌اند.
- زمان دقیق پیام کاربر: UNKNOWN / UNVERIFIED؛ زمان اجرای workflow جایگزین آن نیست.


## Interaction anchor and audit-resolution lineage — 2026-10-20
- `INTERACTION-ANCHOR-AND-AUDIT-REASONING-2026-10-20-001` / `IAAR-2026-10-20-001`: [سند مرجع زندهٔ لنگر تعامل و مسیر رفع نقص‌های ممیزی](reference/REFERENCE-DOCUMENTS/INTERACTION-ANCHOR-AND-AUDIT-REASONING-2026-10-20-001.md).
- ممیزی ساختاری `39449959962` و دروازهٔ بین‌لایه‌ای `39449959904` روی commit `ebadb73f6f107555b5054714aefab175d2a519bd` هر دو PASS گزارش شدند.
- `main.yml` run `39449957651` و `automatic-final-registration-proof.yml` run `39449956059` همچنان failure گزارش می‌شوند؛ علت در شواهد فعلاً در دسترس تعیین نشده و پیگیری باز است.
- زمان دقیق پیام کاربر `UNKNOWN / UNVERIFIED`؛ زمان workflowها UTC و جداگانه ثبت شده‌اند. Library/Buffer/Persistent Memory و capture سراسری گفتگو اثبات‌نشده‌اند. Dropbox `OPEN / WAITING`.


## Behavior trace event — IAAR-2026-10-20-001
- Event: [EVT-0025 — لنگر تعامل و مسیر رفع نقص‌های ممیزی](architecture/BEHAVIOR-TRACE/EVT-0025-INTERACTION-ANCHOR-AND-AUDIT-REASONING-2026-10-20.md).
- سند مرجع کامل: [INTERACTION-ANCHOR-AND-AUDIT-REASONING-2026-10-20-001](reference/REFERENCE-DOCUMENTS/INTERACTION-ANCHOR-AND-AUDIT-REASONING-2026-10-20-001.md).
- صف زنده: [OPEN-GAPS-RECOVERY-REGISTER-2026-10-15-001](architecture/INTEGRATION-QUEUE/OPEN-GAPS-RECOVERY-REGISTER-2026-10-15-001.md).
- پیگیری باز GitHub: [Issue #18 — علت‌یابی دو workflow شکست‌خورده](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/18).

## Active governance rule — dual timestamps (2026-10-20)
- `DUAL-TIMESTAMP-AVAILABILITY-RULE-2026-10-20-001` / `DTAR-2026-10-20-001`: record assistant/system reference time (UTC, source-labelled) and Tehran local time (Asia/Tehran) together whenever both are available; if Tehran time is unavailable, mark it UNKNOWN / UNAVAILABLE and preserve the exact available system time. Never invent or backfill a missing user-message timestamp.
- Applied to anchor: [IAAR reference](reference/REFERENCE-DOCUMENTS/INTERACTION-ANCHOR-AND-AUDIT-REASONING-2026-10-20-001.md) and [EVT-0025](architecture/BEHAVIOR-TRACE/EVT-0025-INTERACTION-ANCHOR-AND-AUDIT-REASONING-2026-10-20.md).


## Architecture event — dual timestamp rule
- [EVT-0026 — تصویب و اتصال قاعدهٔ زمان‌گذاری دوگانه](architecture/BEHAVIOR-TRACE/EVT-0026-DUAL-TIMESTAMP-AVAILABILITY-RULE-2026-10-20.md).
- Rule: `DUAL-TIMESTAMP-AVAILABILITY-RULE-2026-10-20-001` / `DTAR-2026-10-20-001`; status ACTIVE / LIVING / GOVERNING.


## Interaction anchor and workflow recovery — EVT-0027
- `UNIVERSAL-INTERACTION-ANCHOR-AND-WORKFLOW-RECOVERY-2026-10-20-001` / `UIAWR-2026-10-20-001`: [سند مرجع جامع لنگر تعامل، حاکمیت ثبت و بازیابی دو گردش کاری](reference/REFERENCE-DOCUMENTS/UNIVERSAL-INTERACTION-ANCHOR-AND-WORKFLOW-RECOVERY-2026-10-20-001.md).
- Event: [EVT-0027 — لنگر جامع تعامل و بازیابی دو گردش کاری](architecture/BEHAVIOR-TRACE/EVT-0027-UNIVERSAL-INTERACTION-ANCHOR-AND-WORKFLOW-RECOVERY-2026-10-20.md).
- اصلاحات workflow روی مخزن ثبت شده‌اند: artifact paths برای ثبت نهایی اصلاح شد (commit `2a3398132ca8e196295d2d61bf7c96d12ce7d84c`) و فیلتر اجرای Evidence Gate گسترش یافت (commit `75f1fff4a42a6fc1465a2164a4d82db30934a95c`).
- اجرای تاریخی `39449957651` و `39449956059` شکست‌خورده باقی می‌مانند؛ endpointهای job خالی و retry با HTTP 403 رد شد. علت دقیق تاریخی `UNKNOWN / UNVERIFIED`.
- **Issue #18 CLOSED**؛ نتیجهٔ ثبت‌شده در issue و شواهد تازه روی commit `e794777002503dda66ebd9b8fa110f37ac1e973d` نشان می‌دهند jobهای Evidence/Final Registration موفق بوده‌اند. اجرای workflowهای جدید روی این commit نیز `39459069207`, `39459069274`, `39459069335`, `39459069289`, `39459069488` و `39459069432` با `success` پایان یافتند؛ این امر همچنان به معنی اثبات capture سراسری همه پیام‌های ChatGPT نیست.
- زمان دقیق پیام کاربر و زمان دقیق ثبت این رخداد در شواهد این نوشتن موجود نیست؛ حدس زده نمی‌شود.


## Behavior trace event — ICMCRR-HAIF-2026-10-20-001
- Event: [EVT-0026 — تداوم معماری Master–Child–Rahm](architecture/BEHAVIOR-TRACE/EVT-0026-INTERACTION-CONTINUITY-MASTER-CHILD-RAHM-2026-10-20.md).
- سند مرجع جامع: [INTERACTION-CONTINUITY-MASTER-CHILD-RAHM-REGISTRATION-2026-10-20-001](reference/REFERENCE-DOCUMENTS/INTERACTION-CONTINUITY-MASTER-CHILD-RAHM-REGISTRATION-2026-10-20-001.md).
- سند مادر MRV: [MRV Architecture and Living Reference Contract](reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md).
- صف زنده: [OPEN-GAPS-RECOVERY-REGISTER-2026-10-15-001](architecture/INTEGRATION-QUEUE/OPEN-GAPS-RECOVERY-REGISTER-2026-10-15-001.md).
- وضعیت: ثبت و پیوندهای مخزن پس از نوشتن، بازخوانی و تطبیق شدند؛ گیت‌های اجرای خودکار و مقصدهای بیرونی همچنان باز هستند.
- زمان دقیق پیام: UNKNOWN / UNVERIFIED؛ زمان commit جایگزین زمان پیام نیست.


## Project goal and gap reconciliation — PGGR-2026-10-20-001
- Canonical reference: [هدف نهایی پروژه و تطبیق شکاف‌ها](reference/REFERENCE-DOCUMENTS/PROJECT-GOAL-AND-GAP-RECONCILIATION-2026-10-20-001.md).
- Behavior event: [EVT-0028](architecture/BEHAVIOR-TRACE/EVT-0028-PROJECT-GOAL-GAP-RECONCILIATION-2026-10-20.md).
- MRV, architecture queue and open-gap register cross-linked; repository read-back/match verified for those five files. Library, Buffer, Persistent Memory, Dropbox and end-to-end automatic execution remain open/unverified.
- Exact user-message time: UNKNOWN / UNVERIFIED.


## Main 0.0 continuation lock — P0ML-2026-10-20-002
- Main checkpoint: [PALANG-0.0-MAIN-LOCK-2026-10-20-002](../checkpoints/PALANG-0.0-MAIN-LOCK-2026-10-20-002.md).
- Behavior event: [EVT-0029](architecture/BEHAVIOR-TRACE/EVT-0029-MAIN-0.0-LOCK-2026-10-20.md).
- Prior 0.0 anchors are preserved; Dropbox failover anchor remains separately OPEN / WAITING.
- Repository registration is separate from Library, Buffer, Persistent Memory and Dropbox; exact user-message time is UNKNOWN / UNVERIFIED.


## ثبت فرمان جاری — 2026-10-20
- Event: [EVT-0030](architecture/BEHAVIOR-TRACE/EVT-0030-REGISTER-COMMAND-ACKNOWLEDGEMENT-2026-10-20.md)
- Stable ID: `REGISTER-COMMAND-ACKNOWLEDGEMENT-2026-10-20-001`; Production ID: `RCA-2026-10-20-001`.
- مربوط به درخواست «ثبت کن» روی نقطهٔ ادامهٔ جاری؛ لنگر اصلی ۰.۰ جایگزین یا بسته نمی‌شود.
- مقصدهای Buffer، Persistent Memory، Library و Dropbox مستقل‌اند و در این ثبت اثبات نشده‌اند.


## 0.0 anchor-count and open-gap audit — 2026-10-20
- Stable ID: `PALANG-0.0-ANCHOR-COUNT-AND-GAP-AUDIT-2026-10-20-001`; Production ID: `P0ACGA-2026-10-20-001`; Version: 1.0.0.
- Canonical reference: [ممیزی تعداد نقاط ۰.۰، هدف پروژه و شکاف‌های باز](docs/reference/REFERENCE-DOCUMENTS/PALANG-0.0-ANCHOR-COUNT-AND-GAP-AUDIT-2026-10-20-001.md).
- Finding: no evidence-based reason to create a fourth 0.0 solely to reach a count; use the existing main lock as the governing resume entry, preserve the current anchor and independent Dropbox anchor, and do not claim a complete historical count.
- Open: G-AUTO-02/03/04/05/06/07/08; automatic all-interaction execution and end-to-end recovery remain unproven. Dropbox remains OPEN / WAITING.
- Repository write/read-back: MATCHED for the canonical audit file. This does not verify Library, Buffer, Persistent Memory, or Dropbox.
- Exact user-message timestamp: UNKNOWN / UNVERIFIED.


## ثبت تعامل جاری و ممیزی شکاف‌ها — 2026-10-20
- Stable ID: `INTERACTION-REGISTRATION-AND-GAP-CLOSURE-2026-10-20-001`; Production ID: `IRGC-2026-10-20-001`; Version: 1.0.0.
- سند مرجع: [ثبت تعامل جاری و ممیزی شکاف‌ها](reference/REFERENCE-DOCUMENTS/INTERACTION-REGISTRATION-AND-GAP-CLOSURE-2026-10-20-001.md).
- رویداد: [EVT-0032](architecture/BEHAVIOR-TRACE/EVT-0032-INTERACTION-REGISTRATION-AND-GAP-CLOSURE-2026-10-20.md).
- نتیجهٔ read-back: سند، رویداد و چهار نمایهٔ مرتبط بازخوانی شدند و شناسه/پیوند مورد انتظار تطبیق شد؛ شکاف محدود ثبت همین تعامل در مخزن CLOSED / VERIFIED است. اجرای خودکار سراسری، تطبیق کامل تاریخی ۰.۰، Dropbox، Buffer، Persistent Memory، Library و بازیابی سرتاسری همچنان OPEN / UNVERIFIED هستند.
- زمان دقیق پیام کاربر: UNKNOWN / UNVERIFIED؛ حدس زده نمی‌شود.


## سند مرجع معماری تداوم زنده و ثبت دوزمانه — 2026-10-20
- Stable ID: `TWO-TIME-ANCHORING-AND-LIVING-CONTINUITY-ARCHITECTURE-2026-10-20-001`; Production ID: `TTALCA-2026-10-20-001`; Version: 1.0.0.
- سند مرجع: [ثبت دوزمانه، لنگرگذاری و تداوم زنده](reference/REFERENCE-DOCUMENTS/TWO-TIME-ANCHORING-AND-LIVING-CONTINUITY-ARCHITECTURE-2026-10-20-001.md).
- رویداد: [EVT-0033](architecture/BEHAVIOR-TRACE/EVT-0033-TWO-TIME-ANCHORING-AND-LIVING-CONTINUITY-2026-10-20.md).
- قرارداد مادر اصلاح‌شده: [UIALAC-2026-10-20-001](reference/REFERENCE-DOCUMENTS/UNIVERSAL-INTERACTION-ANCHOR-AND-LIVING-ARCHITECTURE-CONTRACT-2026-10-20-001.md), amendment v1.1.0.
- زمان پیام کاربر: UNKNOWN / UNVERIFIED. زمان پردازش دستیار در سند ثبت شده: 2026-10-20T22:20:19+03:30 (Asia/Tehran); زمان commit/read-back فیلدهای جدا هستند.
- دامنهٔ ثبت مخزنی پس از read-back بسته می‌شود؛ لنگرگذاری خودکار سراسری، مقصدهای مستقل و گراف کامل تاریخی ۰.۰ همچنان OPEN / UNVERIFIED هستند.


## لنگر خروجی دستیار — EVT-0034
- [EVT-0034 — گزارش اجرای ثبت و راستی‌آزمایی](architecture/BEHAVIOR-TRACE/EVT-0034-ASSISTANT-EXECUTION-AND-VERIFICATION-REPORT-2026-10-20.md).
- خروجی مربوط به اجرای قاعدهٔ ثبت دوزمانه، اصلاح قرارداد مادر به نسخهٔ ۱.۱.۰ و ثبت سند تداوم زنده است.
- زمان پیام کاربر: UNKNOWN / UNVERIFIED؛ زمان پردازش دستیار برای این لنگر: 2026-10-20T22:23:18+03:30 (Asia/Tehran).


## قرارداد ثبت زنده، لنگرگذاری و آزمون — 2026-10-20
- Stable ID: `LIVING-ANCHORING-REGISTRATION-AND-TEST-GOVERNANCE-2026-10-20-001`; Production ID: `LARTG-2026-10-20-001`; Version: 1.0.0.
- سند مرجع: [LARTG](reference/REFERENCE-DOCUMENTS/LIVING-ANCHORING-REGISTRATION-AND-TEST-GOVERNANCE-2026-10-20-001.md).
- رویداد ورودی: [EVT-0035](architecture/BEHAVIOR-TRACE/EVT-0035-LIVING-ANCHORING-AND-TEST-GOVERNANCE-2026-10-20.md).
- زمان پیام کاربر: UNKNOWN / UNVERIFIED؛ زمان پردازش دستیار: 2026-10-20T22:31:33+03:30. آزمون پذیرش فعال اما نتیجهٔ کامل هنوز اثبات نشده است.

- لنگر خروجی دستیار و گزارش آزمون: [EVT-0036](architecture/BEHAVIOR-TRACE/EVT-0036-ASSISTANT-REGISTRATION-AND-TEST-RESULT-2026-10-20.md).


## سند مرجع مادر — فرمان ثبت کامل و معماری HAIF قابل‌انتقال
- Stable ID: `UNIVERSAL-REGISTER-AND-PORTABLE-HAIF-ARCHITECTURE-MASTER-REFERENCE-2026-10-20-001`; Production ID: `URPHA-2026-10-20-001`; Version: 1.0.0.
- سند: [URPHA](reference/REFERENCE-DOCUMENTS/UNIVERSAL-REGISTER-AND-PORTABLE-HAIF-ARCHITECTURE-MASTER-REFERENCE-2026-10-20-001.md).
- ورودی: [EVT-0037](architecture/BEHAVIOR-TRACE/EVT-0037-UNIVERSAL-REGISTER-AND-PORTABLE-HAIF-REQUEST-2026-10-20.md).
- قرارداد مادر به اصلاحیهٔ v1.2.0 ارتقا می‌یابد تا فرمان «ثبت کن» چرخهٔ کامل را الزام کند.
- زمان پیام کاربر: UNKNOWN / UNVERIFIED؛ زمان پردازش تدوین سند مرجع: 2026-10-20T22:58:42+03:30.
