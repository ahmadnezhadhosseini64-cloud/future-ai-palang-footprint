# PMA Portable Runtime Bridge

Production ID: `MPGG-2026-09-01-001`
Reference record: `MPGG-2026-09-01-001`
Adapter specification: `PMA-2026-09-01-001`
Status: `ACTIVE / IMPLEMENTED / EXTERNAL-MEMORY-BRIDGE-PENDING`

## Purpose

This directory implements the repository-side execution boundary defined by PMA. It does **not** claim direct access to ChatGPT Persistent Memory.

The runtime provides:

1. stable Production ID preservation;
2. deterministic payload hashing;
3. durable Pending/Recovery representation;
4. write/read-back/match verification against the configured durable adapter store;
5. explicit reconciliation and status reporting;
6. a hard boundary that prevents a repository-side success from being reported as ChatGPT Persistent Memory success.

## Proof boundary

`Repository Adapter Store VERIFIED` is not equivalent to `ChatGPT Persistent Memory VERIFIED`.

The latter requires an actual provider bridge capable of independent read-back from ChatGPT Persistent Memory. Until such a bridge exists, the Memory provider state remains `UNVERIFIED / PENDING`.

## Execution contract

`WRITE → READ-BACK → VERIFY → RECONCILE → STATUS`

A failed or unavailable provider never deletes the Pending record and never changes the Production ID.