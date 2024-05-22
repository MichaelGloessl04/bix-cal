import pytest
from fastapi.testclient import TestClient
from contextlib import asynccontextmanager


@pytest.fixture()
def crud_session_in_memory():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from crud.crud import Crud

    engine = create_engine('sqlite:///:memory:')
    crud = Crud(engine)
    session = sessionmaker(bind=engine)
    populate(session)
    yield crud, session
    engine.dispose()


@pytest.fixture()
def client():
    import os
    from main import app, session

    os.environ['TESTING'] = 'True'

    populate(session)

    with TestClient(app) as client:
        yield client


def populate(session):
    import json
    import os

    from crud import Models

    datasets = []

    with open(os.path.join(os.path.dirname(__file__), 'data\\valid\\people.json'), 'r') as f:
        datasets.append([Models.Person(**person) for person in json.load(f)])

    with open(os.path.join(os.path.dirname(__file__), 'data\\valid\\rating.json'), 'r') as f:
        datasets.append([Models.Rating(**rating) for rating in json.load(f)])

    with open(os.path.join(os.path.dirname(__file__), 'data\\valid\\user.json'), 'r') as f:
        datasets.append([Models.User(**user) for user in json.load(f)])

    with session() as s:
        for dataset in datasets:
            s.add_all(dataset)
            s.commit()
