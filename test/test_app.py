from app import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}
