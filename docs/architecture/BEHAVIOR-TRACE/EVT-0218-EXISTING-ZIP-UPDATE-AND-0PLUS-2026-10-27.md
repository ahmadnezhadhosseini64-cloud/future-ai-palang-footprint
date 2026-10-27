# EVT-0218 — به‌روزرسانی بستهٔ اولیه و ثبت 0+

- Stable ID: HAIF-EVT-0218-EXISTING-ZIP-UPDATE-20261027
- Production ID: G6IP-EVT-0218
- Version: 1.0.0
- Status: IMPLEMENTATION RECORDED / BUILD RECEIPT PENDING
- Root: [POINT-0/043 (0+)](../../0.0/anchors/GPT6-RAHM-USER-POINT-0-20261027-043-INDEPENDENT-HOST-RECOVERY-HARD-AUDIT.md)
- Input: [IN-081](../../0.0/anchors/PALANG-0.0-IN-20261027-081-ZIP-UPDATE-AND-POINT-0PLUS.md)
- Output: [OUT-080](../../0.0/anchors/PALANG-0.0-OUT-20261027-080-ZIP-UPDATE-AND-POINT-0PLUS.md)
- Continuation: [CURRENT-093](../../0.0/anchors/PALANG-0.0-CURRENT-20261027-093-EXISTING-ZIP-UPDATE.md)
- Queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)

The user correctly distinguished updating the existing initial ZIP from merely updating repository documents. The previous turn updated docs and manifest only; it did not update/build the starter ZIP. This correction advances the same starter package line from v0.3.0 to v0.3.1, preserves its stable package ID and historical v0.3.0 digest, adds the independent-host recovery protocol inside the package, and updates the existing CI packaging step to produce the versioned artifact from the clean package directory.

Build result and artifact SHA-256 remain PENDING until a fresh workflow run is inspected. Independent AI-host acceptance and restart persistence remain OPEN / NOT VERIFIED.
