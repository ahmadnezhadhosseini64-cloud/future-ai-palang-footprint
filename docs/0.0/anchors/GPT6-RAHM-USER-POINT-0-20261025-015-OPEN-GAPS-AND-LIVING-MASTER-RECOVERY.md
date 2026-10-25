# POINT-0/015 — Open Gaps, Living Master and Verifiable Recovery

- Stable ID: G6IP-POINT-0-015-20261025
- Status: REGISTERED; repository read-back pending for this new chain; all unproven gates remain OPEN.
- Purpose: Establish this user instruction as a new root point without overwriting earlier 0.0 points.
- Previous active checkpoint: [CURRENT-065](./PALANG-0.0-CURRENT-20261025-065-AUTONOMOUS-CONTINUITY-AND-RECOVERY.md).
- Next chain: [IN-059](./PALANG-0.0-IN-20261025-059-OPEN-GAPS-AND-LIVING-MASTER-RECOVERY.md) → [OUT-058](./PALANG-0.0-OUT-20261025-058-OPEN-GAPS-AND-LIVING-MASTER-RECOVERY.md) → [EVT-0174](../../architecture/BEHAVIOR-TRACE/EVT-0174-OPEN-GAPS-AND-LIVING-MASTER-RECOVERY-2026-10-25.md) → [CURRENT-066](./PALANG-0.0-CURRENT-20261025-066-OPEN-GAPS-AND-LIVING-MASTER-RECOVERY.md).
- Living mother: [HAIF Initial Model Master Reference](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- Active continuation: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md).

## User directive preserved
Treat this interaction as a new Point 0; connect it to the prior checkpoint and existing graph; keep every unconfirmed/unproven claim open and actively tracked; document architectural gaps, defects, and next steps as the next 0.0; evolve and maintain the living master so it can be extracted, recovered, independently read back and verified.

## Governance
- Preserve historical checkpoints; never overwrite a prior point to simulate continuity.
- UTC is canonical. Tehran time is a derived display of the same repository commit instant, not a second canonical clock.
- Registration, read-back, validation, test pass, integration, external-host proof and persistent recovery are distinct statuses.
- An unresolved claim stays OPEN / NOT VERIFIED / NOT RUN / NOT PROVEN, with a concrete evidence requirement.
- No claim of autonomous background execution, external storage, independent AI-host recovery or persistence without an observed receipt.
- Every durable milestone must connect the user input, assistant output, behavior event, current checkpoint, mother, index, queue and portable manifest.

## Required recovery sequence
1. Recover this chain from Point 0 alone and from OUT alone; compare reconstructed state.
2. Independently read back all chain links and every changed parent surface.
3. Validate manifest JSON and verify exact Git blob SHA values; compute SHA-256 only from exact bytes and record the producing run.
4. Execute runtime unit tests and a clean init → IN/OUT → checkpoint → export → import → recovery round trip; preserve command, exit code, Python version, commit and UTC.
5. Inspect current CI run and artifact receipts, not a stale successful run.
6. Continue NEXT-051 findings one by one; no speculative merging, renumbering or bulk deletion.
7. Keep independent-host, restart persistence, second-host persistence, idle/background execution and external destinations open until directly evidenced.

## Open architecture gaps
- Full canonical-state reconstruction from independent IN/OUT roots: OPEN.
- Current manifest exact-byte digests and package archive digest: OPEN until checked against a current run.
- Runtime tests and clean round-trip on current revision: OPEN until actual receipts.
- Repository-wide collision/ambiguous-parent findings: OPEN / REVIEW_REQUIRED.
- Clean independent AI-host and second-host import: OPEN / NOT RUN unless a real host receipt is recorded.
- Restart persistence, automatic capture, idle/background operation and external storage: OPEN / NOT PROVEN.
- Cross-surface synchronization (mother/index/queue/manifest/overlay): must be independently re-read after each update.

## Acceptance rule
Do not close any gate because a document exists. Close only when the required evidence is attached, independently read back, and reconciled against the exact revision. If blocked, record blocker, owner/action, evidence needed and next check in CURRENT-066/NEXT-051.

This record is a repository artifact; its final canonical registration timestamp is the actual last-change Git commit timestamp, in UTC with the Tehran equivalent derived from that instant.
