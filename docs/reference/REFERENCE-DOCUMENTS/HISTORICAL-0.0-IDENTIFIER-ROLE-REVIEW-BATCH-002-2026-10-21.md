# داوری معنایی دستهٔ دوم — شناسه‌های پایدار و Reference IDهای قدیمی

- Stable ID / شناسهٔ پایدار: HISTORICAL-0.0-IDENTIFIER-ROLE-REVIEW-BATCH-002-2026-10-21
- Production ID / شناسهٔ تولید: H0IRRB2-2026-10-21-001
- Version: 1.0.0
- Date: 2026-10-21
- Exact user-message time: UNKNOWN / UNVERIFIED
- Status: ACTIVE / LIVING / PARTIAL
- Parent: [H0IRAR — دفتر داوری گروه‌ها](./HISTORICAL-0.0-IDENTIFIER-AND-RELATION-ADJUDICATION-REGISTER-2026-10-21-001.md)
- Fresh parser evidence: [run 39517920781](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/actions/runs/39517920781)
- Audited commit: `07c0915db52e66061c7c905081c2bfe77a32e807`
- Audit UTC: `2026-10-20T23:53:43Z`

## 1. Parser correction that changes the semantic model

The expanded extractor previously treated generic `Reference ID` labels as if they were Stable IDs. This mixed two identifier namespaces and produced false Stable-ID collision groups. The parser now emits `REFERENCE_ID` separately from `STABLE_ID`; those IDs remain usable for lineage/parent resolution but are not silently relabeled as Stable IDs.

The fresh workflow passed with:
- 500 source files, 500 text nodes, 0 decode errors;
- 1,020 local Markdown edges, 0 missing links;
- 38 declared parent edges, 0 unresolved/ambiguous;
- 30 Stable ID groups, 43 Production ID groups, 7 Reference ID groups, 8 EVT short-number groups, 11 exact-content duplicate groups;
- 695 line-level identifier occurrences.

This is an improved extraction model. It does not itself decide every occurrence's meaning.

## 2. Stable ID decisions — five additional groups

### S-03 — Fifth certificate attachment

- Definition: `docs/reference/REFERENCE-DOCUMENTS/گواهی/گواهی های ارسالی اولیه/نقطه ۰.۰ پنجم - گواهی چکیده پیوست شماره ۲.md`, line 4, explicitly declares Stable ID `CERTIFICATE-INBOX-0.0-FIFTH-ATTACHMENT-02-2026-10-19-001`.
- Reference/catalog occurrence: the certificate-inbox `README.md`, line 180, lists the same Stable ID inside its inventory.
- Decision: point file = DEFINES; README entry = REFERENCES/CATALOGS. Not a true identity conflict.

### S-04 — Third certificate checkpoint

- Definition: `docs/reference/REFERENCE-DOCUMENTS/گواهی/گواهی های ارسالی اولیه/نقطه ۰.۰ سوم - ثبت کامل صندوق گواهی.md`, line 7, declares Stable ID `CERTIFICATE-INBOX-0.0-THIRD-2026-10-19-001`.
- Reference/catalog occurrence: certificate-inbox `README.md`, line 102, lists the checkpoint Stable ID.
- Decision: checkpoint file = DEFINES; README entry = REFERENCES/CATALOGS. Not a true identity conflict.

### S-05 — Living anchoring registration and test governance

- Definition: `docs/reference/REFERENCE-DOCUMENTS/LIVING-ANCHORING-REGISTRATION-AND-TEST-GOVERNANCE-2026-10-20-001.md`, line 3, declares the Stable ID.
- Reference/catalog occurrence: `docs/REFERENCE_INDEX.md`, line 157, lists the same Stable ID and Production ID and links the reference document.
- Decision: reference document = DEFINES; index entry = REFERENCES. Not a true identity conflict.

### S-06 — Interaction registration and gap closure

- Definition: `docs/reference/REFERENCE-DOCUMENTS/INTERACTION-REGISTRATION-AND-GAP-CLOSURE-2026-10-20-001.md`, line 4, declares Stable ID `INTERACTION-REGISTRATION-AND-GAP-CLOSURE-2026-10-20-001`.
- Reference/catalog occurrences: `docs/REFERENCE_INDEX.md`, line 134, and `docs/architecture/INTEGRATION-QUEUE/README.md`, line 687, list the ID and point to the reference document.
- Decision: reference document = DEFINES; index and integration queue = REFERENCES/OPEN-WORK TRACKING. Not a true identity conflict.

### S-07 — Three-layer registration architecture

- Definition: `docs/reference/REFERENCE-DOCUMENTS/THREE-LAYER-SYNCHRONOUS-DURABLE-REGISTRATION-2026-10-06-001.md`, line 3, declares Stable ID `THREE-LAYER-REGISTRATION-ARCHITECTURE-2026-10-06-001`.
- Reference occurrence: `docs/reference/REFERENCE-DOCUMENTS/NO-LOSS-REGISTRATION-DURABLE-OVERFLOW-2026-10-06-001.md`, line 188, mentions the same Stable ID inside a later explanatory section; it is not the front-matter identity of that No-Loss document.
- Decision: synchronous durable registration document = DEFINES; No-Loss overflow document = REFERENCES/DEPENDS_ON. Not a true identity conflict.

## 3. Legacy Reference ID namespace — all seven groups triaged

These are `Reference ID` occurrences, not Stable ID groups. The new extractor keeps this namespace separate.

| Reference ID | Definition and relationship decision | Status |
|---|---|---|
| `MPPA-2026-09-28-001` | `architecture/memory/MEMORY-PERSISTENCE-PROOF-ARCHITECTURE-2026-09-28.md`, line 2, defines the older reference identity. The 2026-09-29 architecture references it as the prior version that the new architecture supersedes as current. Preserve the older record as historical lineage. | ROLE DECIDED; preserve as superseded historical reference |
| `MPPA-2026-09-29-002` | `architecture/memory/MEMORY-PERSISTENCE-PROOF-ARCHITECTURE-2026-09-29.md`, line 3, defines the newer reference identity. The older 2026-09-28 architecture mentions the newer ID in its body. | ROLE DECIDED; newer current-reference candidate |
| `REF-DRFR-2026-08-30-001` | `docs/reference/REF-DURABLE-REGISTRATION-FAILURE-RECOVERY-2026-08-30.md`, line 3, defines the reference record. `docs/architecture/DURABLE_REGISTRATION_FAILURE_RECOVERY.md`, line 5, declares it as the associated reference pointer for the architecture. | ROLE DECIDED; reference document defines, architecture references |
| `REF-GAPC-2026-08-31-001` | `docs/reference/REFERENCE-DOCUMENTS/MASTER-REFERENCE-GAPC-2026-08-31-001.md` and `provenance/MASTER-REFERENCE-GAPC-2026-08-31-001.md` have identical SHA-256 and identical Reference ID metadata. The reference-vault path is the canonical reference-role candidate; provenance path remains a mirror. | ROLE MIRROR DECIDED; canonical pointer still governed/provisional |
| `REF-ICG-2026-08-30-001` | `docs/reference/REF-INTEGRATION-COMPLETION-GATE-2026-08-30.md`, line 3, defines the reference record. `docs/architecture/INTEGRATION-COMPLETION-GATE.md`, line 4, points to it from the architecture. | ROLE DECIDED; reference document defines, architecture references |
| `REF-PRNT-2026-08-30-001` | `docs/reference/REF-PERMANENT-REGISTRATION-NOT-TRACE-2026-08-30.md`, line 3, defines the reference record. Architecture files `ARCH-PRNT-2026-08-30-001.md`, `PERMANENT_REGISTRATION_MATRIX.md`, and evidence file `EVIDENCE-PRNTP-2026-08-30-001.md` point to that Reference ID. | ROLE DECIDED; reference document defines, architecture/evidence reference |
| `REF-RRC-2026-08-30-001` | `docs/reference/REF-REGISTRATION-ROUTING-CLOSURE-2026-08-30.md`, line 3, defines the reference record. The verification-final, verification-v2, verification and provenance-registration-evidence files use the same ID to identify the record they verify/support. | ROLE DECIDED; reference document defines, verification/provenance records reference |

## 4. What is and is not closed

- Five additional Stable ID groups received bounded definition-vs-reference decisions (S-03 through S-07).
- Seven legacy Reference ID groups were classified in their own identifier namespace.
- No source files were deleted, renamed, or automatically merged.
- The 30 remaining Stable ID groups and 43 Production ID groups still require group-by-group review. The 7 Reference ID role decisions do not close all relationships in those files.
- EVT groups and exact-content duplicate groups retain their separate decisions/statuses.
- Structural links are navigational edges; the semantic claim of each edge still needs evidence review.
- The 991/1,009 historical link counts must be tied to their respective audited commits. Latest parser audit run 39517920781 reports 1,020 local links and 0 missing.

## 5. Read-back requirements

The next audit must confirm this new batch's local links and current metadata extraction. Each final semantic decision should be copied into the main group ledger with a link to this batch; this batch remains the detailed evidence record.

## Change log

- v1.0.0 — five additional Stable ID groups and all seven legacy Reference ID groups reviewed by source path, exact metadata line and relationship role.
