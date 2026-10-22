# EVT-0104 — Candidate architecture signals and behavior-hunter gate

- Stable ID: PALANG-BEHAVIOR-HUNTER-CANDIDATE-SIGNALS-2026-10-22-001
- Production ID: EVT-0104
- Version: 1.0.0
- Status: REGISTERED / READ-BACK VERIFICATION PENDING / ACTIVE / LIVING / OPEN
- Interaction: INT-20261022-016
- Input anchor: IN-20261022-016
- Output anchor: OUT-20261022-016
- Live Inbox item: INBOX-20261022-003
- Parent master: PALANG-UNIVERSAL-PROJECT-RECONSTRUCTION-MASTER-2026-10-22-001
- Behavior master: LIVING-BEHAVIOR-ARCHITECTURE-FORESIGHT-MASTER-REFERENCE-2026-10-22-001
- Continuation master: CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001
- Implementation issue: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/20

## Trigger and evidence
The user explicitly listed six signals from the previous two assistant outputs that should have been detected and connected:
1. Permanent live-inbox contract.
2. The master reference has a distinct role and is not replaced by the inbox.
3. Every interaction has a traceable input/output chain.
4. Growth is additive and historical architecture/evidence must not be silently overwritten.
5. Registration is distinct from completion/validation/integration.
6. Repository registration is not proof of automatic host-wide interaction capture.

## Candidate ledger
| Candidate ID | Label | Candidate | Evidence basis | Next validation |
|---|---|---|---|---|
| CAND-016-01 | OBSERVATION | Live Inbox is an intake/tracking surface, not the parent architecture. | User's explicit signal 1 and 2 in INT-20261022-016. | Verify in code/docs that intake never substitutes for master linkage. |
| CAND-016-02 | ARCHITECTURE RULE / OBSERVATION | Interaction provenance requires distinct IN and OUT anchors linked to an event. | User's explicit signal 3; existing project interaction-anchor contract. | End-to-end cold-start from either anchor. |
| CAND-016-03 | ARCHITECTURE RULE / OBSERVATION | Evolution must be append-only/versioned; preserve earlier evidence and architecture. | User's explicit signal 4. | Add a regression test for no silent overwrite and version/provenance preservation. |
| CAND-016-04 | ARCHITECTURE RULE / OBSERVATION | REGISTERED, READ-BACK VERIFIED, TESTED, VALIDATED, INTEGRATED, ACTIVE and LIVING are separate states. | User's explicit signal 5 and project status contract. | State-transition tests and UI/docs status vocabulary check. |
| CAND-016-05 | OBSERVATION / OPEN GAP | Repo writes and read-back do not prove automatic capture from the host. | User's explicit signal 6 and Issue #20 status. | Verify authorized producer path, capture permissions, durable storage and restart recovery. |
| CAND-016-06 | HYPOTHESIS | Prior miss likely arose because candidate extraction/linking was not a mandatory pre-finalization gate. | Inference from the observed miss; not proven root cause. | Instrument candidate extraction and uniqueness gate, then test against known examples. |

## Required behavior-hunter pipeline
1. Read visible input and assistant output as two evidence sources; do not infer hidden reasoning or claim unseen background processing.
2. Extract candidate architecture rules, patterns, feedback, errors, contradictions, missing evidence and actionable gaps.
3. Label each candidate OBSERVATION, INFERENCE, HYPOTHESIS or UNKNOWN; architectural rule is a category/type, not a substitute for epistemic label.
4. Preserve exact evidence and source anchors.
5. Check identifier uniqueness against repository paths/IDs before creating any artifact.
6. Route accepted candidates to Live Inbox, the relevant component master, universal parent master and implementation queue.
7. Write, read back, verify IDs/links and record actual UTC commit timestamp plus derived Asia/Tehran equivalent.
8. Keep implementation and validation open until tests demonstrate them.

## Failure and limitation
The current assistant workflow failed to harvest all six candidates when the prior outputs were first produced. This event registers them now and records the miss. It does not prove the hunter is continuously active in the background. Automated capture, permission boundary, runtime extraction and end-to-end restart recovery remain OPEN / NOT PROVEN under Issue #20.

## Recovery route
INT-20261022-016 -> IN/OUT-016 -> EVT-0104 -> INBOX-20261022-003 -> behavior master + universal master + model-initial queue -> Issue #20.
