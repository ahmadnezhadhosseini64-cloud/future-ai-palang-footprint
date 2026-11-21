# CURRENT-125 — Easy read-only GitHub connection for a new host

- Point: POINT-0/072.
- Input / Output: IN-115 / OUT-114.
- Event / time: EVT-0291 / TIME-BINDING-EVT-0291.
- Previous checkpoint: CURRENT-124.
- Sole active queue: NEXT-051.
- Status: PROPOSAL REGISTERED ON HOST-INTAKE BRANCH / NOT MERGED.
- Living master target: v1.7.79.
- Package source target: 0.4.4.
- Immediate scope: official GitHub connector discovery, user-guided authorization in host UI, read-only repository access and latest-state recovery.
- Main branch integration: NOT DONE.
- Canonical ZIP rebuild and exact hash/receipt: PENDING.
- Independent-host connector and read-only access test: NOT RUN.
- Owner phrase/password gate («احمد نژادحسینی») and expanded authentication design: OPEN / DEFERRED TO LATER PHASE.
- Repository writes, broker deployment, host-intake write enforcement and branch protection: OPEN / OUT OF CURRENT SCOPE.
- Preserve all prior anchors, CURRENT-065/CURRENT-066 ambiguity, open gates and NEXT-051. No NEXT-052 created.

## Acceptance gates
1. New host can identify whether the official GitHub connector is available.
2. If not connected, host gives clear steps to connect/authorize GitHub through the host product's official UI; no credentials are pasted into chat.
3. Connected account can read the exact repository ahmadnezhadhosseini64-cloud/future-ai-palang-footprint.
4. Host reads main HEAD SHA and fetches the current living master, latest verified package pointer, ZIP and receipts.
5. Wrong/missing account or missing repository permission blocks recovery and yields an explicit status.
6. No repository write operation is attempted in this phase.
7. The same read-only path is documented in the mother and ZIP independently.
8. Real independent-host receipt and restart proof remain required before HOST_RECOVERED.
