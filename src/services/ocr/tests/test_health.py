from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.routes.health import router


def test_health_endpoint_returns_ok() -> None:
    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "albarania-ocr"}
