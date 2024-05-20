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
    allow_origins=['http://localhost:5000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', response_model=str)
async def root():
    with open('./assets/about.md', 'r') as f:
        return f.read()


@app.get('/person/', response_model=List[ApiTypes.Person])
async def get_persons(search_term: str = None):
    crud: Crud = resources['crud']
    try:
        if search_term:
            return crud.search(Models.Person, ['name', 'surname'], search_term)
        else:
            return crud.get(Models.Person)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/person/{person_id}', response_model=ApiTypes.Person)
async def get_person(person_id: int):
    crud: Crud = resources['crud']
    return crud.get_single(Models.Person, person_id)


@app.get('/person/{person_id}/entries', response_model=List[ApiTypes.Entry])
async def get_person_entries(person_id: int):
    crud: Crud = resources['crud']
    return crud.search(Models.Entry, ['person_id'], str(person_id))


@app.get('/person/{person_id}/scores', response_model=ApiTypes.Score)
async def get_person_score(person_id: int):
    crud: Crud = resources['crud']
    scores = {}
    categories = ['hot', 'crazy', 'nice']

    entries = crud.search(Models.Entry, ['person_id'], str(person_id))

    if not entries:
        raise HTTPException(status_code=404, detail='Person has no entries')

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
    crud: Crud = resources['crud']
    return crud.create(Models.Person, person.model_dump())


@app.put('/person/{person_id}', response_model=ApiTypes.Person)
async def update_person(person_id: int, person: ApiTypes.PersonNoID):
    crud: Crud = resources['crud']
    return crud.update(Models.Person, person_id, person.model_dump())


@app.delete('/person/{person_id}')
async def delete_person(person_id: int):
    crud: Crud = resources['crud']
    return crud.delete(Models.Person, person_id)


@app.get('/entry/', response_model=List[ApiTypes.Entry])
async def get_entries():
    crud: Crud = resources['crud']
    return crud.get(Models.Entry)


@app.get('/entry/{entry_id}', response_model=ApiTypes.Entry)
async def get_entry(entry_id: int):
    crud: Crud = resources['crud']
    return crud.get_single(Models.Entry, entry_id)


@app.post('/entry/', response_model=ApiTypes.Entry)
async def create_entry(entry: ApiTypes.EntryNoID):
    crud: Crud = resources['crud']
    return crud.create(Models.Entry, entry.model_dump())


@app.put('/entry/{entry_id}', response_model=ApiTypes.Entry)
async def update_entry(entry_id: int, entry: ApiTypes.EntryNoID):
    crud: Crud = resources['crud']
    return crud.update_or_create(Models.Entry, entry_id, entry.model_dump())


@app.delete('/entry/{entry_id}')
async def delete_entry(entry_id: int):
    crud: Crud = resources['crud']
    return crud.delete(Models.Entry, entry_id)


@app.get('/user/id/{user_id}', response_model=ApiTypes.User)
async def get_user(user_id: int):
    crud: Crud = resources['crud']
    return crud.get_single(Models.User, user_id)


@app.get('/user/id/{user_id}/entries', response_model=List[ApiTypes.Entry])
async def get_user_entries(user_id: int):
    crud: Crud = resources['crud']
    return crud.search(Models.Entry, ['author_id'], str(user_id))


@app.get('/user/id/{user_id}/entries/{person_id}', response_model=ApiTypes.Entry)
async def get_user_entries(user_id: int, person_id: int):
    crud: Crud = resources['crud']
    entries = crud.search(Models.Entry, ['author_id'], str(user_id))
    if person_id in [entry.person_id for entry in entries]:
        return [entry for entry in entries if entry.person_id == person_id][0]
    else:
        return None

@app.get('/user/{email}', response_model=ApiTypes.User)
async def get_user(email: str):
    crud: Crud = resources['crud']
    user = crud.get_where(Models.User, 'email', email)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user[0]


@app.post('/user/', response_model=ApiTypes.User)
async def create_user(user: ApiTypes.UserNoID):
    crud: Crud = resources['crud']
    if crud.search(Models.User, ['email'], user.email):
        raise HTTPException(status_code=409, detail='User already exists')
    return crud.create(Models.User, user.model_dump())


@app.delete('/user/{email}')
async def delete_user(email: str):
    crud: Crud = resources['crud']
    user = crud.get_where(Models.User, 'email', email)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return crud.delete(Models.User, user[0].id)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=5001, reload=True)
