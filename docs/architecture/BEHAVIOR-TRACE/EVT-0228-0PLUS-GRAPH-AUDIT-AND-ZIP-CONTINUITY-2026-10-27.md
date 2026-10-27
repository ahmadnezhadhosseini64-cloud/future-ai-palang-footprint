# EVT-0228 — خاک‌برداری گراف 0 / 0+ / 0.0 و تداوم ZIP اولیه

- Stable ID: HAIF-EVT-0228-GRAPH-AUDIT-ZIP-CONTINUITY-20261027
- Production ID: G6IP-EVT-0228
- Root: [POINT-0/053 (0+)](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261027-053-0PLUS-GRAPH-AUDIT-AND-ZIP-CONTINUITY.md)
- Input: [IN-091](../../0.0/anchors/PALANG-0.0-IN-20261027-091-0PLUS-GRAPH-AUDIT-AND-ZIP-CONTINUITY.md)
- Output: [OUT-090](../../0.0/anchors/PALANG-0.0-OUT-20261027-090-0PLUS-GRAPH-AUDIT-AND-ZIP-CONTINUITY.md)
- Checkpoint: [CURRENT-103](../../0.0/anchors/PALANG-0.0-CURRENT-20261027-103-0PLUS-GRAPH-AUDIT-AND-ZIP-CONTINUITY.md)
- Queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

The exact artifact for v0.3.7 was downloaded and inspected. It retains the canonical ZIP filename and stable package ID, with 30,573 nested ZIP bytes, SHA-256 fcc09933dd67ca1300af051e14dbcf80c76b6f620dc6c9623323caca307969fb, 11 files and 23/23 tests. The outer Actions wrapper hash is a different object and must not be confused with the nested ZIP hash.

The audit also found stale live pointers and duplicate-numbered files for POINT-0/045, CURRENT-095, IN-083, OUT-082 and EVT-0220. Historical files remain untouched; collisions are OPEN until provenance establishes the correct parent/role.

The test-only source change altered the package bytes while manifest remained 0.3.7. Version 0.3.8 is now being prepared in the same package identity and canonical filename. Its archive receipt and real independent-host acceptance remain separate gates.
