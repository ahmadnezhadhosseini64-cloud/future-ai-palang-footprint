# EVT-0219 — Existing starter ZIP in-place update

- Root: POINT-0/044
- IN: IN-082
- OUT: OUT-081
- Checkpoint: CURRENT-094
- Active queue: NEXT-051
- Observed defect: package source/manifest changes were previously described too close to ZIP update, despite no fresh archive receipt.
- Corrective rule: only a freshly built archive under the established canonical filename, with exact-byte hash/size and workflow artifact read-back, qualifies as updated ZIP. Do not create a second version-named package ZIP.
- Historical ZIP digest remains historical and must not be reused as the updated digest.
- Host acceptance remains a separate gate.
- Status: OPEN pending build receipt and real host test.
