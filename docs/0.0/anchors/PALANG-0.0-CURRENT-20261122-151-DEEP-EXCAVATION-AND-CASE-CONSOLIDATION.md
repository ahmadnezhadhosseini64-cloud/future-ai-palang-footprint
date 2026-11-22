# CURRENT-151 — Deep excavation, legacy pointer disposition and ten-case execution docket

- Stable ID: HAIF-CURRENT-151-POINT-0-DEEP-EXCAVATION-CASE-CONSOLIDATION-2026-11-22
- Status: ACTIVE / LIVING / SOURCE-LEVEL-READBACK-VERIFIED / EXTERNAL-GATES-OPEN
- Canonical root: POINT-0
- Golden baseline: POINT-0/GOLDEN
- Previous checkpoint: CURRENT-150
- Point: POINT-0/089
- Input: IN-133
- Output: OUT-132
- Event: EVT-0320 → TIME-BINDING-EVT-0320
- Event registration UTC: 2026-11-22T11:44:58Z
- Event registration Tehran: 2026-11-22T15:14:58+03:30
- Sole active queue: NEXT-051
- Owner: @ahmadnezhadhosseini64-cloud

## Canonical chain

POINT-0/GOLDEN → CURRENT-150 → POINT-0/089 → IN-133 → OUT-132 → EVT-0320 → TIME-BINDING-EVT-0320 → CURRENT-151 → sole NEXT-051.

No parallel root, Golden baseline, master or queue is created.

## Operational disposition of CURRENT-065 / CURRENT-066

CURRENT-065 and CURRENT-066 remain immutable historical checkpoints, not competing live pointers. Neither is retroactively selected as the winner. Their recoverable work is consolidated by function into Issue #20 (runtime, interaction capture and cold-start recovery), Issue #21 (historic source/rule/lesson census), and the existing NEXT-051 graph triage. The quarantined EVT-0178 draft remains quarantined; canonical EVT-0178 and EVT-0179 collision evidence remain intact. CURRENT-151 is now the sole live continuation pointer.

This resolves the operational ambiguity for current execution. It does not claim that every historical Stable-ID, Production-ID, event-number or parent-edge collision is closed.

## Storage and mirror simplification

- Buffer: WAITING / DEFERRED / NON-BLOCKING; no implementation or connector work required.
- Dropbox: WAITING / DEFERRED / NON-BLOCKING; no provisioning or synchronization work required.
- Neither is a core acceptance dependency. Reopen only on a demonstrated need.
- Mirror registration is supporting evidence only. It is useful only if the destination is independently controlled and exact-byte read-back plus recovery are proven. A same-control-plane duplicate or a mirror with byte differences does not establish independent persistence.

## Ten independent Partner cases

Issues #114–#123 have each been extended with:
- an independent stable case ID;
- input and expected output;
- dependency declaration;
- actual issue-creation UTC and prior read-back time;
- current evidence boundary;
- OPEN status;
- independent acceptance criteria and verification method.

All ten remain OPEN. They are children of NEXT-051, not a new queue. No external service is represented as provisioned.

## Issues #20 and #21

Issue #20 is the runtime track: stable INT/IN/OUT pairing, privacy/provenance, schema validation, append-only repository ledger, reverse lookup and cold-start recovery. Buffer and Dropbox are explicitly non-blocking and deferred.

Issue #21 is the historic source-census track: source → rule/lesson → component → test → evidence → gap. Its six-lesson and 14-source-family maps are partial evidence, not a complete census. Work should proceed in bounded source-family batches.

Both issues remain OPEN and independent. One cannot substitute for the other's acceptance.

## Package and exact-main evidence

The last exact-main architecture audit and Evidence Gate passed on main SHA 30d1d3b2de09078131fa3c8a0ff7c492a7ab0d7e. The earlier Portable RAHM Conformance failure was caused by stale 1.7.95 / CURRENT-140 package pins; the source correction has been made. PR candidate SHA bf7e7ab3fc79e598bf5456605dae2bfa75ef929c passed Portable RAHM Conformance run 45020163367 and Living Architecture Audit run 45020163375. The 24 Starter tests, 31 architecture/governance tests, package digest/inventory, paired-master byte read-back, ZIP extraction and artifact round-trip passed. PR #137 merged to Golden as 41487c7ddab3a7847e569e2fe3ac5d2d69fcca87; a fresh run on the exact post-merge Golden HEAD is pending. Release publication was skipped because the run was a PR. Independent real-host recovery and automatic live ChatGPT capture remain NOT RUN / NOT PROVEN.

At the last branch comparison, Golden and main remain DIVERGED; exact ahead/behind counts are dynamic and must be read from GitHub. Main was not modified by this work.

## Feasible work versus owner-side gates

Source inspection, issue docketing, source changes, branch/PR preparation, tests and read-back can be advanced through the connected repository. Actual private hosting, GitHub App registration/installation, OAuth broker, remote MCP deployment, OpenAI API project/key, secure secret configuration, Ruleset enforcement, private RAHM provisioning and genuine independent-host recovery require owner-side provisioning and direct receipts.

No AI host is ACTIVE until identity, isolation, persistence, recovery and negative-access tests are independently proven.

## Governance

Any party, including an AI collaborator, may propose a design improvement or candidate promotion. Only the owner may authorize and approve promotion to MASTER. Hosts remain PUBLIC READ ONLY to MASTER, with no direct or indirect write path, RAHM access, secrets, bypass or auto-merge.

## PR candidate conformance evidence — PR #137

- Tested source SHA: bf7e7ab3fc79e598bf5456605dae2bfa75ef929c (PR candidate before squash merge).
- Portable RAHM Conformance: run 45020163367 / job 137201049892 — SUCCESS.
- Living Architecture Audit: run 45020163375 / job 137201050285 — SUCCESS.
- Starter source and extracted ZIP: 24 tests PASS; architecture/governance audit: 31 tests PASS.
- Synthetic host adapter tests: synthetic ingest, authentication, durable read-back, idempotent retry, conflicting retry rejection and restart recovery all PASS.
- RAHM export package: 1,433,152 bytes; SHA-256 357f770a66e561b851578c2b4db23b2e6b20207ded1a11df6718699a7d95101c.
- Canonical starter ZIP: 281,026 bytes; SHA-256 2046e3ee8aa9f567a42e4f5c85c4d2cba98223671536fd65723df82d2185cbfd.
- Uploaded starter artifact: ID 14753028941; artifact-wrapper SHA-256 49b25df527418e5c50e8aeafad4ea7e3cca7ef230572da8bb4afb75789fb0f64.
- Downloaded artifact receipt, paired-master byte comparison, ZIP inventory/CRC and extracted 24-test round-trip: PASS.
- Release publication was SKIPPED because the run was a PR event. Independent real-host import/restart and automatic live ChatGPT capture were NOT RUN / NOT PROVEN.
- The PR was merged to Golden as commit 41487c7ddab3a7847e569e2fe3ac5d2d69fcca87. A fresh exact-post-merge Golden run is required; PR candidate receipts do not certify the merge commit.

## Acceptance boundary

CURRENT-151 records source-level reconciliation and issue updates. It does not close the portable package, exact-current-main audit, service provisioning, external API/OAuth/MCP, private RAHM, independent-host recovery or security gates. Those remain OPEN / NOT VERIFIED / NOT RUN until their own evidence is read back.

## Exact-SHA verification boundary

The PR #137 receipts (runs 45020163367 and 45020163375) tested the earlier 1.8.1 candidate SHA bf7e7ab3fc79e598bf5456605dae2bfa75ef929c. The portable mother and manifest were subsequently advanced to 1.8.2 / EXPORT_MANIFEST 1.8.39. Therefore the earlier candidate receipts are historical evidence only and do not certify the current 1.8.2 package bytes. The current 1.8.2 source must pass both Portable RAHM Conformance and Living Architecture Audit on the exact candidate tree before it can be called CI-verified. Release publication remains main-only; clean independent-host recovery remains a separate acceptance gate.

## Historical transition notice — retained under CURRENT-150 stable family

As of the proposed stable-identity transition, this CURRENT-151 record is preserved unchanged as historical transition evidence. Its findings, receipts and open gates are incorporated by reference into [CURRENT-150.01](PALANG-0.0-CURRENT-20261122-150-REVISION-01-STABLE-ANCHOR-IDENTITY-LOCK.md). It is no longer the resolver for the live current pointer once CURRENT-150.01 is accepted and merged. The historical event, timestamps and prior "current at that moment" state remain intact. No renumbering or deletion has occurred.
