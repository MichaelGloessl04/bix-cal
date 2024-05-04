from typing import List
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from . import api_types as ApiTypes
from crud import Crud, Models, create_engine

resources = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """start the character device reader"""
    print('lifespan started')
    engine = create_engine('sqlite:///database.db')
    resources['crud'] = Crud(engine)
    yield
    engine.dispose()
    resources.clear()
    print('lifespan finished')


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/person', response_model=List[ApiTypes.Person])
async def get_persons():
    return resources['crud'].get(Models.Person)


@app.get('/person/{person_id}', response_model=ApiTypes.Person)
async def get_person(person_id: int):
    return resources['crud'].get_single(Models.Person, person_id)


@app.get('/person/{person_id}/entries', response_model=List[ApiTypes.Entry])
async def get_person_entries(person_id: int):
    return resources['crud'].search(Models.Entry, ['person_id'], str(person_id))


@app.post('/person', response_model=ApiTypes.Person)
async def create_person(person: ApiTypes.Person):
    return resources['crud'].create(Models.Person, person.dict())
