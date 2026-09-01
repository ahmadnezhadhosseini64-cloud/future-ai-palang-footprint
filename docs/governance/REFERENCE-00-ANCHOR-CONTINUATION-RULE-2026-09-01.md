# Reference Document — 0.0 Anchor / Continuation Rule

**Production ID:** OOA-2026-09-01-001
**Status:** FINAL / ACTIVE / LIVING / PERMANENT
**Type:** Reference / Governance / Architecture Rule

## Rule

`0.0` is the stable anchor and continuation point for the active project path. It is not the last message, last topic, or last command.

A newly created command, document, or production receives its own stable ID, provenance, status, and architectural position. Closing that item does not overwrite or relocate `0.0`.

Unrelated conversation topics have no authority to modify `0.0`.

When the user later says `0.0` and then `start/شروع کن`, the system must retrieve the 0.0 anchor, reconstruct the state of that project path, and continue from the stored continuation point rather than from the most recent conversational topic or production.

## Separation / Anti-Contamination

- Unrelated topic → no effect on 0.0.
- New command/production → independent record.
- Closed command/production → closed record; does not become 0.0.
- 0.0 → stable continuation anchor.
- `start/شروع کن` after 0.0 → Retrieve → Reconcile → Continue.

## Evidence Rule

This rule governs navigation and continuity. It does not convert unverified assumptions into verified facts. Provisional items remain in their designated provisional/recovery layer until Evidence and Verification authorize promotion to Canonical.

## Recovery Rule

If continuity is uncertain, do not guess. Retrieve the 0.0 reference and associated lineage/status records first. Preserve stable IDs and provenance.

## Architectural Effect

No new command, unrelated topic, temporary detour, or closed production may silently overwrite, redefine, or replace the 0.0 anchor.

This document is the reference record for the 0.0 Anchor / Continuation Rule and is intended to remain permanently retrievable as part of the living architecture.
