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
| VTP-01 | Repository write/read-back | Fetch the event, master reference, queue, and this test plan after each write; record paths and blob SHAs. | Every expected file is present and contains the intended Stable ID, status, and next action after independent fetch. | PARTIAL: EVT-0115, master and queue read-back were verified; this plan awaits its own post-write read-back. |
| VTP-02 | Semantic field reconciliation | Compare canonical audit and Library mirror for Stable ID, Version, Next Action, and Destination Statuses. | All key fields retain the same meaning. Any semantic mismatch is recorded as a failure even if lengths match. | NOT RUN for fresh current copies. |
| VTP-03 | Accepted 7-character tolerance | Compare lengths and content; separately inspect key fields and any changed lines. | A 7-character length difference alone is not a blocker only when key-field meaning matches; no silent claim of byte-for-byte identity. | POLICY RECORDED; fresh comparison NOT RUN. |
| VTP-04 | Library write and independent read-back | If mismatch requires repair, write from the canonical source, then re-open/read Library independently. Capture before/after evidence and content/field comparison. | Independent read-back confirms intended content and key-field match. A write response alone is insufficient. | BLOCKED / NOT VERIFIED until Library access works. |
| VTP-05 | Destination-state honesty | Inspect claims for Repository, Library, Buffer, Persistent Memory, Dropbox, and external recovery separately. | Each destination has its own evidence-backed status; unknown or untested destinations remain NOT VERIFIED / NOT RUN. | POLICY CHECK DEFINED; recheck during execution. |
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
