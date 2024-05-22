import json
import os

from fastapi.testclient import TestClient

from main import app


def test_get_person(client):
    test_client = TestClient(app)
    _people = []
    
    with open(os.path.join(os.path.dirname(__file__), '..', 'data\\valid\\people.json'), 'r') as f:
        _people = json.load(f)
    
    people = test_client.get('/person/')
    
    assert people.status_code == 200
    assert len(people.json()) == len(_people)
    for person, _person in zip(people.json(), _people):
        assert person['id'] == _person['id']
        assert person['user_id'] == _person['user_id']
        assert person['name'] == _person['name']
        assert person['surname'] == _person['surname']
        assert person['image_url'] == _person['image_url']
