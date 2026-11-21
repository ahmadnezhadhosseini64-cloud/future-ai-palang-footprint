# Durable Host Event Ledger — Legacy Intake Frozen

This directory preserves the historical repository-side event ledger contract. It is NOT an active host write destination.

- The former host-intake branch and legacy direct GitHub worker are frozen/disabled.
- No AI host may write to any branch, PR, issue, workflow, release, or setting in the canonical master repository.
- The legacy worker now exits with LEGACY_DIRECT_GITHUB_WORKER_DISABLED and performs no GitHub API request.
- New host outputs remain in the host's own private workspace. The owner exports and redacts selected material into the private RAHM repository.
- Only the owner-controlled promotion workflow may create a bot-authored PR into CHILD-CANDIDATES; it never auto-merges or modifies the living Master.
- Raw private conversations, secrets, credentials, personal data, and unredacted payloads must never be copied into the public master.
- Historical records on any old intake branch are evidence only; they do not prove live host capture, host persistence, or authorization.

Current policy: docs/architecture/RAHM/README.md and CURRENT-139.
