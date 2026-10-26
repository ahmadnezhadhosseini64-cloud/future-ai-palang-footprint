# CURRENT-084 — Deep Excavation and Initial Model Completion

- Stable ID: HAIF-CURRENT-084-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION-20261026
- Production ID: HAIF-C084
- Version: 1.0.0
- Status: ACTIVE / LIVING / OPEN / EXECUTION REQUIRED
- Root: [POINT-0/036](./GPT6-RAHM-USER-POINT-0-20261026-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md)
- Chain: [IN-072](./PALANG-0.0-IN-20261026-072-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md) → [OUT-071](./PALANG-0.0-OUT-20261026-071-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION.md) → [EVT-0206](../../architecture/BEHAVIOR-TRACE/EVT-0206-POINT-0-036-DEEP-EXCAVATION-INITIAL-MODEL-COMPLETION-2026-10-26.md)
- Previous execution checkpoint: [CURRENT-083](./PALANG-0.0-CURRENT-20261026-083-IDENTIFIER-AND-PARENT-GRAPH-REPAIR.md)
- Canonical time binding: [POINT-0/036 chain time binding](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-POINT-0-036-CHAIN-2026-10-26.md)
- Existing active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Live repository observations before this checkpoint
- Main was read back at SHA `a406683307d5b90b8302bd40a34801723a8b5c00`.
- `scripts/build_historical_graph_manifest.py` imports both `graph_identifier_roles.metadata_header` and `parent_edge_resolution.resolve_parent_target`.
- Unit tests exist for both helper modules, and the living audit workflow contains explicit unittest and py_compile steps for them. Therefore the earlier CURRENT-083 statement that these helpers were not yet wired into CI is stale and must be reconciled with current receipts.
- Recent workflow receipts on this head include successful Pending Registration Drain, Production Detection Safety Net and Reconciliation Watchdog. These are not a substitute for the living graph audit and portable RAHM conformance.
- The latest known graph-audit baseline from the prior CURRENT-083 is 4 missing local links, 2 unresolved parent edges, 0 ambiguous parent edges, 63 Stable-ID groups, 92 Production-ID groups, 7 Reference-ID groups and 41 event-number groups. Treat these as a historical baseline only, not current counts.

## Path A — executable initial model
- Local runtime and portable RAHM package must build and pass integrity/import/export/recovery tests on the same exact SHA.
- Independent GPT-host import, restart, round-trip, automatic capture, background runtime and durable host persistence are NOT RUN until real destination receipts are supplied.
- MASTER remains governing authority; RAHM is the validation environment; CHILD promotion requires independent evidence and explicit acceptance.

## Path B — repository excavation and graph repair
- Rerun the living graph audit after the identifier parser and parent resolver changes.
- Read the generated audit artifact back; record exact SHA, digest and current counts.
- Review the 4 historical missing-link findings and fix only links whose intended target is evidenced.
- Adjudicate Stable-ID, Production-ID, Reference-ID and event-number groups in small batches, retaining role decisions and source hashes.
- Reconcile CURRENT-065/CURRENT-066 lineage using provenance and consumers, not number ordering.
- Keep unresolved and ambiguous cases OPEN; preserve NEXT-051 and do not create NEXT-052.

## Verified audit receipt — prior exact head
- Living Architecture Audit run [40347006195](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40347006195) passed on exact SHA cf877f9a84d767bb6f0f3566b90efe4fd5dcd83c; artifact ID 12661441741, digest sha256:3e937e32efd25bb71db2e471a49f8c7b2961302ce2ee4bb0e514bef824ac2ab8.
- In that run: helper tests passed (5 parent resolver tests and 4 metadata-header tests); compile checks passed; local Markdown links missing = 0; manifest decode errors = 0; unresolved parent edges = 2; ambiguous parent edges = 0.
- Manifest semantic collision classes: 23 Stable-ID groups (1 unreviewed/open), 68 Production-ID groups (66 unreviewed/open), 5 Reference-ID groups (5 open), 41 event-number groups (3 unreviewed/open), 11 exact-content duplicate groups.
- The separate raw graph report still showed 63/92/7/41 raw collision counts and flagged two generated Python bytecode files as decode errors. This revealed that the raw audit was still scanning body references and bytecode unlike the canonical manifest.
- Corrective change on a later commit: scripts/audit_historical_0_0_graph.py now excludes __pycache__/.pyc and derives identifier/parent definitions from the bounded metadata header. This correction is awaiting exact-head rerun; do not mark it validated until that run finishes.

- Conformance failure and correction: Portable RAHM Conformance run 40347913506 failed because the changed file scripts/audit_historical_0_0_graph.py no longer matched the pinned EXPORT_MANIFEST.json digest/blob. The manifest entry has now been refreshed to the exact script SHA256 and Git blob SHA. This is a corrected integrity mismatch, not a code-test failure; exact-head conformance must pass before it is marked resolved.

## Latest exact-head audit and portable conformance receipt
- Tested SHA: bd6da9f592850ad2b9274de54ebfa247f765ba59.
- Living Architecture Audit [40348139100](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40348139100): SUCCESS. Artifact 12663235201; digest sha256:8835a22653c1a78d03af1283bc7999d27549f70ff932e000a1c0aa72c8a9900b.
- Portable RAHM Conformance [40348138992](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40348138992): SUCCESS on the same SHA. Evidence artifact 12661674025; digest sha256:6f31e2bd7ef2a2e79e9a17522caf951b010aed700068d5ffdccad3407e16b57a. Package artifact 12661367970; digest sha256:72dabfa9a4a7a5eab004ac2c223c80403b4dcc3813a9a41903f80418763e1eac.
- Verified outputs: 0 decode errors; 0 missing local Markdown links; 23 Stable-ID collision groups; 68 Production-ID groups; 5 Reference-ID groups; 41 event-number groups; 11 exact-content duplicate groups. Parent edges: 79 declared, 2 unresolved, 0 ambiguous. Two unresolved edges both point to the missing standalone HAIF-CORE-MASTER-CHILD-RAHM-2026-09-15-001 artifact; do not fabricate or substitute it.
- Unit checks: current-pointer suite 8 passed; semantic-role suite 11 passed; parent resolver 5 passed; metadata-header 4 passed; starter engine 13 passed; host-adapter simulated tests passed; py_compile passed. Time normalization audit: 4,798 files scanned, 2,869 timestamp strings normalized and paired, 0 parse/ambiguity errors, 0 Tehran offset/value failures, 0 UTC-label failures.
- Portable package verification: 50 exact-byte manifest files matched; 127 live-reference files scanned; EXACT_BYTE_SHA256_SCAN=PASS; LIVE_REFERENCE_SHA256_SCAN=PASS; PORTABLE_PACKAGE_BUILD=PASS; package contains 178 files, 634,386 bytes, SHA256 acf1e2c37a3eed4854a889e8667067b111d3b0e1994f732569a692a56952c254.
- Scope limitation: these are repository CI and package conformance results, not proof of an independent interactive GPT host import, restart, durable persistence or live-chat producer. Path A external-host acceptance remains NOT RUN.

## Acceptance gate
CURRENT-084 stays OPEN until the exact-head audit and portable conformance have both completed, their logs/artifacts have been read back, and graph changes are reconciled in the master/index/queue. External-host acceptance remains a separate gate.

## Latest verification refresh — code head 4d41fa60c1ee360cccea05164d61152ac79cc577
- Living Architecture Audit [40348437372](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40348437372) — SUCCESS on this code SHA; artifact 12661729460, digest sha256:aefe553328dca7fb4aa848f5e0851fb6d7b2fa84a64783a20584fb260579a6f7.
- Portable RAHM Conformance [40348437106](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40348437106) — SUCCESS on the same SHA. Evidence artifact 12662357802, digest sha256:d921e6864296d36b8e1f3c4db8fa52fb89e9ac0789d283aa7dacfaa1e02c1d0b; package artifact 12662282368, digest sha256:3f9b016ddf19b4b75b8481f7f652194d7811c3b8d981c70bd38065f0d81c9733. Package SHA256 7d81087bf66f0d3f20ed39cb1d79b2ce2ddec364ad478b18414fd654299be676; 178 package files, 127 live references, exact-byte and live-reference scans PASS.
- Final raw audit after the scanner fix: decode_errors=0; local_markdown_links_missing=0; Stable-ID=23, Production-ID=68, Reference-ID=5, event-number=41, exact-content duplicates=11; 79 declared parent edges, 2 unresolved, 0 ambiguous. Unresolved master-artifact gap remains OPEN.
- The subsequent main commit da3b1e726aea53807e1e2676eeac3e4872af5879 only adds the successful Evidence Gate receipt file; it does not modify source code. A final post-registration audit/conformance is being triggered by this checkpoint refresh.
