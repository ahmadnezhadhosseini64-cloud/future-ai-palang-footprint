# CURRENT-094 — Starter ZIP in-place update checkpoint

- Root: [POINT-0/044](./GPT6-RAHM-USER-POINT-0-20261027-044-STARTER-ZIP-INPLACE-UPDATE.md)
- Chain: POINT-0/044 → IN-082 → OUT-081 → EVT-0219 → CURRENT-094 → NEXT-051
- Existing package line: `prototype/haif-gpt6-starter/`, stable IDs preserved, source currently v0.3.1.
- Canonical archive filename to replace/refresh: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip` (legacy filename retained deliberately; not a separate version ZIP).
- Build workflow: must build this archive from the existing starter source directory and upload it with the same artifact name.
- Completed: registered point/input/output/event/checkpoint; documented distinction between source update and actual ZIP update.
- Verified: workflow run 40489753805 SUCCESS; same canonical ZIP filename rebuilt; size 19,042 bytes; SHA-256 3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83; 16/16 tests pass after fresh extraction; artifact downloaded and read back.
- Independent-host import, negative controls in the actual AI host, and restart persistence: NOT RUN.
- NEXT-051 remains the only active queue. No NEXT-052.
- Status: ZIP BUILD + ARTIFACT READ-BACK VERIFIED / HOST ACCEPTANCE OPEN / LIVING.


## Verified ZIP replacement receipt — run 40489753805

- Workflow result: SUCCESS on exact source commit `95e42fdffa0f0de956220403200c6f2390cfe645`.
- Run: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40489753805
- Artifact ID: `12726786662`; artifact name: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean`.
- Canonical filename preserved: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
- Internal package version: `0.3.1`; stable ID `HAIF-GPT6-PORTABLE-STARTER-20261025-004`; production ID `HAIF-G6PS-20261025-004`.
- Updated archive bytes: `18,815`; SHA-256: `3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83`.
- Inventory: 8 expected files including `INDEPENDENT_HOST_RECOVERY_PROTOCOL.md`; ZIP CRC/integrity check PASS; starter package unit tests PASS; exact-byte RAHM manifest scan PASS.
- Update mode: rebuilt the existing package under the same canonical filename and stable identity; no separate version-named ZIP.
- Real independent AI-host import/recovery and restart persistence: NOT RUN. Keep those gates OPEN.
- Status: ZIP BUILD + ARTIFACT READ-BACK VERIFIED; real-host acceptance NOT VERIFIED.


## Identity correction
POINT-0/043 is the 0+ production marker on canonical root 0. POINT-0/044 is retained as the 0.0 continuation anchor, not a second canonical zero. This resolves the label/identity conflict without deleting or renumbering the historical anchor.
