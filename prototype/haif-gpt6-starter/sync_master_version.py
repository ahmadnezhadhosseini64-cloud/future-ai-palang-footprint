#!/usr/bin/env python3
"""Synchronize the portable starter mother and manifest from one canonical source."""
from __future__ import annotations
import argparse, json, os, re, sys, tempfile
from pathlib import Path

VERSION_RE = re.compile(r"^##\s+نسخهٔ\s+(\d+\.\d+\.\d+)\b")

def extract_version(master_bytes: bytes) -> str:
    try:
        text = master_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("canonical mother is not valid UTF-8") from exc
    first = next((line for line in text.splitlines() if line.strip()), "")
    match = VERSION_RE.match(first)
    if not match:
        raise ValueError("canonical mother first heading does not contain a semantic version")
    return match.group(1)

def _atomic_replace(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data); stream.flush(); os.fsync(stream.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)

def synchronize(source: Path, target: Path, manifest_path: Path) -> dict:
    source, target, manifest_path = source.resolve(), target.resolve(), manifest_path.resolve()
    if len({source, target, manifest_path}) != 3:
        raise ValueError("source, target and manifest must be three distinct files")
    source_bytes = source.read_bytes()
    version = extract_version(source_bytes)
    old_target = target.read_bytes() if target.exists() else None
    old_manifest = manifest_path.read_bytes()
    manifest = json.loads(old_manifest.decode("utf-8"))
    stable_id, production_id = manifest.get("stable_id"), manifest.get("production_id")
    if not all(isinstance(v, str) and v.strip() for v in (stable_id, production_id)):
        raise ValueError("manifest stable_id/production_id missing; refusing to sync")
    previous = manifest.get("current_living_master_version")
    manifest["current_living_master_version"] = version
    new_manifest = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\\n").encode("utf-8")
    try:
        _atomic_replace(target, source_bytes)
        _atomic_replace(manifest_path, new_manifest)
        check = json.loads(manifest_path.read_text(encoding="utf-8"))
        if target.read_bytes() != source_bytes:
            raise RuntimeError("mother byte read-back mismatch")
        if check.get("current_living_master_version") != version:
            raise RuntimeError("manifest version read-back mismatch")
        if check.get("stable_id") != stable_id or check.get("production_id") != production_id:
            raise RuntimeError("stable package identity changed")
    except Exception:
        if old_target is None: target.unlink(missing_ok=True)
        else: _atomic_replace(target, old_target)
        _atomic_replace(manifest_path, old_manifest)
        raise
    return {"status":"SYNCED_AND_READBACK_VERIFIED","source_version":version,
            "previous_version":previous,"stable_id":stable_id,"production_id":production_id,
            "source_bytes":len(source_bytes)}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True); parser.add_argument("--target", required=True)
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(synchronize(Path(args.source),Path(args.target),Path(args.manifest)),ensure_ascii=False,indent=2))
        return 0
    except Exception as exc:
        print(f"BLOCKED: {exc}",file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
