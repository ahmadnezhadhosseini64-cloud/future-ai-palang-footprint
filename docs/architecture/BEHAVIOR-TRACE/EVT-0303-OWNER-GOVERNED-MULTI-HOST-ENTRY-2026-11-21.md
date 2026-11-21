# EVT-0303 — ورود یک‌پیامی و فضای کاری محصور میزبان

- Event ID: EVT-0303
- Project date: 2026-11-21
- Parent: POINT-0/083 → IN-126 → OUT-125
- Status: REGISTERED ON BRANCH / PENDING MAIN MERGE
- Governing architecture: existing HAIF multi-host governance and HOST-WORKSPACES protocol
- New one-message entry: prototype/universal-host/ONE_MESSAGE_MULTI_HOST_ENROLLMENT_FA.md

## Event

در پاسخ به دستور مالک، مسیر ورود میزبان تازه به معماری موجود HAIF به یک مأموریت یک‌پیامی و read-only تبدیل شد. میزبان باید مرجع عمومی مخزن را بخواند، هویت/قابلیت‌های واقعی را اعلام کند، تا تأیید مالک در وضعیت PROPOSED بماند و workspace خصوصی خودش را فقط در صورت پشتیبانی واقعی محیط آماده کند.

## Security and governance

- Central repository permission for the new host: PUBLIC READ ONLY.
- No direct repository write, branch, PR, issue, release, settings or workflow mutation.
- No official Host ID self-assignment; owner assigns after direct receipt and identity review.
- Workspace must be private to the destination host; shared-repository folders are not security boundaries.
- Host outputs remain observations/proposals until owner review, RAHM validation and explicit promotion decision.
- No automatic host activation, registry provisioning, broker deployment or dashboard is claimed.

## Chain

POINT-0/082 → CURRENT-135 → POINT-0/083 → IN-126 → OUT-125 → EVT-0303 → TIME-BINDING-EVT-0303 → CURRENT-136 → NEXT-051

## Evidence

- Existing multi-host architecture and host workspace protocols were read from the public repository.
- New onboarding instruction was created on branch host/onboarding-readonly-multihost-point-083.
- Main merge, destination-host acceptance and workspace recovery remain OPEN.
