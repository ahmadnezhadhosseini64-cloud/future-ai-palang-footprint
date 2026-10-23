# Test-to-Architecture Learning Loop — حلقهٔ یادگیری آزمون به معماری

- Stable ID: `PALANG-TEST-TO-ARCHITECTURE-LEARNING-LOOP-2026-10-23-001`
- Production ID: `TALL-HAIF-2026-10-23-001`
- Version: `1.0.0`
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Status: `ACTIVE / LIVING / DESIGN-REGISTERED / IMPLEMENTATION-PENDING`
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
