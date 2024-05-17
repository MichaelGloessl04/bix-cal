import pytest


@pytest.fixture
def crud_session_in_memory():
    from sqlalchemy.orm import sessionmaker
    from crud import Crud, create_engine
    engine = create_engine('sqlite:///:memory:')
    crud = Crud(engine)
    session = sessionmaker(bind=engine)
    yield crud, session
    engine.dispose()
    crud = None
    session = None


@pytest.fixture
def client_resources():
    from ..main import app, resources
    from fastapi.testclient import TestClient
    client = TestClient(app)
    yield client, resources
    client = None
