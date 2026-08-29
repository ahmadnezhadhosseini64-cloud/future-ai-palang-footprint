# Production Registry — Cross-Layer Integrity Control Plane

**Project:** Future AI / Palang Footprint  
**Owner:** Ahmad Nezhadhosseini  
**Location:** Iran — Gonbad-e Kavus  
**Date:** 2026-08-30  
**Status:** ACTIVE CONTROL-PLANE SPECIFICATION

## Purpose
Provide a durable, auditable index for valuable project productions so that architectural rules, definitions, commands, decisions, tests, evidence, and other material outputs can be reconciled across durable layers.

## Required record
Every important production must have a unique `production_id` and, where applicable, a `trace_id`.

Minimum fields:

- `production_id`
- `trace_id`
- `type`
- `title`
- `version`
- `created_at`
- `created_at_timezone`
- `owner`
- `location`
- `source_context`
- `memory_state`
- `repository_state`
- `execution_state`
- `evidence_state`
- `verification_state`
- `approval_state`
- `reconciliation_state`
- `canonical_destination`
- `artifact_path`
- `last_verified_at`
- `notes`

## State rules
`RECEIVED → INTERPRETED → REQUIREMENTS_RESOLVED → EXECUTED → EVIDENCE_CAPTURED → VERIFIED → REGISTERED → RECONCILED → COMPLETED`

Allowed exception states: `PENDING`, `BLOCKED`, `FAILED`, `UNVERIFIED`, `SYNC_GAP`, `CONFLICT`, `PARTIAL`, `STALE`.

## Cross-layer invariant
A production is `RECONCILED` only when all required destinations for that production are independently verified. Presence in one layer cannot imply presence in another.

## Pending rule
If a required destination is unavailable, the production remains in `PENDING`/`SYNC_GAP` with a unique ID and must be discoverable on the next valid reconciliation opportunity.

## Idempotency
`production_id` is the idempotency key. A retry must update/reconcile the same production record rather than create a duplicate canonical production.

## Human approval
A production requiring human approval remains `AWAITING_APPROVAL` until approval evidence exists. Automation may detect, validate, queue, and report it, but must not silently convert it to canonical status.

## Critical limitation
This registry is a repository-side control plane. It cannot independently read ChatGPT persistent memory. Therefore it must never claim `memory_state=VERIFIED` without evidence supplied by a capability that can actually verify that layer.

## Live-system requirement
A future reconciler must consume this registry, detect stale/pending/conflicting records, reconcile when capabilities are available, and emit traceable evidence. A workflow that only validates static files is an integrity gate, not a complete cross-layer reconciler.
