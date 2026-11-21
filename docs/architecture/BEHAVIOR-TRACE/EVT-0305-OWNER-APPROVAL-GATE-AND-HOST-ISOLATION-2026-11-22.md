# EVT-0305 — Owner approval gate and host isolation

- Stable ID: HAIF-EVT-0305-OWNER-APPROVAL-GATE-2026-11-22
- Date: 2026-11-22
- Parent chain: POINT-0/085 → IN-128 → OUT-127
- Status: OWNER-DIRECTED / DESIGN DECISION RECORDED / IMPLEMENTATION PARTIAL

## Event
The owner explicitly approved finalizing the existing owner-only master / isolated per-host workspace architecture and adding an owner approval gate before any non-owner proposal is promoted into MASTER.

## Decision
- Preserve public read-only access to the canonical master source for hosts.
- No host receives master write credentials, collaborator access, branch/PR/issue/release/workflow/settings permissions, or bypass.
- Each verified host works in its own isolated runtime and, if persistent Git storage is needed, an owner-created private repository dedicated to that host.
- Host outputs remain proposals until owner export, quarantine, provenance/hash/test review and explicit owner approval.
- Require one owner approval and Code Owner review for non-owner/automation-authored PRs, dismiss stale approvals on new commits, and resolve review threads.
- Do not claim this GitHub review gate is configured until Ruleset values are changed in UI and read back.

## GitHub constraint
A PR author cannot approve their own PR. Owner-authored PRs therefore need an owner-only, PR-scoped bypass or a trusted owner-controlled promotion bot. No host may receive either capability.

## Evidence state
Live Ruleset 27814009 is active on main. Deletion, non-fast-forward and pull-request rules are active. At event registration, live required approvals were 0 and Code Owner review was false. Configuration remains pending UI action and read-back.

## Continuity
This event continues canonical POINT-0 and the sole active NEXT-051. No parallel root or queue is created.