import os
import json
from crud import Models


def test_get_rating(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _rating = []
    with open(os.path.join(os.path.dirname(__file__), '..','data\\valid\\ratings.json'), 'r') as f:
        _rating = [Models.Rating(**data) for data in json.load(f)][0]

    with session() as s:
        rating = crud.get_rating(1)
        assert isinstance(rating, Models.Rating)
        assert rating.id == _rating.id
        assert rating.person_id == _rating.person_id
        assert rating.rating == _rating.rating
        assert rating.comment == _rating.comment


def test_get_person_ratings(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _ratings = []
    with open(os.path.join(os.path.dirname(__file__), '..','data\\valid\\ratings.json'), 'r') as f:
        _ratings = [Models.Rating(**data) for data in json.load(f)][0:1]

    with session() as s:
        ratings = crud.get_person_ratings(1)
        for rating, _rating in zip(ratings, _ratings):
            assert isinstance(rating, Models.Rating)
            assert rating.id == _rating.id
            assert rating.person_id == _rating.person_id
            assert rating.rating == _rating.rating
            assert rating.comment == _rating.comment


def test_post_rating(crud_session_in_memory):
    crud, session = crud_session_in_memory

    _rating = Models.Rating(
        person_id=1,
        user_id=1,
        score=5.
        comment='Great!'
    )

    with session() as s:
        rating = crud.post_rating(_rating)
        assert isinstance(rating, Models.Rating)
        assert rating.id == _rating.id
        assert rating.person_id == _rating.person_id
        assert rating.rating == _rating.rating
        assert rating.comment == _rating.comment
        
