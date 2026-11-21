# CURRENT-125 — نقطهٔ جاری و وضعیت تحویل آخرین نسخه

- Status: ACTIVE / LIVING / POINT-0/072 REGISTERED / PACKAGE REBUILD REQUIRED / HOST ACCEPTANCE OPEN
- Parent: [CURRENT-124](PALANG-0.0-CURRENT-20261121-124-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md)
- Point: [POINT-0/072](GPT6-RAHM-USER-POINT-0-20261121-072-CURRENT-CHAT-ANCHOR-0PLUS.md)
- Input: [IN-115](PALANG-0.0-IN-20261121-115-CURRENT-CHAT-ANCHOR.md)
- Output: [OUT-114](PALANG-0.0-OUT-20261121-114-CURRENT-CHAT-ANCHOR.md)
- Event: [EVT-0291](../../architecture/BEHAVIOR-TRACE/EVT-0291-SET-CURRENT-POINT-AND-LATEST-DELIVERY-2026-11-21.md)
- Time: [TIME-BINDING-EVT-0291](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0291-SET-CURRENT-POINT-AND-LATEST-DELIVERY-2026-11-21.md)
- Master: [سند مرجع مادر](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Sole queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Confirmed state
- Repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint; default branch main; authenticated connection reports push permission.
- Parent checkpoint: CURRENT-124; previous canonical point: POINT-0/071.
- Latest pre-registration main HEAD observed: 7e68d94094096da263569625b6422e06a5d6988d.
- Latest prior package receipt: internal 0.4.3, canonical ZIP 238096 bytes, SHA-256 6cb016339822274586187b01e7fde74ec6623594167be2196d71c1d3959e0d38, 18 files, CRC PASS, extracted tests 24/24 PASS; built from source commit adde4cd8859e94a3f44083dd91f7d549ef684cc8.
- Paired master in that package: 1.7.77. Current repository master is 1.7.78; package rebuild and exact-head verification required.
- Sole active queue remains NEXT-051. Do not create NEXT-052.

## Open gates
Package rebuild on exact new HEAD; paired master digest; artifact round-trip; fresh-host import; independent IN/OUT reconstruction; host OAuth authorization; private durable workspace; broker/worker and repository read-back; restart persistence; second-host acceptance; live/idle capture; graph collision and ambiguous-parent triage; CURRENT-065/CURRENT-066 adjudication; Issues #20 and #21.

## Acceptance rule
Repository registration, package build, extracted tests, exact-byte artifact read-back and independent host acceptance are separate statuses. No gate is PASS without its direct evidence.
