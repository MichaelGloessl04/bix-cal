import pydantic


class PersonNoID(pydantic.BaseModel):
    creator_id: int
    name: str
    surname: str

    class Config:
        orm_mode = True


class Person(PersonNoID):
    id: int

    class Config:
        orm_mode = True


class EntryNoID(pydantic.BaseModel):
    person_id: int
    author_id: int
    hot: float
    crazy: float
    nice: float
    comment: str

    class Config:
        orm_mode = True


class Entry(EntryNoID):
    id: int

    class Config:
        orm_mode = True


class Score(pydantic.BaseModel):
    score: float
    hot: float
    crazy: float
    nice: float

    class Config:
        orm_mode = True


class UserNoID(pydantic.BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class User(UserNoID):
    id: int

    class Config:
        orm_mode = True
