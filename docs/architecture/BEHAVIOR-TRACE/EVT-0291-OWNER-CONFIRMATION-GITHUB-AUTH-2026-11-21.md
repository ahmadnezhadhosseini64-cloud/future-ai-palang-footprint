# EVT-0291 — Owner confirmation and secure GitHub authorization — 2026-11-21

- Point: POINT-0/072 (0++ marker on the canonical root, not a new root).
- Input / Output: IN-115 / OUT-114.
- Time binding: TIME-BINDING-EVT-0291.
- Current: CURRENT-125.
- Sole active queue: NEXT-051.
- Status: PROPOSAL REGISTERED ON HOST-INTAKE BRANCH; NOT MERGED.

## Behavior contract
A new host receiving the living master or portable ZIP asks for the exact owner-confirmation phrase «احمد نژادحسینی» before repository operations. The phrase is public in the artifacts and is not a password, identity proof, OAuth credential or permission. After phrase match, the host must use official GitHub OAuth/connector and verify the connected GitHub owner account `ahmadnezhadhosseini64-cloud`. Start READ-ONLY. Writes require least-privilege broker/worker, host-intake quarantine, owner-reviewed PR and exact read-back. Never request or store passwords, PATs or secrets in chat.

## Source changes
- Added `prototype/haif-gpt6-starter/OWNER-CONFIRMATION-AND-GITHUB-AUTHORIZATION-CONTRACT.md`.
- Updated `ONE_MESSAGE_HOST_BOOTSTRAP_FA.md`, `GPT6_HOST_INSTRUCTIONS.md`, package `README.md`, package `manifest.json`.
- Updated living mother to v1.7.79.
- Added POINT-0/072, IN-115, OUT-114, CURRENT-125 and this event/time-binding.

## Evidence boundary
This event records source changes on a proposal branch only. It does not claim main-branch integration, ZIP rebuild, OAuth activation, broker deployment, branch protection, or real external-host acceptance.
