from fastapi.testclient import TestClient

from app import create_app


def client_for(tmp_path):
    app = create_app(tmp_path / "test-haif.sqlite3")
    return TestClient(app)


def test_anchor_write_readback_and_retrieval(tmp_path):
    with client_for(tmp_path) as client:
        created = client.post(
            "/api/v1/anchors",
            json={
                "resume_summary": "Continue prototype work",
                "open_tasks": ["add semantic graph"],
                "timezone": "Asia/Tehran",
                "source_origin": "test fixture",
            },
        )
        assert created.status_code == 201
        payload = created.json()
        assert payload["status"] == "WRITE_READBACK_VERIFIED"
        assert payload["content_sha256"]
        assert payload["open_tasks"] == ["add semantic graph"]

        fetched = client.get(f"/api/v1/anchors/{payload['anchor_id']}")
        assert fetched.status_code == 200
        assert fetched.json()["resume_summary"] == "Continue prototype work"
        assert fetched.json()["content_sha256"] == payload["content_sha256"]


def test_second_anchor_does_not_replace_first(tmp_path):
    with client_for(tmp_path) as client:
        first = client.post("/api/v1/anchors", json={"resume_summary": "Anchor A"}).json()
        second = client.post("/api/v1/anchors", json={"resume_summary": "Anchor B"}).json()

        assert first["anchor_id"] != second["anchor_id"]
        listed = client.get("/api/v1/anchors").json()
        ids = {item["anchor_id"] for item in listed["items"]}
        assert first["anchor_id"] in ids
        assert second["anchor_id"] in ids
        assert listed["count"] == 2


def test_event_links_to_anchor_and_does_not_invent_message_time(tmp_path):
    with client_for(tmp_path) as client:
        anchor = client.post("/api/v1/anchors", json={"resume_summary": "Anchor for event"}).json()
        event_response = client.post(
            "/api/v1/events",
            json={
                "event_type": "DECISION",
                "summary": "Use local SQLite for prototype",
                "anchor_id": anchor["anchor_id"],
                "source_origin": "test fixture",
            },
        )
        assert event_response.status_code == 201
        event = event_response.json()
        assert event["status"] == "WRITE_READBACK_VERIFIED"
        assert event["anchor_id"] == anchor["anchor_id"]
        assert event["user_message_time"] is None
        fetched = client.get(f"/api/v1/events/{event['event_id']}")
        assert fetched.status_code == 200
        assert fetched.json()["summary"] == "Use local SQLite for prototype"


def test_event_rejects_unknown_anchor(tmp_path):
    with client_for(tmp_path) as client:
        response = client.post(
            "/api/v1/events",
            json={
                "event_type": "NOTE",
                "summary": "Must not point to missing anchor",
                "anchor_id": "missing-anchor",
            },
        )
        assert response.status_code == 404
        assert response.json()["detail"] == "ANCHOR_NOT_FOUND"


def test_health_discloses_local_only_persistence(tmp_path):
    with client_for(tmp_path) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["persistence_scope"] == "LOCAL_SQLITE_ONLY"
        assert response.json()["external_persistence"] == "UNVERIFIED"


def test_document_ingest_readback_and_search_preserve_provenance(tmp_path):
    with client_for(tmp_path) as client:
        created = client.post(
            "/api/v1/documents",
            json={
                "title": "HAIF master reference",
                "source_path": "docs/architecture/master.md",
                "version": "1.2.0",
                "content": "HAIF preserves interaction continuity and evidence provenance.",
                "source_origin": "repository test fixture",
            },
        )
        assert created.status_code == 201
        document = created.json()
        assert document["status"] == "WRITE_READBACK_VERIFIED"
        assert document["content_sha256"]
        assert document["source_path"] == "docs/architecture/master.md"
        assert document["version"] == "1.2.0"

        found = client.get("/api/v1/search", params={"q": "PROVENANCE"})
        assert found.status_code == 200
        result = found.json()
        assert result["status"] == "RETRIEVED_WITH_PROVENANCE"
        assert result["count"] == 1
        assert result["items"][0]["document_id"] == document["document_id"]
        assert result["items"][0]["source_path"] == "docs/architecture/master.md"
        assert result["items"][0]["version"] == "1.2.0"
        assert result["items"][0]["retrieval_method"] == "CASEFOLD_SUBSTRING"


def test_document_search_returns_no_false_match(tmp_path):
    with client_for(tmp_path) as client:
        client.post(
            "/api/v1/documents",
            json={"title": "Reference A", "source_path": "a.md", "content": "continuity only"},
        )
        result = client.get("/api/v1/search", params={"q": "nonexistent-token"}).json()
        assert result["count"] == 0
        assert result["items"] == []


def test_document_survives_app_restart_with_same_hash_and_provenance(tmp_path):
    db_path = tmp_path / "restart-haif.sqlite3"
    with TestClient(create_app(db_path)) as first_client:
        created = first_client.post(
            "/api/v1/documents",
            json={
                "title": "Restart continuity proof",
                "source_path": "docs/reference/master.md",
                "version": "2.0.1",
                "content": "The anchor must remain retrievable after restart.",
                "source_origin": "restart test fixture",
            },
        )
        assert created.status_code == 201
        original = created.json()

    with TestClient(create_app(db_path)) as restarted_client:
        found = restarted_client.get("/api/v1/search", params={"q": "retrievable after restart"})
        assert found.status_code == 200
        result = found.json()
        assert result["count"] == 1
        item = result["items"][0]
        assert item["document_id"] == original["document_id"]
        assert item["content_sha256"] == original["content_sha256"]
        assert item["source_path"] == "docs/reference/master.md"
        assert item["version"] == "2.0.1"
        assert item["source_origin"] == "restart test fixture"


def test_repository_ingestion_manifest_preserves_source_path_version_and_commit(tmp_path, monkeypatch):
    import json
    from io import BytesIO

    import ingest_repository_docs as importer

    for relative in importer.ALLOWLIST:
        source = tmp_path / relative
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text("# Reference title\n- Version / نسخه: 2.4.1\nsource evidence", encoding="utf-8")

    monkeypatch.setattr(importer, "current_commit", lambda _root: "abc123-test-commit")
    captured = []

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def read(self):
            return json.dumps({
                "status": "WRITE_READBACK_VERIFIED",
                "document_id": "doc-test",
                "content_sha256": "a" * 64,
            }).encode("utf-8")

    def fake_urlopen(request, timeout):
        assert timeout == 20
        captured.append(json.loads(request.data.decode("utf-8")))
        return FakeResponse()

    monkeypatch.setattr(importer, "urlopen", fake_urlopen)
    report = importer.ingest("http://haif.test/", tmp_path)

    assert report["complete"] is True
    assert report["verified_count"] == len(importer.ALLOWLIST)
    assert len(captured) == len(importer.ALLOWLIST)
    assert all(payload["version"] == "2.4.1" for payload in captured)
    assert all("commit=abc123-test-commit" in payload["source_origin"] for payload in captured)
    assert {payload["source_path"] for payload in captured} == set(importer.ALLOWLIST)


def test_repository_ingestion_fails_closed_when_source_is_missing(tmp_path, monkeypatch):
    import ingest_repository_docs as importer

    monkeypatch.setattr(importer, "current_commit", lambda _root: "abc123-test-commit")
    report = importer.ingest("http://haif.test", tmp_path)

    assert report["complete"] is False
    assert report["verified_count"] == 0
    assert all(item["status"] == "SOURCE_MISSING" for item in report["results"])


def test_real_repository_allowlist_ingests_searches_and_survives_restart(tmp_path, monkeypatch):
    import json
    from io import BytesIO
    from pathlib import Path

    import ingest_repository_docs as importer

    root = Path(__file__).resolve().parents[2]
    missing = [relative for relative in importer.ALLOWLIST if not (root / relative).is_file()]
    assert missing == []

    db_path = tmp_path / "real-repository-ingest.sqlite3"
    first_client_context = client_for(tmp_path)
    # Use a dedicated app database and adapt the importer's HTTP client to this real API
    # TestClient. The document payloads come from the checked-out repository files.
    first_client_context.close() if hasattr(first_client_context, "close") else None
    from fastapi.testclient import TestClient
    from app import create_app

    with TestClient(create_app(db_path)) as client:
        def local_api_urlopen(request, timeout):
            assert timeout == 20
            payload = json.loads(request.data.decode("utf-8"))
            response = client.post("/api/v1/documents", json=payload)

            class Response:
                def __enter__(self):
                    return self

                def __exit__(self, *_args):
                    return False

                def read(self):
                    return json.dumps(response.json(), ensure_ascii=False).encode("utf-8")

            return Response()

        monkeypatch.setattr(importer, "urlopen", local_api_urlopen)
        monkeypatch.setattr(importer, "current_commit", lambda _root: "integration-test-commit")
        report = importer.ingest("http://local-test", root)
        assert report["complete"] is True
        assert report["verified_count"] == 6
        assert len({item["source_path"] for item in report["results"]}) == 6

        search = client.get(
            "/api/v1/search",
            params={"q": "this file itself is not proof"},
        )
        assert search.status_code == 200
        result = search.json()
        assert result["count"] == 1
        item = result["items"][0]
        assert item["source_path"] == (
            "docs/reference/REFERENCE-DOCUMENTS/"
            "PALANG-RETURN-EXECUTION-MASTER-ANCHOR-2026-10-21-001.md"
        )
        assert item["source_origin"].endswith("commit=integration-test-commit; allowlisted repository document")
        assert item["content_sha256"]

        expected = {
            "document_id": item["document_id"],
            "content_sha256": item["content_sha256"],
            "source_path": item["source_path"],
            "version": item["version"],
            "source_origin": item["source_origin"],
        }

    with TestClient(create_app(db_path)) as restarted_client:
        restarted = restarted_client.get(
            "/api/v1/search",
            params={"q": "this file itself is not proof"},
        )
        assert restarted.status_code == 200
        assert restarted.json()["count"] == 1
        restored = restarted.json()["items"][0]
        assert {key: restored[key] for key in expected} == expected


def interaction_payload(sequence=5, summary="Continue from model initial"):
    suffix = f"20261022-{sequence:03d}"
    return {
        "interaction_id": f"INT-{suffix}",
        "input_id": f"IN-{suffix}",
        "output_id": f"OUT-{suffix}",
        "sequence": sequence,
        "version": "1.0.0",
        "status": "VALIDATED",
        "time_evidence": {
            "repository_commit_utc": None,
            "tehran_equivalent": None,
            "message_timestamp": None,
            "event_timestamp": None,
            "operation_timestamp": None,
            "test_timestamp": None,
            "message_timestamp_status": "NOT_EXPOSED",
        },
        "input": {
            "content_ref": "conversation-context://IN-20261022-005",
            "content_status": "REFERENCE_ONLY",
            "summary": "User asks to continue the initial model path.",
        },
        "output": {
            "content_ref": "repository-reference://OUT-20261022-005",
            "content_status": "REFERENCE_ONLY",
            "summary": summary,
        },
        "behavior_analysis": [{
            "candidate": "The current continuation target is the initial model path, not the independent Dropbox branch.",
            "classification": "OBSERVATION",
            "evidence_refs": ["EVT-0091"],
            "confidence": 1.0,
            "counterevidence": [],
        }],
        "lineage": {
            "parent_ids": ["EVT-0084", "EVT-0085", "EVT-0091"],
            "related_event_ids": ["EVT-0084", "EVT-0085", "EVT-0091"],
            "architecture_refs": ["PALANG-CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-2026-10-22-001"],
            "gap_ids": ["PALANG-BEHAVIOR-HUNTER-RUNTIME-GAP-2026-10-22-001"],
            "evidence_refs": ["EVT-0091"],
            "recovery_pointer": "docs/reference/REFERENCE-DOCUMENTS/CONTINUATION-MODEL-INITIAL-NOT-DROPBOX-MASTER-REFERENCE-2026-10-22-001.md",
        },
        "verification": {
            "schema_validation": "PASS",
            "readback": "PASS",
            "runtime_capture": "NOT_VERIFIED",
            "notes": ["Test payload only; does not prove automatic host capture."],
        },
    }


def test_interaction_pair_write_readback_and_reverse_lookup_by_all_ids(tmp_path):
    payload = interaction_payload()
    with client_for(tmp_path) as client:
        created = client.post("/api/v1/interactions", json=payload)
        assert created.status_code == 201, created.text
        stored = created.json()
        assert stored["status"] == "WRITE_READBACK_VERIFIED"
        assert stored["content_sha256"]

        for lookup_id in (payload["interaction_id"], payload["input_id"], payload["output_id"]):
            response = client.get(f"/api/v1/interactions/{lookup_id}")
            assert response.status_code == 200
            assert response.json()["interaction_id"] == payload["interaction_id"]
            assert response.json()["input_id"] == payload["input_id"]
            assert response.json()["output_id"] == payload["output_id"]
            assert response.json()["content_sha256"] == stored["content_sha256"]


def test_interaction_pair_idempotent_retry_does_not_duplicate(tmp_path):
    payload = interaction_payload()
    with client_for(tmp_path) as client:
        first = client.post("/api/v1/interactions", json=payload)
        second = client.post("/api/v1/interactions", json=payload)
        assert first.status_code == 201
        assert second.status_code == 201
        assert second.json()["status"] == "IDEMPOTENT_REPLAY_READBACK_VERIFIED"
        assert second.json()["content_sha256"] == first.json()["content_sha256"]


def test_interaction_pair_conflicting_reuse_fails_closed(tmp_path):
    payload = interaction_payload()
    with client_for(tmp_path) as client:
        first = client.post("/api/v1/interactions", json=payload)
        assert first.status_code == 201
        changed = interaction_payload(summary="Conflicting reuse")
        response = client.post("/api/v1/interactions", json=changed)
        assert response.status_code == 409
        assert response.json()["detail"] == "INTERACTION_ID_CONFLICT"


def test_interaction_pair_survives_app_restart_and_unknown_lookup_is_404(tmp_path):
    db_path = tmp_path / "interaction-restart.sqlite3"
    payload = interaction_payload()
    with TestClient(create_app(db_path)) as client:
        created = client.post("/api/v1/interactions", json=payload)
        assert created.status_code == 201, created.text
        expected = created.json()

    with TestClient(create_app(db_path)) as restarted:
        recovered = restarted.get(f"/api/v1/interactions/{payload['input_id']}")
        assert recovered.status_code == 200
        assert recovered.json()["interaction_id"] == payload["interaction_id"]
        assert recovered.json()["content_sha256"] == expected["content_sha256"]
        assert recovered.json()["output_id"] == payload["output_id"]
        missing = restarted.get("/api/v1/interactions/INT-20261022-999")
        assert missing.status_code == 404
        assert missing.json()["detail"] == "INTERACTION_NOT_FOUND"


def test_interaction_pair_rejects_mismatched_ids(tmp_path):
    payload = interaction_payload()
    payload["output_id"] = "OUT-20261022-006"
    with client_for(tmp_path) as client:
        response = client.post("/api/v1/interactions", json=payload)
        assert response.status_code == 422
        assert response.json()["detail"] == "INTERACTION_ID_PAIR_MISMATCH"

