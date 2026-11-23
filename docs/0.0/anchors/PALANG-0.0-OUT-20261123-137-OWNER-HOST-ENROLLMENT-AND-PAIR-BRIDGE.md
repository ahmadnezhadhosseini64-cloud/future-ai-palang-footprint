# OUT-137 — خروجی مالک: طراحی پل جفتی و مسیر کم‌اصطکاک میزبان

- Input: [IN-138](PALANG-0.0-IN-20261123-138-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE.md)
- Bridge: [BRIDGE-0138](PALANG-0.0-BRIDGE-20261123-0138-IN-138-OUT-137.md)
- Event: [EVT-0325](../../architecture/BEHAVIOR-TRACE/EVT-0325-OWNER-HOST-ENROLLMENT-AND-PAIR-BRIDGE-2026-11-23.md)
- Current candidate: CURRENT-150.05
- Sole queue candidate: NEXT-051.05
- Status: ACTIVE / LIVING / IMPLEMENTATION-IN-PROGRESS

## 1. تصمیم معماری

پیشنهاد مالک دربارهٔ پل مستقل بین هر ورودی و خروجی پذیرفته شد. از این پس هر تعامل پروژه‌ای باید یک جفت IN/OUT و یک Bridge record مستقل داشته باشد:
POINT-0/GOLDEN → prior CURRENT/queue → IN-N → BRIDGE-N → OUT-N → EVT → TIME-BINDING → CURRENT revision → same NEXT queue revision.
شناسهٔ Bridge، شمارهٔ IN و OUT را صریحاً به هم متصل می‌کند. Bridge باید به والد قبلی و checkpoint/صف بعدی نیز ارجاع دهد. این یک لایهٔ ردیابی است، نه ریشه یا صف موازی.

## 2. تصمیم اتصال میزبان تازه

- مخزن مادر Public است؛ برای READ/clone/fetch عمومی نیازی به عضویت یا OAuth نیست.
- میزبان جدید ابتدا با یک پیام واحد، آدرس مخزن و دستورالعمل ورود را می‌خواند و exact main HEAD و blob SHA اسناد کلیدی را گزارش می‌کند.
- شناسهٔ خودساختهٔ میزبان فقط HOST-CLAIM-ID موقت است و هویت یا ثبت رسمی محسوب نمی‌شود.
- میزبان باید یک challenge یک‌بارمصرف مالک را در رسید خود بازتاب دهد؛ اگر runtime از کلید عمومی/امضای دیجیتال پشتیبانی کند، proof-of-possession با کلید موقت میزبان افزوده می‌شود. نبود این قابلیت با عنوان UNVERIFIED CLAIM ثبت می‌شود، نه شکست READ عمومی.
- مالک پس از بررسی رسید، هویت/منشأ و قابلیت‌های واقعی، Host ID رسمی را صادر می‌کند.
- عضویت AI host به‌عنوان collaborator در مخزن مادر ممنوع است. میزبان هرگز MASTER/main یا RAHM را نمی‌نویسد/نمی‌خواند.
- فضای کاری خصوصی باید در runtime میزبان واقعاً جدا و پایدار باشد یا در یک private repository اختصاصی که مالک provision کرده است. دسترسی نوشتن، اگر لازم شد، فقط از broker/GitHub App محدود به همان repo و بدون افشای token به مدل انجام می‌شود.
- مسیر سادهٔ اولیه: PUBLIC READ → HOST RECEIPT → OWNER REVIEW → OFFICIAL HOST ID → PRIVATE WORKSPACE. تا قبل از ایجاد سرویس مستقل، write-back از طریق export مالکانه و نه credential میزبان انجام می‌شود.

## 3. کارهای بررسی‌شده

1. وضعیت واقعی شاخهٔ کاری و PR #145 بازخوانی شد؛ شاخهٔ chat-point0-continuation-20261123 در commit caa36bc5abcfd0ee86736d47e6d3460c0fa5d610 بود و PR #145 باز و ادغام‌نشده بود.
2. دریافت شد که .03 و .04 قبلاً در همان PR ثبت شده‌اند؛ از ساختن شماره‌های تکراری اجتناب شد و revision بعدی به‌صورت افزایشی زیر همان خانواده در نظر گرفته شد.
3. ده Issue #114–#123 بررسی شدند؛ هر ده هنوز OPEN هستند. ترتیب وابستگی‌ها حفظ شد.
4. Issue #20: آزمون‌های runtime محلی، fixtureهای جفت IN/OUT و تطبیق زنجیره قبلاً PASS شده‌اند؛ capture خودکار پیام زنده، persistence، restart و بازیابی میزبان مستقل هنوز اثبات نشده‌اند.
5. Issue #21: inventory کامل مسیرهای درخت main با 6,716 ورودی و 644 مسیر در خانواده‌های هدف ثبت شده؛ 21 گروه basename تکراری (17 گروه دارای blob متفاوت و 4 گروه byte-identical) شناسایی شده؛ 9 گروه بررسی محتوایی اولیه دارند؛ بقیهٔ تطبیق معنایی باز است.
6. پل و پروتکل enrollment در این revision به‌صورت سند اجرایی مستقل افزوده می‌شوند؛ این ثبت به‌تنهایی میزبان واقعی را provision یا فعال نمی‌کند.

## 4. وضعیت پذیرش

- ثبت IN/OUT/Bridge/Event/Time-Binding/Current/Next: انجام شد؛ همهٔ هفت رکورد اصلی و سند پروتکل از شاخه fetch-back شدند.
- Read-back: VERIFIED برای IN-138، BRIDGE-0138، OUT-137، EVT-0325، TIME-BINDING-EVT-0325، CURRENT-150.05، NEXT-051.05، schema و receipt template؛ indexها و چهار ورودی میزبان نیز fetch-back شدند.
- JSON parse: PASS برای HOST-ENROLLMENT-RECEIPT-SCHEMA-2026-11-23.json.
- زمان رویداد: commit EVT-0325 برابر `ab4632a8260900f559a8a506d6b6d0220c3e820a`؛ UTC `2026-11-23T06:56:46Z`؛ تهران `2026-11-23T10:26:46+03:30`.
- شاخه در زمان بازخوانی گروه اصلی: `056c76819f64ea6e0a1d81a7c8b5fa67b768d526`; PR #145 همچنان OPEN / UNMERGED.
- exact-SHA CI برای این revision: PENDING تا اجرای خودکار workflowها روی آخرین head.
- Golden merge و main publication: NOT DONE؛ نیازمند مسیر owner-controlled.
- GitHub App/OAuth، private Partner hosting، private RAHM، API key، MCP endpoint: NOT PROVISIONED.
- میزبان مستقل و restart recovery: NOT RUN.
- هر ده Partner issues و Issue #20/#21: OPEN.

## 5. تعهد گزارش بعدی

در پاسخ «چکار کردی؟» تعداد موارد زیر جداگانه اعلام شود: انجام‌شده با شاهد؛ ناقص/منتظر آزمون؛ متوقف‌شده در مرز ابزار/حساب؛ اقدام دقیق لازم از مالک؛ و پیشنهادهایی که برای هدف فعلی غیرضروری تشخیص داده و از مسیر اصلی کنار گذاشته شده‌اند.

## Simpler implementation route confirmed from official documentation

- Public-read enrollment needs no additional service.
- GitHub's official remote MCP endpoint can be evaluated before building a custom GitHub MCP server; toolsets can be narrowed and the host app must support GitHub OAuth/App authorization.
- OpenAI Responses API supports remote MCP calls and explicit tool approvals.
- Cloudflare Workers remains an optional managed host for a thin owner broker only if privileged owner-side operations cannot be handled through the official GitHub MCP or secure owner UI.
- Sources: https://github.com/github/github-mcp-server · https://developers.openai.com/api/docs/guides/tools-connectors-mcp · https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/ · https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/.
- No service has been provisioned or deployed by this research.


## Local runtime Bridge implementation — bounded CI result

The existing dependency-free runtime was extended rather than replaced:
- Generates BRIDGE-YYYYMMDD-NNN alongside INT/IN/OUT.
- Stores a bridge object binding bridge_id, input_id, output_id, event_id, previous event hash and MATCHED status.
- Rejects mismatched bridge/input/output/event/parent links during state verification.
- Supports reverse lookup by BRIDGE ID.
- Primary interaction schema, portable RAHM schema and fixtures now require/contain the bridge pair link.
- Added runtime tests for Bridge ID generation, reverse lookup and mismatch rejection.

**CI evidence:** Interaction ledger validation and recovery run 45128386247 completed SUCCESS on candidate SHA 69208ef7013b78f3bf6a5e6f1c9e0b342465bd30. Jobs schema-validation, recover-from-input and recover-from-output all SUCCESS.

**Portable conformance correction:** run 45128386249 failed only at manifest digest reconciliation for the two intentionally modified portable schema/fixture files. Their exact SHA-256 and Git blob SHA-1 values were updated in EXPORT_MANIFEST.json (version 1.8.46). A fresh exact-head conformance run is still required; no PASS is claimed yet.

**Package build scope:** on candidate SHA 69208, the same canonical ZIP filename was rebuilt; 24 extracted tests passed, ZIP integrity and source-byte read-back passed, but the overall workflow remained failed at the stale manifest digests. The artifact is not promoted or treated as the latest verified release.


## Shared canonical references

- Living mother: [سند مرجع مادر مدل اولیه هوش مصنوعی](../../architecture/مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md).
- Independent-host recovery proof protocol: [INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL](../../architecture/مدل%20اولیه%20AI/INDEPENDENT-HOST-RECOVERY-PROOF-PROTOCOL-2026-10-27-001.md).
- Portable host protocol: [INDEPENDENT_HOST_RECOVERY_PROTOCOL](../../../prototype/haif-gpt6-starter/INDEPENDENT_HOST_RECOVERY_PROTOCOL.md).
- Portable export manifest: [EXPORT_MANIFEST](../../portable/RAHM/EXPORT_MANIFEST.json).
