from crud import Models

from ..data.data import get_users


def test_get_user(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _users = get_users()[0]

    user = crud.get_user(1)
    assert isinstance(user, Models.User)
    assert user.id == _users.id
    assert user.person_id == _users.person_id
    assert user.username == _users.username
    assert user.email == _users.email


def test_get_user_by_email(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _users = get_users()[1]

    user = crud.get_user_by_email('jsmith@example.com')
    assert isinstance(user, Models.User)
    assert user.id == _users.id
    assert user.person_id == _users.person_id
    assert user.username == _users.username
    assert user.email == _users.email


def test_post_user(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _user = Models.User(
        person_id=None,
        username='j.smith',
        email='jsmith@example.at'
    )

    user = crud.post_user(_user)
    assert isinstance(user, Models.User)
    assert user.id == 3
    assert user.person_id == _user.person_id
    assert user.username == _user.username
    assert user.email == _user.email
