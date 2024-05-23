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

    def get_rating(self, rating_id: int) -> Rating:
        with Session(self._engine) as session:
            return session.query(Rating).where(Rating.id == rating_id).one()

    def get_person_ratings(self, person_id: int) -> List[Rating]:
        with Session(self._engine) as session:
            return session.query(Rating).where(Rating.person_id == person_id).all()

    def post_rating(self, rating: Rating) -> Rating:
        with Session(self._engine) as session:
            session.add(rating)
            session.commit()
            session.refresh(rating)
            return rating

    def put_rating(self, rating_id: int, rating: Rating) -> Rating:
        with Session(self._engine) as session:
            rating.id = rating_id
            session.merge(rating)
            session.commit()
            return rating

    def delete_rating(self, rating_id: int) -> Rating:
        with Session(self._engine) as session:
            rating = session.query(Rating).where(Rating.id == rating_id).one()
            session.delete(rating)
            session.commit()
            return rating
