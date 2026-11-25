#!/usr/bin/env python3
"""Append-only bridge between the packaged living-master snapshot and canonical successor."""
import hashlib
import json
import re
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
SOURCE = ROOT / "docs/architecture/مدل اولیه AI/سند مرجع مادر مدل اولیه هوش مصنوعی.md"
CURRENT = PACKAGE / "LIVING_MASTER_REFERENCE.md"
MANIFEST_PATH = PACKAGE / "manifest.json"
BRIDGE = PACKAGE / "LIVING_MASTER_VERSION_BRIDGE.md"


def version_of(text: str) -> str:
    patterns = (
        r"(?m)^## نسخهٔ ([0-9]+\.[0-9]+\.[0-9]+)",
        r"(?m)^- Version / نسخه: ([0-9]+\.[0-9]+\.[0-9]+)$",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    raise SystemExit("LIVING_MASTER_VERSION_NOT_FOUND")


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    canonical_text = SOURCE.read_text(encoding="utf-8")
    canonical_version = version_of(canonical_text)
    history = manifest.get("living_master_history", [])
    known = {entry["version"]: entry for entry in history}

    if not CURRENT.is_file():
        raise SystemExit("PACKAGED_PREDECESSOR_MISSING")
    previous_bytes = CURRENT.read_bytes()
    previous_text = previous_bytes.decode("utf-8")
    previous_version = version_of(previous_text)

    if previous_version != canonical_version:
        historical_name = f"LIVING_MASTER_REFERENCE-{previous_version}-HISTORICAL.md"
        historical_path = PACKAGE / historical_name
        digest = hashlib.sha256(previous_bytes).hexdigest()
        if historical_path.exists():
            existing = historical_path.read_bytes()
            if existing != previous_bytes:
                raise SystemExit(f"HISTORICAL_SNAPSHOT_COLLISION: {historical_name}")
        else:
            historical_path.write_bytes(previous_bytes)
        existing_entry = known.get(previous_version)
        entry = {"version": previous_version, "file": historical_name, "sha256": digest}
        if existing_entry and existing_entry != entry:
            raise SystemExit(f"HISTORICAL_LINEAGE_CONFLICT: {previous_version}")
        if not existing_entry:
            history.append(entry)
            known[previous_version] = entry

    # Verify every retained historical snapshot before changing the current pointer.
    history.sort(key=lambda item: tuple(int(part) for part in item["version"].split(".")))
    for entry in history:
        path = PACKAGE / entry["file"]
        if not path.is_file():
            raise SystemExit(f"HISTORICAL_SNAPSHOT_MISSING: {entry['file']}")
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != entry["sha256"]:
            raise SystemExit(f"HISTORICAL_SNAPSHOT_DIGEST_MISMATCH: {entry['file']}")
        if version_of(path.read_text(encoding="utf-8")) != entry["version"]:
            raise SystemExit(f"HISTORICAL_SNAPSHOT_VERSION_MISMATCH: {entry['file']}")

    CURRENT.write_text(canonical_text, encoding="utf-8")
    latest_predecessor = history[-1]["version"] if history else None
    lines = [
        "# Living Master Version Bridge — append-only lineage",
        "",
        "This bridge links every retained historical packaged snapshot to the current canonical living master.",
        "",
    ]
    for entry in history:
        lines.append(
            f"- Historical predecessor: [{entry['version']}](./{entry['file']}) — "
            f"preserved byte-for-byte; SHA-256: {entry['sha256']}"
        )
    lines.extend([
        f"- Current successor: [{canonical_version}](./LIVING_MASTER_REFERENCE.md) — synchronized from the canonical repository master.",
        "- Relationship: each historical snapshot remains intact; the current successor advances the same POINT-0/GOLDEN lineage and does not erase, rename, or replace any predecessor.",
        "- Direction: predecessor → successor. The canonical master retains its own version history; this bridge makes the portable package lineage explicit.",
        "- Stable package identity and canonical ZIP filename remain unchanged. No separate versioned ZIP is created.",
        "",
        "Conformance fails closed if a historical snapshot is missing, altered, or disconnected from its recorded version and digest.",
        "",
    ])
    BRIDGE.write_text("\n".join(lines), encoding="utf-8")
    manifest["living_master_history"] = history
    manifest["previous_living_master_version"] = latest_predecessor
    manifest["current_living_master_version"] = canonical_version
    manifest["living_master_version_bridge"] = BRIDGE.name
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"LIVING_MASTER_LINEAGE={','.join(entry['version'] for entry in history)}->{canonical_version}")
    print(f"LIVING_MASTER_HISTORY_COUNT={len(history)}")


if __name__ == "__main__":
    main()
