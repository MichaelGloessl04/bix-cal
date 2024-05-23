import os
import json
from crud import Models


def test_get_user(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _user = []
    with open(os.path.join(os.path.dirname(__file__), '..','data\\valid\\users.json'), 'r') as f:
        _user = [Models.User(**data) for data in json.load(f)][0]

    with session() as s:
        user = crud.get_user(1)
        assert isinstance(user, Models.User)
        assert user.id == _user.id
        assert user.username == _user.username
        assert user.password == _user.password
        assert user.email == _user.email
        assert user.image_url == _user.image_url


def test_get_user_person_rating(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _user = []
    with open(os.path.join(os.path.dirname(__file__), '..','data\\valid\\users.json'), 'r') as f:
        _user = [Models.User(**data) for data in json.load(f)][0]

    with session() as s:
        user = crud.get_user_person_rating(1)
        assert isinstance(user, Models.User)
        assert user.id == _user.id
        assert user.username == _user.username
        assert user.password == _user.password
        assert user.email == _user.email
        assert user.image_url == _user.image_url
