# Reference Index

**Project:** Future AI / Palang Footprint  
**Reference Point:** 0.0  
**Status:** ACTIVE  
**Last Updated:** 2026-10-20 — LIARC-2026-10-20-001 and ABV-2026-10-20-001 linked; historical verification dates remain historical.

## Canonical References

| ID | Document | Role | Status |
|---|---|---|---|
| LIARC-2026-10-20-001 | `docs/reference/REFERENCE-DOCUMENTS/LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001.md` | قرارداد اجرای خودکار، لنگرگذاری، ممیزی معماری و تطبیق مقصدها | Repository structural audit EXECUTED / VERIFIED in run 39447083005; external integrations remain OPEN / NOT PROVEN |
| CEASR-2026-10-20-001 | `docs/reference/REFERENCE-DOCUMENTS/COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001.md` | سند مرجع خاک‌برداری جامع؛ لنگرها، معماری، شکاف‌های اتصال و مسیر بازیابی | Repository read-back verified; destination reconciliation and external layers remain open |
| EXCAVATION-ROUTINE-EXECUTION-CONTRACT-2026-10-20-001 | `docs/architecture/INTEGRATION-QUEUE/EXCAVATION-ROUTINE-EXECUTION-CONTRACT-2026-10-20-001.md` | قرارداد حاکم اجرای روتین خاک‌برداری؛ تکمیل کارهای باز و آزمون مقصدها | REPOSITORY WRITE + READ-BACK VERIFIED; external destinations and full routine execution remain unverified |
| UIALAC-2026-10-20-001 | `docs/reference/REFERENCE-DOCUMENTS/UNIVERSAL-INTERACTION-ANCHOR-AND-LIVING-ARCHITECTURE-CONTRACT-2026-10-20-001.md` | قرارداد جامع لنگرگذاری، ثبت، مستندسازی، سه سطح ماندگاری و تداوم زنده | REPOSITORY WRITE + READ-BACK VERIFIED; architecture index linked; Buffer/Persistent Memory and automatic execution unverified |
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
