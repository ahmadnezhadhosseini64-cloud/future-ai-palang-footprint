# POINT-0/022 — Portable HAIF Starter Engine

- Stable ID: HAIF-POINT-0-022-PORTABLE-STARTER-ENGINE-20261025
- Production ID: HAIF-P0-022-20261025
- Version: 1.0.0
- Status: REGISTERED / LIVING / ACTIVE DEVELOPMENT / OPEN
- Parent: [POINT-0/021](./GPT6-RAHM-USER-POINT-0-20261025-021-INITIAL-MODEL-COMPLETION-GATE.md)
- IN: [IN-052](./PALANG-0.0-IN-20261025-052-PORTABLE-STARTER-ENGINE.md)
- OUT: [OUT-052](./PALANG-0.0-OUT-20261025-052-PORTABLE-STARTER-ENGINE.md)
- Event: [EVT-0185](../../architecture/BEHAVIOR-TRACE/EVT-0185-PORTABLE-HAIF-GPT6-STARTER-ENGINE-2026-10-25.md)
- Execution checkpoint: [CURRENT-069](./PALANG-0.0-CURRENT-20261025-069-PORTABLE-STARTER-ENGINE-AND-GATE-CLOSURE.md)
- Existing queue retained: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Living mother: [HAIF Initial Model Master Reference](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)

## User intent

Make this interaction a new Point 0; close CURRENT-068's open gates as far as evidence permits; build a usable initial model, not another document-only layer; prepare the fastest practical portable starter for GPT-6; keep it connected to all Future AI / Palang Footprint architecture and preserve existing project continuity.

## Implementation started

A runnable starter package is being built inside the canonical repository at prototype/haif-gpt6-starter/. It contains:
- standard-library Python runtime;
- independent anchor, IN, OUT and event IDs;
- append-only hash-linked event records;
- explicit open-gap registry with evidence-gated closure;
- Master → Child proposal and evidence-gated promotion;
- portable export/import with SHA-256 verification;
- GPT-6 host instructions, manifest, state schema and tests.

This is an executable prototype package, not a native GPT plugin. A GPT host can use the instructions and uploaded state if supported; actual GitHub writes, automatic capture, durable host memory and background execution still require real host permissions/integrations.

## Continuity rule

No historical anchor, checkpoint, queue, event or unresolved graph item is replaced. CURRENT-069 supersedes CURRENT-068 only as the next execution checkpoint; CURRENT-068 remains historical evidence for its own acceptance gates. NEXT-051 remains active for historical graph work; no duplicate next queue is created.

## Timestamp rule

The exact user-message timestamp is UNKNOWN / UNVERIFIED unless captured by a trusted host. Repository registration time is the actual commit time in UTC, with Tehran time derived from the same instant.
