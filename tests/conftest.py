import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


@pytest.fixture  # reusable code block
def client():
    return TestClient(app)
