# CURRENT-152 — POINT-0++ / Organization-first and owner-controlled RAHM architecture

- Stable ID: HAIF-CURRENT-152-ORG-RAHM-OWNER-RELEASE-2026-11-24
- Status: ACTIVE / OWNER-APPROVED / GOLDEN-WORKING-BRANCH-MERGED / SOURCE-READ-BACK-VERIFIED / CI-NOT-VERIFIED / MAIN-PUBLICATION-PENDING / IMPLEMENTATION-PARTIAL
- Canonical root: POINT-0
- Golden baseline: POINT-0/GOLDEN
- Parent: CURRENT-151 → POINT-0/090 → IN-134 → OUT-133 → EVT-0321 → TIME-BINDING-EVT-0321
- Sole active queue: NEXT-051
- Owner: @ahmadnezhadhosseini64-cloud

## Current decision state
- Organization-first migration approved; current personal master is not transferred until dry-run and rollback checks pass.
- Central RAHM must be a separate PRIVATE owner-only repository.
- Each verified host gets one separate PRIVATE owner-created development repository; hosts can genuinely write, edit, test and prepare proposals only in their own workspace.
- Hosts have no access to central RAHM, MASTER or other hosts' repositories.
- HOST = DEVELOPMENT AUTHORITY in own workspace; OWNER = RELEASE AUTHORITY for central RAHM and MASTER.
- Three layers: owner identity/MFA; external second secret; owner-only release controls.
- Organization Owner can still deliberately change organization rules. Independent security custody is not appointed by this decision.
- Organization-level repository rulesets require an eligible plan; verify GitHub Team/Enterprise feature access before Organization setup.

## Execution gates carried in sole NEXT-051
1. Owner creates Organization and verifies eligible plan, organization slug, roles, base permissions, 2FA, repository policies and org rulesets.
2. Test that organization-level rulesets protect repositories and repo admins cannot weaken them.
3. Owner creates central PRIVATE `future-ai-palang-rahm`; read back privacy, repository ID/full name, access list, Apps, deploy keys and connector access.
4. Create one private host repository per verified Host ID; verify each host's write boundary and cross-host denial.
5. Configure owner release controls and read back required review, Code Owner, stale-review dismissal and conversation resolution.
6. Run negative tests for host→MASTER, host→RAHM, host A↔host B, revoked credentials and admin-surface denial.
7. Prepare migration inventory and rollback; audit Pages/custom domain, Actions, secrets, Apps, OAuth, webhooks, packages, releases, rulesets, permissions and history.
8. Transfer master only after all gates pass; then verify repository identity, history, HEAD/tree, Pages, Actions, integrations and rulesets.
9. Run exact-Golden conformance and independent-host recovery after the relevant changes.

## Non-claims
Organization, central RAHM, host repos, App/broker and master transfer are NOT CREATED / NOT VERIFIED. Ruleset enforcement is not complete. No host is ACTIVE. This checkpoint is proposal-only until merged into the existing Golden lineage and read back.


## Golden working branch publication receipt

- PR #159: MERGED.
- Target branch: `work/current151-exact-golden-verify-20261122`.
- Merge commit: `3d1dd8baed7f0ff1ebc2a12daa53786d2e16e4b8`.
- Commit time: UTC `2026-11-24T06:38:33Z`; Tehran `2026-11-24T10:08:33+03:30`.
- Main/MASTER publication: NOT PERFORMED.
- Workflow runs on the merge commit: none returned. CI and exact-Golden conformance remain NOT VERIFIED.
- PR #158: CLOSED / SUPERSEDED / UNMERGED; it was based on the stale CURRENT-145 pointer and duplicate identifiers.
