# REFERENCE DOCUMENT MIRROR PROTOCOL — 2026-09-29

Stable ID: REFERENCE-DOCUMENT-MIRROR-PROTOCOL-2026-09-29-001
Status: ACTIVE / LIVING

## Rule
هرگاه کاربر «سند مرجع» بخواهد یا یک Artifact به‌طور رسمی به‌عنوان Reference پذیرفته شود، همان Artifact باید با همان Stable ID و Version در Reference Documents Vault نگهداری شود.

## Required mirrors
1. Canonical Repository: docs/reference/REFERENCE-DOCUMENTS/
2. Persistent Library: /Future AI/Palang Footprint/Master Reference Vault/Reference Documents/
3. Persistent-memory pointer/state: Stable ID + version + locations + status + evidence state.

## No silent divergence
Mirrorها نباید نسخه‌های متفاوت و بدون Lineage داشته باشند. اختلاف باید ثبت و Reconcile شود.

## Registration gate
WRITE → READ-BACK → MATCH → VERIFY → RECONCILE → STATUS

«Registered» فقط پس از Evidence متناسب قابل اعلام است.

## Retrieval rule
وقتی کاربر می‌گوید «سند مرجع بده»، Reference Documents Vault باید قبل از تولید مجدد بررسی شود و نسخه موجود با Lineage آن بازیابی شود.
