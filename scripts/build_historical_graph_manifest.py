#!/usr/bin/env python3
"""Build a path-keyed, non-destructive historical graph manifest for CI evidence."""
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse, unquote
from datetime import datetime, timezone
import hashlib, json, re, subprocess
from semantic_role_decisions import apply_role_decisions, load_decisions

ROOT = Path(".").resolve()
OUT = ROOT / "audit-output"
OUT.mkdir(exist_ok=True)
try:
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
except Exception:
    commit = "UNKNOWN"
run_utc = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
files = sorted(p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts and p.suffix != ".pyc" and "audit-output" not in p.parts)
evidence = [p for p in files if p.parent.relative_to(ROOT).as_posix() == "evidence" and re.fullmatch(r"evidence-gate-.*\.txt", p.name)]
source_files = [p for p in files if p not in evidence]
stable_map, prod_map, reference_id_map, evt_map, sha_map = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
nodes, local_edges, missing_links, decode_errors, identifier_occurrences = [], [], [], [], []
def vals(body, pattern):
    return sorted(set(m.group(1).strip().strip(chr(96) + "' ") for m in re.finditer(pattern, body, re.I | re.M)))
def id_vals(body, pattern):
    # Keep only conservative identifier tokens; ignore placeholders and prose.
    excluded = {"unknown", "unverified", "none", "null", "n/a", "na", "tbd", "pending",
                "not-assigned", "not-assigned-yet", "not-applicable", "placeholder"}
    result = set()
    for value in vals(body, pattern):
        if not value.strip():
            continue
        token = value.split()[0].strip(" ' ,;:()[]{}")
        if not token or token.casefold() in excluded:
            continue
        if "$" in token or token.startswith(("{{", "<")) or "}}" in token or "%s" in token:
            continue
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/+-]*", token):
            continue
        result.add(token)
    return sorted(result)
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
    stable = id_vals(body, r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Stable ID(?:\s*/\s*شناسهٔ پایدار)?|Stable-ID|Canonical Stable ID|Stable Reference ID|Stable Report ID|شناسهٔ پایدار(?: این نقطه)?|شناسه پایدار(?: این نقطه)?)(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    prod = id_vals(body, r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Production ID(?:\s*/\s*شناسهٔ تولید)?|Production-ID|Production / Registration ID|شناسهٔ تولید|شناسه تولید|شناسهٔ ثبت)(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    reference_ids = id_vals(body, r"^\s*(?:[-*]\s*)?(?:\*\*)?Reference ID(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    versions = vals(body, r"^\s*(?:[-*]\s*)?(?:\*\*)?Version(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    parent_values = vals(body, r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Parent(?: input| event| reference| protocol| architecture| excavation)?|Parent ID|Parent Stable ID)(?:\*\*)?\s*:\s*(?:\*\*)?`?([^`\r\n]+)")
    parents = []
    for pv in parent_values:
        # Prefer visible Markdown link labels over URL paths, so a full event ID is not
        # double-counted with its short EVT number from the filename.
        labels = re.findall(r"\[([^\]]+)\]\(", pv)
        scan_values = labels if labels else [pv]
        for value in scan_values:
            ids = re.findall(r"\b(?:[A-Z0-9]+(?:[-._][A-Z0-9]+){2,}|EVT-\d+)\b", value)
            parents.extend(ids)
    for x in stable: stable_map[x].append(relpath)
    for x in prod: prod_map[x].append(relpath)
    for x in reference_ids: reference_id_map[x].append(relpath)
    # Preserve line-level occurrences for human semantic review. The role is only a
    # candidate; even a metadata-looking line is not automatically accepted as a definition.
    for line_no, line in enumerate(body.splitlines(), 1):
        for ident in stable:
            if ident in line:
                metadata_label = line_no <= 40 and bool(re.match(r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Stable ID|Stable-ID|Canonical Stable ID|Stable Reference ID|Stable Report ID|شناسهٔ پایدار|شناسه پایدار)", line, re.I))
                identifier_occurrences.append({"identifier_type": "STABLE_ID", "identifier_value": ident,
                    "path": relpath, "line": line_no, "line_text": line.strip()[:240],
                    "role_candidate": "DEFINITION_OR_METADATA_REVIEW" if metadata_label else "REFERENCE_REVIEW",
                    "role_status": "UNREVIEWED"})
        for ident in prod:
            if ident in line:
                metadata_label = line_no <= 40 and bool(re.match(r"^\s*(?:[-*]\s*)?(?:\*\*)?(?:Production ID|Production-ID|Production / Registration ID|شناسهٔ تولید|شناسه تولید|شناسهٔ ثبت)", line, re.I))
                identifier_occurrences.append({"identifier_type": "PRODUCTION_ID", "identifier_value": ident,
                    "path": relpath, "line": line_no, "line_text": line.strip()[:240],
                    "role_candidate": "DEFINITION_OR_METADATA_REVIEW" if metadata_label else "REFERENCE_REVIEW",
                    "role_status": "UNREVIEWED"})
        for ident in reference_ids:
            if ident in line:
                metadata_label = line_no <= 40 and bool(re.match(r"^\s*(?:[-*]\s*)?(?:\*\*)?Reference ID", line, re.I))
                identifier_occurrences.append({"identifier_type": "REFERENCE_ID", "identifier_value": ident,
                    "path": relpath, "line": line_no, "line_text": line.strip()[:240],
                    "role_candidate": "DEFINITION_OR_METADATA_REVIEW" if metadata_label else "REFERENCE_REVIEW",
                    "role_status": "UNREVIEWED"})
    evt = re.match(r"EVT-(\d+)-", p.name)
    if evt: evt_map[evt.group(1)].append(relpath)
    own_edges = []
    # Markdown navigation is only meaningful in Markdown documents. Python tests,
    # code templates and fixture strings may contain illustrative Markdown links;
    # counting those as repository edges creates false missing-link findings.
    if p.suffix.lower() in {".md", ".markdown", ".mdx"}:
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
decision_path = ROOT / "data" / "interaction-pairs" / "semantic-role-decisions.jsonl"
role_decisions, role_decision_parse_errors = load_decisions(decision_path)
stable_collisions, stable_decision_summary = apply_role_decisions(stable_collisions, nodes, role_decisions, "STABLE_ID")
prod_collisions, prod_decision_summary = apply_role_decisions(prod_collisions, nodes, role_decisions, "PRODUCTION_ID")
reference_collisions, reference_decision_summary = apply_role_decisions(groups(reference_id_map), nodes, role_decisions, "REFERENCE_ID")
evt_collisions, evt_decision_summary = apply_role_decisions(evt_collisions, nodes, role_decisions, "EVENT_NUMBER")
accepted_decision_ids = set()
for decision_summary in (stable_decision_summary, prod_decision_summary, reference_decision_summary, evt_decision_summary):
    accepted_decision_ids.update(decision_summary.get("accepted_decision_ids", []))
accepted_decisions_by_key = {d.get("decision_id"): d for d in role_decisions if d.get("decision_id") in accepted_decision_ids}
for occurrence in identifier_occurrences:
    for decision in accepted_decisions_by_key.values():
        if occurrence.get("identifier_type") != decision.get("identifier_type") or occurrence.get("identifier_value") != decision.get("identifier_value"):
            continue
        matching = [p for p in decision.get("paths", []) if p.get("path") == occurrence.get("path")]
        if matching:
            occurrence["role_status"] = "ROLE-ADJUDICATED"
            occurrence["decision_id"] = decision.get("decision_id")
            occurrence["adjudicated_role"] = matching[0].get("role")
            break

id_to_paths = defaultdict(set)
for mapping in (stable_map, prod_map, reference_id_map):
    for ident, paths in mapping.items():
        for p in paths: id_to_paths[ident].add(p)
# A short EVT number is a path locator, not a unique identity; preserve all paths if duplicated.
for node in nodes:
    if node["event_number"]:
        id_to_paths[f"EVT-{node['event_number']}"].add(node["path"])
# Explicit canonical path preferences grounded in repository registry/lineage documents.
canonical_preferred_paths = {
    "ARCH-2026-08-29-001": "architecture/ARCH-2026-08-29-001-living-evolutionary-architecture.md",
    "PMA-2026-09-01-001": "architecture/memory/PERSISTENT-MEMORY-ADAPTER-SPEC-2026-09-01.md",
    "MPPA-2026-09-29-002": "architecture/memory/MEMORY-PERSISTENCE-PROOF-ARCHITECTURE-2026-09-29.md",
    "THREE-LAYER-REGISTRATION-ARCHITECTURE-2026-10-06-001": "docs/reference/REFERENCE-DOCUMENTS/THREE-LAYER-SYNCHRONOUS-DURABLE-REGISTRATION-2026-10-06-001.md",
    "3LR-REG-2026-10-06-001": "docs/reference/REFERENCE-DOCUMENTS/THREE-LAYER-SYNCHRONOUS-DURABLE-REGISTRATION-2026-10-06-001.md",
    "THREE-LEVEL-GOVERNED-REGISTRATION-COMMAND-2026-10-06-001": "docs/reference/REFERENCE-DOCUMENTS/THREE-LEVEL-GOVERNED-REGISTRATION-COMMAND-2026-10-06-001.md",
    "AREP-2026-08-31-001": "docs/protocols/ARCHIVE-REVIVAL-EXECUTION-PATH.md",
    "PMRH-2026-09-06-001": "checkpoints/0.0/PMRH-2026-09-06-LIVE-CHECKPOINT-001.md"
}
path_stems = {Path(n["path"]).stem: n["path"] for n in nodes}
parent_edges, unresolved, ambiguous = [], [], []
for node in nodes:
    for parent in node["declared_parents"]:
        candidates = sorted(id_to_paths.get(parent, set()))
        if not candidates and len(parent) >= 12:
            candidates = sorted({path for ident, paths in id_to_paths.items() if ident.startswith(parent) for path in paths})
        if not candidates and len(parent) >= 12:
            candidates = sorted({n["path"] for n in nodes if Path(n["path"]).stem == parent or Path(n["path"]).stem.startswith(parent + "-") or parent in Path(n["path"]).stem})
        preferred = canonical_preferred_paths.get(parent)
        if preferred and preferred in candidates:
            resolution = "CANONICAL_PREFERRED_WITH_DUPLICATE_OCCURRENCES"
            selected_path = preferred
        elif not candidates:
            resolution, selected_path = "UNRESOLVED", None
        elif len(candidates) == 1:
            resolution, selected_path = "UNIQUE", candidates[0]
        else:
            resolution, selected_path = "AMBIGUOUS", None
        edge = {"source": node["path"], "target_id": parent, "candidate_paths": candidates,
                "selected_path": selected_path, "resolution": resolution}
        parent_edges.append(edge)
        if resolution == "UNRESOLVED": unresolved.append(edge)
        elif resolution == "AMBIGUOUS": ambiguous.append(edge)
# Role-based duplicate decisions are deliberately non-destructive and remain proposals
# until inbound references and source history are checked. Hash keys match the audited bytes.
alias_decisions = {
    "2b018d899aba7b4483a083e170eaea878cab9d024e24c53fc496f70fef4ac24f": {"canonical_candidate": "docs/registrations/REG-2026-09-03-GAP-CLOSURE-OUTCOME-003.md", "status": "PROPOSED_EARLIEST_COMMIT_ALIAS_005_NO_INBOUND_LINKS"},
    "2d503cce1b2bad4533362da439d1668b6a4fb5fbafb6fcd6cf6c950ab93dfc95": {"canonical_candidate": "docs/reference/REFERENCE-DOCUMENTS/GAP-CLOSURE-RETRIEVAL-EVIDENCE-2026-08-31-001.md", "status": "PROPOSED_REFERENCE_WITH_PROVENANCE_MIRROR"},
    "45140056b737bd503a0dc6490677afe3bdb0df9e59abfcc1c624e49f54cad500": {"canonical_candidate": "checkpoints/0.0/0.0-VAULT-INITIAL-POINT-2026-09-13.md", "status": "PROPOSED_CHECKPOINT_WITH_REFERENCE_MIRROR"},
    "4944e965c2326ed54e8aeabb2814bb0f6bb6fc12641cf07540c93cc3ed823deb": {"canonical_candidate": "docs/governance/0.0-VAULT/LIVING-STATUS-2026-09-13.md", "status": "PROPOSED_GOVERNANCE_WITH_REFERENCE_MIRROR"},
    "4cf0b6b7be9aa5b989be1a7fdca7d481c3ee883436b70ac5ed0762565c961049": {"canonical_candidate": "docs/governance/0.0-VAULT/0.0-VAULT-GOVERNANCE-2026-09-13.md", "status": "PROPOSED_GOVERNANCE_WITH_REFERENCE_MIRROR"},
    "605b48decf4cbd0f87535b8cf78bf01b5362907f5094faac3886ba8f8da73f6f": {"canonical_candidate": "checkpoints/0.0/REG-2026-09-03-GAP-CLOSURE-OUTCOME-001.md", "status": "PROPOSED_EARLIEST_COMMIT_ALIAS_002_NO_INBOUND_LINKS"},
    "7023f4ce9e459b3acf0eeaf371c02103b4adce7554b5d1c4043edf42bb1b4f73": {"canonical_candidate": "docs/governance/0.0-VAULT/PRODUCTION-REGISTRY-REFERENCE-2026-09-13.md", "status": "PROPOSED_GOVERNANCE_WITH_REFERENCE_MIRROR"},
    "8764cc78241e5b880cf277fa720e6bd13dd68d63e0e1856f1e7d101bbb7b588d": {"canonical_candidate": "docs/reference/REFERENCE-DOCUMENTS/ADIP-2026-08-31-001.md", "status": "PROPOSED_REFERENCE_WITH_PROVENANCE_MIRROR"},
    "9cb520f4f1c27f5f6b79fdfb2c133883599665b2c9c952932cfb3441eae8c0e9": {"canonical_candidate": "registry/0.0-VAULT-REGISTRY-2026-09-13.md", "status": "PROPOSED_REGISTRY_WITH_REFERENCE_MIRROR"},
    "a0384763731682830b11f5678fa4c45bb7378f6b73fe5ca9eed202be77147a43": {"canonical_candidate": "docs/reference/REFERENCE-DOCUMENTS/MASTER-REFERENCE-GAPC-2026-08-31-001.md", "status": "PROPOSED_REFERENCE_WITH_PROVENANCE_MIRROR"},
    "d3921368cf3ad35d6b428860c67ad47f4e395c731f9249dc7b84006614558dad": {"canonical_candidate": "architecture/0.0-VAULT-ARCHITECTURAL-PLACEMENT-2026-09-13.md", "status": "PROPOSED_ARCHITECTURE_WITH_REFERENCE_MIRROR"}
}
alias_edges = []
for group in duplicates:
    decision = alias_decisions.get(group["sha256"], {"canonical_candidate": None, "status": "OPEN_NO_DECISION"})
    alias_edges.append({"candidate_paths": group["paths"], "sha256": group["sha256"], **decision,
                        "acceptance": "PROPOSED_NOT_FINAL_UNTIL_INBOUND_LINK_AND_HISTORY_REVIEW"})
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
               "reference_id_collision_groups": len(groups(reference_id_map)),
               "reviewed_stable_id_collision_groups": stable_decision_summary["groups_reviewed"],
               "unreviewed_stable_id_collision_groups": stable_decision_summary["groups_unreviewed"],
               "event_number_collision_groups": len(evt_collisions), "exact_content_duplicate_groups": len(duplicates),
               "declared_parent_edges": len(parent_edges), "unresolved_parent_edges": len(unresolved),
               "ambiguous_parent_edges": len(ambiguous), "proposed_alias_edges": len(alias_edges),
               "identifier_occurrences": len(identifier_occurrences)},
    "nodes": nodes, "parent_edges": parent_edges, "unresolved_parent_edges": unresolved,
    "semantic_role_decisions": {"stable_id": stable_decision_summary, "production_id": prod_decision_summary, "reference_id": reference_decision_summary, "event_number": evt_decision_summary, "parse_errors": role_decision_parse_errors},
    "ambiguous_parent_edges": ambiguous, "local_link_edges": local_edges, "missing_local_links": missing_links,
    "stable_id_collisions": stable_collisions, "production_id_collisions": prod_collisions,
    "reference_id_collisions": reference_collisions,
    "event_number_collisions": evt_collisions, "exact_content_duplicate_groups": duplicates,
    "proposed_alias_edges": alias_edges, "decode_errors": decode_errors,
    "semantic_status": "STRUCTURAL AUDIT WITH SOURCE-HASH-VERIFIED ROLE ANNOTATIONS. Human semantic review and architecture relationship adjudication remain required."
}
# Build a review queue that exposes every ID occurrence and inbound/outbound local links.
# It is a triage aid, not semantic proof or an automatic promotion decision.
inbound = defaultdict(list)
outbound = defaultdict(list)
for edge in local_edges:
    outbound[edge["source"]].append(edge)
    if edge["exists"]:
        inbound[edge["resolved_path"]].append(edge)
for occurrence in identifier_occurrences:
    occurrence["inbound_local_link_count"] = len(inbound.get(occurrence["path"], []))
    occurrence["outbound_local_link_count"] = len(outbound.get(occurrence["path"], []))
link_context_by_path = {
    node["path"]: {
        "inbound": [{"source": e["source"], "target": e["target"]} for e in inbound.get(node["path"], [])],
        "outbound": [{"target": e["target"], "resolved_path": e["resolved_path"], "exists": e["exists"]} for e in outbound.get(node["path"], [])]
    }
    for node in nodes
}
review_queue = {
    "schema": "palang-semantic-review-queue/v1",
    "audit_time_utc": run_utc,
    "repository_commit": commit,
    "scope": "Line-level identifier occurrences with role candidates only; human review required.",
    "counts": {
        "identifier_occurrences": len(identifier_occurrences),
        "stable_id_occurrences": sum(o["identifier_type"] == "STABLE_ID" for o in identifier_occurrences),
        "production_id_occurrences": sum(o["identifier_type"] == "PRODUCTION_ID" for o in identifier_occurrences),
        "reference_id_occurrences": sum(o["identifier_type"] == "REFERENCE_ID" for o in identifier_occurrences),
        "definition_or_metadata_candidates": sum(o["role_candidate"] == "DEFINITION_OR_METADATA_REVIEW" for o in identifier_occurrences),
        "reference_candidates": sum(o["role_candidate"] == "REFERENCE_REVIEW" for o in identifier_occurrences),
        "reviewed_occurrences": sum(o.get("role_status") == "ROLE-ADJUDICATED" for o in identifier_occurrences),
        "unreviewed_occurrences": sum(o.get("role_status") != "ROLE-ADJUDICATED" for o in identifier_occurrences)
    },
    "occurrences": identifier_occurrences,
    "link_context_by_path": link_context_by_path,
    "groups": {
        "stable_id": stable_collisions,
        "production_id": prod_collisions,
        "reference_id": reference_collisions,
        "event_number": evt_collisions,
        "exact_content_duplicates": duplicates
    },
    "semantic_role_decisions": {"stable_id": stable_decision_summary, "production_id": prod_decision_summary, "reference_id": reference_decision_summary, "event_number": evt_decision_summary, "parse_errors": role_decision_parse_errors},
    "semantic_boundary": "Role candidates are not final decisions. Source-hash-verified decisions annotate only matching groups; raw collision counts remain visible and unresolved groups remain open."
}
(OUT / "historical-0.0-semantic-review-queue.json").write_text(json.dumps(review_queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(OUT / "historical-0.0-canonical-graph-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
summary = ["# Historical graph manifest summary", f"- Audit UTC: {run_utc}", f"- Commit: {commit}"]
summary += [f"- {k}: {v}" for k, v in manifest["counts"].items()]
summary += ["", "## Semantic boundary", "- Structural extraction remains distinct from semantic adjudication.", "- Source-hash-verified role decisions annotate reviewed groups; raw collision counts remain visible.", "- Proposed aliases are not automatically accepted; preserve historical files and never auto-delete duplicates.", "- Review parent ambiguities, missing links and identity collisions before closure."]
(OUT / "historical-0.0-graph-manifest-summary.txt").write_text("\n".join(summary) + "\n", encoding="utf-8")
print("\n".join(summary))

for item in missing_links:
    print("GRAPH_MISSING_LOCAL_LINK=" + json.dumps({
        "source": item.get("source"),
        "target": item.get("target"),
        "resolved_path": item.get("resolved_path")
    }, ensure_ascii=False, sort_keys=True))

