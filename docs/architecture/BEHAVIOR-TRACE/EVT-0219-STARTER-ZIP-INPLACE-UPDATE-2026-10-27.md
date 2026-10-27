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
Run 40489753805 succeeded on tested commit 95e42fdffa0f0de956220403200c6f2390cfe645. The existing canonical ZIP filename was rebuilt with internal package version 0.3.1, 19,042 bytes, SHA-256 3a17f64880519a0da714f09a1dc8065fafcd88321fa5674eb2d995dfd8f63e83. Fresh extraction, ZIP CRC, inventory and 16/16 unit tests passed. Real independent-host acceptance remains NOT RUN.
