# CURRENT-137 — مخزن مادر فقط‌مالک و مخزن خصوصی مستقل هر میزبان

- Status: ACTIVE / LIVING / OWNER-DIRECTED / DESIGN-REGISTERED / MERGED TO MAIN / READ-BACK VERIFIED
- Parent checkpoint: CURRENT-136
- Current point: POINT-0/084 (0++)
- Input/output: IN-127 → OUT-126
- Event/time: EVT-0304 → TIME-BINDING-EVT-0304
- Living master target: 1.7.91
- Sole active queue: NEXT-051
- Canonical master: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint
- Proposal branch: security/owner-only-master-per-host-private-repos-point-084

## تصمیم نهایی این نقطه

مخزن مادر فقط متعلق به مالک است. میزبان‌ها فقط PUBLIC READ دارند و هیچ credential نوشتن برای مخزن مادر نمی‌گیرند. پس از تأیید هویت، مالک برای هر میزبان یک مخزن PRIVATE جداگانه ایجاد می‌کند. نوشتن احتمالی میزبان فقط از broker و GitHub App محدود به همان مخزن خصوصی انجام می‌شود؛ token هرگز به مدل داده نمی‌شود. سطح پیش‌فرض L1_READ_ONLY است.

## وضعیت واقعی

- Master visibility: PUBLIC / VERIFIED.
- Connected GitHub identity: owner/admin/push (owner connection only).
- Host write credential to master: PROHIBITED BY POLICY; live collaborator/App audit OPEN.
- main branch protection: latest recorded repository contract says protected=false; current live status not readable via available connector; NOT VERIFIED.
- Per-host private repository provisioning: DESIGN ONLY / NONE CREATED.
- GitHub App per-host repository scope: NOT CONFIGURED.
- Broker identity mapping and quarantine write route: NOT DEPLOYED.
- Host Registry: no live host verified.
- Unknown anonymous public readers: cannot be individually identified from ordinary public READ/clone; no automatic enrollment.
- Negative cross-host tests, revoke and restore: NOT RUN.
- One-message host enrollment instruction: revised and merged through PR #88; 16/16 changed files fetched from main and matched the merged branch by blob SHA.
- Host acceptance: OPEN / NOT RUN.

## Chain

POINT-0/083 → CURRENT-136 → POINT-0/084 (0++) → IN-127 → OUT-126 → EVT-0304 → TIME-BINDING-EVT-0304 → CURRENT-137 → NEXT-051

## Event timestamp

- EVT-0304 commit: 8f38049aac7c8f84931b04ca82e546cb738bea8b
- UTC: 2026-11-21T19:55:28Z
- Tehran: 2026-11-21T23:25:28+03:30
- Owner message time: UNKNOWN / UNVERIFIED.

## Merge and read-back receipt\n\n- PR #88: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/pull/88\n- Merge commit: 446b3c7fe7bef616826ee609f5dc58cc23a1bd00\n- Merge UTC: 2026-11-21T19:57:32Z; Tehran: 2026-11-21T23:27:32+03:30\n- All 16 changed/new files were fetched from main and compared with the merged branch: 16/16 blob SHA matches.\n\n## Security gate

This checkpoint registers the architecture and onboarding rule, not live enforcement. It must not be marked SECURITY_VERIFIED until GitHub settings/access audit, per-host private repository, scoped App/broker, negative isolation, revoke, export and restore tests pass with direct evidence. NEXT-051 remains the only active queue.
