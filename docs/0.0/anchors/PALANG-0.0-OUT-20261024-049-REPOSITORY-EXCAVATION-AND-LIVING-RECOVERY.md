# OUT-049 — Repository Excavation and Living Recovery

- Stable ID: `G6IP-RAHM-OUT-049-20261024`
- Production ID: `G6IP-OUT-049`
- Version: 1.0.1
- Status: REGISTERED / READ-BACK VERIFIED; scoped checks passed; global audit remains REVIEW_REQUIRED.
- Parent input: [IN-050](./PALANG-0.0-IN-20261024-050-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY.md)
- Parent point: [User Point 0/006](./GPT6-RAHM-USER-POINT-0-20261024-006-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY.md)
- Event: [EVT-0159](../../architecture/BEHAVIOR-TRACE/EVT-0159-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY-2026-10-24.md)

## Verified repository excavation snapshot
- Repository: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`
- Inspected default-branch tree head: `7b3abd6de1014eebbc5ee54bf26b4ee0d09e2cca`.
- Latest inspected commit: `0104a0799a574cb78c5b121a0bcd9192b857ed51`, committed at UTC `2026-10-24T18:51:33Z`; Tehran equivalent `2026-10-24T22:21:33+03:30`. This is repository commit time, not exact user-message time.
- Portable manifest: version 1.3.6, 37 listed files; all 37 paths existed in the inspected tree.
- Portable conformance run [40122633966](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40122633966): workflow SUCCESS; valid schema fixture 0 errors; invalid fixture rejected with 4 errors; strict exact-byte SHA-256 scan PASS for the manifest as it existed at that run; limited IN/OUT checkpoint-link equivalence PASS; archive build PASS, 38 files, 208866 bytes, archive SHA-256 `c2770ea2aa10b67c2a0eaa5cb3975bbb1698a3c7cd3f9fabc15f39b73aded32e`. This is a CI artifact, not a clean AI-host import.
- Structural audit [40122633902](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40122633902): workflow SUCCESS but content result `REVIEW_REQUIRED`; 3,728 files including generated evidence; 5,506 local-link edges; 11 missing local links; 61 stable-ID collision groups (60 unreviewed); 88 production-ID collision groups; 7 reference-ID collision groups; 36 event-number collision groups; 13 ambiguous parent edges; 0 decode errors.
- Synthetic runtime/transfer harnesses [40122634043](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40122634043) and [40122633909](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40122633909) passed their declared CI checks. They do not establish real independent GPT host import, durable memory, or idle background execution.

## Architectural finding
The existing continuity rule in EVT-0158 is correct and must remain active: a new input links to the open NEXT; a delayed/missing visible response must not be represented as background execution; every durable milestone needs visible status; a new input must trigger repository read-back and resume from the latest valid checkpoint.

## Status
Repository excavation performed. Several repository and CI checks pass within their declared scope, while the global graph audit remains REVIEW_REQUIRED and full recovery/real-host gates remain OPEN. This output does not claim full architecture completion.


## Follow-up excavation and executed corrections — 2026-10-24
- Exact current repository tree contains Point 0/006 → IN-050 → OUT-049 → EVT-0159 → CURRENT-057 → NEXT-051; focused link check resolved all links. Earlier claim of missing files was withdrawn as a wrong-filename query error; no files were recreated on that premise.
- Independently read back 13 targeted chain/master/index/queue files; focused relative-link audit found zero broken destinations.
- Strict baseline [run 40124660624](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40124660624), commit `98435ad73b4b7ea9e4da94b9f5abba5af968b753`, manifest v1.4.6: 43/43 exact-byte digests matched; valid schema fixture 0 errors; invalid fixture rejected with 4 errors; limited IN/OUT checkpoint-link equivalence passed; archive 44 files / 224852 bytes / SHA-256 `475ff58474f10a4a75314c964302bac06f7ed15d47e31da1826c31bce293c50a`. This predates link/auditor corrections; final rerun required.
- Corrected six actual documentation links: five in the initial-model mother and the NEXT-034 link in EVT-0132. Corrected the historical graph auditor to ignore Markdown-looking links in Python fixtures as navigation links, while still scanning files for IDs/provenance.
- Added CI gate for Point 0/006 → IN-050 → OUT-049 → EVT-0159 → CURRENT-057 → NEXT-051 and master/index/queue. Post-fix workflow is pending.
- Pre-fix global audit [40124660609](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40124660609) reported 16 links (6 real docs, 10 Python-fixture false positives), 62 stable-ID collision groups (61 unreviewed), 88 production-ID collision groups, 7 reference-ID collision groups, 36 event-number collision groups, 13 ambiguous parents, and one ambiguous timestamp. Post-fix count is pending.
- Clean AI-host import, second-host import, full IN/OUT state reconstruction, actual persistence restart and idle/background execution remain OPEN / NOT VERIFIED.
