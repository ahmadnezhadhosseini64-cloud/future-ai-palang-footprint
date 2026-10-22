# سند مرجع مادر — ادامه از مدل اولیه، نه شاخهٔ Dropbox

- Stable ID: PALANG-CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-2026-10-22-001
- Production ID: CMIND-HAIF-2026-10-22-001
- Version: 1.0.0
- Project: Future AI / Palang Footprint / HAIF
- Owner: احمد پلنگ
- Status: ACTIVE / LIVING / OPEN / EVOLVABLE
- Governing event: EVT-0091
- Interaction pair: INT-20261022-005
- Input anchor: IN-20261022-005
- Output anchor: OUT-20261022-005
- Parent architecture: LBAF / AOGM / FIOBAM / ELVR
- Next execution issue: [Issue #20](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20)

## 1. Purpose / هدف
این سند نقطهٔ بازیابی مستقل برای ادامهٔ مسیر معماری «مدل اولیه» است. هدف، ادامهٔ ساخت مدل HAIF و رفتارشناسی تعامل از آخرین نقطهٔ تأییدشده است؛ نه تغییر مسیر به Dropbox. شاخهٔ Dropbox مستقل و OPEN / WAITING باقی می‌ماند و در این کار دست‌کاری نمی‌شود.

## 2. Interaction evidence / شواهد تعامل
- ورودی جاری: «خوب ادامه شو انجام بده».
- زمان دقیق پیام کاربر: NOT EXPOSED / NOT CAPTURED؛ از زمان commit نتیجه‌گیری نمی‌شود.
- خروجی دستیار: ادامه از وضعیت واقعی مخزن، بررسی مسیر مدل اولیه و اجرای گام بعدی بدون ادعای اثبات‌نشده.
- این ثبت، خلاصهٔ عملیاتی و ارجاع‌محور است؛ متن کامل گفتگو در این مخزن به‌صورت خودکار capture نشده است.

## 3. Confirmed repository state / وضعیت تأییدشدهٔ مخزن
- Repository: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`.
- HAIF v0 prototype exists at `prototype/haif-v0/`; its README explicitly scopes persistence to local SQLite and says automatic capture of all ChatGPT conversations is not implemented.
- Prototype has API patterns for anchors, events, documents, hash-based write/read-back, repository document ingestion, and restart tests.
- Interaction ledger schema and fixture CI passed in run `39750440075`; that proves schema/fixture checks only, not live host capture.
- Issue #20 remains OPEN and tracks the production collector, durable ledger, ID reverse lookup, privacy boundaries, and cold-start recovery.
- Current next 0.0 pointer: `docs/0.0/anchors/PALANG-0.0-RUNTIME-COLLECTOR-PRODUCTION-RECOVERY-2026-10-22-001.md`.

## 4. Model return path / مسیر بازگشت به مدل اولیه
`CAPTURE → CONTEXT-RECALL → PATTERN-EXTRACT → FUTURE-SCENARIOS → PRIORITIZE → BUILD → TEST → READ-BACK → RECONCILE → PROMOTE`

Execution resumes at **BUILD / TEST of the authorized runtime collector and persistent interaction-pair ledger**, after confirming current prototype code and tests. Historical semantic graph reconciliation continues as a parallel backlog unless a specific issue blocks this implementation.

## 5. Error and lesson recorded / خطا و درس ثبت‌شده
- Failure mode: assistant may drift toward an old, still-open Dropbox branch because it appears in the 0.0 graph.
- Correct interpretation: an open branch is not automatically the active continuation target. The latest user-directed 0.0 and explicit continuation path govern.
- Required guard: before acting, read the current anchor, master reference, integration queue and linked issue; classify each branch as ACTIVE TARGET, PARALLEL BACKLOG, or INDEPENDENT WAITING BRANCH.
- This record does not close the Dropbox gap or claim the previous drift was automatically prevented.

## 6. Time governance / حاکمیت زمان
- Canonical repository time: actual last-change Git commit timestamp in UTC.
- Tehran equivalent: derive from that exact UTC instant (UTC+03:30 for 2026-10-22).
- User-message timestamp: NOT EXPOSED / NOT CAPTURED.
- Commit/write, read-back, test and operation timestamps remain separate evidence fields. Do not invent seconds or use commit time as message time.

## 7. Current execution boundary / مرز اجرا
- Repository read-back of the source prototype and current governing documents was performed before this registration.
- No code change to the runtime collector has yet been made by this registration.
- No production runtime capture, ChatGPT-host connection, Buffer, Persistent Memory, external Library, Gmail or Dropbox write is claimed.
- Repository write status becomes VERIFIED only after fetching these exact files back and matching expected IDs/content.

## 8. Required next actions / اقدام‌های بعدی
1. Read back the new event, IN/OUT anchors, this reference, and every index/queue update.
2. Inspect and extend `prototype/haif-v0/app.py` and tests to persist interaction pairs with stable INT/IN/OUT identifiers, source provenance, idempotent append behavior, hash-verified read-back and lookup by any member ID.
3. Add tests for duplicate retry, conflicting ID reuse, unknown lookup, and restart recovery from IN and OUT in a fresh app instance sharing the same durable SQLite file.
4. Run the repository workflow and record the actual run/job evidence.
5. Keep production host capture and all external destinations OPEN until independently connected and tested.
6. Reconcile this event with the model-initial folder, LBAF master reference, behavior trace, 0.0 registry, reference index, and integration queue.

## 9. Recovery pointer / نقطهٔ بازیابی
Start from this document, then follow:
- [EVT-0091](../../architecture/BEHAVIOR-TRACE/EVT-0091-CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-2026-10-22.md)
- [IN-20261022-005](../../0.0/anchors/PALANG-0.0-IN-20261022-005-CONTINUE-MODEL-INITIAL.md)
- [OUT-20261022-005](../../0.0/anchors/PALANG-0.0-OUT-20261022-005-CONTINUE-MODEL-INITIAL.md)
- [LBAF master](./LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-MASTER-REFERENCE-2026-10-22-001.md)
- [Runtime collector 0.0](../../0.0/anchors/PALANG-0.0-RUNTIME-COLLECTOR-PRODUCTION-RECOVERY-2026-10-22-001.md)
- [Issue #20](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20)

---
Append-only rule: do not overwrite earlier 0.0 anchors or initial architecture. Add versioned evidence and reconcile links.


## Addendum v1.0.1 — executable pair-ledger increment and test correction
- Time binding: [TIME-BINDING-CMIND](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-CMIND-2026-10-22-001.md).
- Runtime increment: `prototype/haif-v0/app.py` now exposes `POST /api/v1/interactions` and `GET /api/v1/interactions/{INT|IN|OUT}`; validates against the repository Draft 2020-12 schema; stores canonical JSON in local SQLite; hashes and verifies read-back; supports idempotent identical retry; rejects conflicting ID reuse; and resolves all three paired IDs.
- Dependency: `jsonschema>=4.22,<5`.
- Tests added: schema-backed write/read-back, reverse lookup, idempotency, conflicting reuse, ID mismatch, and restart recovery.
- First real CI run `39823733279`: 15 passed, 1 failed. Failure was an existing ingestion-search test assuming exactly one global result after the new reference introduced another valid match.
- Follow-up run `39823898278`: same test assumption still failed after an insufficiently narrow query change. Both failures are preserved as evidence, not erased.
- Corrective test change: commit `5bae4d711ba2c2cb50f440b6c23af8b65e73fbcf` changes the assertion to select the expected source path. Fresh HAIF Prototype Tests run `39824020260` was last observed QUEUED; result remains PENDING / NOT VERIFIED until completion is fetched.
- Current status: code increment REGISTERED / READ-BACK VERIFIED; feature-specific tests passed in the two runs' 15 passing tests, but the suite as a whole is not PASS because each run had one failure. Fresh corrected run pending.
- Scope boundary: local prototype only. No production ChatGPT-host capture, authentication/deployment hardening, or external destination persistence is claimed.
