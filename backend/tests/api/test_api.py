import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello, World!"

def test_get_persons():
    response = client.get("/person/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_person():
    response = client.get("/person/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)



if __name__ == "__main__":
    pytest.main()