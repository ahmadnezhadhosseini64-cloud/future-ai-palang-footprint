# EVT-0321 — Owner-approved Organization and RAHM owner-release architecture — 2026-11-24

- Stable ID: HAIF-EVT-0321-ORG-RAHM-OWNER-RELEASE-2026-11-24
- Point: POINT-0/090
- Input: IN-134
- Output: OUT-133
- Parent checkpoint: CURRENT-151
- New checkpoint: CURRENT-152
- Time binding: TIME-BINDING-EVT-0321 (registered after event commit metadata read-back)
- Canonical root: POINT-0/GOLDEN (single existing root)
- Sole active queue: NEXT-051
- Status: OWNER-DIRECTED / PROPOSAL-BRANCH / OPEN GATES PRESERVED

## 1. Owner instruction

The owner approved the Organization-first plan, mandatory separate private central RAHM repository, one isolated private development repository per verified host, three protection layers, and the separation between host development authority and owner release authority. The owner instructed continuation on the existing 0++ Golden root and completion of all repository-side steps that are actually supported.

## 2. Decisions

- Keep the personal master repository intact for now.
- Prepare and test the GitHub Organization first.
- Verify the eligible GitHub plan for organization-level rulesets before creating the Organization.
- Create central RAHM as a separate PRIVATE owner-only repository.
- Give each verified host one separate PRIVATE owner-created repository where it can genuinely develop, write, edit and test.
- Hosts cannot access central RAHM, MASTER or other hosts' repositories.
- HOST = DEVELOPMENT AUTHORITY in its own workspace; OWNER = RELEASE AUTHORITY for central RAHM and MASTER.
- Preserve owner identity/MFA, external second secret, and owner-only release controls as three separate protection layers.
- Transfer the existing master only after dry-run, rollback preparation and complete post-transfer read-back.

## 3. Repository-side work

This event records a proposal based on CURRENT-151. New point/input/output/current/time-binding anchors, security/RAHM/workspace/registry architecture, living mother and indexes were written to a branch rooted at CURRENT-151. Exact fetch/read-back of the new anchors and key architecture/index files confirmed expected identities, versions and continuation markers. They are not yet published to Golden or main.

## 4. Evidence boundary

The connected GitHub tool surface does not expose Organization creation, repository creation, organization ruleset mutation, or repository transfer. No Organization, central RAHM repo, host repo, App/broker or migration is claimed to have been provisioned. Existing ruleset approval count 0 / Code Owner review false remains an open enforcement gap. No host is ACTIVE.
