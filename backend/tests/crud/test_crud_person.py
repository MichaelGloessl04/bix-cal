from ...crud import Models

from ..data.data import get_people


def test_get_persons(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _people = get_people()[0:1]

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

    _person = get_people()[0]

    person = crud.get_person(1)
    assert isinstance(person, Models.Person)
    assert person.id == _person.id
    assert person.user_id == _person.user_id
    assert person.name == _person.name
    assert person.surname == _person.surname
    assert person.image_url == _person.image_url


def test_search_person(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _people = get_people()[0:1]

    people = crud.search_person('Doe')
    for person, _person in zip(people, _people):
        assert isinstance(person, Models.Person)
        assert person.id == _person.id
        assert person.user_id == _person.user_id
        assert person.name == _person.name
        assert person.surname == _person.surname
        assert person.image_url == _person.image_url


def test_post_person(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _person = Models.Person(
        user_id=1,
        name='Simon',
        surname='Posch',
        image_url='https://example.com/image.jpg'
    )

    person = crud.post_person(_person)
    assert isinstance(person, Models.Person)
    assert person.id == 5
    assert person.user_id == _person.user_id
    assert person.name == _person.name
    assert person.surname == _person.surname
    assert person.image_url == _person.image_url


def test_delete_person(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _people = get_people()

    person = crud.delete_person(1)
    assert isinstance(person, Models.Person)
    assert person.id == 1
    assert person.user_id == _people[0].user_id
    assert person.name == _people[0].name
    assert person.surname == _people[0].surname
    assert person.image_url == _people[0].image_url
    assert person not in _people[1:]
