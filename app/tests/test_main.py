from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_item():
    respone = client.get("/")
    assert respone.status_code == 200
    assert response.json() == {"Hello": "World"}
