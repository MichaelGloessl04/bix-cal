from typing import List
from sqlalchemy import or_
from sqlalchemy.orm import Session

from crud.models import Base, Person, Rating, User


class Crud:
    def __init__(self, engine):
        self._engine = engine
        Base.metadata.create_all(self._engine)

    def get_persons(self) -> List[Person]:
        with Session(self._engine) as session:
            return session.query(Person).all()

    def get_person(self, person_id: int) -> Person:
        with Session(self._engine) as session:
            return session.query(Person).where(Person.id == person_id).one()
