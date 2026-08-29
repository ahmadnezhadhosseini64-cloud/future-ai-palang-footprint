# Registration Routing Principle

ID: ARCH-REG-2026-08-30-001
Title: Dual Durable Registration & Deferred Reconciliation Principle
Status: ACTIVE / FUNDAMENTAL ARCHITECTURAL RULE
Version: 1.0
Date: 2026-08-30
Reference Point: 0.0

## Rule

When the project owner explicitly declares that an item should be **registered**, the default required destination is BOTH:

1. Persistent AI memory, when the information is appropriate for persistent memory; and
2. The canonical project repository, when repository access/write capability is available.

Registration in only one of these destinations is not a complete registration when both are applicable.

## Repository Unavailability

If the canonical repository is unavailable, inaccessible, or not writable at the moment of registration:

- The item must not be silently dropped.
- It must be placed into a durable Recovery/Pending Registration record with a unique ID and explicit status such as `PENDING_REPOSITORY_REGISTRATION`.
- The pending record must preserve the intended canonical destination/path, content, provenance, timestamp, and reason for deferral when known.
- At the first valid opportunity when repository write capability is available, the system must reconcile the pending item into the canonical repository and update its status with the resulting repository evidence.

## Execution Integrity

Access, intent, design, or an available connector is not evidence that repository registration occurred. A registration claim requires actual repository write evidence, such as a resulting commit SHA and retrievable canonical file/content.

## Checkpoint Interaction

For a `0.0` Checkpoint registration, the complete Checkpoint Schema + Verification Gate remains mandatory. The checkpoint must be recorded in persistent memory and, where available, in the canonical repository. Repository-side registration must be independently verified before being reported as `REGISTERED / PROVEN`.

## Required Operational Flow

REGISTER REQUEST → ROUTE TO MEMORY + CANONICAL REPOSITORY → VERIFY BOTH → if repository unavailable: PERSIST PENDING RECOVERY RECORD → AUTO-RECONCILE ON NEXT VALID WRITE OPPORTUNITY → VERIFY → REPORT STATUS.

## Prohibited Behavior

- Do not interpret «ثبت کن» as memory-only when repository registration is part of the established project registration contract.
- Do not claim repository registration without repository evidence.
- Do not discard a registration request because the repository is temporarily unavailable.
- Do not require the owner to repeatedly restate a pending registration that has already been durably captured.
