# EVT-0210 — POINT-0/038 exact-SHA validation and manifest repair

- Stable ID: HAIF-EVT-0210-POINT-0-038-EXACT-SHA-VALIDATION-20261027
- Production ID: EVT-0210
- Version: 1.0.0
- Status: REGISTERED / ACTIVE / LIVING / EVIDENCE RECORDED
- Root: [POINT-0/038](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261027-038-TEMPORARY-GAP-COVER-AND-GOAL-EXECUTION.md)
- Current checkpoint: [CURRENT-087](../../0.0/anchors/PALANG-0.0-CURRENT-20261027-087-GOAL-EXECUTION-WITH-TEMPORARY-COVER.md)
- Prior decision event: [EVT-0209](./EVT-0209-TEMPORARY-GAP-COVER-AND-GOAL-EXECUTION-2026-10-27.md)

## Exact tested source

- Tested SHA: df89fd802bb3142611a719e0e22b2d5ad03a420f
- Living Architecture Audit: [run 40448952074](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40448952074) — SUCCESS.
- Portable RAHM Conformance and Digest Evidence: [run 40448952045](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40448952045) — SUCCESS.
- Audit artifact: 12708664966; digest sha256:dda435bb82986732b09fe24105721c23604b8ae01dd3e1b2ea1fda147a7b4b03.
- Conformance evidence artifact: 12709651834; digest sha256:a27b70fd925875157523d2e1355b22cd51d52eeb5652ca5cc206df70ccd666e8.
- Portable package artifact: 12708999686; digest sha256:e411b86f42d2a8bf019a19f23d73731f9f6bb0132df4bb5c84634bed6e581bc9.

## Verified audit facts on that SHA

- Structural repository checks: PASS.
- Live current pointer: SCOPED_CONSISTENT; no winner selected by numeric order. Overlay recovery remains CURRENT-066; global project pointer is CURRENT-087.
- Missing local links: 0.
- Ambiguous parent edges: 0; unresolved parent edges: 2.
- Stable-ID groups: 23; 22 reviewed, 1 open.
- Production-ID groups: 68; 2 reviewed, 66 open.
- Reference-ID groups: 5; all 5 open.
- Event-number groups: 41; 38 reviewed, 3 open.
- Exact-content duplicate groups: 11, preserved for review.
- Timestamp normalization: 2,935 strings normalized and paired UTC/Tehran; 0 ambiguity/parse errors.
- Local runtime, IN/OUT independent recovery, host-adapter tests and portable starter-engine tests passed in CI. These are repository/CI tests, not actual external interactive-host acceptance.

## Failure and correction preserved

An earlier conformance run, [40448512567](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40448512567), failed the exact-byte SHA-256 scan because NEXT-051 had been updated while the portable export manifest still carried its previous digest. The file was not rolled back and the gap was not hidden: the manifest's recorded blob/digest was reconciled to the actual repository bytes, then conformance passed on tested SHA df89fd802bb3142611a719e0e22b2d5ad03a420f.

## Boundary

The tested SHA is the exact source for the two successful runs. Subsequent Evidence Gate receipt commits may advance main; those commits are not misrepresented as the tested source. Actual independent interactive-host import, restart/recovery, persistence and round-trip remain NOT RUN until direct target-host receipts exist.
