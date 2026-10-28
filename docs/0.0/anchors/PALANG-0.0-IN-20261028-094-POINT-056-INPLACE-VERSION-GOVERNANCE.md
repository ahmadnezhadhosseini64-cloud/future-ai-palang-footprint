# IN-094 — User input: no version increment; update the same canonical ZIP in place

- Stable ID: HAIF-IN-094-POINT-056-INPLACE-VERSION-GOVERNANCE-20261028
- Parent: [POINT-0/056 (0+)](./GPT6-RAHM-USER-POINT-0-20261028-056-0PLUS-INPLACE-UPDATE-VERSION-GOVERNANCE.md)
- Prior highlight retained: [POINT-0/055](./GPT6-RAHM-USER-POINT-0-20261028-055-0PLUS-ARCHITECTURE-ZIP-MASTER-HARD-AUDIT.md)
- Output: [OUT-093](./PALANG-0.0-OUT-20261028-093-POINT-056-INPLACE-VERSION-GOVERNANCE.md)
- Event: [EVT-0231](../../architecture/BEHAVIOR-TRACE/EVT-0231-POINT-056-INPLACE-VERSION-GOVERNANCE-2026-10-28.md)
- Current: [CURRENT-106](./PALANG-0.0-CURRENT-20261028-106-INPLACE-VERSION-GOVERNANCE.md)

## Captured requirement
The user explicitly reaffirmed: do not create a new version number; update the existing version and rebuild the same canonical ZIP. Version remains 0.3.8. Stable package ID and canonical filename must not change. Prior artifact digest is historical only.

## Required execution
1. Keep manifest version and current_internal_version at 0.3.8.
2. Keep supersedes at 0.3.7 (the previous distinct version), not 0.3.8.
3. Align package docs and tests to the current graph.
4. Trigger/inspect exact-head conformance workflow and verify downloaded ZIP bytes, digest, inventory and extracted tests.
5. Leave external host acceptance gates OPEN until direct host receipts exist.

## Status
REGISTERED / READ-BACK REQUIRED at creation. All gates not directly proven remain OPEN.
