import pydantic


class PersonNoID(pydantic.BaseModel):
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
    hot: float
    crazy: float
    nice: float

    class Config:
        orm_mode = True


class Entry(EntryNoID):
    id: int

    class Config:
        orm_mode = True
