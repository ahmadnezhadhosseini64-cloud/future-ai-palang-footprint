#!/usr/bin/env python3
"""Build the public host bridge from a strict positive allowlist only."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path

ALLOWLIST = {
    "README.md": "README.md",
    "CHARTER.md": "CHARTER.md",
    "SAFE-SNAPSHOT.md": "SAFE-SNAPSHOT.md",
    "VERSION.json": "VERSION.json",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build(source: Path, output: Path) -> dict:
    source = source.resolve(strict=True)
    output.mkdir(parents=True, exist_ok=True)
    output = output.resolve(strict=True)

    # Refuse symlinks and non-regular files in every allowlisted source.
    records = []
    for source_name, output_name in ALLOWLIST.items():
        candidate = source / source_name
        if candidate.is_symlink() or not candidate.is_file():
            raise ValueError(f"allowlisted source missing or not a regular file: {source_name}")
        target = output / output_name
        shutil.copyfile(candidate, target)
        records.append({
            "path": output_name,
            "sha256": sha256(target),
            "bytes": target.stat().st_size,
        })

    manifest = {
        "schema": "palang-host-bridge-manifest/1.0",
        "status": "STATIC_ALLOWLIST_BUILD",
        "source_commit": os.environ.get("GITHUB_SHA", "LOCAL-UNBOUND"),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "files": records,
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    expected = set(ALLOWLIST.values()) | {"manifest.json"}
    actual = {p.relative_to(output).as_posix() for p in output.rglob("*")}
    unexpected = {name for name in actual if name not in expected}
    missing = expected - actual
    non_regular = [p.relative_to(output).as_posix() for p in output.rglob("*") if p.is_symlink() or not p.is_file()]
    if unexpected or missing or non_regular:
        raise ValueError(
            f"artifact inventory mismatch; unexpected={sorted(unexpected)}, "
            f"missing={sorted(missing)}, non_regular={sorted(non_regular)}"
        )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("HOST-BRIDGE"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = build(args.source, args.output)
    print(json.dumps({
        "result": "PASS",
        "file_count": len(manifest["files"]),
        "manifest_sha256": sha256(args.output / "manifest.json"),
        "source_commit": manifest["source_commit"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
