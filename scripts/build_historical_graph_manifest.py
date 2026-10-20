#!/usr/bin/env python3
"""Build a path-keyed, non-destructive historical graph manifest for CI evidence."""
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse, unquote
from datetime import datetime, timezone
import hashlib, json, re, subprocess

ROOT = Path(".").resolve()
OUT = ROOT / "audit-output"
OUT.mkdir(exist_ok=True)
try:
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
except Exception:
    commit = "UNKNOWN"
run_utc = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
files = sorted(p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and "audit-output" not in p.parts)
evidence = [p for p in files if p.parent.relative_to(ROOT).as_posix() == "evidence" and re.fullmatch(r"evidence-gate-.*\.txt", p.name)]
source_files = [p for p in files if p not in evidence]
stable_map, prod_map, evt_map, sha_map = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
nodes, local_edges, missing_links, decode_errors = [], [], [], []
def vals(body, pattern):
    return sorted(set(m.group(1).strip().strip("`' ") for m in re.finditer(pattern, body, re.I | re.M)))
for p in source_files:
    raw = p.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    relpath = p.relative_to(ROOT).as_posix()
    sha_map[sha].append(relpath)
    try:
        body = raw.decode("utf-8")
    except UnicodeDecodeError:
        decode_errors.append(relpath)
        continue
    stable = vals(body, r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Stable ID|Stable-ID|Canonical Stable ID)(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    prod = vals(body, r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Production ID|Production-ID)(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    versions = vals(body, r"^\s*(?:[-*]\s*)?(?:\*\*)?Version(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    parent_values = vals(body, r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Parent(?: input| event| reference| protocol| architecture| excavation)?|Parent ID|Parent Stable ID)(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    parents = []
    for pv in parent_values:
        # Extract only identifier-shaped tokens. Do not turn prose, markdown emphasis,
        # destination labels or path fragments into fabricated parent nodes.
        ids = re.findall(r"\b(?:EVT-\d+|[A-Z0-9]+(?:-[A-Z0-9]+){2,})\b", pv)
        parents.extend(ids)
    for x in stable: stable_map[x].append(relpath)
    for x in prod: prod_map[x].append(relpath)
    evt = re.match(r"EVT-(\d+)-", p.name)
    if evt: evt_map[evt.group(1)].append(relpath)
    own_edges = []
    for m in re.finditer(r"!??\[[^\]]*\]\(([^)]+)\)", body):
        target = m.group(1).strip().split()[0].strip("<>")
        if not target or target.startswith("#"): continue
        u = urlparse(target)
        if u.scheme or u.netloc or not u.path: continue
        candidate = (p.parent / unquote(u.path)).resolve()
        try: resolved = candidate.relative_to(ROOT).as_posix()
        except ValueError: continue
        edge = {"source": relpath, "target": target, "resolved_path": resolved, "exists": candidate.exists()}
        own_edges.append(edge); local_edges.append(edge)
        if not candidate.exists(): missing_links.append(edge)
    nodes.append({"path": relpath, "sha256": sha, "bytes": len(raw), "stable_ids": stable,
                  "production_ids": prod, "versions": versions, "declared_parents": parents,
                  "event_number": evt.group(1) if evt else None, "local_links": own_edges})
def groups(mapping):
    return [{"key": key, "paths": sorted(set(paths))} for key, paths in sorted(mapping.items()) if len(set(paths)) > 1]
stable_collisions, prod_collisions, evt_collisions = groups(stable_map), groups(prod_map), groups(evt_map)
duplicates = [{"sha256": sha, "paths": sorted(paths)} for sha, paths in sorted(sha_map.items()) if len(set(paths)) > 1]
id_to_paths = defaultdict(set)
for mapping in (stable_map, prod_map):
    for ident, paths in mapping.items():
        for p in paths: id_to_paths[ident].add(p)
# A short EVT number is a path locator, not a unique identity; preserve all paths if duplicated.
for node in nodes:
    if node["event_number"]:
        id_to_paths[f"EVT-{node['event_number']}"].add(node["path"])
parent_edges, unresolved, ambiguous = [], [], []
for node in nodes:
    for parent in node["declared_parents"]:
        candidates = sorted(id_to_paths.get(parent, set()))
        edge = {"source": node["path"], "target_id": parent, "candidate_paths": candidates,
                "resolution": "UNRESOLVED" if not candidates else ("UNIQUE" if len(candidates) == 1 else "AMBIGUOUS")}
        parent_edges.append(edge)
        if not candidates: unresolved.append(edge)
        elif len(candidates) > 1: ambiguous.append(edge)
alias_edges = []
for group in duplicates:
    paths = group["paths"]
    for alias in paths[1:]:
        alias_edges.append({"canonical_candidate": paths[0], "alias_candidate": alias,
                            "sha256": group["sha256"], "status": "PROPOSED_ONLY_REQUIRES_REVIEW"})
manifest = {
    "schema": "palang-historical-graph-manifest/v1", "audit_time_utc": run_utc, "repository_commit": commit,
    "scope": "Path-keyed structural manifest. It does not claim complete natural-language semantic adjudication.",
    "counts": {"all_files_including_evidence": len(files), "source_files": len(source_files),
               "generated_evidence_gate_files": len(evidence), "text_nodes_scanned": len(nodes),
               "decode_errors": len(decode_errors), "paths_with_0.0": sum("0.0" in p.as_posix() for p in files),
               "checkpoint_paths": sum("checkpoint" in p.as_posix().lower() for p in files),
               "EVT_files": sum(bool(re.match(r"EVT-\d+-.+", p.name)) for p in files),
               "reference_document_paths": sum(p.relative_to(ROOT).as_posix().startswith("docs/reference/REFERENCE-DOCUMENTS/") for p in files),
               "local_link_edges": len(local_edges), "missing_local_links": len(missing_links),
               "stable_id_collision_groups": len(stable_collisions), "production_id_collision_groups": len(prod_collisions),
               "event_number_collision_groups": len(evt_collisions), "exact_content_duplicate_groups": len(duplicates),
               "declared_parent_edges": len(parent_edges), "unresolved_parent_edges": len(unresolved),
               "ambiguous_parent_edges": len(ambiguous), "proposed_alias_edges": len(alias_edges)},
    "nodes": nodes, "parent_edges": parent_edges, "unresolved_parent_edges": unresolved,
    "ambiguous_parent_edges": ambiguous, "local_link_edges": local_edges, "missing_local_links": missing_links,
    "stable_id_collisions": stable_collisions, "production_id_collisions": prod_collisions,
    "event_number_collisions": evt_collisions, "exact_content_duplicate_groups": duplicates,
    "proposed_alias_edges": alias_edges, "decode_errors": decode_errors,
    "semantic_status": "STRUCTURAL ONLY. Human semantic review and architecture relationship adjudication remain required."
}
(OUT / "historical-0.0-canonical-graph-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
summary = ["# Historical graph manifest summary", f"- Audit UTC: {run_utc}", f"- Commit: {commit}"]
summary += [f"- {k}: {v}" for k, v in manifest["counts"].items()]
summary += ["", "## Semantic boundary", "- Structural extraction only; proposed alias edges are not adjudicated.", "- Preserve historical files; never auto-delete duplicates.", "- Review parent ambiguities, missing links and identity collisions before closure."]
(OUT / "historical-0.0-graph-manifest-summary.txt").write_text("\n".join(summary) + "\n", encoding="utf-8")
print("\n".join(summary))
