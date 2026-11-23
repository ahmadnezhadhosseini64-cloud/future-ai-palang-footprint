# BRIDGE-0138 — پل جفت ورودی IN-138 و خروجی OUT-137

- Stable ID: HAIF-BRIDGE-0138-IN-138-OUT-137-2026-11-23
- Root: POINT-0/GOLDEN
- Parent candidate: CURRENT-150.04 / NEXT-051.04
- Input: [IN-138](PALANG-0.0-IN-20261123-138-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE.md)
- Output: [OUT-137](PALANG-0.0-OUT-20261123-137-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE.md)
- Event: [EVT-0325](../../architecture/BEHAVIOR-TRACE/EVT-0325-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE-2026-11-23.md)
- Time binding: [TIME-BINDING-EVT-0325](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0325-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE-2026-11-23.md)
- Current candidate: [CURRENT-150.05](PALANG-0.0-CURRENT-20261123-150-REVISION-05-HOST-ENROLLMENT-AND-PAIR-BRIDGE.md)
- Sole queue candidate: [NEXT-051.05](PALANG-0.0-NEXT-20261123-051-REVISION-05-HOST-ENROLLMENT-AND-PAIR-BRIDGE.md)
- Status: GRAPH VERIFIED / EXACT-HEAD-CI-PENDING

## Required graph edges

POINT-0/GOLDEN → CURRENT-150.04 → IN-138 ↔ BRIDGE-0138 ↔ OUT-137 → EVT-0325 → TIME-BINDING-EVT-0325 → CURRENT-150.05 → NEXT-051.05

The Bridge is the explicit pair connector. It must link backward to the accepted/parent state and forward to the next checkpoint and the sole queue. It does not create a new root, stable CURRENT family, or NEXT queue.

## Pair integrity contract

A complete interaction pair must contain:
- one immutable IN record with source/provenance and owner intent;
- one OUT record linked to exactly that IN;
- one Bridge record linked bidirectionally to both IN and OUT;
- one event record linking the pair and exact execution scope;
- one time-binding record derived from the event commit metadata;
- one CURRENT revision and one revision of the existing NEXT queue;
- read-back of all records and verification that all references resolve.

The Bridge status is not inferred from the presence of files:
- REGISTERED — records exist.
- READ-BACK VERIFIED — independently fetched records match the committed content.
- GRAPH VERIFIED — all required edges resolve and no duplicate pair identity exists.
- ACCEPTED — relevant CI and controlled Golden promotion completed.
- ACTIVE — runtime capability is actually operating, if the record concerns runtime.

## Evidence fields

Each Bridge must record:
1. Pair ID, IN ID/path, OUT ID/path.
2. Canonical root and accepted parent CURRENT/NEXT.
3. Event ID and time-binding ID.
4. Exact source branch and commit SHA.
5. UTC commit timestamp and derived Tehran timestamp; owner-message time remains UNKNOWN unless independently supplied.
6. Actions actually executed, tool outcomes, test IDs, and read-back refs.
7. Unresolved tasks and exact owner-only gates.
8. Previous pair and next pair/checkpoint links when known; unknown future links stay explicitly pending.

## Anti-complexity rule

Do not add a separate POINT-0 root, a parallel NEXT queue, a new database, or an external bridge service merely to implement this record. The Bridge is initially a small version-controlled Markdown record plus deterministic graph checks. A live transport bridge is a separate runtime capability and remains OPEN until deployed and tested.

## Protocol and receipt schema

- Host enrollment protocol: [HOST-ENROLLMENT-CHALLENGE-AND-PAIR-BRIDGE](../../architecture/HOST-REGISTRY/HOST-ENROLLMENT-CHALLENGE-AND-PAIR-BRIDGE-2026-11-23.md).
- Receipt schema: [HOST-ENROLLMENT-RECEIPT-SCHEMA](../../architecture/HOST-REGISTRY/HOST-ENROLLMENT-RECEIPT-SCHEMA-2026-11-23.json).
- Receipt template: [HOST-ENROLLMENT-RECEIPT-TEMPLATE](../../../prototype/universal-host/HOST-ENROLLMENT-RECEIPT-TEMPLATE.json).


## Graph verification receipt — 2026-11-23

All seven records were fetched again from the working branch and the required edges checked:
- IN-138 contains links to BRIDGE-0138 and OUT-137: PASS.
- BRIDGE-0138 links to both IN-138 and OUT-137: PASS.
- OUT-137 links to IN-138 and BRIDGE-0138: PASS.
- EVT-0325 links the same pair: PASS.
- TIME-BINDING-EVT-0325 binds EVT-0325 to the exact event commit: PASS.
- CURRENT-150.05 and NEXT-051.05 link the same pair and stable root/queue: PASS.

The seven fetched blob SHAs are preserved in the assistant's current verification receipt; the files remain fetchable on PR #145. This verifies the repository graph for this pair, not live capture of all future chats.


## Shared canonical references

- Living mother: [سند مرجع مادر مدل اولیه هوش مصنوعی](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- Independent-host recovery proof protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md).
- Portable host protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md).
- Portable export manifest: [EXPORT_MANIFEST](../../portable/RAHM/EXPORT_MANIFEST.json).


Canonical root: [POINT-0/GOLDEN](GPT6-RAHM-USER-POINT-0-GOLDEN-20261122-001.md).
