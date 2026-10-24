# EVT-0156 — First Master Link Correction and Conformance Harness Recovery

- Stable ID: `G6IP-RAHM-EVT-0156-20261024`
- Production ID: `G6IP-EVT-0156`
- Version: 1.0.0
- Parent: [CURRENT-054](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-054-FIRST-LIVING-MASTER.md)
- Master: [FIRST-LIVING-MASTER](../../portable/RAHM/FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md)
- Next: [NEXT-048](../../0.0/anchors/PALANG-0.0-NEXT-20261024-048-FIRST-MASTER-CONFORMANCE.md)
- Workflow fix commit: [b669e1c](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/commit/b669e1c0828ad36a82b8a6c14421893cf2a0cabf)
- First workflow attempt: [40113909016 — failed](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40113909016)
- Harness correction rerun: [40113998759 — success](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40113998759)
- Latest expanded inventory run: [40114027114](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40114027114) — pending at time of this record.

## Observed and corrected
1. Focused link audit found six relative-link errors in the first master/IN/OUT/index supplement. Paths were corrected; a subsequent fetch of the ten relevant artifacts found zero missing local relative-link targets.
2. Workflow run 40113909016: valid fixture had 0 schema errors; invalid fixture had 4 errors and was correctly rejected. The workflow then failed in the digest-reporting script because it indexed a missing `status` key on successful result objects.
3. The reporting script was corrected to use a safe `get` and to compare any non-pending expected SHA-256 values. Workflow run 40113998759 completed SUCCESS.
4. A later expanded-manifest run was started after inventory growth. Its result must be read before any digest claims are promoted.

## Evidence boundary
- JSON Schema valid/invalid fixture behavior is proven by run 40113909016.
- A fixed digest workflow is proven to complete by run 40113998759, but the latest expanded inventory run must be read for current manifest contents.
- Exact-byte SHA-256 values must be copied from the run output into manifest entries and then verified by a subsequent successful comparison run.
- Full IN/OUT recovery equivalence, clean/second-host AI import, persistence restart, idle background, and repository-wide ID/link remediation remain OPEN / NOT RUN or NOT VERIFIED.
