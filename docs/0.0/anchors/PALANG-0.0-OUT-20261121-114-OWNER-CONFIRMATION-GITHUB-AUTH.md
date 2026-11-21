# OUT-114 — خروجی: مسیر آسان اتصال خواندنی میزبان جدید به GitHub

- Point: POINT-0/072.
- Input: IN-115.
- Event: EVT-0291.
- Time binding: TIME-BINDING-EVT-0291.
- Current: CURRENT-125.
- Sole queue: NEXT-051.

## خروجی طراحی‌شده در شاخهٔ پیشنهاد
1. پیام واحد میزبان به مسیر کوتاه اتصال از طریق GitHub connector رسمی همان محیط هدایت می‌شود.
2. اگر connector متصل نیست، میزبان فقط راهنمای اتصال از رابط رسمی محصول را نشان می‌دهد؛ هیچ credential در چت جمع‌آوری نمی‌کند.
3. پس از اتصال، میزبان دسترسی READ-ONLY به مخزن دقیق و بازیابی HEAD، سند مادر، آخرین ZIP و رسیدها را بررسی می‌کند.
4. قرارداد میزبان، دستورالعمل‌ها، README، manifest و سند مادر دامنهٔ فعلی را به read-only connection محدود می‌کنند.
5. عبارت «احمد نژادحسینی» و طراحی password/owner-confirmation gate به مرحلهٔ بعد موکول و OPEN نگه داشته می‌شوند.

## وضعیت واقعی
- Proposal branch: host-intake-owner-confirmation-github-auth-20261121.
- Main merge: NOT DONE.
- Canonical ZIP rebuild and exact receipt: PENDING.
- Independent-host connector/read-only test: NOT RUN.
- Repository write access, broker, host-intake write path and branch protection: OUT OF SCOPE FOR THIS PHASE / OPEN.
- NEXT-051 remains the sole active execution queue; no parallel queue created.
