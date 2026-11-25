# Living Master Version Bridge — append-only lineage

This document explicitly connects the preserved portable predecessor to the updated living master. Neither document is deleted, overwritten as history, or treated as a second root.

## Linked documents

- **Historical predecessor — 1.7.95:** [LIVING_MASTER_REFERENCE-1.7.95-HISTORICAL.md](./LIVING_MASTER_REFERENCE-1.7.95-HISTORICAL.md). This is the original portable snapshot, retained unchanged.
- **Current successor — canonical living master:** [LIVING_MASTER_REFERENCE.md](./LIVING_MASTER_REFERENCE.md). The build synchronizes this file from `docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md`; its current source version is resolved at build time.

## Continuity rule

`1.7.95 (historical predecessor) → current canonical living master (successor)`

Both documents remain available. The successor continues the same POINT-0/GOLDEN lineage; it does not create another root, replace the predecessor's historical meaning, or silently discard its content. The canonical master itself retains its version history, including the 1.7.95 section.

The build-time synchronizer records SHA-256 for every retained predecessor in `manifest.json` and regenerates this bridge with exact version links and digests. Any missing, altered, or disconnected historical snapshot fails conformance.

The portable package keeps its existing stable identity and canonical ZIP filename. No parallel versioned ZIP is introduced.
