# EVT-0214 — POINT-0/040 Duplicate-ID Collision and Quarantine

- Stable ID: HAIF-EVT-0214-POINT-040-DUPLICATE-ID-QUARANTINE-20261027
- Production ID: HAIF-EVT0214-20261027
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / OPEN
- Canonical root: [POINT-0/040 Initial Model New-Host Handoff](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261027-040-INITIAL-MODEL-NEW-HOST-HANDOFF.md)
- Canonical input/output: [IN-077](../../0.0/anchors/PALANG-0.0-IN-20261027-077-INITIAL-MODEL-NEW-HOST-HANDOFF.md) → [OUT-076](../../0.0/anchors/PALANG-0.0-OUT-20261027-076-INITIAL-MODEL-NEW-HOST-HANDOFF.md)
- Canonical user-request event: [EVT-0213](./EVT-0213-INITIAL-MODEL-NEW-HOST-HANDOFF-2026-10-27.md)
- Canonical checkpoint: [CURRENT-089](../../0.0/anchors/PALANG-0.0-CURRENT-20261027-089-INITIAL-MODEL-NEW-HOST-HANDOFF.md)
- Sole active queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Finding

During continuation, an alternate draft was created using identifiers POINT-0/040, EVT-0213 and CURRENT-089 after the repository already contained canonical records for those IDs. The repository's existing new-host handoff chain is the canonical chain because it already binds the user instruction IN-077, OUT-076, EVT-0213, CURRENT-089, the existing executable starter and the established bootstrap.

## Containment action

The competing files below were not deleted; their historical content was preserved and each was marked QUARANTINED / DUPLICATE ID ARTIFACT / NOT CANONICAL:
- docs/0.0/anchors/GPT6-RAHM-USER-POINT-0-20261027-040-INITIAL-MODEL-TRANSFER-AND-ARCHITECTURE-HARD-AUDIT.md
- docs/architecture/BEHAVIOR-TRACE/EVT-0213-POINT-0-040-INITIAL-MODEL-TRANSFER-AND-HARD-AUDIT-2026-10-27.md
- docs/0.0/anchors/PALANG-0.0-CURRENT-20261027-089-INITIAL-MODEL-TRANSFER-EXECUTION.md

The distinct transfer contract and host prompt remain supplementary materials, not replacement roots or checkpoints. The canonical executable baseline remains prototype/haif-gpt6-starter and the canonical host bootstrap remains docs/architecture/مدل اولیه AI/NEW-HOST-BOOTSTRAP-2026-10-27.md.

## Architecture lesson

Before assigning a new POINT, EVT, CURRENT, IN or OUT identifier, query the live repository and relevant indexes. If a collision is found, preserve the competing record, do not recycle the identifier, do not delete history, and register the collision as a separate event. An ID collision is a durable model-behavior lesson and must remain visible in future audits.

## Remaining work

- Remove quarantined drafts from the live export inventory; keep the quarantine files as historical evidence.
- Add the canonical root, IN/OUT, event, checkpoint, bootstrap and collision event to the live manifest inventory with exact supported digests.
- Update indexes/mother/queue links and independently read back each change.
- Run the supported package digest/conformance workflow and Living Architecture Audit on the exact same final main SHA.
- Independent-host import and cold recovery remain NOT RUN until direct receipts exist.
