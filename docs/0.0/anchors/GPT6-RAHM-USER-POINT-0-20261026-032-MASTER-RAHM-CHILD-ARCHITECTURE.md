# POINT-0/032 — MASTER → RAHM → CHILD architecture and initial-model execution

- Stable ID: `HAIF-POINT-0-032-MASTER-RAHM-CHILD-20261026`
- Production ID: `HAIF-P032`
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / REPOSITORY WRITE PENDING READ-BACK
- Project: Future AI / Palang Footprint / HAIF
- Parent checkpoint: [CURRENT-078](./PALANG-0.0-CURRENT-20261026-078-REVERSIBLE-GRAPH-GAP-COVERS.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md); do not create NEXT-052.
- Related master: [Portable living master](../../portable/RAHM/FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md)
- Related RAHM package: [Initial-model mother](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Related RAHM startup: [RAHM_BOOT](../../portable/RAHM/RAHM_BOOT.md)

## User intent captured
The original Future AI / Palang Footprint project is the **MASTER**: it preserves canonical rules, historical interaction/behavior records, architecture patterns, evidence, versions and promotion authority. The new initial-model project/package is the **RAHM**: an isolated, exportable experimental environment that inherits the master's rules but cannot silently rewrite the master. A verified and explicitly accepted result becomes a **CHILD CANDIDATE**, and only after promotion gates pass may it be called a **NEWBORN / INITIAL CHILD VERSION**.

## Architecture and authority

`HUMAN ↔ AI HOST ↔ HAIF`

`MASTER → RAHM → OBSERVE → TEST → EVIDENCE → CHILD CANDIDATE → MASTER REVIEW → PROMOTED CHILD`

- MASTER owns canonical policy, provenance, source interaction pairs, stable IDs, version history, gap register and acceptance criteria.
- RAHM inherits a read-only baseline snapshot plus its own experiment ledger. It may propose changes, never overwrite the MASTER by inference.
- Each RAHM experiment records input, output, event, model/host/tool context when known, expected result, observed result, failure/correction, evidence references and exact artifact version.
- CHILD CANDIDATE is immutable/versioned after packaging; failed or untested candidates remain candidates, not newborn releases.
- NEWBORN means a separately versioned child artifact whose source, test receipts, recovery behavior and explicit master acceptance are recorded. It does not mean merely creating a folder or passing repository CI.
- Feedback from real use returns to MASTER as a proposal with evidence; no self-promotion.

## Verification bridge between repository and interactive project environment
Prepare a portable test bundle so a separate interactive AI project can be tested against the canonical repository. The receiving project must independently:
1. Load the export manifest and startup contract without hidden conversation context.
2. Reconstruct MASTER/RAHM/CHILD roles, current checkpoint, active queue and every OPEN gap.
3. Return a machine-comparable inventory of stable IDs, versions, parent links, status and evidence references.
4. Demonstrate that a RAHM experiment cannot modify MASTER policy without a promotion receipt.
5. Preserve conflicting IDs/parent candidates and reversible covers without closing underlying gaps.
6. Produce an import receipt with destination project/host identifier, import time, source commit, manifest/package digest, test results and read-back evidence.

Until the destination interactive project actually returns these receipts, external-project import is OPEN / NOT RUN / NOT VERIFIED. A repository commit or GitHub Actions success is not proof of an independent AI host.

## Reversible gap covers
Continue to cover (defer) but not close: CURRENT-065/CURRENT-066 conflict; EVT-0195 collision; historical graph/source census; provenance gaps; ambiguous parent edges; orphaned anchors/broken links; Issues #20/#21; exact-final-SHA conformance; external host import; persistence restart; always-on/background execution. Every cover requires a stable gap key, reason, retained evidence and reopening trigger.

## Next executable work — remains within NEXT-051
1. Verify this point and all changed master/index/queue/package files by read-back.
2. Define and run a repository-side RAHM-to-MASTER contract test against exact current SHA.
3. Add an import/reconciliation checklist for the interactive project environment; do not claim the environment was created or imported from this repository.
4. Regenerate portable manifest digests and run exact-head conformance after all final writes.
5. Preserve every failed, skipped or unavailable check as OPEN with a next action.

## Time
- Canonical repository registration time: to be read from the actual final commit timestamp in UTC; Tehran equivalent is UTC+03:30.
- User-message timestamp: not independently captured by the repository tool; UNKNOWN / UNVERIFIED.
