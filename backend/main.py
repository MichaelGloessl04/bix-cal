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
    try:
        if search_term:
            return resources['crud'].search(
                Models.Person,
                ['name', 'surname'],
                search_term
            )
        else:
            return resources['crud'].get(
                Models.Person
            )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


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


@app.get('/person/{person_id}/score', response_model=ApiTypes.Score)
async def get_person_score(
        person_id: int):
    scores = {}
    categories = ['hot', 'crazy', 'nice']

    entries = resources['crud'].search(
        Models.Entry,
        ['person_id'],
        str(person_id)
    )

    if not entries:
        raise HTTPException(status_code=404, detail='No entries found')

    for category in categories:
        scores[category] = sum(
            [getattr(entry, category) for entry in entries]
        ) / len(entries)

    scores['score'] = sum(
        [entry.hot + entry.nice + (4 - entry.crazy) for entry in entries]
    ) / len(entries)

    return scores


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


@app.get('/user/', response_model=List[ApiTypes.User])
async def get_users(username: str, password: str):
    _validate_user(username, password)
    return resources['crud'].search(
        Models.User,
        ['username'],
        [username]
    )


@app.get('/user/{entries}', response_model=List[ApiTypes.Entry])
async def get_user_entries(username: str, password: str):
    _validate_user(username, password)
    user = resources['crud'].search(
        Models.User,
        ['username'],
        [username]
    )
    return resources['crud'].search(
        Models.Entry,
        ['author_id'],
        str(user.id)
    )


@app.post('/user/', response_model=ApiTypes.User)
async def create_user(user: ApiTypes.UserNoID):
    return resources['crud'].create(
        Models.User,
        user.model_dump()
    )


@app.put('/user/{user_id}', response_model=ApiTypes.User)
async def update_user(username: str, password: str, new_user: ApiTypes.UserNoID):
    _validate_user(username, password)
    user = resources['crud'].search(
        Models.User,
        ['username'],
        [username]
    )
    return resources['crud'].update(
        Models.User,
        user.id,
        new_user.model_dump()
    )


def _validate_user(username, password):
    user = resources['crud'].search(
        Models.User,
        ['username'],
        [username]
    )
    if not user:
        raise HTTPException(status_code=404, detail='No users found')
    if password != user.password:
        raise HTTPException(status_code=401, detail='Invalid password')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=5001, reload=True)
