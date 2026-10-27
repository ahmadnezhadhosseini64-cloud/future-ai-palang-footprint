# OUT-081 — Starter ZIP in-place update execution record

- Parent: [IN-082](./PALANG-0.0-IN-20261027-082-STARTER-ZIP-INPLACE-UPDATE.md)
- Root: [POINT-0/044](./GPT6-RAHM-USER-POINT-0-20261027-044-STARTER-ZIP-INPLACE-UPDATE.md)
- Existing package source: `prototype/haif-gpt6-starter/`, currently version 0.3.1 and stable IDs HAIF-GPT6-PORTABLE-STARTER-20261025-004 / HAIF-G6PS-20261025-004.
- Historical original ZIP receipt: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`, SHA-256 `297b3b329143c4b99f55373db0c4bb97896b0e484253622e63eeb32a4429f164`, 16,266 bytes. This is historical evidence, not the updated archive's digest.
- Action: keep the same canonical filename and package identity while building replacement bytes from current starter source; do not publish a separate version-named ZIP.
- Required proof: exact file inventory, unit tests, archive SHA-256 and size, artifact read-back.
- Status: source/workflow update is not equal to archive replacement; await workflow receipt. Real independent-host import remains NOT RUN.

- Current checkpoint: [CURRENT-094](./PALANG-0.0-CURRENT-20261027-094-STARTER-ZIP-INPLACE-UPDATE.md)
- Independent-host protocol: [repository protocol](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md)
- Package recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Package manifest: [manifest.json](../../../prototype/haif-gpt6-starter/manifest.json)

- RAHM export manifest: [EXPORT_MANIFEST.json](../../portable/RAHM/EXPORT_MANIFEST.json)

- Sole active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Acceptance gates: OPEN / NOT VERIFIED — fresh ZIP build receipt pending; real independent-host import NOT RUN; restart persistence NOT RUN.

- Living mother reference: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)


## Final archive receipt

- Exact build commit: `fa930e8e895eae7dea3f7eb13449321c5658a2c2`.
- Successful run: [40489299348](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40489299348).
- Artifact ID: `12726786662`.
- Same canonical ZIP filename: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`.
- Current ZIP size: 18,815 bytes.
- Current ZIP SHA-256: `b3429acaa5d33fb93dec7ad0ba8c1cdf233fbb28b8839794eea74457013e1309`.
- Package unit tests PASS; ZIP CRC PASS; 8-file inventory PASS; exact-byte manifest scan PASS.
- The old digest `297b3b329143c4b99f55373db0c4bb97896b0e484253622e63eeb32a4429f164` remains historical and is not reused.
- Real independent-host import and restart persistence remain OPEN / NOT RUN.
