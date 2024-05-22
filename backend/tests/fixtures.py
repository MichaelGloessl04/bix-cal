import pytest


@pytest.fixture()
def crud_session_in_memory():
    from sqlalchemy.orm import sessionmaker

    from crud import Crud, create_engine

    engine = create_engine('sqlite:///:memory:')
    crud = Crud(engine)
    session = sessionmaker(bind=engine)
    populate(session)
    yield crud, session
    engine.dispose()


@pytest.fixture()
def client():
    import os
    from fastapi.testclient import TestClient
    
    from main import app

    os.environ['TESTING'] = 'True'
    yield TestClient(app)


def populate(session):
    import json
    import os

    from crud import Models

    datasets = []
    paths = [
        ('data\\valid\\people.json', Models.Person),
        ('data\\valid\\ratings.json', Models.Rating),
        ('data\\valid\\users.json', Models.User),
    ]

    for path, model in paths:
        with open(os.path.join(os.path.dirname(__file__), path), 'r') as f:
            datasets.append([model(**data) for data in json.load(f)])

    with session() as s:
        for dataset in datasets:
            s.add_all(dataset)
            s.commit()
