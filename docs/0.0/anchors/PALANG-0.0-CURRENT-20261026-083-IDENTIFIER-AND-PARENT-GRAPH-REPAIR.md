# CURRENT-083 — Identifier and parent-graph repair

- Stable ID: HAIF-CURRENT-083-IDENTIFIER-PARENT-GRAPH-REPAIR-20261026
- Production ID: HAIF-C083
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/035](./GPT6-RAHM-USER-POINT-0-20261026-035-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Chain: [IN-071](./PALANG-0.0-IN-20261026-071-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md) → [OUT-070](./PALANG-0.0-OUT-20261026-070-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md) → [EVT-0205](../../architecture/BEHAVIOR-TRACE/EVT-0205-POINT-0-035-IDENTIFIER-AND-PARENT-GRAPH-REPAIR-2026-10-26.md)
- Previous checkpoint: [CURRENT-082](./PALANG-0.0-CURRENT-20261026-082-INTERACTIVE-RAHM-EXECUTION.md)
- Canonical repository time binding: [TIME-BINDING-CURRENT-083](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-CURRENT-083-POINT-0-035-2026-10-26.md).
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## State at checkpoint creation
- Source-specific parent resolver and metadata-header identifier extraction exist in repository.
- The audit for SHA 8aac51fa544d56913d01a148371c160f4a6a0714 reports 4 missing local links, 2 unresolved parent edges, 0 ambiguous parent edges, 63 stable-ID groups, 92 production-ID groups, 7 reference-ID groups and 41 event-number groups. These are baseline counts, not a claim that this checkpoint closes them.
- The new helper modules/tests were not yet explicitly wired into the workflow's compile/test steps.
- The exact source of CURRENT-065/CURRENT-066 lineage conflict remains open.
- RAHM independent host import/restart/round-trip remains NOT RUN.

## Next execution actions
1. Wire helper modules and tests into CI; rerun both unit tests.
2. Correct missing links only where evidence identifies the intended canonical target.
3. Run audit and portable conformance on the exact same final main SHA; read logs/artifacts back.
4. Review stable/production/reference/event collisions in small batches, retaining source hashes and role decisions.
5. Keep NEXT-051 active; no NEXT-052.
