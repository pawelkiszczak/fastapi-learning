
# Ensure repo root is on sys.path so `project_3` package is importable under pytest
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from fastapi import status
from fastapi.testclient import TestClient

from todoapp import main

client = TestClient(main.app)


def test_return_health_check():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "healthy"}
