from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_page():
    response = client.get("/pages/boat.lifestyle")
    assert response.status_code == 200
