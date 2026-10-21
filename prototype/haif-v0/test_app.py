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
