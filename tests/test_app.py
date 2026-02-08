import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_read_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_signup_activity():
    response = client.post("/activities/sample_activity/signup?email=test@example.com")
    assert response.status_code in [200, 400]  # 200 for success, 400 for duplicate
    assert "message" in response.json() or "detail" in response.json()


def test_unregister_activity():
    response = client.delete("/activities/sample_activity/unregister?email=test@example.com")
    assert response.status_code in [200, 404]  # 200 for success, 404 for not found
    assert "message" in response.json() or "detail" in response.json()