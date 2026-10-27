# CURRENT-097 — ادامهٔ 0.0: یک بستهٔ اولیه، یک هویت، یک نام ZIP

- Stable ID: HAIF-CURRENT-097-SAME-STARTER-ZIP-CONTINUITY
- Production ID: G6IP-CURRENT-097
- Version: 1.0.0
- Status: ACTIVE / LIVING / IN PROGRESS / NOT COMPLETE
- Chain: POINT-0/047 → IN-085 → OUT-084 → EVT-0222 → CURRENT-097 → NEXT-051.
- Living master: [سند مرجع مادر مدل اولیه](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Existing package source: [HAIF starter](../../../prototype/haif-gpt6-starter/README.md)
- Recovery protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL.md](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md)
- Active queue: [NEXT-051](./PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Verified versus open
- VERIFIED: CI built the established canonical ZIP filename from the same package identity at internal version 0.3.2; 19,242 bytes; SHA-256 `861be3d9998e96c8588d03642f70d01a6e2060b7b5056f45ef50008fc6f61da4`; eight members; 16/16 tests passed.
- OPEN: internal version declaration mismatch in the downloaded v0.3.2 ZIP; a newer manifest value alone is not a new verified archive.
- OPEN: fresh build of reconciled source on one exact final SHA, download, extraction, byte/hash/inventory read-back and tests.
- NOT RUN: actual import to a separate AI host, independent IN/OUT recovery, negative controls, and restart persistence.

Permanent package rule: one stable package ID, one canonical archive filename, one source root. Update the source, rebuild the same ZIP name, produce a new exact-byte receipt, and preserve previous hashes as historical evidence. NEXT-051 remains the only active queue; do not create NEXT-052.
