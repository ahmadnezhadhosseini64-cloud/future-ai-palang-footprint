# QUARANTINED DUPLICATE CHECKPOINT ARTIFACT — NOT THE CANONICAL CURRENT-089

> CURRENT-089 was already assigned to the canonical Initial Model New-Host Handoff. Preserve this alternate checkpoint as collision evidence only. Canonical checkpoint: [CURRENT-089 Initial Model New-Host Handoff](./PALANG-0.0-CURRENT-20261027-089-INITIAL-MODEL-NEW-HOST-HANDOFF.md); canonical root: [POINT-0/040](./GPT6-RAHM-USER-POINT-0-20261027-040-INITIAL-MODEL-NEW-HOST-HANDOFF.md).

# QUARANTINED — CURRENT-089 duplicate draft (historical content retained)

- Stable ID: HAIF-CURRENT-089-INITIAL-MODEL-TRANSFER-20261027
- Production ID: HAIF-C089-20261027
- Version: 1.0.0
- Status: QUARANTINED / DUPLICATE ID ARTIFACT / NOT CANONICAL
- Root: [POINT-0/040](./GPT6-RAHM-USER-POINT-0-20261027-040-INITIAL-MODEL-TRANSFER-AND-ARCHITECTURE-HARD-AUDIT.md)
- Parent: [POINT-0/039](./GPT6-RAHM-USER-POINT-0-20261027-039-MIRROR-SYNC-AND-ARCHITECTURE-CONTINUATION.md)
- Transfer contract: [Initial Model Host Transfer Bootstrap](../portable/RAHM/INITIAL-MODEL-HOST-TRANSFER-BOOTSTRAP-2026-10-27.md)
- Host prompt: [HOST-BOOTSTRAP-PROMPT](../portable/RAHM/HOST-BOOTSTRAP-PROMPT-2026-10-27.md)
- Sole queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Mother reference: [Initial AI Model Master Reference](../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)

## Objective
Prepare a host-independent candidate package that can be loaded into a new AI host without relying on previous conversation context. Candidate-package readiness is distinct from independent-host acceptance.

## Ordered work under NEXT-051
1. Read back POINT-0/040, this checkpoint, transfer contract and host prompt.
2. Add all four artifacts to EXPORT_MANIFEST.json with exact Git blob SHA-1 and SHA-256 derived from actual bytes. Read back and independently recompute.
3. Update mother reference, behavior-trace index, reference index and integration queue; read back every changed file.
4. Rediscover current main and relevant workflow runs. Run Living Architecture Audit and Portable RAHM Conformance on the same final SHA after all edits.
5. Check links and IDs; do not decide CURRENT-065/CURRENT-066 by inference.
6. Keep Issues #20/#21 open until their acceptance criteria have direct evidence.
7. Buffer/Persistent Memory NOT VERIFIED; Dropbox OPEN / NOT VERIFIED; external host import and cold recovery NOT RUN until direct receipts exist.

## Acceptance gates
- Transfer contract and prompt exist and are read-back verified.
- Manifest includes every required file and exact checksums.
- Current source and indexes are linked rather than copied as if current.
- A new host can use repository authority and rediscover the latest root.
- Real independent-host import and restart-recovery receipt exists before claiming operational readiness.

## Status boundary
This checkpoint does not claim the new host has been tested. NEXT-051 remains the sole queue; no NEXT-052 is created.
