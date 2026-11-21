# EVT-0289 — Single-message GPT-6 host bootstrap (2026-11-21)

- Input: [IN-114](../../0.0/anchors/PALANG-0.0-IN-20261121-114-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md)
- Output: [OUT-113](../../0.0/anchors/PALANG-0.0-OUT-20261121-113-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md)
- Current: [CURRENT-124](../../0.0/anchors/PALANG-0.0-CURRENT-20261121-124-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP.md)
- Sole queue: [NEXT-051](../../0.0/anchors/PALANG-0.0-NEXT-20261024-051-FULL-GRAPH-TRIAGE-AND-CLEAN-HOST-RECOVERY.md)
- Time: [TIME-BINDING-EVT-0289](./TIME-BINDING-EVT-0289-SINGLE-MESSAGE-GPT6-HOST-BOOTSTRAP-2026-11-21.md)
- Master: [سند مرجع مادر](../مدل%20اولیه%20AI/سند%20مرجع%20مادر%20مدل%20اولیه%20هوش%20مصنوعی.md)
- Bootstrap: [SINGLE_MESSAGE_GPT6_HOST_BOOTSTRAP_FA.md](../../../prototype/haif-gpt6-starter/SINGLE_MESSAGE_GPT6_HOST_BOOTSTRAP_FA.md)

رویداد ثبت معماری پیام واحد برای نمونهٔ تازهٔ همان نقش GPT-6 Host است. پیام اتصال رسمی GitHub، بازیابی سند مادر و بستهٔ آخر، ساخت workspace خصوصی در محیط میزبان، بازیابی زنجیره و رسید پذیرش را هدایت می‌کند. 0++ فقط نشانگر همان ریشهٔ POINT-0 است. میزبان از READ-ONLY شروع می‌کند؛ پیام نمی‌تواند مجوز، broker یا حافظهٔ پایدار ایجاد کند. ثبت مخزنی فقط از broker و پس از read-back مجاز است. package source target 0.4.2 و نام/هویت canonical ثابت می‌ماند. اتصال میزبان، workspace پایدار، broker، آزمون جداسازی، clean-host recovery و restart persistence OPEN / NOT RUN هستند.