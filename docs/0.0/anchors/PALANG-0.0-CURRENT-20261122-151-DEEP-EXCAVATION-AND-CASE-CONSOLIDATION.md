# CURRENT-151 — Deep excavation, legacy pointer disposition and ten-case execution docket

- Stable ID: HAIF-CURRENT-151-POINT-0-DEEP-EXCAVATION-CASE-CONSOLIDATION-2026-11-22
- Status: ACTIVE / LIVING / SOURCE-LEVEL-READBACK-PENDING / EXTERNAL-GATES-OPEN
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

The last exact-main architecture audit and Evidence Gate passed on main SHA 30d1d3b2de09078131fa3c8a0ff7c492a7ab0d7e. Portable RAHM Conformance failed because the portable starter manifest, tests and documents still pin living-master version 1.7.95 / CURRENT-140 while Golden's mother is version 1.8.0 / CURRENT-150. The package is NOT VERIFIED. The source correction and a fresh exact-SHA conformance run remain required.

At the last branch comparison, Golden was 217 commits ahead and 26 behind main. Main was not modified by this work.

## Feasible work versus owner-side gates

Source inspection, issue docketing, source changes, branch/PR preparation, tests and read-back can be advanced through the connected repository. Actual private hosting, GitHub App registration/installation, OAuth broker, remote MCP deployment, OpenAI API project/key, secure secret configuration, Ruleset enforcement, private RAHM provisioning and genuine independent-host recovery require owner-side provisioning and direct receipts.

No AI host is ACTIVE until identity, isolation, persistence, recovery and negative-access tests are independently proven.

## Governance

Any party, including an AI collaborator, may propose a design improvement or candidate promotion. Only the owner may authorize and approve promotion to MASTER. Hosts remain PUBLIC READ ONLY to MASTER, with no direct or indirect write path, RAHM access, secrets, bypass or auto-merge.

## Acceptance boundary

CURRENT-151 records source-level reconciliation and issue updates. It does not close the portable package, exact-current-main audit, service provisioning, external API/OAuth/MCP, private RAHM, independent-host recovery or security gates. Those remain OPEN / NOT VERIFIED / NOT RUN until their own evidence is read back.