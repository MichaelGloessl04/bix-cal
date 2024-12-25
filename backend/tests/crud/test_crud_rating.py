from ...crud import Models

from ..data.data import get_ratings


def test_get_rating(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _rating = get_ratings()[0]

    rating = crud.get_rating(1)
    assert isinstance(rating, Models.Rating)
    assert rating.id == _rating.id
    assert rating.person_id == _rating.person_id
    assert rating.user_id == _rating.user_id
    assert rating.score == _rating.score
    assert rating.hot == _rating.hot
    assert rating.crazy == _rating.crazy
    assert rating.nice == _rating.nice
    assert rating.comment == _rating.comment


def test_get_person_ratings(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _ratings = get_ratings()[0:1]

    ratings = crud.get_person_ratings(1)
    for rating, _rating in zip(ratings, _ratings):
        assert isinstance(rating, Models.Rating)
        assert rating.id == _rating.id
        assert rating.person_id == _rating.person_id
        assert rating.user_id == _rating.user_id
        assert rating.score == _rating.score
        assert rating.hot == _rating.hot
        assert rating.crazy == _rating.crazy
        assert rating.nice == _rating.nice
        assert rating.comment == _rating.comment


def get_user_person_rating(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _rating = get_ratings()[0]

    ratings = crud.get_user_person_rating(1, 2)
    for rating, _rating in zip(ratings, _rating):
        assert isinstance(rating, Models.Rating)
        assert rating.id == _rating.id
        assert rating.person_id == _rating.person_id
        assert rating.user_id == _rating.user_id
        assert rating.score == _rating.score
        assert rating.hot == _rating.hot
        assert rating.crazy == _rating.crazy
        assert rating.nice == _rating.nice
        assert rating.comment == _rating.comment


def test_post_rating(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _rating = Models.Rating(
        person_id=4,
        user_id=1,
        score=5,
        hot=5,
        crazy=5,
        nice=5,
        comment='Great person'
    )

    rating = crud.post_rating(_rating)
    assert isinstance(rating, Models.Rating)
    assert rating.id == 4
    assert rating.person_id == _rating.person_id
    assert rating.user_id == _rating.user_id
    assert rating.score == _rating.score
    assert rating.hot == _rating.hot
    assert rating.crazy == _rating.crazy
    assert rating.nice == _rating.nice
    assert rating.comment == _rating.comment


def test_put_rating(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _rating = Models.Rating(
        id=1,
        person_id=2,
        user_id=1,
        score=5,
        hot=5,
        crazy=5,
        nice=5,
        comment='Great person'
    )

    rating = crud.put_rating(1, _rating)
    assert isinstance(rating, Models.Rating)
    assert rating.id == 1
    assert rating.person_id == _rating.person_id
    assert rating.user_id == _rating.user_id
    assert rating.score == _rating.score
    assert rating.hot == _rating.hot
    assert rating.crazy == _rating.crazy
    assert rating.nice == _rating.nice
    assert rating.comment == _rating.comment

def test_delete_rating(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _ratings = get_ratings()

    rating = crud.delete_rating(1)
    assert isinstance(rating, Models.Rating)
    assert rating.id == _ratings[0].id
    assert rating.person_id == _ratings[0].person_id
    assert rating.user_id == _ratings[0].user_id
    assert rating.score == _ratings[0].score
    assert rating.hot == _ratings[0].hot
    assert rating.crazy == _ratings[0].crazy
    assert rating.nice == _ratings[0].nice
    assert rating.comment == _ratings[0].comment
    assert rating not in _ratings[1:]
