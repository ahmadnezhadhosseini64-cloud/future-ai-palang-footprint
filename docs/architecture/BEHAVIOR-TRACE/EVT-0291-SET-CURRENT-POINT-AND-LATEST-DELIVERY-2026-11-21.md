# EVT-0291 — ثبت نقطهٔ جاری و درخواست تحویل آخرین نسخه — 2026-11-21

- Stable ID: PALANG-EVT-0291-SET-CURRENT-POINT-AND-LATEST-DELIVERY-2026-11-21
- Production ID: HAIF-EVT-0291
- Version: 1.0.0
- Type: USER-AUTHORIZED-CONTINUATION / CANONICAL-ROOT-EXTENSION
- Point: [POINT-0/072](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261121-072-CURRENT-CHAT-ANCHOR-0PLUS.md)
- Input: [IN-115](../../0.0/anchors/PALANG-0.0-IN-20261121-115-CURRENT-CHAT-ANCHOR.md)
- Output: [OUT-114](../../0.0/anchors/PALANG-0.0-OUT-20261121-114-CURRENT-CHAT-ANCHOR.md)
- Time binding: [TIME-BINDING-EVT-0291](./TIME-BINDING-EVT-0291-SET-CURRENT-POINT-AND-LATEST-DELIVERY-2026-11-21.md)
- Current: [CURRENT-125](../../0.0/anchors/PALANG-0.0-CURRENT-20261121-125-CURRENT-CHAT-ANCHOR.md)
- Sole queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

## Observation
The owner explicitly instructed: “همین جا رو نقطه ۰ کن و اتصال بده ب باقی نقاط و آخرین نسخه رو بده بهم الان”.
Exact user-message time: UNKNOWN / UNVERIFIED; commit time must not be substituted for message time.

## Action
Register this as POINT-0/072 on the existing canonical POINT-0 root. Preserve POINT-0/071 → IN-114 → OUT-113 → EVT-0289 → TIME-BINDING-EVT-0289 → CURRENT-124. Append IN-115 / OUT-114 / EVT-0291 / TIME-BINDING-EVT-0291 / CURRENT-125. EVT-0290 is already a mirror-only event and is not reused. Keep NEXT-051 as the sole queue; do not create NEXT-052. Update the living master to 1.7.79.

## Package evidence carried forward
Last verified package observed: internal 0.4.3; canonical ZIP 238096 bytes; SHA-256 6cb016339822274586187b01e7fde74ec6623594167be2196d71c1d3959e0d38; 18 files; CRC PASS; extracted tests 24/24 PASS; source commit adde4cd8859e94a3f44083dd91f7d549ef684cc8; paired master 1.7.77. This is prior verified evidence, not a fresh build against the current master.

## Status
This event records owner authorization and repository continuation. It does not claim a new ZIP build, exact-current-head RAHM, real independent-host acceptance, automatic message capture or restart persistence.
