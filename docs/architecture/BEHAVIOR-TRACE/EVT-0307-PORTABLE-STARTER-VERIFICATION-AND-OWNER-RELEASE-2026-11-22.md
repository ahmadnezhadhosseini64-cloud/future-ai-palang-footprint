# EVT-0307 — تأیید بستهٔ قابل‌انتقال و انتشار نسخهٔ پایدار

- Stable ID: HAIF-EVT-0307-PORTABLE-STARTER-VERIFICATION-AND-OWNER-RELEASE-2026-11-22
- Parent: POINT-0/086 → CURRENT-139
- Status: PACKAGE_VERIFIED / RELEASE_PUBLISHED / HOST_RECOVERY_NOT_RUN
- Main commit: 891829cc123d876a3e63f93331981e0af5107868
- Workflow: Portable RAHM Conformance and Digest Evidence
- Workflow run: 44964082773
- Workflow created UTC: 2026-11-21T23:54:59Z
- Workflow completed UTC: 2026-11-21T23:55:33Z

## Canonical package

- Stable release: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/tag/haif-latest-verified
- Asset: haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip
- SHA-256: 0823141628db6d62fc6a5d320f8ca0c291f941bca446286f894e75a299a811f5
- Asset size: 272,688 bytes
- Stable SHA-256 asset: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/download/haif-latest-verified/haif-gpt6-starter-v0.3.0-0plus-bootstrap-clean.zip.sha256
- Package receipt asset: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/download/haif-latest-verified/haif-gpt6-starter-zip-receipt.json
- Release metadata asset: https://github.com/ahmadnezhadhosseini64-cloud/future-ai-palang-footprint/releases/download/haif-latest-verified/latest-verified-export.json
- Artifact ID in workflow run: 14731355000
- Artifact container SHA-256: fe7e4716a25f77091754b0fccbc60bfb7afbd9e82689506378e781aae18ba81f

## Verification

- Portable package build: PASS.
- ZIP CRC/integrity: PASS.
- Source-byte read-back: PASS.
- Extracted ZIP tests: PASS.
- Same-run artifact download by name and exact artifact digest: PASS.
- Paired living-master artifact read-back: PASS.
- Durable stable release publication: PASS.
- RAHM Security and Promotion Conformance run 44964082658: PASS.
- Living Architecture Audit run 44964082615: PASS.
- GitHub Pages deployment run 44964082566: PASS.
- Independent clean-host import/recovery: NOT RUN. PACKAGE_VERIFIED does not mean HOST_RECOVERED.

## Governance note

The portable release publisher has contents:write only to update the stable release assets after a protected main update. It contains no git commit/push to main and is not accessible to hosts. Manual workflow dispatch is owner-only. The Promotion App and host identities remain separate and receive no release permission.
