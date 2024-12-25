from fastapi.testclient import TestClient


def client():
    # has to be a lazy import to run after conftest.py sets up the env var
    from demo.routed_app import app

    return TestClient(app)


def test_routed():
    response = client().get("/api")
    assert response.status_code == 200
    # root_path inconsistent!
    assert response.json() == {"message": "Hello World", "root_path": ""}


def test_routed_url():
    response = client().get("/api/get-health-url")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "health-url": "http://testserver/api/health",
    }
