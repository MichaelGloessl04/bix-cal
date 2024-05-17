import os
import pytest


def test_root(client_resources):
    expected = ''
    path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'about.md')
    
    client, _ = client_resources
    
    with open(path) as f:
        expected = f.read()

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == expected


if __name__ == "__main__":
    pytest.main()
