# Verifiable Test Plan from EVT-0115 — Live Mirror Sync Recovery

- Stable ID: `PALANG-VERIFIABLE-TEST-PLAN-EVT-0115-2026-10-23-001`
- Production ID: `VTP-HAIF-EVT0115-2026-10-23-001`
- Version: `1.0.0`
- Status: `ACTIVE / LIVING / PROPOSED — tests defined; execution evidence not yet collected`
- Parent event: [EVT-0115](../BEHAVIOR-TRACE/EVT-0115-LIVE-MIRROR-SYNC-RECOVERY-AND-MASTER-REGISTRATION-2026-10-23.md)
- Scope: repository registration, canonical-to-Library mirror recovery, destination-state honesty, restart/retrieval, scheduling claims, timestamps, and preservation of historical 0.0 anchors.
- Governance: a defined test is not a passed test. Mark PASS only with captured evidence; mark BLOCKED with exact error and retry condition; use NOT RUN when no execution occurred. Do not infer Library, Buffer, Persistent Memory, or Dropbox success from repository evidence.

## Test matrix

| Test ID | Test | Procedure / observable evidence | Pass criterion | Current state |
|---|---|---|---|---|
| VTP-01 | Repository write/read-back | Fetch the event, master reference, queue, test plan, Behavior Hunter spec, generator, unit tests, fixture, workflow and observatory index; record paths and blob SHAs. | Each expected repository file is present after an independent fetch and contains the intended identifiers/content. | PASS for current listed repository artifacts: independent fetch/read-back completed; see EVT-0116 and latest blob SHAs recorded in the continuation evidence. This does not prove the CI workflow ran. |
| VTP-02 | Semantic field reconciliation | Compare canonical audit and Library mirror for Stable ID, Version, Next Action, and Destination Statuses. | All key fields retain the same meaning. Any semantic mismatch is recorded as a failure even if lengths match. | NOT RUN for fresh current copies. |
| VTP-03 | Accepted 7-character tolerance | Compare lengths and content; separately inspect key fields and any changed lines. | A 7-character length difference alone is not a blocker only when key-field meaning matches; no silent claim of byte-for-byte identity. | POLICY RECORDED; fresh comparison NOT RUN. |
| VTP-04 | Library write and independent read-back | If mismatch requires repair, write from the canonical source, then re-open/read Library independently. Capture before/after evidence and content/field comparison. | Independent read-back confirms intended content and key-field match. A write response alone is insufficient. | BLOCKED / NOT VERIFIED until Library access works. |
| VTP-05 | Destination-state honesty | Inspect claims for Repository, Library, Buffer, Persistent Memory, Dropbox, and external recovery separately. | Each destination has its own evidence-backed status; unknown or untested destinations remain NOT VERIFIED / NOT RUN. | PARTIAL PASS: source audit's stale Library status was corrected; Library verification is limited to the older exact mirror, latest revision not synced. Buffer/Persistent Memory NOT VERIFIED; Dropbox OPEN / NOT VERIFIED; external recovery NOT RUN. |
| VTP-06 | Restart/retrieval from event only | In a fresh continuation, start from EVT-0115 and recover canonical path, master link, queue item, next action, accepted tolerance, and destination statuses without relying on this chat's narrative. | All required continuation fields can be recovered from repository records; gaps are explicitly listed. | NOT RUN. |
| VTP-07 | Scheduled continuation claim | Inspect the one-off automation record and, after its scheduled time, capture actual execution/result evidence if available. | Distinguish “scheduled/created” from “executed successfully”; no completion claim without execution evidence and resulting read-back. | SCHEDULE WAS CREATED per conversation record; execution NOT VERIFIED. |
| VTP-08 | UTC canonical timestamp | Fetch actual Git commit metadata for each repository change; derive Tehran time from that same UTC instant. | UTC matches real commit metadata; Tehran is a conversion of the same instant, not a separate guessed time. | Apply to this plan's commit and subsequent changes. |
| VTP-09 | Historical 0.0 preservation | Compare relevant anchor paths/IDs before and after changes; do not overwrite or collapse multiple anchors. | Prior anchor identities and contents remain intact; any missing or changed anchor is reported and investigated. | NOT RUN as an end-to-end test. |
| VTP-10 | Blocker capture and retry | Reattempt Library read/write only when available; if it fails, capture exact tool error, target, time evidence if available, and next retry condition. | Failure remains visible as OPEN/BLOCKED; no fabricated success and no endless retry claim. | Prior error recorded: `container_session_unavailable`; fresh retry NOT RUN. |

## Execution protocol

1. Start from this plan and EVT-0115; fetch the current canonical audit and Library mirror.
2. Execute VTP-02 and VTP-03 before making any write.
3. If a semantic mismatch requires correction, perform VTP-04. If access fails, record the exact error and stop claiming completion.
4. Execute VTP-01, VTP-05, VTP-06, VTP-08, and VTP-09 with observable repository evidence.
5. Treat VTP-07 as pending until an actual automation execution/result can be inspected.
6. Update this matrix with evidence links, commit SHA, actual UTC commit time, and Tehran conversion derived from UTC. Do not mark the whole plan PASS while any required test is blocked or unrun.

## Current conclusion

The recovery route and tests are now specified in the repository architecture. This is a test plan, not proof that the mirror has synchronized. Library, Buffer, Persistent Memory, Dropbox, restart recovery, and external end-to-end execution remain unverified unless new evidence is added.


## Live update — EVT-0116 (2026-10-23)

- Behavior Hunter architecture: [PALANG-BEHAVIOR-HUNTER-TEST-GENERATION-AND-GROWTH-GATE-2026-10-23-001](./PALANG-BEHAVIOR-HUNTER-TEST-GENERATION-AND-GROWTH-GATE-2026-10-23-001.md).
- Event: [EVT-0116](../BEHAVIOR-TRACE/EVT-0116-BEHAVIOR-HUNTER-LIVE-TEST-ACTIVATION-2026-10-23.md).
- VTP-02: PARTIAL / FAIL-CLOSED. The live comparison found a contradictory stale Library status in the canonical audit; corrected in commit `a2374d7da36a5af69b1bdf17f6dfd673bc03c97f` (UTC `2026-10-23T17:34:39Z`, Tehran `2026-10-23T21:04:39+03:30`). Post-update read-back and mirror refresh remain pending.
- VTP-03: length check PASS (8,915 vs 8,908; delta 7); semantic acceptance PENDING until the corrected source is mirrored and read back.
- VTP-04: BLOCKED for this execution; Library read is available but a Library write/refresh action is not exposed through the current tool surface.
- Behavior Hunter implementation paths: `scripts/behavior-hunter/generate_candidate_tests.py`; `tests/behavior-hunter/test_generate_candidate_tests.py`; `data/interaction-pairs/interaction-pairs.jsonl`; `.github/workflows/palang-behavior-hunter.yml`.
- Workflow commit `9d908b15220a9f4a97fd1c56ae32edd393d18196` — UTC `2026-10-23T17:33:36Z`; Tehran `2026-10-23T21:03:36+03:30`. EVT-0116 commit `b3147c9fb16726eabe77858ec204dc5989907137` — UTC `2026-10-23T17:35:07Z`; Tehran `2026-10-23T21:05:07+03:30`.
- Five unit tests are authored, but the actual CI run/artifact has not been independently retrieved: NOT VERIFIED, not PASS. Candidate generation is not execution success.
- Live host capture remains OPEN: the generator consumes structured interaction records in the repository and does not yet automatically capture every ChatGPT interaction. No automatic Master promotion; successful tests feed Child/Rahm review only.


## Repository read-back evidence — EVT-0116 continuation

Independent GitHub fetch/read-back returned the following current blobs after writes:
- Canonical audit: `de1b75f07241c9b313e476af5f1417177ff78c10`.
- This test plan: `a83665a32122b49210083cda1182902a5b85f18c`.
- Behavior Hunter architecture: `93108610b3e30d454efde61d950eee3440b29ae7`.
- EVT-0116: `e1e9a23905e20ae8308444d237f2f53bf6a99155`.
- Master reference: `f228bac8684dee3f88662c568ee4dc4b24f78200`.
- Integration queue: `c84b3d0ab4294c2ccddc3d863663a8e3419fc724`.
- Behavior Observatory index: `fd6d94f3ed3bec1bb23603eeaedbefa0765a8efc`.
- Generator: `5bc67ec4128b6d85f55bff70c80a9beb40cdb191`.
- Unit tests: `f95e67cf030e27964b962e77c36c3f82df0ce30e` (read-back confirmed the corrected import path).
- Structured IN/OUT fixture: `7ba9204e732035cfc7e5c69ccb9b9b721f899774`.
- CI workflow: `6ac98ae03adda11eb3a94038a1c7c859bb250a30`.

Repository commit timestamps observed from GitHub metadata (UTC canonical; Tehran derived):
- Source audit correction `a2374d7da36a5af69b1bdf17f6dfd673bc03c97f`: UTC `2026-10-23T17:34:39Z`; Tehran `2026-10-23T21:04:39+03:30`.
- Test-plan update `e30c08e434f8ae37d0668e0f146ab1cc4e37e4db`: UTC `2026-10-23T17:35:48Z`; Tehran `2026-10-23T21:05:48+03:30`.
- Master update `e07d538c4d5ac407d2a3414c0f4d205270e76a6b`: UTC `2026-10-23T17:36:06Z`; Tehran `2026-10-23T21:06:06+03:30`.
- Queue update `8a08b7e86a0992fb2b5eb279ea697db2caa72af9`: UTC `2026-10-23T17:36:10Z`; Tehran `2026-10-23T21:06:10+03:30`.
- Unit-test import fix `5d3c8ae44296e949ff3a16a97817c9a06d839eee`: UTC `2026-10-23T17:36:23Z`; Tehran `2026-10-23T21:06:23+03:30`.
- Observatory index update `e8e013f5360d5e7f533b5a56c2031d440a878a13`: UTC `2026-10-23T17:36:33Z`; Tehran `2026-10-23T21:06:33+03:30`.

CI run and uploaded artifact are NOT VERIFIED because the available GitHub actions interface in this execution does not expose a workflow-run listing/dispatch operation. The workflow is configured to run on relevant pushes; do not mark the unit tests or generated artifact PASS until the actual run evidence is retrieved. Host-wide live capture remains OPEN.


## Library mirror refresh result — 2026-10-23
- Library overwrite succeeded at the canonical mirror path; stable Library file ID `libfile_7ac3c9a6ec14819198eb2751e204aa48`; new snapshot file ID `file_00000000422c8230b7b9709a831fd252`.
- Independent Files search/read returned the refreshed snapshot and EVT-0116 addendum. Metadata modified UTC `2026-10-23T17:39:33.763445Z` (metadata time only; exact read-back operation time was not exposed).
- VTP-02: PASS for semantic key fields in the refreshed mirror — Stable ID, Test ID, Version 1.0.0, next-action chain BOART-FOLLOWUP-01 → 02 → 03, and per-destination status states. No byte-for-byte whole-file equality claim.
- VTP-03: PASS for the accepted seven-character tolerance rule; the refreshed archival mirror includes additive reconciliation notes, so whole-file length differs intentionally.
- VTP-04: PASS for this exact mirror artifact/version: overwrite succeeded and independent retrieval/read-back confirmed the new snapshot.
- Remaining gates: VTP-06 restart recovery NOT RUN; VTP-07 scheduled execution NOT VERIFIED; VTP-09 historical 0.0 end-to-end preservation NOT RUN. Behavior Hunter CI run/artifact NOT VERIFIED and live host capture OPEN.
