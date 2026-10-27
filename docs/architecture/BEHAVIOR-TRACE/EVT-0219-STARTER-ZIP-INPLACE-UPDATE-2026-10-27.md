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
- Status: ZIP BUILD + ARTIFACT READ-BACK VERIFIED; real-host test OPEN / NOT RUN.


## Verified archive receipt
Run 40489299348 succeeded on tested commit fa930e8e895eae7dea3f7eb13449321c5658a2c2. The existing canonical ZIP filename was rebuilt with internal package version 0.3.1, 18,815 bytes, SHA-256 b3429acaa5d33fb93dec7ad0ba8c1cdf233fbb28b8839794eea74457013e1309. Fresh extraction, ZIP CRC, inventory and 15/15 unit tests passed. Real independent-host acceptance remains NOT RUN.
