from typing import List
from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from crud import Crud, Models, create_engine

import api_types as ApiTypes

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


@app.get('/person/', response_model=List[ApiTypes.Person])
async def get_persons(search_term: str = None):
    if search_term:
        return resources['crud'].search(
            Models.Person,
            ['name', 'email'],
            search_term
        )
    return resources['crud'].get(
        Models.Person
    )


@app.get('/person/{person_id}', response_model=ApiTypes.Person)
async def get_person(person_id: int):
    return resources['crud'].get_single(
        Models.Person,
        person_id
    )


@app.get('/person/{person_id}/entries', response_model=List[ApiTypes.Entry])
async def get_person_entries(person_id: int):
    return resources['crud'].search(
        Models.Entry,
        ['person_id'],
        str(person_id)
    )


@app.get('/person/{person_id}/score', response_model=float)
async def get_person_score(person_id: int):
    entries = resources['crud'].search(
        Models.Entry,
        ['person_id'],
        str(person_id)
    )
    if not entries:
        raise HTTPException(status_code=404, detail='No entries found')
    return sum(
        [entry.hot + entry.nice + (4 - entry.crazy) for entry in entries]
    ) / len(entries)


@app.post('/person/', response_model=ApiTypes.Person)
async def create_person(person: ApiTypes.PersonNoID):
    return resources['crud'].create(
        Models.Person,
        person.model_dump()
    )


@app.put('/person/{person_id}', response_model=ApiTypes.Person)
async def update_person(person_id: int, person: ApiTypes.PersonNoID):
    return resources['crud'].update(
        Models.Person,
        person_id,
        person.model_dump()
    )


@app.get('/entry/', response_model=List[ApiTypes.Entry])
async def get_entries():
    return resources['crud'].get(
        Models.Entry
    )


@app.get('/entry/{entry_id}', response_model=ApiTypes.Entry)
async def get_entry(entry_id: int):
    return resources['crud'].get_single(
        Models.Entry,
        entry_id
    )


@app.post('/entry/', response_model=ApiTypes.Entry)
async def create_entry(entry: ApiTypes.EntryNoID):
    return resources['crud'].create(
        Models.Entry,
        entry.model_dump()
    )


@app.put('/entry/{entry_id}', response_model=ApiTypes.Entry)
async def update_entry(entry_id: int, entry: ApiTypes.EntryNoID):
    return resources['crud'].update(
        Models.Entry,
        entry_id,
        entry.model_dump()
    )


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=5001, reload=True)
