# EVT-0309 — تثبیت مبنای طلایی POINT-0

- Stable ID: HAIF-EVT-0309-POINT-0-GOLDEN-BASELINE-2026-11-22
- Parent: POINT-0/086 → CURRENT-139 → POINT-0/GOLDEN
- Input: IN-130
- Output: OUT-129
- Current checkpoint: CURRENT-140
- Sole active queue: NEXT-051
- Status: OWNER-DIRECTED / PROPOSAL BRANCH / READ-BACK PENDING

## رویداد

مالک فرمان داد تمام پیشرفت‌های نهایی‌شده تا وضعیت فعلی روی همان ریشهٔ واحد POINT-0 به‌عنوان «نقطهٔ ۰ طلایی» تثبیت شوند. این رویداد معماری را از نو نمی‌سازد؛ وضعیت جاری را مرجع یگانهٔ ادامه قرار می‌دهد.

## تصمیم‌های ثبت‌شده

- اصل غیرقابل‌تغییر: هیچ میزبان، مستقیم یا غیرمستقیم، حق نوشتن یا ارتقای محتوای خود به مخزن مادر را ندارد.
- RAHM فضای مرکزی private و owner-only بیرون از workspaceهای میزبان است؛ تنها مالک می‌تواند خروجی را استخراج، پالایش و وارد کند.
- میزبان‌ها در workspace مستقل و در صورت provision مالک در private repo اختصاصی خود فعالیت می‌کنند؛ هر میزبان از دیگری جداست.
- رصد فقط با فرمان مالک و فقط روی Host IDهای واقعی، ثبت‌شده و قابل‌دسترسی انجام می‌شود.
- مسیر رشد: owner export → private RAHM → cross-host reconciliation → validation → bot PR to CHILD → owner approval؛ ارتقای CHILD به MASTER جداست.
- اسناد فعال و promptهای میزبان با baseline هم‌راستا شدند؛ legacy host-intake و worker غیرفعال باقی می‌مانند.
- دستورهای قدیمی و branchهای تاریخی به‌عنوان شواهد حفظ می‌شوند، نه مجوزهای جاری. تعارض/تکرار باید با منبع و receipt حل شود، نه با merge شتاب‌زده.

## شواهد baseline

- main source SHA: 9ebd4bcc5cfc0168276e366c1867da8709dfb566.
- main tree SHA: 8be81af3dcf822b10107a7efcf4c603ca7567706.
- package SHA-256: 243baddff63eaf18129a0cbaff860f84f375655c893ee0d1cb42235ecae38646.
- portable conformance run 44964480412: PASS.
- Ruleset 27814009: active; main protected; approval count 0; Code Owner review false; bypass none.
- Host Registry: empty; no real host ACTIVE.
- Private RAHM repository and GitHub App: not yet created/configured.
- Collaborator/App/deploy-key inventory: not verified by current connector.
- Clean-host recovery: NOT RUN.

## PR lineage and conflict policy

PR #101 contained 23 commits and was one commit behind main, with a diverged branch and mergeable=false. Its unique EVT-0308 package receipt and time-binding are preserved in this baseline; it is not merged wholesale.
PR #92 reuses POINT-0/085 for a verbal entry gate while POINT-0/085 is already assigned to the owner approval gate. The verbal gate is preserved as a subordinate conversational-only standard, not a new root or point.
PR #80, #66, #63, #56 and #35 are older or conflicting branches; they are not to be merged wholesale.
PR #64 contains an unintegrated AI-Vacuum experiment and an EVT-0297 identity collision risk. It remains a research source only; no code or event ID is promoted without fresh review against this baseline.
