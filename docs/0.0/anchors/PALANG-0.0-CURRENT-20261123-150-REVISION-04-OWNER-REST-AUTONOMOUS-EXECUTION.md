# CURRENT-150.04 — ادامهٔ خودکار، استراحت مالک و بررسی ده‌گانه

- Stable family: CURRENT-150
- Revision: 150.04
- Status: ACTIVE / LIVING / GOLDEN-BRANCH-CANDIDATE / EXACT-SHA-VALIDATION-PENDING
- Root: POINT-0/GOLDEN
- Parent: CURRENT-150.03
- Input: IN-137
- Output: OUT-136
- Event: EVT-0324
- Sole queue family: NEXT-051; candidate revision NEXT-051.04
- Owner: @ahmadnezhadhosseini64-cloud

## Continuity rule
The owner should not need to repeat the instruction to anchor relevant project interactions to POINT-0/GOLDEN. The assistant should preserve the canonical lineage automatically in relevant conversations, and make repository records when authorized tools are available. A conversational reference is not a repository commit; only Git metadata establishes the recorded commit time.

## Current verified boundaries
- PR #145 remains open and unmerged. CURRENT-150.03 / NEXT-051.03 are candidates; .02 remains the last accepted Golden state until owner-controlled promotion.
- Living mother remains 1.8.4; no downgrade.
- Ruleset 27814009 is active but currently has zero required approvals and Code Owner review disabled.
- Partner issues #114–#123 remain open.
- Independent-host acceptance, restart persistence, live capture, private RAHM/Partner provisioning, and durable release refresh remain open/not verified.

## Execution principles
Prefer the simplest secure route that meets the architecture. Do not create services, repos, apps, or credentials before verifying the minimum required capability and permissions. Prefer managed hosting and provider secret managers over bespoke infrastructure where compatible; prefer GitHub OIDC over long-lived cloud deployment credentials where supported. Keep owner credentials out of model context.

## Automation boundary
A scheduled task can trigger a bounded project review at a chosen time/frequency and notify the owner. It does not provide continuous thought between runs. Recurring supported cadences are daily, weekly, or monthly with flexible timing; exact recurring minute/hour cannot be promised. A one-time scheduled run can use a specific date/time. No schedule is created until the owner defines a preferred time.

## Acceptance
This is a candidate continuation record only. It does not merge Golden, modify main, provision external infrastructure, or close any operational gate.
