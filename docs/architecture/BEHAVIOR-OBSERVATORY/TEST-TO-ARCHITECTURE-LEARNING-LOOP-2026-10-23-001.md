# Test-to-Architecture Learning Loop — حلقهٔ یادگیری آزمون به معماری

- Stable ID: `PALANG-TEST-TO-ARCHITECTURE-LEARNING-LOOP-2026-10-23-001`
- Production ID: `TALL-HAIF-2026-10-23-001`
- Version: `1.0.0`
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Status: `ACTIVE / LIVING / IMPLEMENTED-IN-REPOSITORY / CI-VERIFICATION-PENDING / OWNER-GATED`
- Parent event: `EVT-0117`
- Related architecture: [Behavior Hunter](./PALANG-BEHAVIOR-HUNTER-TEST-GENERATION-AND-GROWTH-GATE-2026-10-23-001.md)
- Canonical timestamp rule: repository commit UTC is authoritative; Tehran is derived from the same instant.

## 1. Audit finding: the prior growth gate was too narrow

The previous design correctly prevented unsupported PASS claims and automatic MASTER promotion, but it treated architecture growth mainly as a Child/Rahm proposal. It did not define a repeatable mechanism that turns verified test outcomes into reusable architecture patterns, design changes, governance rules, schemas, recovery methods, workflow improvements, or regression controls. The generator emits candidate tests, not architecture insights. The old gate was a safe first layer, not a complete learning loop.

## 2. Expanded mission

Behavior Hunter is an evidence-led design and architecture learning system, not merely a test generator. It may propose improvements anywhere in Future AI / Palang Footprint / HAIF when interaction evidence or test outcomes support them.

Eligible proposal domains:
- architecture structure, interfaces, adapters, and component boundaries;
- schemas, identifiers, provenance, event chains, and data contracts;
- continuity, restart recovery, resume pointers, and preservation of all 0.0 anchors;
- verification, evidence quality, destination-state honesty, and auditability;
- user interaction, clarification, output quality, and error recovery;
- automation, CI, observability, reporting, and repository workflows;
- security, privacy, data minimization, permissions, and failure containment;
- reusable patterns, anti-patterns, test templates, and regression suites;
- documentation and onboarding where evidence shows recurring confusion or failure.

These are proposal domains, not permission for uncontrolled changes. The system may generate, compare, rank, and test proposals; adoption follows explicit gates.

## 3. Bidirectional learning

Use all observable result classes as learning signals:
1. Verified PASS — identify which invariant/pattern worked and whether it generalizes.
2. FAIL — preserve the counterexample, classify root cause, and create a regression test.
3. BLOCKED — expose missing interfaces, access, permissions, or observability as architecture gaps.
4. NOT RUN — record an evidence gap, never interpret it as success.
5. Repeated near-duplicates — propose a shared abstraction or reusable test while retaining source links.
6. User correction or explicit acceptance — record observable feedback, not hidden chain-of-thought.
7. Source/mirror drift — propose stronger synchronization contracts and semantic reconciliation.

## 4. Learning pipeline

`IN/OUT + EVENTS + TEST RESULTS + FEEDBACK`
→ `ANCHOR + PROVENANCE`
→ `GENERATE CANDIDATE TESTS`
→ `EXECUTE`
→ `VERIFY EVIDENCE`
→ `EXTRACT PATTERN / FAILURE / GAP`
→ `FORM ARCHITECTURE HYPOTHESIS`
→ `COMPARE EXISTING RULES + COUNTEREXAMPLES`
→ `DESIGN OPTIONS + TRADE-OFFS`
→ `PROTOTYPE / REGRESSION TEST`
→ `VERSIONED PROPOSAL`
→ `OWNER REVIEW`
→ `CANONICAL INTEGRATION`
→ `POST-INTEGRATION VERIFICATION`.

Each stage records its status and evidence separately. No stage may be silently skipped.

## 5. Required architecture insight record

Each proposed insight includes:
- `insight_id`, title, version, originating event/test IDs;
- category and affected components;
- observed facts separated from hypothesis/inference;
- supporting evidence locators and source commit/run identifiers;
- counterexamples, failed tests, and conflicting evidence;
- confidence label with explicit rationale, not fabricated probability;
- expected benefit, risks, costs, reversibility, and affected interfaces;
- proposed change and alternatives where meaningful;
- required tests, regression coverage, and rollback/containment plan;
- state: `OBSERVED`, `HYPOTHESIS`, `PROPOSED`, `PROTOTYPED`, `VERIFIED`, `APPROVED`, `INTEGRATED`, or `REJECTED`;
- owner decision and post-integration verification evidence.

## 6. Evidence and promotion rules

- PASS means only that the exact test passed against its stated criterion.
- One passing test may suggest a local improvement; a general architectural pattern needs repeated evidence, an explicit rationale, or a controlled prototype.
- Failures and blocked tests are first-class learning signals; never discard them because a later run passes.
- Contradictory evidence triggers reconciliation rather than averaging away the conflict.
- Preserve provenance and every historical 0.0 anchor; append, do not silently overwrite.
- Avoid redundant retests: rerun only after source/code/dependency/deployment changes, new risk/evidence, regression, or changed acceptance criterion.
- Candidate insights may target any architecture layer, not only Child/Rahm. Child/Rahm are possible validation stages, not the exclusive destination.
- No automatic canonical MASTER mutation. Owner approval is required for normative rules, structural changes, interfaces, permission changes, or production-impacting behavior. Low-risk reversible experiments may run in an isolated branch/prototype under explicit policy, with evidence and rollback.
- After approved integration, run relevant regression tests and independently read back canonical artifacts.

## 7. Anti-patterns to detect

- treating a generated candidate as a passed test;
- assuming a configured workflow actually ran;
- using repository evidence to claim Library or other destination success;
- treating character count as semantic equality;
- overfitting architecture to one example;
- ignoring user correction or failed attempts;
- converting absence of evidence into PASS;
- promoting a pattern without counterexample search or regression coverage;
- repeating a closed test without material change;
- narrowing every useful finding into one predetermined branch/module.

## 8. First implementation backlog

- TALL-01: extend the structured record schema to represent test outcomes and architecture insights.
- TALL-02: add deterministic extraction of proposal candidates from PASS/FAIL/BLOCKED/NOT RUN and feedback.
- TALL-03: validate proposals against evidence, counterexamples, duplicates, and existing rules.
- TALL-04: add tests for useful proposals from successful and failed cases.
- TALL-05: persist a versioned insight manifest/artifact with source IDs and traceable links.
- TALL-06: add post-integration regression/read-back verification.
- TALL-07: prove actual CI execution and artifact retrieval; separately implement and verify live host capture.
- TALL-08: add recovery test rebuilding current work state from event + insight records without narrative chat context.

## 9. Initial audit status

- Design gap identified and recorded.
- This document establishes the expanded architecture policy.
- Insight extraction and independent execution are pending.
- Existing five unit tests are authored but actual CI execution has not been independently retrieved.
- Live capture of every ChatGPT IN/OUT remains OPEN.
- This record does not claim that the learning loop is fully automated or operational end-to-end.


## Implementation addendum — deterministic insight candidate extractor
- Extractor: `scripts/behavior-hunter/extract_architecture_insights.py`.
- Unit tests: `tests/behavior-hunter/test_extract_architecture_insights.py`.
- Four explicitly illustrative outcome records (PASS, FAIL, BLOCKED, NOT RUN): `data/interaction-pairs/test-outcomes.jsonl`. These examples are fixtures, not claims about production test execution.
- Workflow: `.github/workflows/palang-behavior-hunter.yml` now runs the extractor and uploads candidate-test and architecture-insight JSON manifests in one artifact bundle. Relevant architecture/reference changes were added to workflow path filters.
- Extractor states are proposals only; PASS without evidence is rejected; FAIL creates a regression/anti-pattern candidate; BLOCKED creates an architecture-gap candidate; NOT RUN creates an evidence-gap candidate. Every proposal has source IDs, evidence fields, UNASSESSED confidence, OWNER_REVIEW_REQUIRED and `master_mutation: false`.
- Commit registering extractor: `004974970583fc214d97b4b42638fcc3d6a4c05e`; unit tests: `e811cc864b9bf74ad699d5b19f7f67e9234195df`; outcome fixture: `68075ea7fddad8ec25b6d3d63ccdf42fe6d38149`; workflow update: `d15af1dce6a4f79420dc972bc8324dacdf12defd`.
- Important: files are registered, but this addendum does not claim the CI workflow has actually passed. Independent run/job/artifact evidence remains required. The implementation is a deterministic candidate extractor, not yet a full root-cause engine or live ChatGPT host adapter.


## 10. Implementation addendum — architecture update gate

- Gate: `scripts/behavior-hunter/architecture_update_gate.py`.
- Regression tests: `tests/behavior-hunter/test_architecture_update_gate.py`.
- Proposal fixture: `data/interaction-pairs/architecture-update-proposal-fixture.json`; it uses the controlled EVT-0120 evidence target and its recorded SHA-256. It is a fixture proposal, not proof of a production architecture change.
- CI now runs the gate and publishes `architecture-update-gate.json` with the existing candidate/evidence manifests.
- The gate checks required proposal fields, allowed lifecycle state, repository-confined evidence locators, exact SHA-256, counterexamples, required tests, rollback plan, owner decision and protected architecture paths.
- Safety invariant: the gate only emits a decision manifest; it never mutates MASTER or canonical architecture. Promotion remains false even when an approval decision is represented; integration requires a separate explicit, reviewable change followed by regression and independent read-back.
- Test cases cover valid proposal, missing schema fields, wrong/missing evidence, path traversal, protected targets, integration without approval and approval-state mismatch.
- The previous statement that insight extraction and independent execution were pending is superseded by the implementation addenda above. Current CI status and artifact inspection must be recorded separately; live host-wide capture and fresh-session recovery remain unproven.


## 11. Append-only architecture evolution ledger — EVT-0126
- New validator: `scripts/behavior-hunter/validate_architecture_update_ledger.py`.
- Regression suite: `tests/behavior-hunter/test_architecture_update_ledger.py`.
- Version history: `data/interaction-pairs/architecture-update-ledger.jsonl`; version 1.0.0 is retained and version 1.1.0 records the user-authorized integration of ledger validation. Earlier entries are not rewritten.
- CI runs the validator and emits `architecture-update-ledger.json`.
- The validator checks required fields, unique change/version pairs, monotonic sequence, explicit supersedes links, source events, evidence references, rollback plan, and explicit owner approval for APPROVED/INTEGRATED states.
- The validator is read-only: no canonical mutation, no history rewrite, and no approval of future proposals. It complements the evidence proposal gate; neither gate alone proves host-wide capture or fresh-session recovery.
- Status: implementation registered; the exact new CI run and generated manifest must be read back before EVT-0126 can be marked CI-VERIFIED.


## 12. Verified ledger validator execution — EVT-0126
- [Run 40014035299](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40014035299): SUCCESS; 65 tests passed on tested SHA `11499b652676d6d89eea0fca42d528acc1d8b2e4`.
- Artifact `12528275489`, SHA-256 `6ae23e424080b598395a558bc5f9ba4550e06e7dea9bda934f05f782d0526793`, downloaded and inspected.
- Ledger manifest PASS: 2 records, 2 unique versions, 1 change stream, zero errors. Version 1.0.0 retained; version 1.1.0 records the explicitly authorized integration of the append-only validator.
- Evidence proposal gate remains separate and owner-gated; fixture proposal decision is PENDING; no automatic promotion or canonical mutation.
- Both repository recovery directions RECOVERED; fresh-session recovery remains NOT RUN; runtime-wide capture and external persistence remain unproven.


## 13. Tamper-evident append-only ledger — verified
- Ledger rows now include a canonical-JSON `record_sha256` and `previous_record_sha256`; the chain starts with `GENESIS`. Any row edit or broken predecessor link is rejected.
- Regression tests include tampered row and broken/reordered chain; earlier version 1.0.0 is preserved and linked to 1.1.0.
- [Run 40014712373](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40014712373) passed 67 tests on SHA `965713b2ef2ca4873176015128313da9c03c1b48`.
- Artifact `12527726978`, ZIP SHA-256 `6ddf0b23d3f33db2cdfc6cb4b1e7154899bf1477a0466ba5c01a2a3c7325c07b`, inspected: ledger PASS, hash chain verified, zero errors; both recovery directions RECOVERED.
- Interim test/fixture failures were fixed and retained as lessons in EVT-0126. Fresh-session recovery remains NOT RUN; no host-wide capture or external persistence claim.


## 14. Deep repository audit feeds architecture growth — EVT-0127
- The Living Architecture Audit is an active evidence source for model growth, not just a final status label. The inspected artifact found 5 broken links, 60 Stable ID collision groups, 71 Production ID collision groups, 7 reference-ID collision groups, 30 event-number collision groups, 11 exact duplicate groups, 13 ambiguous parent edges, 11 proposed alias edges and one unresolved timestamp.
- Five local-link targets were checked against repository paths and repaired; the next audit must verify the new count before closure.
- Collision/duplicate resolution must be semantic and history-aware. No bulk renaming, deletion or alias promotion is allowed solely because identifiers/content collide.
- The separate workflow evidence shows bounded CI runtime transfer and automatic registration proof; it does not prove universal ChatGPT-host capture or arbitrary external persistence.
- [NEXT-028](../../0.0/anchors/PALANG-0.0-NEXT-20261023-028-POST-REPAIR-AUDIT-AND-SEMANTIC-RECONCILIATION.md) is the active next gate.


## 15. Latest-pair recovery and status transparency — EVT-0129
- [EVT-0129](../BEHAVIOR-TRACE/EVT-0129-LIVING-REGISTRATION-ARCHITECTURE-GROWTH-AND-RECOVERY-REPAIR-2026-10-24.md) records that earlier recovery manifests still recovered IN-026/OUT-026 after the active project had advanced to IN-030/OUT-030. That green result was historical-pair proof, not current-continuation proof.
- Resolver implementation now discovers the newest shared interaction ID and refuses fallback when that latest pair is incomplete or non-reciprocal.
- Regression coverage targets latest pair discovery, both directions, invalid newest pair, stale master reference, and non-inference of fresh-session/host-wide/external capabilities.
- [Interaction Execution Status Protocol](./INTERACTION-EXECUTION-STATUS-AND-LIVING-REGISTRATION-PROTOCOL-2026-10-24-001.md) defines durable status vocabulary and the visible execution lifecycle.
- Architecture ledger version 1.2.0 appended; versions 1.0.0 and 1.1.0 retained. Verification is not complete until CI and manifests prove the current pair.


## Status-transparency and current-pair addendum — EVT-0130
- A successful recovery applies only to the exact pair and source SHA named by its artifact; never carry a historical pair's PASS forward to a new pair.
- Latest verified baseline before this pair: run 40060077581 on SHA `15bf46b3debe4131c6eb8c210ec0c334f76b449c`; both directions recovered IN-031/OUT-031; ledger PASS with 3 hash-linked records.
- Pair 032 / EVT-0130 / NEXT-032 is newly registered. CI recovery and artifact read-back for pair 032 are pending.
- User-facing status protocol: acknowledge promptly; report RUNNING only while a real operation is underway; report VERIFIED only after independent read-back; name OPEN gaps and next durable action. Do not claim background execution or live ChatGPT UI instrumentation.
- Preserve issue status: #19 real-document acceptance OPEN; #20 runtime capture/end-to-end recovery OPEN; #21 historical census/semantic reconciliation OPEN. Fresh-session recovery NOT RUN; external persistence and host-wide capture NOT PROVEN.


## Verified current pair — EVT-0130
- Pair 032 is now recovered in both directions on tested SHA `6936932f39d21d5af422d357ee0b41082a9f281e` (run 40060524636); artifact 12547123152 inspected, SHA-256 `c8a8cd44292be51def96d51dc4930fcaf5a304137f901053b69c1640784209ab`.
- The missing reciprocal link in the first attempt was caught, recorded and repaired. No prior history was overwritten.
- Remaining boundaries: fresh-session NOT RUN; host-wide capture/external persistence NOT PROVEN; Issues #19/#20/#21 OPEN.


## Architecture growth backlog from verified audit — EVT-0130
- Add template-aware link-audit exclusions/diagnostics for literal placeholders in test code; do not create fake files to silence false positives.
- Build a provenance-first semantic adjudication workflow for duplicate/colliding IDs and ambiguous parent edges; aliases stay proposed until reviewed.
- Resolve the one timestamp parse/timezone ambiguity using the original source line; keep UTC canonical and Tehran derived from the same instant.
- Keep pair-032 repository recovery separate from fresh-session recovery, host-wide capture and external persistence.


## 11. Status transparency and durable terminal receipts
- The workflow now emits a machine-readable terminal receipt from `scripts/behavior-hunter/emit_status_receipt.py`, including on prior-step failure via `if: always()`.
- Receipt fields include event/pair IDs, stage, terminal status, workflow run ID, tested commit SHA, UTC timestamp, and derived Asia/Tehran equivalent.
- Regression tests explicitly verify that failure remains failure and that the receipt does not claim chat UI heartbeat, host-wide capture, or external persistence.
- This is an additive capability; it does not replace the architecture-update proposal gate or append-only hash-linked version ledger. Previous versions remain intact.
- Exact CI and artifact verification must be appended after the workflow completes.


## 12. Living graph drift detector
- The read-only detector `scripts/behavior-hunter/check_living_graph_drift.py` compares the latest bidirectional pair against master, queue, global index, 0.0 index, behavior-trace index, observatory and durable status receipt.
- Regression tests cover complete graph, missing master link and missing durable receipt.
- Run 40062120276: 74 tests passed; `living-graph-drift.json` returned PASS, six nodes checked, zero failures; artifact ZIP SHA-256 `e45208b1bd2b63fa4e30fedcf27b9701532b8c85feee298ae18cbd6105c0d332`.
- Ledger 1.4.0 records the capability append-only; next CI must validate the five-record chain. This is repository drift detection only, not cross-session recovery or external persistence.
