# EVT-0073 — اتصال قرارداد ثبت خودکار ورودی/خروجی به معماری

## شناسنامه
- Event ID: EVT-0073
- Stable ID: EVT-0073-AUTOMATIC-INTERACTION-REGISTRATION-CONTRACT-2026-10-21
- Production ID: EVT-AIRC-2026-10-21-001
- Version: 1.0.0
- Event type: USER_INPUT + ASSISTANT_ARCHITECTURE_CHANGE
- Project: Future AI / Palang Footprint / HAIF
- Owner: احمد پلنگ (Ahmad Nezhadhosseini)
- User message time: UNKNOWN / UNAVAILABLE (trusted per-message timestamp not exposed in current context)
- Assistant processing time UTC: UNKNOWN / UNAVAILABLE (no trusted live execution clock exposed for this operation; not substituted with commit time)
- Repository commit time: record from GitHub commit metadata after write.
- Canonical contract: [Automatic Interaction Registration Contract](../GOVERNANCE/AUTOMATIC-INTERACTION-REGISTRATION-CONTRACT-2026-10-21-001.md)
- Related standard: [Assistant Timestamp Anchor Standard](../GOVERNANCE/ASSISTANT-TIMESTAMP-ANCHOR-STANDARD-2026-10-21-001.md)
- Status: REGISTERED; read-back and integration evidence pending.

## Input / ورودی کاربر
کاربر خواست قرارداد ثبت خودکار به معماری و ساختمان دائمی و زندهٔ پروژه متصل شود؛ از این پس همهٔ ورودی‌های کاربر و خروجی‌های دستیار باید پیش‌فرض پابند، زمان‌گذاری، لنگر مستقل، مستندسازی، پیونددهی و راستی‌آزمایی شوند، بدون نیاز به تکرار فرمان «ثبت کن». کاربر همچنین چکش فهم و اجرای قاعده را درخواست کرد.

## Decision / تصمیم معماری
«ثبت کن» دیگر شرط شروع ثبت نیست؛ فقط فرمانی برای اجرای چرخهٔ کامل و رسیدگی ویژه است. سیاست ثبت خودکار برای همهٔ پیام‌ها حاکم می‌شود، اما نباید ثبت این سیاست با اثبات اجرای خودکار در جریان زندهٔ ChatGPT اشتباه شود.

## Changes
1. Created canonical governing contract: `docs/architecture/GOVERNANCE/AUTOMATIC-INTERACTION-REGISTRATION-CONTRACT-2026-10-21-001.md`.
2. Contract defines event envelope, independent anchors, timestamp-source rules, preservation, links, read-back, per-destination state, security boundaries, host-adapter needs, and 10 acceptance tests.
3. Next integrate this contract into timestamp standard, governing master, reference index, and integration queue.
4. Runtime auto-capture is not claimed. GitHub Actions sees repository events; it does not inherently receive live ChatGPT messages. A real host adapter and successful end-to-end tests are still required.

## PEH / چکش
- PASS: requirement understood as a standing default, not an optional response to «ثبت کن».
- PASS: governing contract file written to canonical repository; commit/read-back still needs separate evidence.
- OPEN: connect all master/index/queue paths and fetch them back.
- OPEN: implement and test live host adapter.
- NOT RUN: AIRC-T01 through AIRC-T10, including six-document recovery, restart, idempotency, and independent destination tests.
- UNVERIFIED: Buffer, Library, Persistent Memory, Dropbox.
