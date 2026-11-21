# QUARANTINED_DUPLICATE_ID_NONCANONICAL — CURRENT-125 — ثبت نقطهٔ جاری و تحویل آخرین نسخه

- Status: QUARANTINED_DUPLICATE_ID_NONCANONICAL; canonical point/input/output/current records use the earlier CURRENT-CHAT-ANCHOR path set.nt: [CURRENT-124](PALANG-0.0-CURRENT-20261121-124-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md).
- Point: [POINT-0/072](GPT6-RAHM-USER-POINT-0-20261121-072-SET-CURRENT-POINT-AND-LATEST-DELIVERY.md)؛ ادامهٔ همان ریشهٔ canonical POINT-0.
- Input: [IN-115](PALANG-0.0-IN-20261121-115-SET-CURRENT-POINT-AND-LATEST-DELIVERY.md)
- Output: [OUT-114](PALANG-0.0-OUT-20261121-114-SET-CURRENT-POINT-AND-LATEST-DELIVERY.md)
- Event: [EVT-0291](../../architecture/BEHAVIOR-TRACE/EVT-0291-SET-CURRENT-POINT-AND-LATEST-DELIVERY-2026-11-21.md)
- Time: [TIME-BINDING-EVT-0291](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0291-SET-CURRENT-POINT-AND-LATEST-DELIVERY-2026-11-21.md)
- Master: [سند مرجع مادر](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Sole queue: [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Canonical chain
POINT-0/072 → IN-115 → OUT-114 → EVT-0291 → TIME-BINDING-EVT-0291 → CURRENT-125 → NEXT-051

## Reconciliation
POINT-0/071 and CURRENT-124 remain preserved. EVT-0290 remains mirror-only and is not reused. The living master is advanced to 1.7.79. NEXT-051 remains the sole active queue.

## Package and host gates
The last previously verified ZIP is internal 0.4.3 with 18 files, 238096 bytes, SHA-256 6cb016339822274586187b01e7fde74ec6623594167be2196d71c1d3959e0d38, CRC PASS and 24/24 extracted tests on source commit adde4cd8859e94a3f44083dd91f7d549ef684cc8, paired with master 1.7.77. It is not a fresh package paired with the updated master. Rebuild and exact-current-head RAHM/Audit are required. Independent host import, restart persistence and automatic capture remain OPEN / NOT RUN / NOT VERIFIED.


## Duplicate identifier reconciliation
This later parallel file set reused POINT-0/072, IN-115, OUT-114 and CURRENT-125. It is preserved for forensic history but is not canonical. The earlier registered CURRENT-CHAT-ANCHOR path set is canonical; its event is uniquely EVT-0291 because EVT-0290 was already assigned to the mirror-only event.
