# POINT-0/047 — ثبت ورودی کاربر دربارهٔ بستهٔ اولیهٔ واحد و تداوم 0.0

- Stable ID: HAIF-POINT-0-047-SAME-STARTER-ZIP-CONTINUITY-20261027
- Production ID: HAIF-P047-SAME-STARTER-ZIP-20261027
- Parent/context: POINT-0/046 and CURRENT-096; POINT-0/043 remains the 0+ production marker.
- Continuation: IN-085 → OUT-084 → EVT-0222 → CURRENT-097 → NEXT-051.
- User intent: make this interaction the canonical point 0; continue implementation as 0.0; keep improving the original starter package, with one stable package identity and one canonical ZIP filename.
- Verified baseline: workflow run 40508128142 on commit 2621508611935e243fe4085c9045193ae19bfedf passed; canonical filename `haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip`; internal version 0.3.2; 19,242 bytes; SHA-256 `861be3d9998e96c8588d03642f70d01a6e2060b7b5056f45ef50008fc6f61da4`; eight package members; 16/16 package tests passed.
- Correction/gap: the downloaded nested ZIP's recovery protocol still labels itself version 0.3.1 while the manifest says 0.3.2. This is a real internal-version consistency gap; do not call the package fully reconciled until the source and rebuilt ZIP agree.
- Required rule: source change is not a ZIP update. Rebuild under the same canonical filename, capture exact ZIP SHA-256/bytes/inventory, download artifact, extract nested ZIP, compare receipt and run tests.
- Real independent-host import/recovery and restart persistence remain NOT RUN / NOT VERIFIED.
- NEXT-051 remains the only active queue. Do not create NEXT-052.
- Status: REGISTERED IN SOURCE; package version consistency and fresh exact-head ZIP receipt remain OPEN.
