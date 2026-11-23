# Host-safe snapshot — POINT-0/GOLDEN

**Snapshot status:** design-only / not yet released  
**Canonical continuation:** POINT-0/GOLDEN → NEXT-051  
**Architecture:** one private mother repository; allowlist-only public bridge; independent host workspaces.

## Non-negotiable roles
- Owner: human authority and final approval.
- Palang Control: authorized audit and validation agent, only when its real connector permissions are active.
- RAHM WOMB: private growth and validation environment.
- RAHM Evidence Ledger: deterministic provenance/hash/receipt subsystem; not an AI model.
- CHILD: controlled candidate lifecycle; not a host workspace.
- MASTER: authoritative source of truth.

## Host boundary
Hosts receive only this published snapshot and task instructions. They work in their own workspace. They receive no Git write access, repository credentials, RAHM endpoint, token, webhook or direct/indirect route into the core.

## Approval gates
1. Owner separately approves admission into accepted CHILD.
2. Owner separately approves promotion from accepted CHILD to MASTER.

## Current operational caveat
The source repository is still public at the time this snapshot was authored. This snapshot must not be used as a security claim or as an active host invitation until the repository privacy and allowlist deployment gates pass.
