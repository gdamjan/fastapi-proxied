from fastapi.testclient import TestClient


def client():
    # has to be a lazy import to run after conftest.py sets up the env var
    from demo.simple_app import app

    return TestClient(app)


def test_simple():
    response = client().get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World", "root_path": ""}


def test_simple_url():
    response = client().get("/get-health-url")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "health-url": "http://testserver/health"}
