#!/usr/bin/env python3
"""Structural audit for canonical living-architecture records.
This checks repository structure only; it does not prove external persistence.
"""
from pathlib import Path
import sys

ROOT = Path(".")
required = {
    "reference index": "docs/REFERENCE_INDEX.md",
    "master reference contract": "docs/reference/REFERENCE-DOCUMENTS/MRV-ARCHITECTURE-AND-LIVING-REFERENCE-CONTRACT-2026-09-15-001.md",
    "current 0.0 anchor": "checkpoints/PALANG-0.0-CURRENT-2026-10-20-001.md",
    "architecture queue": "docs/architecture/INTEGRATION-QUEUE/README.md",
    "open gaps register": "docs/architecture/INTEGRATION-QUEUE/OPEN-GAPS-RECOVERY-REGISTER-2026-10-15-001.md",
    "behavior trace index": "docs/architecture/BEHAVIOR-TRACE/README.md",
    "excavation contract": "docs/architecture/INTEGRATION-QUEUE/EXCAVATION-ROUTINE-EXECUTION-CONTRACT-2026-10-20-001.md",
    "comprehensive excavation reference": "docs/reference/REFERENCE-DOCUMENTS/COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001.md",
    "living automation contract": "docs/reference/REFERENCE-DOCUMENTS/LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001.md",
}
errors = []
for label, rel in required.items():
    if not (ROOT / rel).is_file():
        errors.append(f"MISSING_REQUIRED_FILE label={label!r} path={rel}")

expected_ids = (
    "COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001",
    "LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001",
)
for rel, label in (
    ("docs/REFERENCE_INDEX.md", "REFERENCE_INDEX"),
    ("docs/architecture/INTEGRATION-QUEUE/README.md", "ARCHITECTURE_QUEUE"),
):
    path = ROOT / rel
    if path.is_file():
        content = path.read_text(encoding="utf-8")
        for stable_id in expected_ids:
            if stable_id not in content:
                errors.append(f"{label}_MISSING_ID id={stable_id}")

print("LIVING_ARCHITECTURE_AUDIT")
print(f"required_files_checked={len(required)}")
print("external_persistence_tested=false")
print("chatgpt_all_conversation_capture_tested=false")
if errors:
    print(f"result=FAIL errors={len(errors)}")
    for error in errors:
        print(error)
    sys.exit(1)
print("result=PASS structural_repository_checks")
