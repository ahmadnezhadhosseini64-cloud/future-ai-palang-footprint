## PR #100 and EVT-0308 — latest main/package receipt

- PR #100: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/100
- Merge commit / current main HEAD: 9ebd4bcc5cfc0168276e366c1867da8709dfb566
- Git UTC: 2026-11-22T00:00:12Z; Tehran: 2026-11-22T03:30:12+03:30
- Proposal tree SHA and merged main tree SHA exact match: 8be81af3dcf822b10107a7efcf4c603ca7567706 (11 changed files).
- main.protected=true.
- Portable conformance run 44964480412: SUCCESS; stable release refreshed at 2026-11-22T00:00:37Z.
- Latest canonical ZIP SHA-256: 243baddff63eaf18129a0cbaff860f84f375655c893ee0d1cb42235ecae38646; size 272,688 bytes.
- Stable release: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified.
- [EVT-0308](../../architecture/BEHAVIOR-TRACE/EVT-0308-PORTABLE-STARTER-VERIFICATION-AND-OWNER-RELEASE-2026-11-22.md) → [TIME-BINDING-EVT-0308](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0308-PORTABLE-STARTER-VERIFICATION-AND-OWNER-RELEASE-2026-11-22.md).
- Clean-host recovery remains NOT RUN; package verification is not independent-host recovery.

## Follow-up merge and package verification — PR #98 / #99 / EVT-0307

- PR #98: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/98
  - Merge commit: 4f193e69e52e6a8eb1d7ae9520f2b2778ac69cf8
  - Git UTC: 2026-11-21T23:52:16Z; Tehran: 2026-11-22T03:22:16+03:30
  - Proposal and merge tree SHA exact match: 5b4e0baec0160625d64669935ae5ca9bfda49a7e.
- PR #99: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/99
  - Merge commit: 891829cc123d876a3e63f93331981e0af5107868
  - Git UTC: 2026-11-21T23:54:56Z; Tehran: 2026-11-22T03:24:56+03:30
  - Proposal and merge tree SHA exact match: 2acb118181684dfed01e9305b8e5b8c89a6ad1f6.
- Current main HEAD: 891829cc123d876a3e63f93331981e0af5107868; branch protected=true.
- EVT-0307: [Portable starter package verification](../../architecture/BEHAVIOR-TRACE/EVT-0307-PORTABLE-STARTER-VERIFICATION-AND-OWNER-RELEASE-2026-11-22.md) → [TIME-BINDING-EVT-0307](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0307-PORTABLE-STARTER-VERIFICATION-AND-OWNER-RELEASE-2026-11-22.md).
- Main portable workflow run 44964082773: SUCCESS; stable release tag haif-latest-verified refreshed.
- Canonical ZIP: haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip; package SHA-256 0823141628db6d62fc6a5d320f8ca0c291f941bca446286f894e75a299a811f5; size 272,688 bytes.
- Release: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified.
- ZIP CRC, source-byte read-back, extracted tests, same-run artifact download/read-back and durable release publication: PASS.
- Independent clean-host recovery: NOT RUN; PACKAGE_VERIFIED is not HOST_RECOVERED.
- Main RAHM Security Conformance, Living Architecture Audit, Pages deployment, Evidence Gate, Execution Controller, Pending Registration Audit, Cross-Layer Integrity, CPREL and reconciliation workflows: PASS.

## PR #97 — merge and full-tree read-back receipt

- PR: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/97
- Merge commit: 67c85da41e1d455271f55eb8affbe92811e816af
- Git commit time UTC: 2026-11-21T23:45:30Z
- Tehran equivalent: 2026-11-22T03:15:30+03:30
- Proposal branch head: 1601cf0da32cd8907f050a3edc2390f141ab1fe0
- Proposal tree SHA: 9191d83e75713d95536b017563c27e326524cbe4
- Merged main tree SHA: 9191d83e75713d95536b017563c27e326524cbe4
- Full repository tree exact match: PASS. All 51 changed files are included in the merge tree.
- PR RAHM Security and Promotion Conformance: PASS (run 44963255990).
- PR Living Architecture Audit: PASS (run 44963256010).
- Main RAHM Security and Promotion Conformance: PASS (run 44963342878).
- Main Living Architecture Audit: PASS (run 44963342868).
- Main Evidence Gate, Execution Controller, Pending Registration Audit and Cross-Layer Integrity: PASS.
- Portable package build, ZIP CRC, source-byte comparison, artifact download/read-back and extracted tests passed; the final durable-release update failed with HTTP 403 because this workflow had contents:read. A follow-up change restores contents:write only for release publication, without any git push/commit to main.
- GitHub Pages deployment initially failed to find the uploaded artifact; the failed deployment job was rerun (attempt 2) and completed SUCCESS.

# EVT-0306 — RAHM مرکزی مالک و دروازه ارتقای میزبان‌ها

- Stable ID: HAIF-EVT-0306-RAHM-CENTRAL-OWNER-GATE-2026-11-22
- Parent chain: POINT-0/085 → CURRENT-138 → POINT-0/086 → IN-129 → OUT-128
- Owner: ahmadnezhadhosseini64-cloud
- Status: REGISTERED / MERGED TO MAIN / FULL-TREE READ-BACK VERIFIED / CI PASS / IMPLEMENTATION PARTIAL
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
