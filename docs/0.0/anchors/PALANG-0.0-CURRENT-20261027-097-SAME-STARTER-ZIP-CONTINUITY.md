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
- FIXED IN SOURCE: the previous audit found a stale test expecting v0.3.2 while manifest declared v0.3.3; README and recovery protocol also lagged. Source files have been aligned to v0.3.3, supersedes v0.3.2.
- OPEN: fresh build of reconciled source on one exact final SHA, download, extraction, byte/hash/inventory read-back and tests; current paired workflows must finish.
- NOT RUN: actual import to a separate AI host, independent IN/OUT recovery, negative controls, and restart persistence.

Permanent package rule: one stable package ID, one canonical archive filename, one source root. Update the source, rebuild the same ZIP name, produce a new exact-byte receipt, and preserve previous hashes as historical evidence. NEXT-051 remains the only active queue; do not create NEXT-052.


## Hard audit evidence and correction

- Exact failing run: [Living Architecture Audit 40515730267](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/40515730267). The canonical ZIP rebuild step succeeded and uploaded artifact `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean`; source tests failed 1 of 16 due to test expecting 0.3.2 while manifest was 0.3.3.
- Corrected source: README title/version, recovery protocol version and manifest-version test now align to 0.3.3; test expects `supersedes=0.3.2`.
- New exact-head CI and a newly downloaded/extracted canonical ZIP receipt must pass before this package is marked READY for transfer. Independent host acceptance is a separate open gate.
