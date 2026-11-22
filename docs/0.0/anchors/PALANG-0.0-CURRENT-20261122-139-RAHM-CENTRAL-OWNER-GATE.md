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


## Direct references

- [POINT-0/086 (0++)](GPT6-RAHM-USER-POINT-0-20261122-086-RAHM-CENTRAL-OWNER-GATE.md)
- [IN-129](PALANG-0.0-IN-20261122-129-RAHM-CENTRAL-OWNER-GATE.md) → [OUT-128](PALANG-0.0-OUT-20261122-128-RAHM-CENTRAL-OWNER-GATE.md)
- [EVT-0306](../../architecture/BEHAVIOR-TRACE/EVT-0306-RAHM-CENTRAL-OWNER-GATE-AND-CHILD-PROMOTION-2026-11-22.md) → [TIME-BINDING-EVT-0306](../../architecture/BEHAVIOR-TRACE/TIME-BINDING-EVT-0306-RAHM-CENTRAL-OWNER-GATE-2026-11-22.md)
- Sole active [NEXT-051](PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- [RAHM policy](../../architecture/RAHM/README.md) · [Owner monitoring commands](../../architecture/RAHM/OWNER-MONITORING-COMMANDS.md) · [Promotion App setup](../../architecture/RAHM/PROMOTION-APP-SETUP.md) · [CHILD area](../../architecture/CHILD-CANDIDATES/README.md)
# CURRENT-139 — رحم مرکزی مالک و دروازه ارتقای میزبان‌ها

- Stable ID: HAIF-CURRENT-139-RAHM-CENTRAL-OWNER-GATE-2026-11-22
- Status: ACTIVE / LIVING / OWNER-DIRECTED / DESIGN-APPROVED / MERGED TO MAIN / FULL-TREE READ-BACK VERIFIED / CI PASS / PACKAGE-VERIFIED / RELEASE-PUBLISHED / HOST-RECOVERY-NOT-RUN / OPERATIONAL-SETUP-PENDING
- Parent checkpoint: CURRENT-138
- Current point: POINT-0/086 (0++)
- Input/output: IN-129 → OUT-128
- Event/time: EVT-0306 → TIME-BINDING-EVT-0306
- Living master target: 1.7.94
- Sole active queue: NEXT-051
- Canonical master: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Owner / sole intended reviewer: @ahmadnezhadhosseini64-cloud

## Canonical chain

POINT-0/084 → CURRENT-137 → POINT-0/085 → CURRENT-138 → POINT-0/086 (0++) → IN-129 → OUT-128 → EVT-0306 → TIME-BINDING-EVT-0306 → CURRENT-139 → EVT-0307 → TIME-BINDING-EVT-0307 → EVT-0308 → TIME-BINDING-EVT-0308 → NEXT-051.

## Architecture decision

The owner has approved a permanent, owner-controlled route for new hosts. Every host works in its own isolated workspace. On the owner's explicit command, ChatGPT/the HAIF control plane checks the live registry and issues the next unique Host ID only after a verifiable enrollment receipt; a host never self-assigns an official ID. Hosts have PUBLIC READ ONLY access to the master and no master-write, branch, PR, issue, release, workflow, settings, or bypass permissions.

RAHM is a central owner-only control plane, not a folder inside a host workspace. Because the master repository is public, raw/private host exports belong in a separate owner-controlled PRIVATE repository named future-ai-palang-rahm. The public master stores only policy, schema, validation code, workflow code, and sanitized Child candidates.

## Permanent learning and promotion path

HOST PRIVATE WORKSPACE → OWNER-COMMANDED MONITOR/EXPORT → PRIVATE RAHM QUARANTINE → CROSS-HOST RECONCILIATION → RAHM VALIDATION → PROMOTION-APP BOT PR → OWNER REVIEW/APPROVAL → CHILD-CANDIDATE.

A Child candidate is not the living Master. Any later promotion into canonical Master documents requires a separate owner-directed PR and a separate explicit owner approval.

## What was implemented in the repository

- RAHM architecture README, owner monitoring commands and private repository provisioning template.
- Candidate manifest JSON Schema and owner-only public control-plane index.
- CHILD-CANDIDATES landing-area contract.
- Python candidate validator/stager with allowlisted file extensions, fixed destination, manifest identity checks, exact SHA-256 and byte-count checks, size limits, secret-pattern checks, symlink/path-traversal rejection, required evidence files, and explicit owner-redaction/Child authorization attestations.
- Unit tests for valid staging and key negative cases.
- Owner-only workflow_dispatch that checks the caller is the repository owner and the ref is main; reads the private RAHM repository; verifies it is private; validates the candidate; uses a narrowly scoped GitHub App token to create a bot-authored branch and PR into CHILD. It does not merge, does not auto-merge, and does not edit the living Master.
- Hard-audit corrections: direct-to-main evidence and registration automation was removed or converted to read-only/artifact-only behavior; unnecessary contents:write permissions were removed from read-only validation workflows; portable conformance retains it only to publish the canonical ZIP release and never pushes to main.
- Legacy host adapter is fully disabled and fail-closed; no GitHub API request or write is attempted.

## Live security facts and remaining gates

- main is protected and the active Ruleset 27814009 requires PRs and blocks deletion/non-fast-forward updates.
- Live required approval count remains 0; Code Owner review remains OFF; stale-review dismissal and review-thread resolution remain OFF. The required owner approval is not yet enforced.
- CODEOWNERS assigns every path to @ahmadnezhadhosseini64-cloud.
- The authenticated GitHub connector identity is the same owner account. It can perform owner-authorized repository operations; it is not a separate bot identity.
- The bot PR route is implemented in code but NOT operational until the private RAHM repo, GitHub App, variables/secrets, and private-repo connector access are configured.
- The private RAHM repository is NOT CREATED / NOT VERIFIED. No promotion App is installed. No host is registered or ACTIVE.
- ChatGPT can inspect RAHM records only after its GitHub connection is granted read access to the private RAHM repository. Direct live inspection of an individual host workspace additionally requires read access to that exact host-private repository; otherwise review is snapshot-based from owner exports.
- Collaborator/team/App/deploy-key audit and negative cross-host tests remain OPEN / NOT VERIFIED.
- ChatGPT can perform technical review on accessible proposals and report findings; the final GitHub approval remains the owner's account. No AI or Bot can self-approve or auto-merge.

## Acceptance condition

Do not mark HOST_SECURITY_VERIFIED, RAHM_OPERATIONAL, or PROMOTION_GATE_ACTIVE until:
1. private RAHM repo exists and is read-back verified PRIVATE;
2. owner-only access is verified and ChatGPT connector can read it on command;
3. promotion GitHub App is installed only on master with Contents:write and Pull requests:write, no bypass;
4. required repository variables/secrets are configured without exposing credentials;
5. the workflow completes a real bot-authored PR from a synthetic candidate;
6. the owner approves that PR and the Ruleset read-back confirms approval=1 and Code Owner review=true;
7. negative tests prove no host can access another host, RAHM, or master-write.
