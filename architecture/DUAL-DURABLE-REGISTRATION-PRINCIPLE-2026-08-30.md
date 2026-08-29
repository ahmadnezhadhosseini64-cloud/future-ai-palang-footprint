# Dual Durable Registration & Deferred Reconciliation Principle

ID: ARCH-REG-2026-08-30-001
Status: ACTIVE / FUNDAMENTAL ARCHITECTURAL RULE
Reference Point: 0.0
Date: 2026-08-30

## Rule
When the project owner explicitly says «ثبت کن» (register it), registration must be routed to both persistent AI memory, when appropriate, and the canonical project repository when repository access/write capability is available.

Registration in only one destination is incomplete when both are applicable.

## Repository Unavailability
If the canonical repository is unavailable or not writable, the request must not be lost. It must enter a durable Pending/Recovery Registration record with a unique ID, intended canonical destination/path, complete content, provenance, timestamp, and explicit status `PENDING_REPOSITORY_REGISTRATION`.

At the first valid write opportunity, the pending record must be automatically reconciled into the canonical repository, then verified and its status updated with repository evidence.

## Evidence Rule
Connection, access, intent, or design is not evidence that registration occurred. A registration claim requires actual repository write evidence, including a resulting commit SHA and retrievable canonical content.

## Checkpoint Rule
For 0.0 checkpoints, the full Checkpoint Schema + Verification Gate remains mandatory. The checkpoint must be persisted and repository-registered when available; repository registration must be verified before being reported as PROVEN.

## Required Flow
REGISTER REQUEST → MEMORY + CANONICAL REPOSITORY → VERIFY BOTH → if unavailable: PERSIST PENDING → AUTO-RECONCILE → VERIFY → REPORT STATUS.

## Prohibited
Never interpret «ثبت کن» as memory-only when repository registration is part of the established contract. Never silently drop a pending registration. Never claim repository registration without evidence.
