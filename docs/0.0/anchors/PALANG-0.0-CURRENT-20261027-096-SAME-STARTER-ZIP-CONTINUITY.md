# CURRENT-096 — Same initial ZIP, continuous 0.0 development

- Stable ID: HAIF-CURRENT-096-SAME-STARTER-ZIP-CONTINUITY-20261027
- Production ID: G6IP-CURRENT-096
- Version: 1.0.0
- Status: ACTIVE / LIVING / IN PROGRESS / NOT COMPLETE
- Chain: POINT-0/046 → IN-084 → OUT-083 → EVT-0221 → CURRENT-096 → NEXT-051.
- Parent ZIP confirmation: [POINT-0/045](./GPT6-RAHM-USER-POINT-0-20261027-045-EXISTING-ZIP-UPDATE-CONFIRMATION.md) and [CURRENT-095](./PALANG-0.0-CURRENT-20261027-095-EXISTING-ZIP-UPDATE-CONFIRMATION.md).
- Living mother: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر مدل اولیه هوش مصنوعی.md)
- Existing package source: [HAIF starter](../../../prototype/haif-gpt6-starter/README.md)
- In-package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Verified baseline before this continuation
- Existing canonical filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
- Internal package version: 0.3.1.
- Stable package ID: `HAIF-GPT6-PORTABLE-STARTER-20261025-004`.
- Latest verified workflow: [40506089579](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40506089579), exact tested SHA `dc37693a5dc2983dd0d3b70a8dd0d010d6dd1aad).
- Nested ZIP: 19,042 bytes; SHA-256 `3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83`; 8 files; ZIP CRC PASS; 16/16 tests PASS.
- Outer artifact wrapper from the same run: 19,634 bytes; SHA-256 `15aedf51bef0f263dfd8f19aa0e13a027a76e4b62e5fc83c0655496045936b52`. Do not confuse this with the nested canonical ZIP digest.

## Architecture: update one package, not fork many
- [x] Preserve the original Stable ID and canonical archive filename.
- [x] Rebuild the canonical ZIP from the same source folder through the existing CI workflow.
- [x] Inspect the downloaded artifact, nested archive, file inventory and ZIP CRC.
- [x] Confirm internal version 0.3.1 and recovery protocol is present.
- [x] Updated the same package manifest lineage to POINT-0/046 / CURRENT-096; internal version advanced to 0.3.2 without changing Stable ID or canonical ZIP filename.
- [x] Fresh exact-head paired audit/conformance passed on tested SHA c6af49386493f5c542336d54511f66085c1b7906.
- [x] Read back the exact-head artifact receipt, ZIP hash, size, inventory and test output: run 40507481687; nested ZIP 19,242 bytes; SHA-256 861be3d9998e96c8588d03642f70d01a6e2060b7b5056f45ef50008fc6f61da4; 8 files; ZIP CRC PASS; 16/16 CI tests PASS.
- [ ] Resolve the intentional filename-vs-internal-version label discrepancy without breaking canonical filename continuity.
- [ ] Import into a genuinely independent AI host with no prior chat context; reconstruct separately from IN and OUT.
- [ ] Negative controls, independent read-back and cold restart/persistence.
- [ ] Preserve unresolved identity/parent conflicts and all other open gaps.

This checkpoint does not claim the new exact-head ZIP is built until the workflow for the commit containing CURRENT-096 completes. Actual independent-host acceptance remains OPEN / NOT RUN. NEXT-051 remains the sole active queue; do not create NEXT-052.


## Exact verified v0.3.2 archive receipt — run 40507481687
- Tested source SHA: `c6af49386493f5c542336d54511f66085c1b7906`; paired Living Architecture Audit and Portable RAHM Conformance both PASS on that same SHA.
- Workflow: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40507481687
- Artifact ID: `12735876293`; outer artifact wrapper 19,842 bytes, SHA-256 `39e11184ca4c3cb4a3255c8a2678af7b9d8057afe447b08d6dcd7a7d36df7722`.
- Downloaded and inspected nested canonical ZIP: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`, 19,242 bytes, SHA-256 `861be3d9998e96c8588d03642f70d01a6e2060b7b5056f45ef50008fc6f61da4`; ZIP CRC PASS; 8-file inventory; internal version 0.3.2; stable package ID unchanged.
- Starter tests succeeded in CI (16 tests); real independent-host acceptance remains NOT RUN.
- The tested SHA is the source revision for this receipt; later evidence-ledger commits do not alter the ZIP bytes. Do not claim the external host gate passed.
