#!/usr/bin/env python3
"""Reproducible canonical ZIP builder with an external SHA-256 receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import zipfile
from pathlib import Path

FIXED_TIME = (2020, 1, 1, 0, 0, 0)
EXCLUDED_NAMES = {".git", "__pycache__", ".pytest_cache", "node_modules", ".venv", "venv"}
EXCLUDED_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}
EXCLUDED_EXACT = {".env", ".env.local", ".env.production", "credentials.json", "secrets.json"}


def is_excluded(rel: Path) -> bool:
    parts = rel.parts
    if any(part in EXCLUDED_NAMES for part in parts):
        return True
    name = rel.name.lower()
    if name in EXCLUDED_EXACT or name.startswith(".env."):
        return True
    if any(name.endswith(suffix) for suffix in EXCLUDED_SUFFIXES):
        return True
    return False


def safe_entries(source: Path, output: Path) -> list[tuple[Path, str]]:
    root = source.resolve()
    out_resolved = output.resolve()
    entries = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if is_excluded(rel) or path.is_dir():
            continue
        if path.is_symlink():
            raise ValueError(f"symlink rejected: {rel}")
        resolved = path.resolve()
        if not resolved.is_relative_to(root):
            raise ValueError(f"path escapes source root: {rel}")
        if resolved == out_resolved:
            continue
        arcname = rel.as_posix()
        if arcname.startswith("/") or ".." in Path(arcname).parts:
            raise ValueError(f"unsafe archive path: {arcname}")
        entries.append((path, arcname))
    return sorted(entries, key=lambda pair: pair[1])


def build_archive(source: Path, output: Path, receipt: Path | None = None) -> dict[str, object]:
    source = source.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    entries = safe_entries(source, output)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path, arcname in entries:
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = ((stat.S_IFREG | (0o755 if os.access(path, os.X_OK) else 0o644)) << 16)
            info.flag_bits = 0
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    result = {"archive": output.name, "sha256": digest, "size_bytes": output.stat().st_size,
              "file_count": len(entries), "paths": [name for _, name in entries],
              "source_root": str(source), "timestamp_policy": "fixed-2020-01-01T00:00:00"}
    if receipt:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    result = build_archive(args.source, args.output, args.receipt)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
