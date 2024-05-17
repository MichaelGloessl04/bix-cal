import pydantic


class PersonNoID(pydantic.BaseModel):
    creator_id: int
    name: str
    surname: str

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class Person(PersonNoID):
    id: int

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class EntryNoID(pydantic.BaseModel):
    person_id: int
    author_id: int
    hot: float
    crazy: float
    nice: float
    comment: str

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class Entry(EntryNoID):
    id: int

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class Score(pydantic.BaseModel):
    score: float
    hot: float
    crazy: float
    nice: float

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class UserNoID(pydantic.BaseModel):
    username: str
    email: str

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class User(UserNoID):
    id: int

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )
