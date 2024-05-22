import os

from typing import List
from fastapi import FastAPI, HTTPException

from sqlalchemy.orm import sessionmaker

from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from crud import Crud, create_engine

import api_types as ApiTypes

from tests.fixtures import populate

resources = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """start the character device reader"""
    print('lifespan started')
    if os.getenv('TESTING'):
        print('testing')
        engine = create_engine('sqlite:///:memory:')
        crud = Crud(engine)
        session = sessionmaker(bind=engine)
        populate(session)
    else:
        engine = create_engine('sqlite:///database.db')
        crud = Crud(engine)
        session = sessionmaker(bind=engine)
    resources['crud'] = crud
    resources['session'] = session
    resources['engine'] = engine
    yield engine
    engine.dispose()
    resources.clear()
    print('lifespan finished')


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', response_model=str)
async def root():
    return 'Hello World'


@app.get('/about', response_model=str)
async def about():
    with open('./assets/about.md', 'r') as f:
        return f.read()


@app.get('/person/', response_model=List[ApiTypes.Person], tags=['person'])
def get_person(search_term: str = None):
    crud: Crud = resources['crud']
    if search_term:
        return crud.search_person(search_term)
    else:
        return crud.get_persons()


@app.get('/person/{person_id}', response_model=ApiTypes.Person, tags=['person'])
def get_person(person_id: int):
    crud: Crud = resources['crud']
    return crud.get_person(person_id)


@app.post('/person/', response_model=ApiTypes.Person, tags=['person'])
def post_person(person: ApiTypes.PersonNoID):
    crud: Crud = resources['crud']
    crud.post_person(person)
    return crud.get_person(person.id)


@app.delete('/person/{person_id}', response_model=ApiTypes.Person, tags=['person'])
def delete_person(person_id: int):
    crud: Crud = resources['crud']
    return crud.delete_person(person_id)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=5001, reload=True)
