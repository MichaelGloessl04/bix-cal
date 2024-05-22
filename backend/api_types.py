import pydantic


class PersonNoID(pydantic.BaseModel):
    user_id: int
    name: str
    surname: str
    image_url: str

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class Person(PersonNoID):
    id: int

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class RatingNoID(pydantic.BaseModel):
    person_id: int
    user_id: int
    score: float
    hot: float
    crazy: float
    nice: float
    comment: str

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class Rating(RatingNoID):
    id: int

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class AvgEntry(pydantic.BaseModel):
    score: float
    hot: float
    crazy: float
    nice: float

    model_config = pydantic.ConfigDict(
        from_attributes=True
    )


class UserNoID(pydantic.BaseModel):
    person_id: int
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
