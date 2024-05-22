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

    def search_person(self, search_term: str) -> List[Person]:
        with Session(self._engine) as session:
            return session.query(Person).filter(
                or_(
                    Person.name.like(f'%{search_term}%'),
                    Person.surname.like(f'%{search_term}%')
                )
            ).all()

    def post_person(self, person: Person) -> Person:
        with Session(self._engine) as session:
            session.add(person)
            session.commit()
            session.refresh(person)
            return person

    def delete_person(self, person_id: int) -> Person:
        with Session(self._engine) as session:
            person = session.query(Person).where(Person.id == person_id).one()
            session.delete(person)
            session.commit()
            return person
