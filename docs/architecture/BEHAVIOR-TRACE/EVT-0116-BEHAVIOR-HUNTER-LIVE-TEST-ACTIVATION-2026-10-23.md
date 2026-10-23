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


## Post-write read-back and continuation state
- Repository artifact read-back completed after the initial writes. Current observed blob SHAs: audit `de1b75f07241c9b313e476af5f1417177ff78c10`; test plan before this event update `fcd250a9ab16022bac5aa8c3bab7e59991ce8e67`; Behavior Hunter spec `93108610b3e30d454efde61d950eee3440b29ae7`; master reference before its latest status addendum `f228bac8684dee3f88662c568ee4dc4b24f78200`; queue before its latest status addendum `c84b3d0ab4294c2ccddc3d863663a8e3419fc724`; observatory index `fd6d94f3ed3bec1bb23603eeaedbefa0765a8efc`; generator `5bc67ec4128b6d85f55bff70c80a9beb40cdb191`; unit tests `f95e67cf030e27964b962e77c36c3f82df0ce30e`; fixture `7ba9204e732035cfc7e5c69ccb9b9b721f899774`; workflow `6ac98ae03adda11eb3a94038a1c7c859bb250a30`.
- Test-plan latest status commit `ae1943a91b5451cbc0afb35129043c305e4bb4dc`: UTC `2026-10-23T17:37:20Z`; Tehran `2026-10-23T21:07:20+03:30`.
- Master latest status update commit `e8770d6be88ec9d92170e8bc36ec022b03c0307c`; queue latest status update commit `6b84d1435fc4dffde5cb1619803dfcb565981be3`. Their commit UTC/Tehran conversions must be read from actual commit metadata before any exact timestamp is quoted.
- Confirmed status: repository write/read-back PASS for the listed artifacts; VTP-02 PARTIAL / FAIL-CLOSED pending refreshed Library mirror; VTP-03 length delta check PASS but semantic acceptance pending; VTP-04 blocked by absent Library write/refresh action; GitHub Actions run/artifact NOT VERIFIED; live host capture OPEN.


## Superseding destination result — Library mirror refreshed
- This section supersedes earlier statements in this event that the Library refresh was still pending. The exact Library mirror was overwritten and independently read back after that upload.
- Current Library snapshot file ID: `file_00000000422c8230b7b9709a831fd252`; stable Library file ID: `libfile_7ac3c9a6ec14819198eb2751e204aa48`; destination path remains `/Future AI/Palang Footprint/Master Reference Vault/Reference Documents/LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001.md`.
- Independent read-back snapshot metadata: modified UTC `2026-10-23T17:39:33.763445Z`; this is file metadata time, not the exact read-back operation time.
- VTP-02 PASS for semantic key fields in the refreshed mirror; VTP-03 PASS for the agreed length-tolerance rule; VTP-04 PASS for overwrite + independent read-back of this exact artifact/version. No byte-for-byte whole-file equality is claimed.
- The repository's latest test-plan closure note is commit `ce6c0f7b370932c50be3dcbf21c7dee7baf67e3f`, blob `e6330f9ad69c4d571ad6a23a85286d00c8347c28`.
- Still open: Behavior Hunter CI run/artifact NOT VERIFIED; host-wide live IN/OUT capture OPEN; VTP-06 and VTP-09 NOT RUN; VTP-07 execution NOT VERIFIED; Buffer/Persistent Memory NOT VERIFIED; Dropbox OPEN / NOT VERIFIED; external recovery NOT RUN.
