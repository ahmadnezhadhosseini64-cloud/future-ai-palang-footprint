# EVT-0306 — RAHM مرکزی مالک و دروازه ارتقای میزبان‌ها

- Stable ID: HAIF-EVT-0306-RAHM-CENTRAL-OWNER-GATE-2026-11-22
- Parent chain: POINT-0/085 → CURRENT-138 → POINT-0/086 → IN-129 → OUT-128
- Owner: ahmadnezhadhosseini64-cloud
- Status: REGISTERED / IMPLEMENTATION PARTIAL
- Event artifact commit: 9a3a35fafe82b04492277c944570098f66c58ffc; Git UTC 2026-11-21T23:27:47Z; Tehran 2026-11-22T02:57:47+03:30.

## Event

مالک خواست یک مسیر دائمی برای معرفی میزبان‌های جدید، محیط مستقل هر میزبان، رصد انتخابی با Host ID، استخراج دانش ارزشمند، انتقال به RAHM مرکزی، آزمون و تطبیق، و ورود فقط با تأیید مالک به CHILD ساخته شود. هیچ میزبان حق نوشتن به مخزن مادر یا RAHM ندارد.

## Hard-audit findings

1. Main is public; a folder in main is not a privacy boundary.
2. The connected GitHub identity is the repository owner account. Owner-authored PRs cannot be approved by that same account.
3. The active Ruleset 27814009 currently has required approvals=0 and Code Owner review=false.
4. Legacy automation had direct-to-main write paths in main.yml, pending-registration-drain.yml, and control-plane/controller.py. These were converted to artifact-only/read-only behavior in this change.
5. execution-controller.yml and rahm-portable-conformance.yml had unnecessary contents:write permissions; they are now read-only.
6. host_adapter_github_worker.py is now fully disabled and fails closed before any GitHub API request; the legacy host-intake route is frozen.
7. Existing Host Registry contains no verified live hosts. No host is enrolled or active by this event.

## Implemented

- Owner-controlled RAHM architecture and private-store provisioning template.
- Candidate manifest schema and validation script.
- Unit tests for valid staging, traversal, digest mismatch, unredacted data, missing owner approval, secret patterns, symlinks and duplicate candidate paths.
- Manual owner-only workflow that reads private RAHM, validates a candidate and creates a bot-authored PR into CHILD. No auto-merge; no Master edit.
- Existing automatic main-write paths removed or converted to read-only/artifact evidence.

## Not yet proven

Private RAHM repository, promotion App, credentials/secrets, ChatGPT private-repo connector access, Ruleset approval=1, actual bot PR, CI test run, collaborator/App/deploy-key audit, host enrollment, broker, and negative cross-host isolation tests.
