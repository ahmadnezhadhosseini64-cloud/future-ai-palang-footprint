# POINT-0/064 (0+) — تثبیت چرخهٔ روزانهٔ خبر ۰۷ و ۲۳ و پیوستگی ۲۴ساعته

- Stable ID: `HAIF-POINT-0-064-NEWS-CADENCE-24H-CONTINUITY-2026-11-07-001`
- Production ID: `HAIF-RAHM-POINT-064-NEWS-CADENCE-24H`
- Version: 1.0.0
- Project: Future AI / Palang Footprint — آیندهٔ AI / ردپای پلنگ
- Parent: POINT-0/063 (0+) → CURRENT-114 → NEXT-051.
- Designation: NEW USER-TURN ROOT / 0+ HIGHLIGHT / APPEND-ONLY.
- User-message timestamp: UNKNOWN / UNVERIFIED.
- Repository registration timestamp: to be bound to exact Git commit metadata.
- Status: ROOT REGISTRATION; cross-file read-back and integration pending.

## 1. User intent

The user confirms a permanent daily news routine with two automatic reports and two manual suggested windows:
- 07:00 Asia/Tehran: automatic morning report, every day.
- 23:00 Asia/Tehran: automatic night report, every day.
- 11:00 and 15:00: manual suggested windows only; if the user appears and requests «بروزرسانی خبر», perform an incremental update at that time.
- The user may be offline, not open the app or miss the 11:00, 15:00 or 23:00 manual opportunity. The next 07:00 report must not depend on presence or missed manual requests.

## 2. Coverage windows and continuity contract

### Daily 07:00 report
The morning report's coverage window is exactly the preceding 24 hours:
`[previous calendar day 07:00, current day 07:00)` in Asia/Tehran.
Example of the rule: the report at 07:00 on day D covers 07:00 on day D-1 through just before 07:00 on day D. It must include all important events in that window, even if the user made no manual request at 11:00, 15:00 or 23:00 on day D-1. Do not shorten the window based on attendance or prior manual interactions. Clearly disclose any source/data gaps.

### Daily 23:00 report
The night report's coverage window is the same day's 07:00–23:00 in Asia/Tehran. It is a regular automatic daily report, not conditional on user presence or an on-demand request.

### Manual 11:00 and 15:00 updates
These are not scheduled automations. They are user-triggered incremental reports when the user appears and says «بروزرسانی خبر». Any other time the same phrase is valid and should trigger an update from the latest actually delivered report/update, without pretending that missed reports occurred.

### No fabricated continuity
- Never claim a missed manual report was delivered.
- Never claim background monitoring between runs.
- Distinguish event time, publication time, market quote time, report execution time and Git registration time.
- When accessible, deduplicate unchanged stories while still reporting significant new developments and corrections.
- If prior manual-report history is unavailable to an automatic task, state that limitation rather than claiming to know it.
- 07:00 and 23:00 are independent daily automations; each must run even if the user does not open the app.

## 3. Automation records

### Morning automation — existing task updated
- Automation ID: `6aef62341be0819185b2b0c8c126e672`
- Title: «خلاصه صبحگاهی ایران، سیاست، دلار و آب‌وهوا»
- Schedule: daily, DTSTART `2026-11-08T07:00:00`, timezone `Asia/Tehran`.
- Enabled: true.
- Prompt updated to require exact rolling 24-hour coverage from 07:00 previous day to 07:00 current day, independent of user attendance.
- Creation is historical; this task was updated, not duplicated.

### Night automation — newly created
- Automation ID: `6aef6dcfc5c8819182290d92908e94d7`
- Title: «گزارش شبانه ایران، جهان و آب‌وهوا»
- Schedule: daily, DTSTART `2026-11-07T23:00:00`, timezone `Asia/Tehran`.
- Enabled: true.
- Coverage: same-day 07:00–23:00.
- This is a separate daily automatic report, not the manual 11:00/15:00 window.

### Confirmed vs unconfirmed runtime
The automation actions returned success and enabled configuration. This confirms saved schedule configuration only; it does not prove a future run, delivery, uninterrupted background execution or successful report content. Run receipts must be checked after actual occurrences.

## 4. News scope retained

Continue the established broad daily coverage: Iran/domestic; Iran–US–Israel conflict and diplomacy/security; world politics; Iran/world economy; separately labeled free-market and official/exchange rates; gold, coins, euro, oil, inflation and essentials; Middle East, US, Europe, Russia/Ukraine, China and other powers; major global events; significant nature/wildlife/water/fish/migratory-bird news; and Gonbad-e Kavus, Golestan weather. Use reliable linked sources, compare independent sources for conflict/political claims, separate verified facts from claims and analysis, and label rate units/market/time. Do not invent news or values.

## 5. New execution chain

Required chain:
POINT-0/064 (0+) → IN-103 + OUT-102 → EVT-0256 → TIME-BINDING-EVT-0256 → CURRENT-115 → existing NEXT-051.

Connect to parent POINT-0/063, POINT-0/062, POINT-0/061 and all earlier 0/0+/0.0 anchors. Maintain central 0.0 registry, Reference Index, Behavior Trace, Integration Queue, living mother, export/recovery manifests and historical branches. No NEXT-052.

## 6. Acceptance tests

- N01: read back morning automation and verify exact daily 07:00 Asia/Tehran schedule and 24-hour rolling-window prompt.
- N02: read back night automation and verify exact daily 23:00 Asia/Tehran schedule and 07:00–23:00 coverage prompt.
- N03: verify manual 11:00/15:00 remain manual and do not create duplicate schedules.
- N04: at next actual 07:00 occurrence, verify report covers previous day 07:00 through current day 07:00.
- N05: at next actual 23:00 occurrence, verify report covers same-day 07:00–23:00.
- N06: test missed manual windows; next morning still covers full 24-hour interval.
- N07: verify source links, publication/event/quote timestamps, free vs official rate separation and Gonbad-e Kavus weather.
- N08: verify missed reports are never fabricated and no between-run monitoring is claimed.
- G01–G06: continue graph-wide anchor/link/identity/parent reconciliation.
- H01–H05: continue fresh-session, restart, clean-host and independent-host recovery.

All tests remain OPEN / NOT RUN until direct run receipts and inspectable evidence exist.

## 7. Governance and next actions

Continue the existing NEXT-051 queue only. Preserve all prior package identity, exact-SHA, RAHM rebuild, living mother, historical graph, runtime, persistent-memory/Buffer, Dropbox, issue and independent-host recovery tasks. Do not create a new queue or declare any test passed without its own evidence.

Apply WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS. UTC is the permanent time base; derive Asia/Tehran (+03:30) from exact UTC metadata. Keep user-message, automation configuration, actual run, report delivery and Git commit times distinct. Unknown values remain UNKNOWN / UNVERIFIED.

This point is append-only and does not replace POINT-0/063 or close any prior open gate.
