# Permanent Registration Matrix — Architecture

**Architecture ID:** ARCH-PRNT-2026-08-30-001  
**Principle ID:** PRNTP-2026-08-30-001  
**Reference ID:** REF-PRNT-2026-08-30-001  
**Version:** 1.0  
**Status:** ACTIVE / CANONICAL

## Role

This architecture prevents the system from confusing a trace with durable registration. Every formal production is evaluated across the required project layers and receives an explicit state in a shared Registration Matrix.

## Required registration layers

`Production → Reference → Architecture → Repository → Memory → Runtime/Playground → Checkpoint/Anchor → Recovery → Evidence → Verification → Final Status`

Not every production requires every layer. The requirement decision must be explicit as `REQUIRED` or `NOT_APPLICABLE`; silence is not a valid state.

## State model

Each layer uses one of:

`SUCCESS | PENDING | FAILED | UNAVAILABLE | NOT_APPLICABLE`

`FINAL / PROVEN` is blocked while any required layer lacks successful evidence.

## Cross-layer identity

A shared Production ID links all records. Reference, architecture, repository path/commit, memory status, runtime/playground placement, checkpoint/anchor, recovery record, evidence and verification must be traceable back to that ID.

## Failure handling

- If Repository is unavailable, preserve the production in an available durable recovery destination and mark Repository `PENDING/UNAVAILABLE`.
- If Memory is unavailable, preserve the production in the Canonical Repository when available and mark Memory `PENDING/UNAVAILABLE`.
- If both are unavailable and no durable writable store exists, mark `UNREGISTERED/RECOVERY REQUIRED`.
- Reconcile at the first valid opportunity and verify the result before closing the pending state.

## Living documentation

The matrix is a living state, not a one-time checklist. Registration state, evidence, reconciliation, architecture placement and continuation impact must be updated when they change.

## Cross-chat behavior

Connection events, greetings, new chats and `00` must retrieve the latest matrix and Continuation Anchor before substantive continuation. They do not reset registration state or create a new project path.

## Invariant

> **Trace is evidence of existence; durable registration is evidence of maintained project state.**
