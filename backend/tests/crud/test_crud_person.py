import json
import os

from crud import Models


def test_get_persons(crud_session_in_memory):
    crud, session = crud_session_in_memory

    with session() as s:
        _people = s.query(Models.Person).all()
        s.commit()
        
        people = crud.get_persons()
        for person, _person in zip(people, _people):
            assert isinstance(person, Models.Person)
            assert person.id == _person.id
            assert person.user_id == _person.user_id
            assert person.name == _person.name
            assert person.surname == _person.surname
            assert person.image_url == _person.image_url


def test_get_person(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _person = None
    
    with open(os.path.join(os.path.dirname(__file__), '..\\data\\valid\\people.json'), 'r') as f:
        _people = [Models.Person(**person) for person in json.load(f)]
        _person = _people[0]

    with session() as s:
        s.add(_person)
        s.commit()

        person = crud.get_person(1)
        assert isinstance(person, Models.Person)
        assert person.id == _person.id
        assert person.user_id == _person.user_id
        assert person.name == _person.name
        assert person.surname == _person.surname
        assert person.image_url == _person.image_url
