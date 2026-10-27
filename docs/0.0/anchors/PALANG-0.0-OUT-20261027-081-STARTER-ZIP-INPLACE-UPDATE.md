# OUT-081 — Starter ZIP in-place update execution record

- Parent: [IN-082](./PALANG-0.0-IN-20261027-082-STARTER-ZIP-INPLACE-UPDATE.md)
- Root: [POINT-0/044](./GPT6-RAHM-USER-POINT-0-20261027-044-STARTER-ZIP-INPLACE-UPDATE.md)
- Existing package source: `prototype/haif-gpt6-starter/`, currently version 0.3.1 and stable IDs HAIF-GPT6-PORTABLE-STARTER-20261025-004 / HAIF-G6PS-20261025-004.
- Historical original ZIP receipt: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`, SHA-256 `297b3b329143c4b99f55373db0c4bb97896b0e484253622e63eeb32a4429f164`, 16,266 bytes. This is historical evidence, not the updated archive's digest.
- Action: keep the same canonical filename and package identity while building replacement bytes from current starter source; do not publish a separate version-named ZIP.
- Required proof: exact file inventory, unit tests, archive SHA-256 and size, artifact read-back.
- Status: ZIP BUILD + ARTIFACT READ-BACK VERIFIED; real independent-host import remains NOT RUN.

- Current checkpoint: [CURRENT-094](./PALANG-0.0-CURRENT-20261027-094-STARTER-ZIP-INPLACE-UPDATE.md)
- Independent-host protocol: [repository protocol](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Package manifest: [manifest.json](../../../prototype/haif-gpt6-starter/manifest.json)

- RAHM export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)

- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- ZIP build receipt: VERIFIED — 19,042 bytes, SHA-256 3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83, 16/16 tests PASS after fresh extraction. Acceptance gates still OPEN / NOT VERIFIED for real independent-host import and restart persistence.

- Living mother reference: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)


## Final archive receipt

- Exact build commit: `95e42fdffa0f0de956220403200c6f2390cfe645`.
- Successful run: [40489753805](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40489753805).
- Artifact ID: `12726786662`.
- Same canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
- Current ZIP size: 19,042 bytes.
- Current ZIP SHA-256: `3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83`.
- Package unit tests PASS; ZIP CRC PASS; 8-file inventory PASS; exact-byte manifest scan PASS.
- The old digest `297b3b329143c4b99f55373db0c4bb97896b0e484253622e63eeb32a4429f164` remains historical and is not reused.
- Real independent-host import and restart persistence remain OPEN / NOT RUN.


## Verified current archive receipt

- Workflow: [40489753805](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40489753805) — SUCCESS.
- Archive filename: haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip (same canonical filename retained).
- Internal package version: 0.3.1; stable ID HAIF-GPT6-PORTABLE-STARTER-20261025-004.
- Size: 19,042 bytes; SHA-256: 3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83.
- Fresh extraction: 16/16 tests PASS; ZIP CRC PASS; 8-file inventory PASS.
- Real independent-host import and restart persistence: OPEN / NOT RUN.
