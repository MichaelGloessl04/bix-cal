import os
import logging

from typing import List
from sqlalchemy import or_
from sqlalchemy.orm import Session

from crud.models import Base, Person, Rating, User

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    encoding='utf-8',
    filename=os.path.join(os.path.dirname(__file__), '..', '..', 'logs', 'crud.log'),
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


class Crud:
    def __init__(self, engine):
        self._engine = engine
        Base.metadata.create_all(self._engine)

    def get_persons(self) -> List[Person]:
        with Session(self._engine) as session:
            try:
                return session.query(Person).all()
            except Exception as e:
                logger.error(e)
                return []

    def get_person(self, person_id: int) -> Person:
        with Session(self._engine) as session:
            try:
                return session.query(Person).where(Person.id == person_id).one()
            except Exception as e:
                logger.error(e)
                return None

    def search_person(self, search_term: str) -> List[Person]:
        with Session(self._engine) as session:
            try:
                return session.query(Person).filter(
                    or_(
                        Person.name.like(f'%{search_term}%'),
                        Person.surname.like(f'%{search_term}%')
                    )
                ).all()
            except Exception as e:
                logger.error(e)
                return []

    def post_person(self, data: dict) -> Person:
        with Session(self._engine) as session:
            try:
                person = Person(**data)
                session.add(person)
                session.commit()
                session.refresh(person)
                return person
            except Exception as e:
                logger.error(e)
                return None

    def delete_person(self, person_id: int) -> Person:
        with Session(self._engine) as session:
            try:
                person = session.query(Person).where(Person.id == person_id).one()
                session.delete(person)
                session.commit()
                return person
            except Exception as e:
                logger.error(e)
                return None

    def get_rating(self, rating_id: int) -> Rating:
        with Session(self._engine) as session:
            try:
                return session.query(Rating).where(Rating.id == rating_id).one()
            except Exception as e:
                logger.error(e)
                return None

    def get_person_ratings(self, person_id: int) -> List[Rating]:
        with Session(self._engine) as session:
            try:
                return session.query(Rating).where(Rating.person_id == person_id).all()
            except Exception as e:
                logger.error(e)
                return []

    def get_user_person_rating(self, user_id: int, person_id: int) -> Rating:
        with Session(self._engine) as session:
            try:
                return session.query(Rating).where(
                    Rating.user_id == user_id,
                    Rating.person_id == person_id
                ).one()
            except Exception as e:
                logger.error(e)
                return None

    def post_rating(self, data: dict) -> Rating:
        with Session(self._engine) as session:
            try:
                rating = Rating(**data)
                session.add(rating)
                session.commit()
                session.refresh(rating)
                return rating
            except Exception as e:
                logger.error(e)
                return None

    def put_rating(self, rating_id: int, data: dict) -> Rating:
        with Session(self._engine) as session:
            try:
                rating = Rating(**data)
                rating.id = rating_id
                session.merge(rating)
                session.commit()
                return rating
            except Exception as e:
                logger.error(e)
                return None

    def delete_rating(self, rating_id: int) -> Rating:
        with Session(self._engine) as session:
            try:
                rating = session.query(Rating).where(Rating.id == rating_id).one()
                session.delete(rating)
                session.commit()
                return rating
            except Exception as e:
                logger.error(e)
                return None

    def get_user(self, user_id: int) -> User:
        with Session(self._engine) as session:
            try:
                return session.query(User).where(User.id == user_id).one()
            except Exception as e:
                logger.error(e)
                return None

    def get_user_by_email(self, email: str) -> User:
        with Session(self._engine) as session:
            try:
                return session.query(User).where(User.email == email).one()
            except Exception as e:
                logger.error(e)
                return None

    def post_user(self, data: dict) -> User:
        with Session(self._engine) as session:
            try:
                user = User(**data)
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
            except Exception as e:
                logger.error(e)
                return None

    def put_user(self, user_id: int, data: dict) -> User:
        with Session(self._engine) as session:
            try:
                user = User(**data)
                user.id = user_id
                session.merge(user)
                session.commit()
                return user
            except Exception as e:
                logger.error(e)
                return None
