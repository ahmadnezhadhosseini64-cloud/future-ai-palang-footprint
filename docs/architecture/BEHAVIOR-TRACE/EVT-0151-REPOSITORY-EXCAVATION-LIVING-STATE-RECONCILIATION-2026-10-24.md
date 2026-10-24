# EVT-0151 — Repository Excavation and Living-State Reconciliation / خاک‌برداری مخزن و تطبیق وضعیت زنده

- Event ID / شناسهٔ رویداد: `EVT-0151`
- Stable ID / شناسهٔ پایدار: `PALANG-REPOSITORY-EXCAVATION-LIVING-STATE-RECONCILIATION-2026-10-24-0151`
- Production ID / شناسهٔ تولید: `G6IP-EVT-0151`
- Version / نسخه: `1.0.0`
- Request / درخواست: «خاکبرداری کن مخزن و زنده کن»
- Repository / مخزن مرجع: `ahmadnezhadhosseini64-cloud/future-ai-palang-footprint`, default branch `main`
- Prior current anchor / نقطهٔ جاری پیشین: [CURRENT-050](../../0.0/anchors/PALANG-0.0-CURRENT-20261024-050-NEW-PROJECT-ARCHITECTURE-STATUS.md)
- Governing mother / سند مادر حاکم: [NPFAP](../../reference/REFERENCE-DOCUMENTS/NEW-PROJECT-FOUNDATIONAL-ARCHITECTURE-PRINCIPLES-2026-10-24-001.md)
- Next gate / گام بعدی: [NEXT-044](../../0.0/anchors/PALANG-0.0-NEXT-20261024-044-EXTRACTABLE-RAHM-CHILD-AND-COLD-START-TEST.md)

## Scope / دامنه
Excavate the canonical repository, retrieve the latest current checkpoint, living mother, active queue, reference index, and recovery gate; detect stale links or outdated continuation assumptions; preserve historical records; and make only evidence-backed additive corrections.

## Observed findings / یافته‌های مشاهده‌شده
1. Repository metadata confirms the public canonical repository exists, default branch is `main`, and connected permissions include push.
2. Latest commit list at inspection began with commit `62e21867278c22edc982dc42a0d3340b425a5209`, committed at `2026-10-24T14:20:59Z` (Tehran equivalent `2026-10-24T17:50:59+03:30`). This is the observed repository time anchor for the inspected snapshot, not the exact user-message time.
3. The reference index identifies CURRENT-050 / EVT-0150 / NPFAP v1.1.4 / NEXT-044 as the current chain.
4. CURRENT-050 says NEXT-044 is the next gate and remains OPEN / NOT RUN.
5. The NEXT-044 body was stale: it still named CURRENT-047, NPFAP v1.0.9, and older acceptance-chain identifiers. Those are historical records, but not the latest recovery target.
6. The live integration queue points to continuing repository source-clause reconciliation under NEXT-036, Issue #21 historic-source census, and Issue #20 runtime capture/reverse lookup/cold-start. These are distinct workstreams; Dropbox remains OPEN / WAITING and is not the target of this request.
7. The repository records are not proof of a successful portable export, fresh-host reconstruction, second-project integration, always-on monitoring, or independent external destinations.

## Correction / اصلاح
Update the active NEXT-044 test specification additively so its current acceptance target is CURRENT-050, IN-043, OUT-042, EVT-0150, NPFAP v1.1.4, Adaptive Discovery v1.1.0, and the reference index; retain the former CURRENT-047 / NPFAP v1.0.9 chain as required historical lineage rather than deleting it.

## Evidence boundary / مرز شواهد
This event documents repository retrieval and the stale-target finding. It does not by itself pass NEXT-044. Export artifact creation, digest validation, fresh-host reconstruction, negative-case testing, and second-project integration remain separate gates until their results are independently evidenced.

## Behavioral lesson / درس رفتارشناسی
“خاک‌برداری” means inspect and reconcile the actual current repository state, not repeat old summaries or drift into the Dropbox branch. When the user’s target is architecture/model continuation, follow CURRENT-050 and the active NEXT-044 gate; explicitly distinguish completed repository reads from unrun recovery tests. Do not imply background execution during silence.

## Status / وضعیت
- Repository metadata and relevant current files: RETRIEVED.
- Stale NEXT-044 acceptance target: FOUND.
- Correction: being applied as an additive update.
- Export and fresh-host recovery: OPEN / NOT RUN.
- Dropbox: OPEN / WAITING; unchanged.
- External Library/Buffer/Persistent Memory destinations: not re-proven by this event.
