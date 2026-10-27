# CURRENT-098 — ادامهٔ 0.0: یک ZIP، بازخوانی بایت‌به‌بایت، آزمون بستهٔ استخراج‌شده

- Stable ID: HAIF-CURRENT-098-SAME-ZIP-READBACK-20261027
- Production ID: G6IP-CURRENT-098
- Version: 1.0.0
- Status: ACTIVE / LIVING / IN PROGRESS / NOT COMPLETE
- Chain: POINT-0/048 (0+ marker) → IN-086 → OUT-085 → EVT-0223 → CURRENT-098 → NEXT-051
- Living master: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Package source: [HAIF GPT-6 Portable Starter](../../../prototype/haif-gpt6-starter/README.md)
- Recovery protocol: [Independent Host Recovery Protocol](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## What is actually complete
- [x] Prior successful same-canonical-filename ZIP build receipt exists on run 40516397323 for source commit aab1654758d29a05edd240c754d780f3f35a3641.
- [x] Stable package ID and canonical ZIP filename remain unchanged.
- [x] Workflow hardening committed: exact archive is extracted, every required file is byte-compared to source, and tests execute from extracted ZIP.
- [ ] Fresh exact-head workflow result and new archive SHA-256.
- [ ] Download/read-back of the uploaded artifact and compare the contained canonical ZIP to the workflow receipt.
- [ ] Real independent-host import, independent IN/OUT reconstruction, negative controls and restart/persistence.

Do not promote this checkpoint to COMPLETE until the three open gates above have direct receipts. Do not create a new version-named ZIP or NEXT-052.
