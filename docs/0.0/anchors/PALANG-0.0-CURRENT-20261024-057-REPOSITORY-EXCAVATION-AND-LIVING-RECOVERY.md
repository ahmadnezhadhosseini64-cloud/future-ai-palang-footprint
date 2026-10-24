# CURRENT-057 — Repository Excavation and Living Recovery

- Stable ID: `G6IP-RAHM-CURRENT-057-20261024`
- Production ID: `G6IP-CURRENT-057`
- Version: 1.0.1
- Status: REGISTERED / READ-BACK VERIFIED for the checkpoint and focused chain; post-fix global audit and strict manifest rerun pending. Host and full graph gates OPEN.
- Parent current: [CURRENT-056](./PALANG-0.0-CURRENT-20261024-056-OUTPUT-CONTINUITY-AND-RECOVERY.md)
- Point 0: [POINT-0/006](./GPT6-RAHM-USER-POINT-0-20261024-006-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY.md)
- Input: [IN-050](./PALANG-0.0-IN-20261024-050-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY.md)
- Output: [OUT-049](./PALANG-0.0-OUT-20261024-049-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY.md)
- Event: [EVT-0159](../../architecture/BEHAVIOR-TRACE/EVT-0159-REPOSITORY-EXCAVATION-AND-LIVING-RECOVERY-2026-10-24.md)
- First living master: [portable RAHM master](../../portable/RAHM/FIRST-LIVING-MASTER-PORTABLE-GPT6-HAIF.md)
- Prior open work preserved: [NEXT-050](./PALANG-0.0-NEXT-20261024-050-FULL-RECOVERY-AND-REAL-HOST-IMPORT.md), [NEXT-049](./PALANG-0.0-NEXT-20261024-049-REAL-HOST-TRANSFER-AND-GRAPH-AUDIT.md)
- New deterministic next: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Verified state at excavation
- Inspected tree head: `7b3abd6de1014eebbc5ee54bf26b4ee0d09e2cca`; latest inspected commit `0104a0799a574cb78c5b121a0bcd9192b857ed51`, UTC `2026-10-24T18:51:33Z`, Tehran `2026-10-24T22:21:33+03:30`.
- Manifest v1.3.6 listed 37 paths; all 37 were present in the inspected tree.
- Conformance [40122633966](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40122633966): declared scope PASS; schema valid 0 errors, invalid rejected with 4 errors, strict digest scan PASS, limited IN/OUT link/checkpoint equivalence PASS, package 38 files / 208866 bytes / SHA-256 `c2770ea2aa10b67c2a0eaa5cb3975bbb1698a3c7cd3f9fabc15f39b73aded32e`.
- Audit [40122633902](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40122633902): workflow SUCCESS, content `REVIEW_REQUIRED`; 3,728 files, 5,506 local links, 11 missing links, 61 stable-ID collision groups (60 unreviewed), 88 production-ID collision groups, 7 reference-ID collision groups, 36 event-number collision groups, 13 ambiguous parent edges.
- CPREL synthetic transfer checks passed declared CI scope; actual independent AI-host import is NOT RUN. Persistent memory and idle/background execution remain NOT VERIFIED.

## Continuity rule activated in the architecture
Every new input must be attached to the latest CURRENT and open NEXT after a repository read-back. If work cannot finish in the same turn, the response must explicitly state PARTIAL/BLOCKED, preserve the next step, and avoid implying invisible processing. New input creates a child branch; it does not cancel older open work.

## OPEN / LIVING
- Full canonical-state and evidence reconstruction independently from IN and OUT.
- Clean independent AI-host import and second-host import.
- Actual persistence after restart and idle/background execution.
- Repository-wide remediation: 11 missing links, 60 unreviewed stable-ID collision groups, 88 production-ID collision groups, 7 reference-ID collision groups, 36 event-number collision groups, 13 ambiguous parent edges.
- Rebuild and revalidate manifest/package after this checkpoint and all master/index/queue updates.
- Independently read back all new files and verify local links before claiming final registration.

## Recovery
Resume from NEXT-051 while keeping NEXT-050 and NEXT-049 open. Do not close any gate merely because it was written into this checkpoint.



## Latest excavation recheck — run 40124425936 / 2026-10-24
- Structural audit workflow completed, but content result remains `REVIEW_REQUIRED`: 3,757 files including generated evidence; 5,564 local-link edges; 16 missing links; 62 stable-ID collision groups (61 unreviewed); 88 production-ID collision groups; 7 reference-ID collision groups; 36 event-number collision groups; 13 ambiguous parent edges; 0 decode errors.
- Strict portable conformance run [40124425568](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40124425568) passed for manifest v1.4.2: schema valid fixture 0 errors, invalid fixture rejected with 4 errors, all expected file digests matched, limited IN/OUT checkpoint-link equivalence passed; package 44 files / 221380 bytes / SHA-256 `591377d03546e6f031ee98614b1c9fbd662dba08a15bc5c68b15bd918282f501`.
- These are repository/CI results only. Full IN/OUT state reconstruction, clean/second AI-host import, actual persistence restart and idle/background execution remain OPEN / NOT VERIFIED.


## Execution receipt — corrections made before advancing this checkpoint
- Read back Point 0/006, IN-050, OUT-049, EVT-0159, CURRENT-057, NEXT-051, portable master, manifest, foundational mother, inherited mother, canonical index and main queue. Focused local-link audit returned zero broken relative links in these target files.
- The first query's claim that chain files were missing was incorrect: it used guessed filenames. Exact canonical files exist and were read back. This correction is preserved as an audit-method lesson.
- Fixed five relative links in `docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md` and the actual NEXT-034 link in EVT-0132.
- Fixed historical graph auditor scope so Markdown-looking link examples embedded in Python test fixtures are not counted as documentation navigation links. Added CI gate `CURRENT_POINT_0_006_NEXT_051_CONTINUITY` to check the latest chain and master/index/queue surfaces.
- Pre-fix conformance run [40124660624](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40124660624) passed v1.4.6's 43 exact-byte file hashes, valid/invalid schema fixtures, limited IN/OUT checkpoint-link equivalence, and archive construction (44 files; 224852 bytes; SHA-256 `475ff58474f10a4a75314c964302bac06f7ed15d47e31da1826c31bce293c50a`). This is historical baseline evidence only; final post-edit rerun remains pending.
- Latest pre-fix global audit [40124660609](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40124660609) returned `REVIEW_REQUIRED`: 3,768 files, 5,564 local-link edges, 16 reported missing links (six real documentation links plus ten links embedded in Python fixture source), 62 stable-ID collision groups (61 unreviewed), 88 production-ID collision groups, 7 reference-ID collision groups, 36 event-number collision groups, 13 ambiguous parent edges, one ambiguous timestamp. Post-fix audit is pending; do not carry 16 forward as the new count until rerun.

## Still OPEN / NOT VERIFIED
- Full canonical-state reconstruction independently from raw IN and raw OUT, including evidence/failure/correction chain equality.
- Clean independent AI-host import and second AI-host import.
- Actual persistent memory after restart and idle/background execution.
- Individual adjudication of remaining missing links, identifier collisions, ambiguous parents and timestamp provenance.
- Final post-edit SHA-256 manifest reconciliation and package build receipt.

## Recovery instruction
Resume from NEXT-051. Do not create NEXT-052 merely to relabel unfinished work. Complete and evidence the current gates first; keep NEXT-049 and NEXT-050 independently OPEN.
