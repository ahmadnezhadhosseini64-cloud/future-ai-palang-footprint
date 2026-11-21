# IN-128 — Owner approval gate and host isolation

- Stable ID: HAIF-IN-128-OWNER-APPROVAL-GATE-2026-11-22
- Parent: POINT-0/085
- Status: OWNER-DIRECTED / RECEIVED
- Owner intent: finalize host onboarding under owner-only master isolation and add one owner approval before non-owner proposals can be promoted to MASTER.

## Input
The user explicitly confirmed the architecture: hosts may read the public master source, but each host works in its own isolated environment/private repository and has no write access to the master. The owner retains exclusive authority over promotion into MASTER. User gave full approval to formalize this design and the owner approval gate.

## Constraints
- Do not create a parallel root or queue.
- Do not grant hosts master credentials, collaborators, bypass, PR or settings access.
- Preserve per-host private workspace isolation and owner-controlled registration.
- Record GitHub's self-approval limitation; PR author cannot approve their own PR.