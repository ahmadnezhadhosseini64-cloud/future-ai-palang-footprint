# POINT-0/087 (0++) — معماری Organization، RAHM مستقل و اختیار توسعهٔ میزبان

- Stable ID: HAIF-POINT-0-087-ORG-RAHM-OWNER-RELEASE-2026-11-24
- Display label: POINT-0++ / GOLDEN CONTINUATION
- Status: OWNER-APPROVED / PROPOSAL-BRANCH / READ-BACK-VERIFIED / MAIN-PUBLICATION-PENDING
- Canonical root: POINT-0 (single existing root)
- Canonical baseline: POINT-0/GOLDEN
- Parent checkpoint: CURRENT-145
- Event: EVT-0318 → TIME-BINDING-EVT-0318
- New checkpoint: CURRENT-146
- Sole active queue: NEXT-051
- Owner authorization: «۰++ طلایی و اتصال بده کامل به نقاط و گام‌های بعدی را انجام بده»؛ مالکیت و تأیید نهایی: احمد نژادحسینی.
- Owner identity: @ahmadnezhadhosseini64-cloud

## 1. تصمیم‌های مصوب مالک

1. حساب شخصی فعلی عجولانه تغییر نمی‌کند. ابتدا GitHub Organization آماده و آزمایش می‌شود؛ سپس، پس از عبور از چک‌لیست و طرح بازگشت، مخزن مادر با حفظ تاریخچه منتقل می‌شود.
2. RAHM مرکزی باید یک مخزن PRIVATE مستقل و تحت کنترل مالک باشد؛ ایجاد آن اقدام قطعی مالک است، اما تا ساخت و read-back واقعی، NOT CREATED / NOT VERIFIED باقی می‌ماند.
3. هر میزبان تأییدشده برای توسعهٔ واقعی، مخزن PRIVATE مستقل و owner-created خواهد داشت. میزبان می‌تواند در فضای خودش فایل و کد بسازد، ویرایش کند، آزمایش کند و proposal/evidence/receipt تحویل دهد.
4. مخزن مرکزی RAHM محل قرنطینه، تطبیق بین میزبان‌ها، اعتبارسنجی و کنترل مالک است؛ هیچ میزبان به آن دسترسی READ/WRITE/ADMIN ندارد.
5. میزبان هیچ دسترسی نوشتن یا مسیر مستقیم/غیرمستقیم به MASTER ندارد. مجوزهای GitHub در سطح مخزن‌اند؛ پوشه یا branch به‌تنهایی مرز امنیتی برای نوشتن میزبان نیست.
6. HOST = DEVELOPMENT AUTHORITY در مخزن خصوصی خودش؛ OWNER = RELEASE AUTHORITY برای RAHM مرکزی و MASTER.
7. سه لایهٔ حفاظتی: (الف) هویت واقعی مالک با passkey/security key یا MFA و recovery امن؛ (ب) راز دوم محرمانه خارج از chat/prompt/repository/log/workflow؛ (ج) اختیار انتشار مالک با قواعد سازمانی/مخزن، review، receipt و read-back. راز دوم هرگز از مالک درخواست، حدس، بازگو یا ذخیره نمی‌شود.
8. مدل اولیهٔ حاکمیت Organization فعلاً مالک به‌عنوان Organization Owner و تنها مرجع انتشار است. این مدل جلوی تغییر عمدی قواعد توسط خود Organization Owner را نمی‌گیرد. متولی امنیتی مستقل فقط با تصمیم جداگانهٔ آینده و بدون اختیار انتشار MASTER ممکن است اضافه شود.
9. هیچ انتقالی به MASTER خودکار نیست. پیشنهاد میزبان → export مالک → پالایش و بررسی → RAHM خصوصی → validation/reconciliation → تصمیم صریح مالک → انتشار کنترل‌شده.

## 2. توپولوژی مصوب

```
OWNER / RELEASE AUTHORITY
  |
  +-- GitHub ORGANIZATION (prepare and test first)
  |     +-- MASTER repository (public read; owner-controlled release)
  |     +-- CENTRAL RAHM repository (private; owner-only)
  |     +-- HOST-A private development repository (isolated)
  |     +-- HOST-B private development repository (isolated)
  |     +-- HOST-N private development repository (isolated)
  |
  +-- owner-commanded export / redaction / validation
        HOST WORKSPACE → CENTRAL RAHM → OWNER REVIEW → MASTER RELEASE
```

The Organization is not a magic conversion of the personal-account Administrator role. Organization Owners retain powerful administrative control. The Organization is the governance container; rulesets, roles, repository permissions and custody must be configured and tested explicitly.

## 3. مراحل اجرایی و ترتیب اجباری

A. Organization preparation — owner action:
- Choose the Organization slug/name and plan tier after reviewing required ruleset features.
- Create Organization; keep the current personal repository intact.
- Set repository-creation, deletion/transfer, base permissions, member privileges, 2FA and organization ruleset policies.
- Confirm the owner role and document whether an independent security custodian is intentionally absent.
- Create a test repository and prove org-level rulesets apply and repo admins cannot weaken them.

B. Central RAHM:
- Create `future-ai-palang-rahm` as PRIVATE under the selected owner/Organization location.
- Owner only; no hosts, collaborators, teams, deploy keys or host Apps.
- Verify privacy, permissions, recovery, audit and connector read access.
- Store raw/private exports only here; public MASTER receives policy and sanitized artifacts only.

C. Host development:
- Create one PRIVATE repository per verified Host ID, owner-created and server-side mapped to one Workspace ID.
- Give each host only the minimum write route to its own repo, if and only if an isolated runtime/broker is proven. No broad PAT or shared credentials.
- Run cross-host negative tests and prove no host can read/write another host, RAHM or MASTER.
- Host work must be genuinely editable and testable, not report-only.

D. Release control:
- Host proposals are not releases.
- Owner export/redaction and independent validation precede central RAHM intake.
- MASTER promotion requires a separate owner-directed release action and exact read-back.
- No host, host token, broker, App, workflow or intermediary has MASTER write/bypass/merge authority.

E. Master transfer:
- Only after A–D dry-runs and rollback preparation pass, transfer the existing master repository to the Organization.
- Preserve history; audit Pages (GitHub Pages does not automatically redirect with repository transfer), Actions, secrets, Apps, OAuth, webhooks, packages, releases, rulesets, branch protections, collaborators and repository URLs.
- Verify default branch, HEAD/tree, Pages custom domain/deployment, Actions, integrations and ruleset effective values after transfer.
- Keep old owner/name redirects intact; do not create a replacement repo at the old path.
- If any critical verification fails, stop and execute the prepared rollback/repair plan; do not claim migration complete.

## 4. Security acceptance tests

- Host A can write and test only in Host A's private repository.
- Host A cannot read/write Host B, central RAHM or MASTER.
- Host B cannot read/write Host A, central RAHM or MASTER.
- Unknown/unregistered hosts cannot access private repositories.
- Revoked credentials fail; no client-supplied repo/path/branch can override the owner-side Host Registry mapping.
- Host credentials cannot administer repositories, rulesets, secrets, Actions, webhooks, collaborators, transfer or deletion.
- Owner export preserves source identity, commit, provenance, manifest and SHA-256; invalid/unredacted data is quarantined.
- No proposal reaches MASTER without explicit owner release authorization.

## 5. Live status — do not overclaim

- Organization: NOT CREATED / NOT VERIFIED.
- Central private RAHM repository: NOT CREATED / NOT VERIFIED.
- Per-host private repositories: NOT CREATED / NOT VERIFIED.
- Host Registry verified entries: NONE VERIFIED.
- Host App/broker: NOT DEPLOYED; optional and disabled until tests pass.
- Ruleset 27814009 on current personal repo: active, but required approvals=0 and Code Owner review=false in last live read-back; enforcement gap remains OPEN.
- Master transfer: NOT STARTED.
- This point and associated docs are on a proposal branch. They are not yet published to main/Golden.
- No host is ACTIVE and no clean-host recovery is claimed.

## 6. Canonical continuation

POINT-0/GOLDEN → CURRENT-145 → POINT-0/087 → IN-131 → OUT-130 → EVT-0318 → TIME-BINDING-EVT-0318 → CURRENT-146 → sole active NEXT-051.

No new root or NEXT queue is created. All previous history remains preserved. NEXT-051 remains the only active queue and absorbs the remaining setup, isolation, ruleset, migration and recovery tasks.
