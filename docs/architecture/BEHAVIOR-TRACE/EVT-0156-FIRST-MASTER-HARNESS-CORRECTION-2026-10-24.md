# EVT-0156 — First Master Link Correction and Conformance Harness Recovery

- Stable ID: `G6IP-RAHM-EVT-0156-20261024`
- Production ID: `G6IP-EVT-0156`
- Version: 1.0.1
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

## Final conformance comparison
- Run [40114363915](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40114363915) completed SUCCESS on commit `2dd1b7836be7832a02f77a79d9d48c6423317538`.
- Valid fixture: 0 validation errors. Invalid fixture: 4 validation errors; expected rejection confirmed.
- Exact-byte SHA-256 comparison: PASS for all 24 files in the manifest inventory.
- The workflow also emitted the manifest's own SHA-256 as external run evidence; because later manifest status updates change its bytes, use the final post-update run for the final manifest digest.
- These results do not prove clean-host/second-host AI import, independent IN/OUT state equivalence, persistence, idle background, or full repository-wide graph repair.

## Latest final package receipt
- [Portable RAHM Conformance run 40114697473](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40114697473) completed SUCCESS.
- 24 manifest file SHA-256 values matched exact checked-out bytes; schema valid fixture passed with 0 errors and invalid fixture was rejected with 4 errors.
- Limited IN/OUT checkpoint/link recovery equivalence passed; the workflow explicitly does not claim full state reconstruction or AI-host transfer.
- Archive artifact: [haif-rahm-portable-package](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40114697473/artifacts/12567559136); 25 files including the manifest, 173,495 bytes uncompressed archive size as logged; archive SHA-256 `109cdb9af62f9f4f270aafea96076a5e0177877eb553551ed2fa268e997478df`.
- The repository-wide structural audit remains REVIEW_REQUIRED; the 11 missing links and identifier/parent/timestamp conflicts are not resolved by this package test.
