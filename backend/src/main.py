import os
import logging
import math

from types import NoneType
from typing import List, Union
from fastapi import FastAPI

from sqlalchemy.orm import sessionmaker

from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from crud import Crud, create_engine

import api_types as ApiTypes

from tests.fixtures import populate

resources = {}

# Ensure the log directory exists
log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

# Set up the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(os.path.join(log_dir, 'api.log'), encoding='utf-8')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """start the character device reader"""
    logger.debug('lifespan started')
    if os.getenv('TESTING'):
        logger.debug('Testing mode')
        engine = create_engine('sqlite:///:memory:')
        crud = Crud(engine)
        populate(sessionmaker(bind=engine))
    else:
        engine = create_engine('sqlite:///database.db')
        crud = Crud(engine)
    resources['crud'] = crud
    yield
    engine.dispose()
    resources.clear()
    logger.debug('lifespan ended')


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', response_model=str)
async def root() -> str:
    """The root endpoint of the API

    Returns:
        str: A simple 'Hello World' message
    """
    return 'Hello World'


@app.get('/about', response_model=str)
async def about() -> str:
    """The about section of the Website

    Returns:
        str: The content of the about section
    """
    with open(os.path.join(os.path.dirname(__file__), 'assets', 'about.md'), 'r') as f:
        return f.read()


@app.get('/person/', response_model=List[ApiTypes.Person], tags=['person'])
def get_persons(search_term: str = None, sort_column: str = None, order: str = None) -> List[ApiTypes.Person]:
    """Get all people in the database

    Args:
        search_term (str, optional): A search term to filter the results. Defaults to None.

    Returns:
        List[ApiTypes.Person]: A list of all people in the database
    """
    crud: Crud = resources['crud']
    if search_term:
        return crud.search_person(search_term, sort_column, order)
    else:
        return crud.get_persons(sort_column, order)


@app.get('/person/{person_id}', response_model=ApiTypes.Person, tags=['person'])
def get_person(person_id: int) -> ApiTypes.Person:
    """Get a person by their ID

    Args:
        person_id (int): A person's ID

    Returns:
        ApiTypes.Person: The person with the given ID
    """
    crud: Crud = resources['crud']
    return crud.get_person(person_id)


@app.post('/person/', response_model=ApiTypes.Person, tags=['person'])
def post_person(person: ApiTypes.PersonNoID) -> ApiTypes.Person:
    """Create a new person

    Args:
        person (ApiTypes.PersonNoID): The new person to create

    Returns:
        ApiTypes.Person: The created person
    """
    crud: Crud = resources['crud']
    return crud.post_person(person.model_dump())


@app.delete('/person/{person_id}', response_model=ApiTypes.Person, tags=['person'])
def delete_person(person_id: int) -> ApiTypes.Person:
    """Delete a person by their ID

    Args:
        person_id (int): The ID of the person to delete

    Returns:
        ApiTypes.Person: The deleted person
    """
    crud: Crud = resources['crud']
    return crud.delete_person(person_id)


@app.get('/rating/{person_id}', response_model=Union[List[ApiTypes.Rating], NoneType], tags=['rating'])
def get_rating(person_id: int) -> ApiTypes.Rating:
    """Get a rating by its ID

    Args:
        rating_id (int): The ID of the rating

    Returns:
        ApiTypes.Rating: The rating with the given ID
    """
    crud: Crud = resources['crud']
    return crud.get_person_ratings(person_id)


@app.get('/rating/person/{person_id}', response_model=List[ApiTypes.Rating], tags=['rating'])
def get_person_ratings(person_id: int) -> List[ApiTypes.Rating]:
    """Get all ratings for a person

    Args:
        person_id (int): The ID of the person

    Returns:
        List[ApiTypes.Rating]: A list of ratings for the person with the given ID
    """
    crud: Crud = resources['crud']
    return crud.get_person_ratings(person_id)


@app.get('/rating/average/{person_id}', response_model=ApiTypes.AvgRating, tags=['rating'])
def get_person_average(person_id: int) -> ApiTypes.AvgRating:
    """Get the average rating for a person

    Args:
        person_id (int): The ID of the person

    Returns:
        ApiTypes.AvgRating: The average rating for the person with the given ID
    """
    crud: Crud = resources['crud']
    ratings = crud.get_person_ratings(person_id)
    if not ratings:
        return ApiTypes.AvgRating(score=0, hot=0, crazy=0, nice=0)
    else:
        return ApiTypes.AvgRating(
            score=sum([rating.score for rating in ratings]) / len(ratings),
            hot=sum([rating.hot for rating in ratings]) / len(ratings),
            crazy=sum([rating.crazy for rating in ratings]) / len(ratings),
            nice=sum([rating.nice for rating in ratings]) / len(ratings),
        )


def calculate_score(rating: ApiTypes.RatingNoID) -> ApiTypes.Rating:
    score = rating.hot + rating.nice - abs(rating.crazy - 4)
    
    mapped_score = 1 + 9 * (score + 4) / 24
    rating.score = mapped_score
    return rating


@app.post('/rating/', response_model=ApiTypes.Rating, tags=['rating'])
def post_rating(rating: ApiTypes.RatingNoID) -> ApiTypes.Rating:
    """Create a new rating

    Args:
        rating (ApiTypes.RatingNoID): The new rating to create

    Returns:
        ApiTypes.Rating: The created rating
    """
    crud: Crud = resources['crud']
    rating = calculate_score(rating)
    return crud.post_rating(rating.model_dump())


@app.put('/rating/{rating_id}', response_model=ApiTypes.Rating, tags=['rating'])
def put_rating(rating_id: int, rating: ApiTypes.RatingNoID) -> ApiTypes.Rating:
    """Update a rating by its ID

    Args:
        rating_id (int): The ID of the rating to update
        rating (ApiTypes.RatingNoID): The new rating data

    Returns:
        ApiTypes.Rating: The updated rating
    """
    crud: Crud = resources['crud']
    rating = calculate_score(rating)
    return crud.put_rating(rating_id, rating.model_dump())


@app.delete('/rating/{rating_id}', response_model=ApiTypes.Rating, tags=['rating'])
def delete_rating(rating_id: int) -> ApiTypes.Rating:
    """Delete a rating by its ID

    Args:
        rating_id (int): The ID of the rating to delete

    Returns:
        ApiTypes.Rating: The deleted rating
    """
    crud: Crud = resources['crud']
    return crud.delete_rating(rating_id)


@app.get('/user/{user_id}', response_model=ApiTypes.User, tags=['user'])
def get_user(user_id: int) -> ApiTypes.User:
    """Get a user by their ID

    Args:
        user_id (int): The ID of the user

    Returns:
        ApiTypes.User: The user with the given ID
    """
    crud: Crud = resources['crud']
    return crud.get_user(user_id)


@app.get('/user/email/{email}', response_model=ApiTypes.User, tags=['user'])
def get_user_by_email(email: str) -> ApiTypes.User:
    """Get a user by their email

    Args:
        email (str): The email of the user

    Returns:
        ApiTypes.User: The user with the given email
    """
    crud: Crud = resources['crud']
    return crud.get_user_by_email(email)


@app.get('/user/rating/{user_id}/{person_id}', response_model=Union[ApiTypes.Rating, NoneType], tags=['user'])
def get_user_person_rating(user_id: int, person_id: int) -> ApiTypes.Rating:
    """Get a user's rating for a person

    Args:
        user_id (int): The ID of the user
        person_id (int): The ID of the person

    Returns:
        ApiTypes.Rating: The user's rating for the person
    """
    crud: Crud = resources['crud']
    return crud.get_user_person_rating(user_id, person_id)


@app.post('/user/', response_model=ApiTypes.User, tags=['user'])
def post_user(user: ApiTypes.UserNoID) -> ApiTypes.User:
    """Create a new user

    Args:
        user (ApiTypes.UserNoID): The new user to create

    Returns:
        ApiTypes.User: The created user
    """
    crud: Crud = resources['crud']
    return crud.post_user(user.model_dump())


@app.put('/user/define-person/{user_id}/{person_id}', response_model=ApiTypes.User, tags=['user'])
def define_person(user_id: int, person_id: int) -> ApiTypes.User:
    """Define a person for a user

    Args:
        user_id (int): The ID of the user
        person_id (int): The ID of the person

    Returns:
        ApiTypes.User: The updated user
    """
    crud: Crud = resources['crud']
    user = crud.get_user(user_id)
    user.person_id = person_id
    api_user = ApiTypes.User(
        id=user.id,
        person_id=user.person_id,
        username=user.username,
        email=user.email
    )
    return crud.put_user(user_id, api_user.model_dump())


@app.delete('/user/{user_id}', response_model=ApiTypes.User, tags=['user'])
def delete_user(user_id: int) -> ApiTypes.User:
    """Delete a user by their ID

    Args:
        user_id (int): The ID of the user to delete

    Returns:
        ApiTypes.User: The deleted user
    """
    crud: Crud = resources['crud']
    return crud.delete_user(user_id)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=5001, reload=True)
