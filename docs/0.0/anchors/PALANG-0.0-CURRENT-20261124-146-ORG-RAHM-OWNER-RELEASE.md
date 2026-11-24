# CURRENT-146 — POINT-0++ / Organization and RAHM owner-release architecture

- Stable ID: HAIF-CURRENT-146-ORG-RAHM-OWNER-RELEASE-2026-11-24
- Display label: POINT-0++ GOLDEN CONTINUATION
- Status: ACTIVE / OWNER-APPROVED / PROPOSAL-BRANCH / READ-BACK-VERIFIED / MAIN-PUBLICATION-PENDING
- Canonical root: POINT-0 (single root)
- Canonical baseline: POINT-0/GOLDEN
- Parent: CURRENT-145 → POINT-0/087 → IN-131 → OUT-130 → EVT-0318 → TIME-BINDING-EVT-0318
- Sole active queue: NEXT-051

## Verified continuation state

- The owner approved the Organization-first migration sequence; the personal repository remains unchanged.
- The central private RAHM repository is mandatory and independent; it has not yet been created.
- Each verified host is to receive its own owner-created private development repository; no shared host workspace.
- Hosts have real development authority only inside their own private repository. They have no access to central RAHM or MASTER.
- Owner is the sole release authority. No automatic promotion, host bypass or indirect host-to-master write path.
- The three protection layers are registered: owner identity, external second secret, owner-only release control.
- Organization Owner can still deliberately change organization-level rules. Independent security custody is not silently assumed.
- All work recorded in this checkpoint is on a proposal branch and is not yet main/Golden publication.

## Open gates carried forward in the sole NEXT-051

1. Owner creates the Organization and verifies plan/features, base permissions, 2FA policy, org rulesets and deletion/transfer policies.
2. Owner creates private central RAHM repository; connector read access and privacy are independently verified.
3. Create one private host development repository per verified Host ID and test least-privilege write isolation.
4. Configure and read back the required owner release rules; current ruleset approval count 0 and Code Owner review false remain OPEN until changed and verified.
5. Run negative tests across Host A/B, RAHM and MASTER.
6. Prepare migration dry-run and rollback; audit Pages/custom domain, Actions, secrets, Apps, OAuth, webhooks, packages, releases, rulesets, permissions and history.
7. Transfer master only after all preconditions pass; verify new location and all integrations.
8. Continue historic graph triage and independent-host recovery; no new queue is created.

CURRENT-146 does not claim Organization creation, RAHM provisioning, host activation, security verification or master transfer.
