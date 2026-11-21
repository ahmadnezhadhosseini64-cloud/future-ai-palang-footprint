# EVT-0297 — رفع ناسازگاری نخستین اجرای میزبان تازه

- Status: RECORDED / OWNER-APPROVED / REPAIR-MERGED / MAIN-READBACK-VERIFIED / TIME-BOUND
- Parent continuation: POINT-0/077 → CURRENT-130 → EVT-0297 → TIME-BINDING-EVT-0297 → NEXT-051
- Scope: first-run one-message GPT host bootstrap only
- Canonical active file: `prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA.md`
- Preserved original: `prototype/haif-gpt6-starter/ONE_MESSAGE_HOST_BOOTSTRAP_FA-ORIGINAL-POINT-074-2026-11-21.md`
- Time binding: [TIME-BINDING-EVT-0297](TIME-BINDING-EVT-0297-FIRST-RUN-HOST-BOOTSTRAP-COMPATIBILITY-REPAIR-2026-11-21.md) — Git UTC 2026-11-21T14:08:03Z / Tehran 2026-11-21T17:38:03+03:30.
- Original bootstrap blob SHA before repair: `0cc04f71881e3678e1184f90889785c3f5514549`
- Original snapshot commit on repair branch: `98b8e75685705f392e4c631dc78f46dea5becdde`
- Corrected active bootstrap blob SHA on repair branch: `8065cb7ccaf9aab58227ecc2e698d5fb5e008625`
- Repair branch: `fix/first-run-host-bootstrap-current-chain`
- Parent main HEAD at branch creation: `c8734674cb0016e81962105841318d472103a968`

## What failed

The active one-message bootstrap still identified the current continuation as POINT-0/074 → IN-117 → OUT-116 → EVT-0293 → CURRENT-127, declared living mother 1.7.82, and directed the new host to fetch old anchor paths. At the time of this repair, the repository's verified current continuation was POINT-0/077 (0++) → IN-120 → OUT-119 → EVT-0296 → TIME-BINDING-EVT-0296 → CURRENT-130 → NEXT-051, with living mother 1.7.84.

This is a first-run source-selection incompatibility: a genuinely fresh host following the active startup message could retrieve an obsolete chain and report an incorrect current checkpoint. The defect is in stale bootstrap pointers, not evidence that OAuth, workspace creation or external host recovery has succeeded or failed.

## Owner-approved correction

The owner explicitly authorized repairing the first-run incompatibility while preserving both the former working version and the incompatibility evidence. The repair therefore:
1. Preserves the exact pre-repair active bootstrap as a separate immutable historical copy; its original blob SHA is recorded above.
2. Updates the active bootstrap's current chain, canonical read set, checkpoint, event/time references and living-master version to the verified POINT-0/077 / CURRENT-130 / 1.7.84 state.
3. Keeps POINT-0/076 and CURRENT-129 as historical parent context, not as the current checkpoint.
4. Keeps NEXT-051 as the sole governing queue; no parallel project or NEXT queue is created.
5. Requires new-host execution to verify the actual HEAD and release receipt; this documentation repair does not claim destination OAuth, workspace, package exact-head verification or HOST-RECOVERED.

## Compatibility acceptance

- [x] Original active bootstrap preserved byte-for-byte in a separate historical file.
- [x] Active bootstrap top-level chain and current master target updated.
- [x] Repair linked to existing POINT-0/077 → CURRENT-130 → NEXT-051 lineage.
- [x] Pull request #65 merged to main.
- [x] Main-branch read-back of all changed files.
- [x] Portable ZIP rebuilt and verified against exact merged source HEAD; evidence-only follow-up commit equivalence verified.
- [ ] Fresh destination host follows corrected bootstrap and returns direct acceptance receipt.

## Status boundary

This event records the identified mismatch and a branch-level correction. It is not a claim of merged-to-main, package-verified or host-recovered status. The historical failure remains part of the permanent lineage and must not be deleted or rewritten.


## Exact-source package and CI verification

- Portable conformance workflow: [Run 44912345970](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44912345970) — SUCCESS.
- Living Architecture Audit: [Run 44912346031](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44912346031) — SUCCESS.
- Cross-Layer Integrity Gate: [Run 44912346113](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/44912346113) — SUCCESS.
- Package build source SHA: `a1ddf3ffff931efebdd28e42b78b5868cb6e9869`.
- Main HEAD read after the Evidence Gate follow-up: `0ee05e21da72b9ea5cb7ce457d1042c418945356`; comparison confirms the only intervening change was `evidence/evidence-gate-44912345887.txt`, so the package source and paired master are byte-equivalent to that current HEAD.
- Canonical ZIP: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`; internal package version `0.4.5`; size `249028` bytes; SHA-256 `84168f0aa74cef377fc7085aca646bdd3c2d7099a61fc21d425968f81908a3ec`.
- Extracted tests: `24/24 PASS`; ZIP CRC/integrity, source-byte read-back, downloaded-artifact round-trip and paired living-master inclusion/byte-match: PASS.
- Durable latest-verified release: [haif-latest-verified](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified).
- Artifact upload ID: `14710546447`.
- Independent destination-host OAuth, workspace creation, restart and HOST-RECOVERED acceptance remain OPEN / NOT RUN; package verification does not close them.
