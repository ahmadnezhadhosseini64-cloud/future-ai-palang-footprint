# EVT-0291 — Easy read-only GitHub connection for a new host — 2026-11-21

- Point: POINT-0/072 (0++ marker on the canonical root, not a new root).
- Input / Output: IN-115 / OUT-114.
- Time binding: TIME-BINDING-EVT-0291.
- Current: CURRENT-125.
- Sole active queue: NEXT-051.
- Status: PROPOSAL REGISTERED ON HOST-INTAKE BRANCH; NOT MERGED.

## Behavior contract
A new AI host receiving the living master or portable ZIP should first read the canonical GitHub repository directly through its public URL without signing in, because the repository is currently PUBLIC. An official GitHub connector is optional for this public read-only path. Verify the exact repository and main HEAD, then recover the living master, latest verified ZIP pointer and receipts. If public retrieval is blocked or the repository becomes PRIVATE, guide the owner to the product's official GitHub OAuth/connection UI. Never request or store passwords, PATs or secrets in chat. Report BLOCKED / NOT CONNECTED / NOT VERIFIED without simulating success.

## Explicitly deferred
The phrase «احمد نژادحسینی», owner-confirmation/password gate, expanded authentication UX and any write authorization are intentionally deferred to a later design phase and remain OPEN. This phase does not attempt repository writes, broker deployment, host-intake writeback or main-branch changes.

## Evidence boundary
This event records source changes on a proposal branch only. It does not claim main-branch integration, ZIP rebuild, successful connection on an independent host, persistent workspace, broker deployment, branch protection or host recovery.
