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
