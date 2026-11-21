# CURRENT-125 — Owner confirmation and secure GitHub authorization

- Point: POINT-0/072.
- Input / Output: IN-115 / OUT-114.
- Event / time: EVT-0291 / TIME-BINDING-EVT-0291.
- Previous checkpoint: CURRENT-124.
- Sole active queue: NEXT-051.
- Status: PROPOSAL REGISTERED ON HOST-INTAKE BRANCH / NOT MERGED.
- Living master target: v1.7.79.
- Package source target: 0.4.4.
- Main branch integration: NOT DONE.
- Canonical ZIP rebuild and exact hash/receipt: PENDING.
- Owner phrase gate: specified; external-host execution NOT RUN.
- GitHub OAuth/account identity check: NOT RUN on independent host.
- Broker/worker, host-intake quarantine, branch protection: NOT VERIFIED.
- Clean-host import and restart: NOT RUN.
- Preserve all prior anchors, CURRENT-065/CURRENT-066 ambiguity, open gates and NEXT-051. No NEXT-052 created.

## Acceptance gates
1. Phrase exact-match and mismatch tests.
2. Proof phrase is not sent to GitHub or treated as a credential.
3. Official OAuth/connector account verification against `ahmadnezhadhosseini64-cloud`.
4. Read-only repository recovery from both master-only and ZIP-only transfers.
5. Negative test: no connector / wrong GitHub account / no broker blocks the relevant action.
6. Host-intake quarantine, owner-reviewed PR and exact read-back.
7. Canonical ZIP rebuild, SHA-256, byte count, CRC, inventory and extracted tests.
8. Real independent host returns raw receipt and restart proof.
