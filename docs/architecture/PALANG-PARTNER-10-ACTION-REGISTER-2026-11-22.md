## CURRENT-151 continuation — 2026-11-22

- Current checkpoint: CURRENT-151 / POINT-0/089.
- Sole queue: NEXT-051; canonical root/baseline: POINT-0/GOLDEN.
- The ten issues #114–#123 are the ten independent Partner dossiers. Their canonical dossier IDs and actual registration UTCs are recorded in this register and repeated in each issue.
- All ten remain OPEN. Their issue bodies now include inputs, expected outputs, dependencies, evidence boundaries, acceptance and read-back methods.
- No service provisioning, GitHub App, OAuth, MCP, OpenAI API, hosting, private RAHM or independent-host acceptance is inferred from dossier creation.

---

# POINT-0/GOLDEN — ده اقدام اجرایی مستقل Palang Partner

- Stable ID: HAIF-POINT-0-GOLDEN-PALANG-PARTNER-10-ACTION-REGISTER-2026-11-22-001
- Status: ACTIVE / LIVING / TEN TRACKING ISSUES CREATED — IMPLEMENTATION OPEN
- Canonical root: POINT-0 (single root)
- Baseline: POINT-0/GOLDEN
- Checkpoint target: CURRENT-151 / POINT-0++
- Sole active queue: NEXT-051 (unchanged; no parallel queue)
- Parent: CURRENT-150 → POINT-0/089 → EVT-0320 → CURRENT-151 → NEXT-051
- Owner: @ahmadnezhadhosseini64-cloud
- Repository: ahmadnezhadhosseini64-cloud/future-ai-palang-footprint

## 1. فرمان بنیادی

هدف نهایی، تبدیل Palang Partner به همکار اجرایی مرکزی و مستقل است: احراز هویت امن مالک، اتصال مجاز به GitHub، محیط کاری واقعی و پایدار، اجرای عملیات مجاز، آزمون، ثبت شواهد، read-back و انتقال گزینشی خروجی به چرخه رشد پروژه.

این سند نقطه/ریشه/صف جدید ایجاد نمی‌کند. ده اقدام زیر ده Issue مستقل برای مدیریت و پذیرش جداگانه‌اند، اما همگی فرزند اجرایی همان NEXT-051 و متصل به POINT-0/GOLDEN هستند. هیچ‌یک به‌تنهایی baseline یا مرجع معماری مستقل نیست.

## 2. ده اقدام مستقل

| # | اقدام | Issue | وضعیت |
|---:|---|---|---|
| 01 | ساخت مخزن خصوصی سرویس و مقصد میزبانی HTTPS | [#114](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/114) | OPEN |
| 02 | ثبت و نصب GitHub App مالک‌محور | [#115](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/115) | OPEN |
| 03 | ساخت OAuth callback، session broker و نگهداری رمزنگاری‌شده توکن | [#116](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/116) | OPEN |
| 04 | پیاده‌سازی remote MCP و ابزارهای GitHub با حداقل مجوز | [#117](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/117) | OPEN |
| 05 | پیکربندی OpenAI API، Responses API و runtime امن | [#118](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/118) | OPEN |
| 06 | استقرار سرویس، HTTPS، health check و pipeline انتشار | [#119](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/119) | OPEN |
| 07 | تکمیل promotion workflow و PR با هویت bot مورداعتماد | [#120](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/120) | OPEN |
| 08 | اعمال گیت تأیید main و ممیزی هویت‌های مخزن | [#121](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/121) | OPEN |
| 09 | ایجاد RAHM خصوصی مالک و مرز امن export/read | [#122](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/122) | OPEN |
| 10 | آزمون سرتاسری RAHM→CHILD، بازیابی میزبان و جداسازی | [#123](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/123) | OPEN |

هر Issue شرح اجرایی، وابستگی و معیار پذیرش مستقل دارد. وضعیت Issueها تا زمان اثبات با شواهد، OPEN باقی می‌ماند.

## 3. ترتیب و وابستگی‌ها

- گام 01 زیرساخت پایه را آماده می‌کند.
- گام 02 به مقصد callback و میزبانی گام 01 نیاز دارد.
- گام 03 به گام‌های 01 و 02 وابسته است.
- گام 04 به گام‌های 01 تا 03 وابسته است.
- گام 05 به secret manager گام 01 و MCP endpoint گام 04 نیاز دارد.
- گام 06 پس از آماده‌شدن اجزای 01، 03، 04 و 05 انجام می‌شود.
- گام 07 به هویت App و workflow امن وابسته است.
- گام 08 باید با مسیر bot-authored PR گام 07 سازگار شود؛ هیچ bypass میزبان مجاز نیست.
- گام 09 می‌تواند به‌صورت موازی با 02 تا 08، فقط با اقدام مالک، provision شود.
- گام 10 پس از فراهم‌شدن مسیرهای لازم، آزمون پذیرش نهایی است. آزمون recovery میزبان می‌تواند مستقل اجرا شود، اما فعال‌سازی Host منوط به همه معیارهاست.

## 4. نقشه وابستگی

```text
01 Private service + hosting
 ├── 02 GitHub App
 │    └── 03 OAuth/session broker
 │         └── 04 Remote MCP
 │              ├── 05 OpenAI Responses integration
 │              │    └── 06 HTTPS deployment
 │              └── 07 Bot-authored promotion workflow
 │                   └── 08 Main approval gate + access audit
 └── 09 Private owner-only RAHM
      └── 10 End-to-end RAHM→CHILD + clean-host recovery/isolation
```

## 5. اصول غیرقابل‌تغییر

1. MASTER فقط مرجع عمومیِ READ ONLY برای میزبان‌هاست؛ هیچ میزبان، مستقیم یا غیرمستقیم، حق نوشتن یا PR به MASTER ندارد.
2. اتصال Palang Partner با هویت مالک، یک Owner Control Plane است و credential میزبان محسوب نمی‌شود.
3. RAHM خصوصی، مرکزی، فقط‌مالک و بیرون از تمام workspaceهای میزبان است.
4. هیچ Secret، token، private key یا داده خام خصوصی در چت، Issue، log عمومی یا مخزن عمومی ثبت نمی‌شود.
5. خروجی میزبان داده نامطمئن است؛ انتقال به RAHM فقط با فرمان مالک و پس از پالایش انجام می‌شود.
6. CHILD نامزد/فرزند است، نه MASTER. هیچ auto-merge یا ارتقای خودکار مجاز نیست.
7. هر عملیات باید با هویت عامل، scope، زمان معتبر، نتیجه و read-back قابل ممیزی باشد.
8. پوشه در مخزن مشترک مرز امنیتی نیست؛ workspace واقعی باید مستقل و دسترسی repo-level محدود باشد.
9. نبود قابلیت در ابزار یا سرویس باید دقیقاً NOT AVAILABLE / NOT RUN ثبت شود؛ هیچ وضعیت ساختگی یا ادعای activation مجاز نیست.
10. هیچ Host تا اثبات identity، workspace isolation، persistence، recovery، permission boundary و acceptance receipt، ACTIVE نیست.

## 6. معیار پایان کل برنامه

برنامه فقط زمانی تکمیل‌شده اعلام می‌شود که:
- سرویس Partner با HTTPS مستقر و قابل دسترس باشد؛
- OAuth هویت مالک را به‌درستی احراز و session/token را امن نگهداری کند؛
- Responses API ابزارهای remote MCP را در scope محدود فراخوانی کند؛
- عملیات مجاز GitHub با read-back و audit اثبات شوند؛
- گیت تأیید مالک و عدم دسترسی میزبان به MASTER/RAHM زنده و آزموده شوند؛
- RAHM خصوصی و owner-only باشد؛
- synthetic candidate با schema/hash/privacy/provenance checks از مسیر RAHM به CHILD برسد؛
- clean-host recovery و negative isolation tests موفق شوند.

## 7. وضعیت آغازین ثبت‌شده

- CURRENT-145: معماری bridge در Golden و main منتشر شده است؛ این فقط تکمیل طراحی است، نه تکمیل runtime.
- ده Issue #114 تا #123 ایجاد شده‌اند.
- مخزن خصوصی Partner، GitHub App، OAuth broker، MCP runtime، OpenAI API project/key، HTTPS deployment، private RAHM و recovery مستقل هنوز تا ارائه رسیدهای واقعی NOT PROVISIONED / NOT VERIFIED هستند.
- NEXT-051 همچنان تنها صف فعال است.
- این ثبت باید از مسیر همان POINT-0/GOLDEN و انتشار کنترل‌شده آن به main ادامه یابد.


## 8. Independent dossier identity and registration ledger

Each action is a separate dossier, not merely a row in a plan. Its GitHub Issue is the working record for input, expected output, dependencies, execution evidence, UTC registration time, status and acceptance/read-back criteria.

| # | Issue | Stable dossier ID | Actual issue registration UTC | State |
|---:|---:|---|---|---|
| 01 | [#114](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/114) | `PALANG-PARTNER-DOSSIER-01-SERVICE-FOUNDATION-2026-11-22-001` | `2026-11-22T07:01:07Z` | OPEN |
| 02 | [#115](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/115) | `PALANG-PARTNER-DOSSIER-02-GITHUB-APP-2026-11-22-001` | `2026-11-22T07:01:09Z` | OPEN |
| 03 | [#116](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/116) | `PALANG-PARTNER-DOSSIER-03-OAUTH-BROKER-2026-11-22-001` | `2026-11-22T07:01:10Z` | OPEN |
| 04 | [#117](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/117) | `PALANG-PARTNER-DOSSIER-04-REMOTE-MCP-2026-11-22-001` | `2026-11-22T07:01:12Z` | OPEN |
| 05 | [#118](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/118) | `PALANG-PARTNER-DOSSIER-05-OPENAI-RESPONSES-RUNTIME-2026-11-22-001` | `2026-11-22T07:01:14Z` | OPEN |
| 06 | [#119](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/119) | `PALANG-PARTNER-DOSSIER-06-DEPLOYMENT-OBSERVABILITY-2026-11-22-001` | `2026-11-22T07:01:16Z` | OPEN |
| 07 | [#120](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/120) | `PALANG-PARTNER-DOSSIER-07-OWNER-PROMOTION-PR-2026-11-22-001` | `2026-11-22T07:01:18Z` | OPEN |
| 08 | [#121](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/121) | `PALANG-PARTNER-DOSSIER-08-MAIN-OWNER-APPROVAL-GATE-2026-11-22-001` | `2026-11-22T07:01:19Z` | OPEN |
| 09 | [#122](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/122) | `PALANG-PARTNER-DOSSIER-09-PRIVATE-RAHM-2026-11-22-001` | `2026-11-22T07:01:21Z` | OPEN |
| 10 | [#123](https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/issues/123) | `PALANG-PARTNER-DOSSIER-10-END-TO-END-RECOVERY-ISOLATION-2026-11-22-001` | `2026-11-22T07:01:23Z` | OPEN |

### Shared execution and promotion rules

- Each Issue contains its own input, expected output, dependencies, currently available evidence, actual UTC registration timestamp, state and acceptance/read-back criteria.
- Issue registration is evidence of tracking only; it is not evidence that an external service was provisioned or tested.
- Any owner, assistant or host may propose a candidate improvement. Promotion to MASTER is a separate owner-controlled decision and requires the owner's approval; no proposal self-authorizes.
- No dossier closes by implication from another dossier. Shared dependencies do not merge their acceptance criteria.
- All ten dossiers remain children of the same POINT-0/GOLDEN and the sole NEXT-051.
