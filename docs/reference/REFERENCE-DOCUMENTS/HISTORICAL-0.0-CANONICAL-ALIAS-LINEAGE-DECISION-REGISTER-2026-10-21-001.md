# دفتر تصمیم‌های canonical / alias / lineage برای گراف تاریخی ۰.۰

- Stable ID: HISTORICAL-0.0-CANONICAL-ALIAS-LINEAGE-DECISION-REGISTER-2026-10-21-001
- Production ID: H0CALDR-2026-10-21-001
- Version: 1.0.0
- Project: Future AI / Palang Footprint — HAIF
- Owner: احمد پلنگ
- Status: ACTIVE / LIVING / PARTIAL — role-based mirror proposals registered; two ambiguous groups remain OPEN
- Parent master: [H0GLMR](./HISTORICAL-0.0-GRAPH-RECONCILIATION-LIVING-MASTER-REFERENCE-2026-10-21-001.md)
- Evidence findings: [H0GAF](./HISTORICAL-0.0-GRAPH-AUDIT-FINDINGS-2026-10-21-001.md)
- Latest structural manifest artifact available at creation: [Living Architecture Audit run 39509351339](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39509351339)
- Scope: repository only. No external storage destination is part of this register.

## 1. Decision policy

An identical SHA proves byte equality, not identical logical role. Canonical/alias decisions must preserve each path and role. A mirror may remain a first-class governance/provenance path while pointing to a canonical content node. No historical file is deleted or silently overwritten. This register records decisions as provisional until inbound links and lineage have been checked.

## 2. Exact-content duplicate groups

| Group | Canonical candidate / relationship | Other path(s) | Status and reason |
|---|---|---|---|
| SHA 4cf0b6b7be9aa5b989be1a7fdca7d481c3ee883436b70ac5ed0762565c961049 | `docs/governance/0.0-VAULT/0.0-VAULT-GOVERNANCE-2026-09-13.md` | `docs/reference/REFERENCE-DOCUMENTS/0.0-VAULT-GOVERNANCE-0.0V-2026-09-13-001.md` | PROPOSED MIRROR — governance path owns the operational policy role; reference-vault path retained as mirror |
| SHA 7023f4ce9e459b3acf0eeaf371c02103b4adce7554b5d1c4043edf42bb1b4f73 | `docs/governance/0.0-VAULT/PRODUCTION-REGISTRY-REFERENCE-2026-09-13.md` | `docs/reference/REFERENCE-DOCUMENTS/PRODUCTION-REGISTRY-REFERENCE-0.0V-REGREF-2026-09-13-001.md` | PROPOSED MIRROR — governance registry instruction remains canonical candidate; reference-vault copy retained |
| SHA 45140056b737bd503a0dc6490677afe3bdb0df9e59abfcc1c624e49f54cad500 | `checkpoints/0.0/0.0-VAULT-INITIAL-POINT-2026-09-13.md` | `docs/reference/REFERENCE-DOCUMENTS/0.0-VAULT-INITIAL-POINT-0.0V-INIT-2026-09-13-001.md` | PROPOSED MIRROR — checkpoint is the original continuation anchor candidate; reference copy retained |
| SHA 4944e965c2326ed54e8aeabb2814bb0f6bb6fc12641cf07540c93cc3ed823deb | `docs/governance/0.0-VAULT/LIVING-STATUS-2026-09-13.md` | `docs/reference/REFERENCE-DOCUMENTS/LIVING-STATUS-0.0V-LIVING-2026-09-13-001.md` | PROPOSED MIRROR — governance status path retained as canonical candidate |
| SHA 9cb520f4f1c27f5f6b79fdfb2c133883599665b2c9c952932cfb3441eae8c0e9 | `registry/0.0-VAULT-REGISTRY-2026-09-13.md` | `docs/reference/REFERENCE-DOCUMENTS/0.0-VAULT-REGISTRY-0.0V-REG-2026-09-13-001.md` | PROPOSED MIRROR — registry path retained as the live registry candidate; reference-vault copy preserved |
| SHA d3921368cf3ad35d6b428860c67ad47f4e395c731f9249dc7b84006614558dad | `architecture/0.0-VAULT-ARCHITECTURAL-PLACEMENT-2026-09-13.md` | `docs/reference/REFERENCE-DOCUMENTS/0.0-VAULT-ARCHITECTURAL-PLACEMENT-0.0V-ARCH-2026-09-13-001.md` | PROPOSED MIRROR — architecture path retained as the implementation/placement candidate |
| SHA 2d503cce1b2bad4533362da439d1668b6a4fb5fbafb6fcd6cf6c950ab93dfc95 | `docs/reference/REFERENCE-DOCUMENTS/GAP-CLOSURE-RETRIEVAL-EVIDENCE-2026-08-31-001.md` | `provenance/GAP-CLOSURE-RETRIEVAL-EVIDENCE-2026-08-31-001.md` | PROPOSED ROLE MIRROR — reference-vault document is the canonical reference candidate; provenance path remains for lineage/provenance role |
| SHA 8764cc78241e5b880cf277fa720e6bd13dd68d63e0e1856f1e7d101bbb7b588d | `docs/reference/REFERENCE-DOCUMENTS/ADIP-2026-08-31-001.md` | `provenance/ADIP-2026-08-31-001.md` | PROPOSED ROLE MIRROR — preserve the provenance copy; verify inbound links before final canonical promotion |
| SHA a0384763731682830b11f5678fa4c45bb7378f6b73fe5ca9eed202be77147a43 | `docs/reference/REFERENCE-DOCUMENTS/MASTER-REFERENCE-GAPC-2026-08-31-001.md` | `provenance/MASTER-REFERENCE-GAPC-2026-08-31-001.md` | PROPOSED ROLE MIRROR — formal reference-vault candidate plus retained provenance mirror |
| SHA 2b018d899aba7b4483a083e170eaea878cab9d024e24c53fc496f70fef4ac24f | `docs/registrations/REG-2026-09-03-GAP-CLOSURE-OUTCOME-003.md` | `docs/registrations/REG-2026-09-03-GAP-CLOSURE-OUTCOME-005.md` | PROPOSED ALIAS — identical SHA; commit 003 at 2026-09-03T03:46:46Z precedes 005 at 03:46:58Z; same commit message; zero inbound local Markdown links found in the manifest. Preserve 005 as historical alias; do not delete. |
| SHA 605b48decf4cbd0f87535b8cf78bf01b5362907f5094faac3886ba8f8da73f6f | `checkpoints/0.0/REG-2026-09-03-GAP-CLOSURE-OUTCOME-001.md` | `checkpoints/0.0/REG-2026-09-03-GAP-CLOSURE-OUTCOME-002.md` | PROPOSED ALIAS — identical SHA; commit 001 at 2026-09-03T03:46:17Z precedes 002 at 03:46:33Z; same commit message; zero inbound local Markdown links found in the manifest. Preserve 002 as historical alias; do not delete. |

## 3. Acceptance status

- 9 groups have a role-based canonical/mirror candidate recorded; they remain PROPOSED until inbound references and lineage are reviewed.
- 2 groups remain explicitly OPEN for human/commit-history adjudication.
- 11 groups are preserved; zero files deleted.
- Proposed alias edges must not be interpreted as fully merged or semantically verified edges.
- Next step: inspect inbound references and Git history for the two OPEN groups and the 9 proposed mirrors, then update statuses with evidence and read-back.

## 4. Relation to ID collisions

Repeated Stable IDs and Production IDs are occurrence groups, not automatically identity conflicts. Indexes, queues, checkpoints and events can legitimately mention a canonical identifier. Each occurrence must be classified as DEFINES, REFERENCES, MIRROR/COPY, SUPERSEDED, or UNRESOLVED before any ID rewrite. EVT number is not a unique key by itself; use full path + Stable ID + Production ID + SHA + lineage.

## 5. Change log

- v1.0.0 — first role-based review of all 11 exact-content duplicate groups reported by the downloaded JSON audit artifact.



## Manifest read-back acceptance
- Verified snapshot: [H0GMS-2026-10-21-001](./HISTORICAL-0.0-GRAPH-MANIFEST-SNAPSHOT-2026-10-21-001.md), audit run 39510053810.
- The manifest builder's 11 duplicate-group decisions now align with this register, including earliest-commit candidates for the two differently numbered outcome/checkpoint pairs; both later copies are preserved as aliases, with no local inbound links found in the audited manifest.
- These remain proposed canonical/mirror relationships pending final lineage review; they are not permission to delete files.



## Latest manifest acceptance evidence
- Latest successful structural run: [39510581209](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39510581209), recorded in [H0GMS v1.4.0](./HISTORICAL-0.0-GRAPH-MANIFEST-SNAPSHOT-2026-10-21-001.md).
- The manifest emitted all 11 duplicate-group decisions from this register, with no missing local links and no unresolved/ambiguous parent edges in that snapshot.
- Repeated ID occurrence groups and EVT-number collision groups remain separate from exact-content duplicate decisions; do not merge them automatically.
