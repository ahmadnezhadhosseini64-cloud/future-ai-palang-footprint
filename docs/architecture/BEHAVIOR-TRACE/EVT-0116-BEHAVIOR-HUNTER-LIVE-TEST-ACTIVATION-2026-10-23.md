# EVT-0116 — فعال‌سازی آزمون‌های چشم پلنگ شکارچی و تطبیق زندهٔ آینه

## شناسنامه
- Event ID: EVT-0116
- Stable ID: PALANG-BEHAVIOR-HUNTER-LIVE-TEST-ACTIVATION-2026-10-23-001
- Production ID: BHLA-HAIF-2026-10-23-001
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN — مولد آزمون و گردش‌کار CI ثبت شده‌اند؛ اجرای واقعی workflow و capture سراسری میزبان هنوز باید با شواهد مستقل تأیید شود.
- Project: Future AI / Palang Footprint / HAIF
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Canonical repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Behavior Hunter architecture: [PALANG-BEHAVIOR-HUNTER-TEST-GENERATION-AND-GROWTH-GATE-2026-10-23-001](../BEHAVIOR-OBSERVATORY/PALANG-BEHAVIOR-HUNTER-TEST-GENERATION-AND-GROWTH-GATE-2026-10-23-001.md)
- Test plan: [VERIFIABLE-TEST-PLAN-FROM-EVT-0115-2026-10-23](../BEHAVIOR-OBSERVATORY/VERIFIABLE-TEST-PLAN-FROM-EVT-0115-2026-10-23.md)
- Source mirror audit: [LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001](../BEHAVIOR-OBSERVATORY/LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001.md)
- Previous event: EVT-0115
- Time governance: actual repository commit UTC is canonical; Tehran equivalent is derived from that exact UTC instant. Do not substitute commit time for message or execution time.

## 1. User request and architectural decision
The user directed that the test system be made living and linked to Behavior Hunter / چشم پلنگ شکارچی. It should derive candidate tests from interaction IN/OUT, verify those tests, preserve failures and blockers, and let only evidence-backed passes inform architecture growth. Passing a test must not auto-promote a change into MASTER.

## 2. Repository implementation written
1. `docs/architecture/BEHAVIOR-OBSERVATORY/PALANG-BEHAVIOR-HUNTER-TEST-GENERATION-AND-GROWTH-GATE-2026-10-23-001.md` — architecture and acceptance gates.
2. `scripts/behavior-hunter/generate_candidate_tests.py` — deterministic candidate-test generator for structured JSONL interaction records.
3. `tests/behavior-hunter/test_generate_candidate_tests.py` — five unit tests for valid records, missing output, unsupported success claims, missing destination states, and candidate-vs-execution status.
4. `data/interaction-pairs/interaction-pairs.jsonl` — one structured EVT-0115 example pair, with evidence and per-destination states.
5. `.github/workflows/palang-behavior-hunter.yml` — CI workflow triggered by relevant pushes to main and manual dispatch; runs unit tests and emits a candidate-test JSON artifact.

These are actual repository writes. Their existence is not, by itself, proof that GitHub Actions has run successfully. Workflow run/artifact evidence remains required.

## 3. Live VTP-02 / VTP-03 comparison
- Canonical source prior blob SHA: `c0ad949c8fd53e2dec7eb1c291171a5486d27742`.
- Library mirror exact file ID: `file_00000000c98481f4bb07be3239e4deba`; stable Library file ID: `libfile_7ac3c9a6ec14819198eb2751e204aa48`.
- Source length: 8,915 characters. Library read-back length: 8,908 characters. Difference: 7 characters.
- Stable ID, Test ID, Version 1.0.0 and BOART-FOLLOWUP-01 → 02 → 03 next-action chain match.
- A contradictory stale status was found inside the canonical source: an earlier section called the Library mirror NOT VERIFIED while later addenda said that this exact mirror had been independently read back. The canonical source was corrected in commit `a2374d7da36a5af69b1bdf17f6dfd673bc03c97f`, blob `de1b75f07241c9b313e476af5f1417177ff78c10`.
- VTP-02: PARTIAL / FAIL-CLOSED until post-update source read-back and a fresh comparison to a refreshed Library mirror are complete.
- VTP-03: length delta criterion PASS (7 characters); semantic acceptance PENDING because the mirror has not been refreshed to the latest corrected source. No byte-for-byte identity claim.
- Library refresh/write is not available through the currently exposed Library tool surface in this execution. This is a bounded tool limitation, not proof that the destination is permanently unavailable.

## 4. Test generator rules
- Missing required IN/OUT/ID/version fields → candidate fail.
- Success wording without evidence → candidate fail.
- Destination states, resume pointer and expected invariants are checked when required.
- Generated records are marked CANDIDATE_READY or CANDIDATE_FAIL, and execution_status remains NOT_RUN until an actual run occurs.
- Passing tests create evidence for a Child/Rahm proposal; they do not auto-edit or promote MASTER.
- The workflow's artifact is the intended independently inspectable test manifest. Its first actual run status has not yet been independently retrieved in this record.

## 5. Remaining open gates
- Confirm post-update source read-back and the real Git commit UTC.
- Refresh the Library mirror from the corrected canonical source, independently read it back and compare Stable ID, Version, Next Action and Destination Statuses.
- Retrieve GitHub Actions run and artifact evidence; do not call the workflow PASS before that evidence is inspectable.
- Prove that the host adapter captures each permitted live IN/OUT pair; current implementation consumes structured records committed to the repository and does not automatically observe every live ChatGPT message.
- Run restart recovery from this event alone and preserve all historical 0.0 anchors.
- Buffer and Persistent Memory remain NOT VERIFIED; Dropbox remains OPEN / NOT VERIFIED; external end-to-end recovery remains NOT RUN.

## 6. Resume contract
Start from EVT-0116 and the test plan. First read back the corrected audit and current master/queue. Then close the semantic mirror mismatch, retrieve CI execution evidence, and only then promote any passing test pattern into a reviewed Child/Rahm proposal. Do not repeat already passing tests unless code, fixture, dependencies, deployment or evidence changed.
