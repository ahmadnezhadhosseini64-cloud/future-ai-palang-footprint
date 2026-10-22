# حاکمیت همگام‌سازی آینه و چرخهٔ ثبت زنده

## شناسنامه
- Stable ID: PALANG-MIRROR-SYNC-GOVERNANCE-2026-10-22-001
- Production ID: MSYNC-HAIF-2026-10-22-001
- Version: 1.0.0
- Project: Future AI / Palang Footprint / HAIF
- Owner: احمد پلنگ / Ahmad Nezhadhosseini
- Project location metadata: گنبد کاووس، ایران
- Status: ACTIVE / LIVING / OPEN
- Repository path: docs/architecture/BEHAVIOR-OBSERVATORY/MIRROR-SYNC-GOVERNANCE-AND-LIVE-REGISTRATION-2026-10-22-001.md
- Related event: EVT-0038
- Current test: LIVE-DESTINATION-STABILITY-AUDIT-2026-10-22-001
- Canonical timestamp rule: the actual repository commit timestamp in UTC is canonical for repository registration; Asia/Tehran is derived from the same instant (+03:30). Message, operation, test and read-back times remain distinct evidence; if unavailable, record UNKNOWN / UNVERIFIED.

## 1. Purpose
Keep the repository reference and its Library mirror aligned through a repeatable, evidence-based process. “Mirror active” means the synchronization workflow is active; it does not mean every destination or every artifact is automatically verified.

## 2. Source of truth and mirror scope
- Canonical source: the exact file at its recorded path on the repository's default branch.
- Mirror destination: /Future AI/Palang Footprint/Master Reference Vault/Reference Documents/.
- Sync scope is file/version-specific. Never infer that the whole Library, Buffer, Persistent Memory or Dropbox is synchronized from one file's success.
- Do not overwrite an older independent 0.0 anchor or erase provenance. New records append and link; they do not replace prior anchors unless an explicit migration is documented.

## 3. Mandatory synchronization lifecycle
1. PRESERVE — retain the existing source and previous mirror evidence.
2. IDENTIFY — record Stable ID, Production ID, Version, repository path and mirror path.
3. READ SOURCE — fetch the exact repository file and record its blob SHA.
4. WRITE MIRROR — copy the exact same source snapshot to the target Library path; use overwrite only for the exact same artifact/path.
5. READ-BACK MIRROR — reopen the Library artifact by its returned file/library ID, not merely by its displayed name.
6. MATCH — compare the full content or a reliable content fingerprint and verify Stable ID, Version and key sections.
7. VERIFY — mark that exact file/version as REGISTERED / READ-BACK VERIFIED only when write and read-back evidence exist.
8. RECONCILE — if content differs, do not mark synced; preserve both fingerprints, classify drift, and repeat from the latest canonical source.
9. REGISTER EVENT — append event ID, repository commit SHA/time, source blob SHA, Library item ID/path/modified time, read-back result, and any limitations.
10. UPDATE INDEXES — link this policy and event from the observatory, integration queue and 0.0 index; read them back.
11. STATUS — report each destination separately.
12. RESUME — retain the next incomplete action and recovery pointer.

## 4. State machine
- PENDING: sync not attempted.
- WRITE-ACCEPTED: destination accepted a write, but no read-back proof yet.
- READ-BACK VERIFIED: exact artifact was reopened and key content matched.
- DRIFT: source and mirror differ; reconciliation required.
- BLOCKED: a needed connector/action is unavailable.
- NOT VERIFIED: evidence is insufficient.
- ACTIVE / LIVING: workflow remains open for future changes and sync checks; this is not a claim that all targets are verified.

## 5. Per-destination rule
Repository, Library, Buffer, Persistent Memory and Dropbox each require their own WRITE → READ-BACK → MATCH → VERIFY evidence. Success in one does not propagate to another. If a destination is inaccessible, preserve a complete recoverable reference and leave that destination OPEN / NOT VERIFIED.

## 6. Trigger and cadence
Run a mirror sync whenever a governed reference file changes, when a new independent test or anchor is added, or when a discrepancy is detected. For a file already mirrored, compare the repository blob SHA/content to the Library read-back; a different source version means the mirror is stale until synchronized. Never claim a live background watcher or automatic synchronization unless an actual automation is configured and verified. This process is currently active as a manual evidence-backed workflow, not an always-running background service.

## 7. Acceptance checklist
- [ ] Source path and Stable ID confirmed.
- [ ] Repository commit SHA and UTC timestamp captured; Tehran derived from same instant.
- [ ] Source blob SHA captured.
- [ ] Exact mirror write accepted.
- [ ] Mirror read-back performed by returned identifier.
- [ ] Full content/fingerprint and version matched.
- [ ] Event and indexes updated and read back.
- [ ] All other destinations independently statused.
- [ ] Next action and unresolved limitations retained.

## 8. Current destination baseline at activation
- Repository: available; this policy and its event must be read back after registration.
- Library: prior audit artifact was independently written and read back; this policy's exact-version mirror requires its own write/read-back.
- Buffer: NOT VERIFIED.
- Persistent Memory: NOT VERIFIED.
- Dropbox: OPEN / NOT VERIFIED; connection, write and retrieve test pending.
- Isolated end-to-end recovery: NOT RUN.

## 9. Active continuation
1. Complete this policy's repository write/read-back and mirror write/read-back.
2. Reconcile the policy/event links in observatory, integration queue and 0.0 index.
3. Continue BOART-FOLLOWUP-01: full master-reference and historical graph audit.
4. Continue BOART-FOLLOWUP-02: actual Dropbox connection, test write, retrieval and content match.
5. Continue BOART-FOLLOWUP-03: isolated external recovery test without damaging the production repository.

## 10. Governed flow
PRESERVE → IDENTIFY → READ SOURCE → WRITE MIRROR → READ-BACK → MATCH → VERIFY → RECONCILE → REGISTER EVENT → UPDATE INDEXES → STATUS → RESUME

حفظ → شناسایی → خواندن منبع → نوشتن آینه → بازخوانی → تطبیق → تأیید → همسان‌سازی → ثبت رویداد → به‌روزرسانی نمایه‌ها → تعیین وضعیت → ادامه.
