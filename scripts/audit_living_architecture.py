#!/usr/bin/env python3
"""Structural audit for Future AI / Palang Footprint living references.
This checks repository structure and link targets only; it does not prove external persistence.
"""
from pathlib import Path
import re
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

index_path = ROOT / "docs/REFERENCE_INDEX.md"
if index_path.is_file():
    index = index_path.read_text(encoding="utf-8")
    for stable_id in (
        "COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001",
        "LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001",
    ):
        if stable_id not in index:
            errors.append(f"REFERENCE_INDEX_MISSING_ID id={stable_id}")

queue_path = ROOT / "docs/architecture/INTEGRATION-QUEUE/README.md"
if queue_path.is_file():
    queue = queue_path.read_text(encoding="utf-8")
    for stable_id in (
        "COMPREHENSIVE-EXCAVATION-ARCHITECTURE-STATE-2026-10-20-001",
        "LIVING-INTERACTION-AUTOMATION-AND-RECONCILIATION-2026-10-20-001",
    ):
        if stable_id not in queue:
            errors.append(f"ARCHITECTURE_QUEUE_MISSING_ID id={stable_id}")

# Validate local Markdown links in the critical index and architecture files.
for rel in (index_path, queue_path, ROOT / "docs/architecture/BEHAVIOR-TRACE/README.md"):
    if not rel.is_file():
        continue
    text = rel.read_text(encoding="utf-8")
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = (rel.parent / target.split("#", 1)[0]).resolve()
        if target.split("#", 1)[0] and not target_path.is_file():
            errors.append(f"BROKEN_LOCAL_LINK source={rel.as_posix()} target={target}")

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
