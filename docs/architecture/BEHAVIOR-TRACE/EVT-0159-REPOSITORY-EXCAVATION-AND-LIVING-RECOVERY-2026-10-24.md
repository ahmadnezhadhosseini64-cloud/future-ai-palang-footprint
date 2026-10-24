# EVT-0159 — Repository Excavation and Living Recovery

- Stable ID: `G6IP-RAHM-EVT-0159-20261024`
- Production ID: `G6IP-EVT-0159`
- Version: 1.0.0
- Status: REGISTERED; read-back required; global graph and real-host gates remain OPEN.
- Point 0: [User Point 0/006](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261024-006-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY.md)
- Input: [IN-050](../../0.0/anchors/PALANG-0.0-IN-20261024-050-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY.md)
- Output: [OUT-049](../../0.0/anchors/PALANG-0.0-OUT-20261024-049-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY.md)
- Prior event: [EVT-0158](./EVT-0158-NO-SILENT-GAP-OUTPUT-CONTINUITY-2026-10-24.md)
- Prior current: [CURRENT-056](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-056-OUTPUT-CONTINUITY-AND-RECOVERY.md)
- Next: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Evidence-backed observation
The user reports that after an input, the assistant may appear to process without a visible output; a later input then seems to displace the unfinished task. This is a reported interaction failure pattern, not proof of the app's internal runtime cause.

## Architecture rule: NO-SILENT-GAP / RESUME-ON-NEW-IN
1. Every material input attaches to the latest valid CURRENT and the active OPEN NEXT.
2. The assistant returns visible status/result at each durable milestone; at turn end, say COMPLETED, PARTIAL, or BLOCKED and identify the next anchor.
3. Never claim invisible background execution or durable capture unless a host runtime and receipt prove it.
4. If a new input arrives while work is open, preserve the prior NEXT and create a child input branch; reconcile priority without deleting the older work.
5. Before acting on a new input, fetch the repository's latest CURRENT, NEXT, master, manifest, index and queue; do not rely only on copied excerpts or remembered summaries.
6. Preserve raw failure, cause hypothesis, correction and retest evidence. Hypotheses are not promoted to facts without evidence.
7. Every repository write is followed by independent read-back. Manifest/package digests are rerun after final changes.
8. Any unverified gate stays OPEN/LIVING and is carried into each subsequent checkpoint.

## Excavation receipt
Latest inspected commit `0104a0799a574cb78c5b121a0bcd9192b857ed51`, UTC `2026-10-24T18:51:33Z` / Tehran `2026-10-24T22:21:33+03:30`.
Conformance [40122633966](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40122633966) passed declared package/schema/digest/limited-recovery scope. Audit [40122633902](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40122633902) completed with `REVIEW_REQUIRED`: 11 missing links, 60 unreviewed stable-ID collision groups, 88 production-ID collision groups, 7 reference-ID collision groups, 36 event-number collision groups and 13 ambiguous parent edges.



## Latest excavation recheck — run 40124425936 / 2026-10-24
- Structural audit workflow completed, but content result remains `REVIEW_REQUIRED`: 3,757 files including generated evidence; 5,564 local-link edges; 16 missing links; 62 stable-ID collision groups (61 unreviewed); 88 production-ID collision groups; 7 reference-ID collision groups; 36 event-number collision groups; 13 ambiguous parent edges; 0 decode errors.
- Strict portable conformance run [40124425568](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40124425568) passed for manifest v1.4.2: schema valid fixture 0 errors, invalid fixture rejected with 4 errors, all expected file digests matched, limited IN/OUT checkpoint-link equivalence passed; package 44 files / 221380 bytes / SHA-256 `591377d03546e6f031ee98614b1c9fbd662dba08a15bc5c68b15bd918282f501`.
- These are repository/CI results only. Full IN/OUT state reconstruction, clean/second AI-host import, actual persistence restart and idle/background execution remain OPEN / NOT VERIFIED.
