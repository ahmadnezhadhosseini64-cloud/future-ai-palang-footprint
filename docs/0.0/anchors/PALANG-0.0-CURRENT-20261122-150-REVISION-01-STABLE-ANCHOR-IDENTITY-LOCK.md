# CURRENT-150.01 — First stable-family revision / 0++ continuity lock

- Stable family ID: CURRENT-150
- Revision: 150.01
- Revision document ID: HAIF-CURRENT-150-REV-01-STABLE-ANCHOR-LOCK-2026-11-22
- Status: CANDIDATE / ACTIVE DEVELOPMENT / EXACT-SHA ACCEPTANCE PENDING
- Canonical root: POINT-0
- Golden baseline: POINT-0/GOLDEN
- Parent stable checkpoint: CURRENT-150
- Transition snapshot preserved: CURRENT-151
- Input: [IN-134](PALANG-0.0-IN-20261122-134-STABLE-ANCHOR-IDENTITY-LOCK.md)
- Output: [OUT-133](PALANG-0.0-OUT-20261122-133-STABLE-ANCHOR-IDENTITY-LOCK.md)
- Event: [EVT-0321](../../architecture/BEHAVIOR-TRACE/EVT-0321-STABLE-ANCHOR-IDENTITY-LOCK-AND-REVISION-RECEIPT-2026-11-22.md)
- Time binding: [TIME-BINDING-EVT-0321](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0321-STABLE-ANCHOR-IDENTITY-LOCK-2026-11-22.md)
- Sole queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Queue revision: NEXT-051.01 (candidate)
- Governing policy: [POINT-0 Stable Anchor and Revision Policy](POINT-0-STABLE-ANCHOR-AND-REVISION-POLICY-2026-11-22.md)

## 1. Stable continuation

`POINT-0/GOLDEN → CURRENT-150 (stable family) → IN-134 → OUT-133 → EVT-0321 → TIME-BINDING-EVT-0321 → CURRENT-150.01 → NEXT-051.01`

This is the same canonical root and same queue. No new Point-0 number, root or queue is introduced. The original CURRENT-150 and CURRENT-151 records remain intact.

## 2. Why CURRENT-151 is preserved but no longer the resolver

The current Golden baseline already contains CURRENT-151, POINT-0/089, IN-133, OUT-132 and EVT-0320. Those records are preserved as a valid historical transition snapshot with their original timestamps and evidence.

The owner now wants the public-facing identity to stop moving. Therefore:
- CURRENT-151 remains an immutable historical record and its prior state is not falsified.
- Its findings and evidence are incorporated into this stable-family revision.
- CURRENT-150.01 becomes the first revision beneath the fixed CURRENT-150 identity.
- Canonical current-pointer registries will resolve to CURRENT-150.01, not to a new CURRENT number.
- The existing NEXT-051 queue is retained and revised as NEXT-051.01.

No historical file is deleted or renumbered.

## 3. Package version and verification

- Golden living mother at the base of this revision is version 1.8.2.
- The authoritative rule is mother-first: package manifest, portable mirror and tests follow the exact current mother. The mother is never downgraded to satisfy stale test literals.
- PR #138 candidate SHA `d63347be5ba8dba564d1c923c95a91d5d2169688` passed Portable RAHM Conformance run `45021299472` and Living Architecture Audit run `45021299450`; the candidate was merged to Golden as `669f46f2b7a12ab9809f36c0ddf69f3e5b50acf4`.
- Candidate receipts recorded 24 starter tests and 31 architecture/governance tests passing, SHA-256 inventory, RAHM archive build, canonical starter ZIP rebuild, downloaded-artifact digest, extraction and extracted tests.
- Exact post-merge Golden audit/conformance remains to be freshly retrieved. PR candidate success is not mislabeled as post-merge proof.

## 4. CURRENT-065 / CURRENT-066 disposition

- CURRENT-065 and CURRENT-066 remain historical and preserved.
- The legacy filename `CURRENT-065-OVERLAY-MANIFEST.json` contains the CURRENT-066 package/checkpoint identity.
- CURRENT-065 is the predecessor; CURRENT-066 is the bounded overlay checkpoint. The CURRENT-109 verifier is a historical recovery test, not a live global pointer.
- The tested scoped-pointer logic reports overlay and global registries separately and does not select a winner by numeric order.
- This specific operational pointer ambiguity is resolved; the full historic source census and all duplicate-ID/parent-edge adjudication remain OPEN under Issue #21.

## 5. Issues #20 and #21

**Issue #20 — runtime, interaction capture and cold-start recovery**
- Local runtime now supports stable daily INT/IN/OUT IDs, reverse lookup from IN or OUT, append-only hash chain, actual-record JSON Schema validation, and local write/read-back.
- Six local runtime tests passed in the prior candidate; synthetic adapter tests and portable CI evidence also passed on candidate workflows.
- Still OPEN: automatic ChatGPT/host capture is NOT_IMPLEMENTED; real independently controlled host import/restart and external persistence are NOT PROVEN. Do not close based on local CLI tests.

**Issue #21 — historic source/lesson census**
- Existing tree inventory, initial six normalized lessons and 14-source-family mapping are partial evidence only.
- Still OPEN: full repository/Git-history source census, semantic extraction of all rules, duplicate/collision and parent-edge adjudication, complete source→rule→component→test→evidence graph, and exact final-SHA audit.
- Do not call the census complete from tree listing or partial crosswalks.

## 6. Buffer and Dropbox

Both remain `WAITING / DEFERRED / NON-BLOCKING`. They are not needed for the core architecture while the canonical repository, owner-controlled export, and an independently verified host recovery path remain the intended core. Reopen only if a concrete requirement and verified connector show a unique benefit. Their historical records are preserved.

## 7. Ten Partner dossiers

Issues #114–#123 remain ten independent OPEN cases under the same NEXT-051 queue. Each keeps its own ID, input/output, dependencies, evidence, actual UTC, acceptance criteria and read-back. No issue is closed merely because its architecture is documented.

## 8. Main and owner gate

- Main remains at the separately audited SHA `30d1d3b2de09078131fa3c8a0ff7c492a7ab0d7e` unless a fresh read-back proves otherwise.
- Ruleset 27814009 was last observed ACTIVE but required approvals=0 and CODEOWNERS review=false; owner approval enforcement is NOT VERIFIED.
- Private Partner hosting, GitHub App, OAuth/MCP, OpenAI API, service deployment, private RAHM and independent-host recovery remain NOT PROVISIONED / NOT VERIFIED / NOT RUN.
- No host direct/indirect write, bypass, auto-merge, force-sync or secret exposure is permitted.

## 9. Acceptance for this revision

This candidate becomes the active CURRENT-150.01 only after:
1. The policy and all current-pointer/index/mother/portable references are updated on one PR based on the latest Golden HEAD.
2. Living Architecture Audit and Portable RAHM Conformance pass on the exact final PR head/merge tree.
3. The PR is merged to POINT-0/GOLDEN and the merge commit/tree is read back.
4. The unsuffixed CURRENT-150 resolver and sole NEXT-051 queue resolve to the latest verified revisions.
5. The ten Partner issues and Issues #20/#21 are read back and remain OPEN until their individual acceptance criteria pass.

