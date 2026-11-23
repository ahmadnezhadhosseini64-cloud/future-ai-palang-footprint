# EVT-0325 — Owner host enrollment and paired-interaction bridge decision

- Event ID: EVT-0325
- Input: IN-138
- Bridge: BRIDGE-0138
- Output: OUT-137
- Current candidate: CURRENT-150.05
- Sole queue candidate: NEXT-051.05
- Canonical root: POINT-0/GOLDEN
- Parent candidate: CURRENT-150.04
- Time binding: TIME-BINDING-EVT-0325
- Status: REGISTERED ON WORKING BRANCH / GOLDEN ACCEPTANCE PENDING

## Owner direction

The owner requested autonomous continuation, a paired bridge between every IN and its matching OUT, and a simple, secure one-message path for a new AI host to read the personal public repository, recover its current architecture, report its capabilities, receive an owner-reviewed identity and work only within a restricted isolated workspace.

## Decision

Public repository READ does not require collaborator membership or OAuth. A host may provide an ephemeral claim identifier, but it cannot self-issue an official Host ID. The owner issues official IDs only after reviewing a challenge-bound receipt and direct evidence. Hosts receive no write path to MASTER/main or RAHM.

Each interaction pair has one Bridge record linking its IN and OUT, parent checkpoint, event/time binding, CURRENT revision and the sole NEXT queue. The Bridge is initially a lightweight repository record and deterministic graph contract, not a new service.

## Actions

- Reviewed the existing candidate branch and PR #145; found CURRENT-150.03 and .04 already recorded on that same open candidate branch. Continued under the existing stable families rather than creating duplicate identities.
- Reviewed Issues #114–#123 and the current bounded evidence for Issues #20/#21.
- Added the host enrollment and pair-bridge contract plus the IN/OUT/Bridge/Event/Current/Next candidate records.
- Added current-pointer and one-message entry updates on the existing working branch only.
- No main/MASTER or Golden merge, private repo, GitHub App, API key, hosting, OAuth, or independent-host activation is claimed.

## Acceptance boundary

This event is not accepted until the exact branch commit is fetched back, the IN/OUT/Bridge graph resolves, and exact-SHA workflows pass. Golden merge remains owner-controlled. Runtime host enrollment and workspace isolation remain NOT RUN.
