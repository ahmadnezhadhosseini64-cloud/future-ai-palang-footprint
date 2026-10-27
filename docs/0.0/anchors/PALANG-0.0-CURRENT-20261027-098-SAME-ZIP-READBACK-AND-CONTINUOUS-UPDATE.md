# CURRENT-098 — ادامهٔ 0.0: یک ZIP، بازخوانی بایت‌به‌بایت، آزمون بستهٔ استخراج‌شده

- Stable ID: HAIF-CURRENT-098-SAME-ZIP-READBACK-20261027
- Production ID: G6IP-CURRENT-098
- Version: 1.0.0
- Status: ACTIVE / LIVING / IN PROGRESS / ZIP ARTIFACT ROUND-TRIP VERIFIED / REAL HOST NOT RUN
- Chain: POINT-0/048 (0+ marker) → IN-086 → OUT-085 → EVT-0223 → CURRENT-098 → NEXT-051
- Living master: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Package source: [HAIF GPT-6 Portable Starter](../../../prototype/haif-gpt6-starter/README.md)
- Recovery protocol: [Independent Host Recovery Protocol](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## What is actually complete
- [x] Prior successful same-canonical-filename ZIP build receipt exists on run 40516397323 for source commit aab1654758d29a05edd240c754d780f3f35a3641.
- [x] Stable package ID and canonical ZIP filename remain unchanged.
- [x] Workflow hardening committed: exact archive is extracted, every required file is byte-compared to source, and tests execute from extracted ZIP.
- [x] Fresh build receipt recorded for run 40518077494; exact canonical ZIP SHA-256 and byte count verified.
- [x] Workflow downloaded its uploaded artifact, compared the contained ZIP bytes/hash to receipt and reran 16 tests from the downloaded archive.
- [ ] Real independent-host import, independent IN/OUT reconstruction, negative controls and restart/persistence.

Do not promote this checkpoint to COMPLETE until the three open gates above have direct receipts. Do not create a new version-named ZIP or NEXT-052.


## Verified canonical ZIP build and artifact round-trip — run 40518077494

- Tested source commit: `b5e29697ec2733c9e9f3ff914525304b2fcb6914`.
- Run: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40518077494
- Uploaded artifact: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40518077494/artifacts/12740188113
- Artifact name: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean`; artifact wrapper: 19,903 bytes; artifact digest SHA-256 `8966f5c58517d1d2c032ae2fcdffb0dd12a1ad8a22f47981ed6b756c1b699d83`.
- ZIP inside artifact: `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`; internal version 0.3.3; 19,268 bytes; SHA-256 `fa226aab5a35a76c3f289b511566257a443821195ebdfdfb21f1cc093026e091`.
- Exact ZIP extracted and source bytes matched: PASS. Tests run from extracted ZIP: 16/16 PASS. Uploaded artifact was downloaded back by the workflow; the contained ZIP's byte count and SHA-256 matched the receipt, ZIP CRC/inventory passed, and tests ran again from the downloaded artifact: PASS.
- This proves the repository CI artifact round-trip for this run. It does NOT prove import into a real independent AI host; that gate remains NOT RUN.
