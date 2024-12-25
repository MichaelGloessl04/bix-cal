import os
import logging

from typing import List
from sqlalchemy import or_
from sqlalchemy.orm import Session

from ..crud.models import Base, Person, Rating, User

log_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(os.path.join(log_dir, 'crud.log'), encoding='utf-8')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class Crud:
    def __init__(self, engine):
        self._engine = engine
        self._logger = logger
        Base.metadata.create_all(self._engine)
        self._logger.debug('Crud initialized')

    def get_persons(self, sort_column: str = None, order: str = None) -> List[Person]:
        self._logger.debug('Getting all persons')
        with Session(self._engine) as session:
            try:
                if sort_column and order:
                    return session.query(Person).order_by(f'{sort_column} {order}').all()
                else:
                    return session.query(Person).all()
            except Exception as e:
                self._logger.warning(e)
                return []

    def get_person(self, person_id: int) -> Person:
        self._logger.debug(f'Getting person with ID {person_id}')
        with Session(self._engine) as session:
            try:
                return session.query(Person).where(Person.id == person_id).one()
            except Exception as e:
                self._logger.warning(f'Person with ID {person_id} not found')
                return None

    def search_person(self, search_term: str, sort_column: str = None, order: str = None) -> List[Person]:
        self._logger.debug(f'Searching for persons with term: {search_term}')
        with Session(self._engine) as session:
            try:
                if sort_column and order:
                    return session.query(Person).filter(
                        or_(
                            Person.name.like(f'%{search_term}%'),
                            Person.surname.like(f'%{search_term}%')
                        )
                    ).order_by(f'{sort_column} {order}').all()
                else:
                    return session.query(Person).filter(
                        or_(
                            Person.name.like(f'%{search_term}%'),
                            Person.surname.like(f'%{search_term}%')
                        )
                    ).all()
            except Exception as e:
                self._logger.warning(e)
                return []

    def post_person(self, data: dict) -> Person:
        self._logger.debug(f'Creating person with data: {data}')
        with Session(self._engine) as session:
            try:
                person = Person(**data)
                session.add(person)
                session.commit()
                session.refresh(person)
                return person
            except Exception as e:
                self._logger.warning(e)
                return None

    def delete_person(self, person_id: int) -> Person:
        self._logger.debug(f'Deleting person with ID {person_id}')
        with Session(self._engine) as session:
            try:
                person = session.query(Person).where(Person.id == person_id).one()
                session.delete(person)
                session.commit()
                return person
            except Exception as e:
                self._logger.warning(f'Person with ID {person_id} not found')
                return None

    def get_rating(self, rating_id: int) -> Rating:
        self._logger.debug(f'Getting rating with ID {rating_id}')
        with Session(self._engine) as session:
            try:
                return session.query(Rating).where(Rating.id == rating_id).one()
            except Exception as e:
                self._logger.warning(f'Rating with ID {rating_id} not found')
                return None

    def get_person_ratings(self, person_id: int) -> List[Rating]:
        self._logger.debug(f'Getting ratings for person with ID {person_id}')
        with Session(self._engine) as session:
            try:
                return session.query(Rating).where(Rating.person_id == person_id).all()
            except Exception as e:
                self._logger.warning(e)
                return []

    def get_user_person_rating(self, user_id: int, person_id: int) -> Rating:
        self._logger.debug(f'Getting rating for user with ID {user_id} and person with ID {person_id}')
        with Session(self._engine) as session:
            try:
                return session.query(Rating).where(
                    Rating.user_id == user_id,
                    Rating.person_id == person_id
                ).one()
            except Exception as e:
                self._logger.warning(e)
                return None

    def post_rating(self, data: dict) -> Rating:
        self._logger.debug(f'Creating rating with data: {data}')
        with Session(self._engine) as session:
            try:
                rating = Rating(**data)
                session.add(rating)
                session.commit()
                session.refresh(rating)
                return rating
            except Exception as e:
                self._logger.warning(e)
                return None

    def put_rating(self, rating_id: int, data: dict) -> Rating:
        self._logger.debug(f'Updating rating with ID {rating_id} with data: {data}')
        with Session(self._engine) as session:
            try:
                rating = Rating(**data)
                rating.id = rating_id
                session.merge(rating)
                session.commit()
                return rating
            except Exception as e:
                self._logger.warning(f'Rating with ID {rating_id} not found')
                return None

    def delete_rating(self, rating_id: int) -> Rating:
        self._logger.debug(f'Deleting rating with ID {rating_id}')
        with Session(self._engine) as session:
            try:
                rating = session.query(Rating).where(Rating.id == rating_id).one()
                session.delete(rating)
                session.commit()
                return rating
            except Exception as e:
                self._logger.warning(f'Rating with ID {rating_id} not found')
                return None

    def get_user(self, user_id: int) -> User:
        self._logger.debug(f'Getting user with ID {user_id}')
        with Session(self._engine) as session:
            try:
                return session.query(User).where(User.id == user_id).one()
            except Exception as e:
                self._logger.warning(f'User with ID {user_id} not found')
                return None

    def get_user_by_email(self, email: str) -> User:
        self._logger.debug(f'Getting user by email: {email}')
        with Session(self._engine) as session:
            try:
                self._logger.debug(f'Getting user by email: {email}')
                return session.query(User).where(User.email == email).one()
            except Exception as e:
                self._logger.warning(f'User with email {email} not found')
                return None

    def post_user(self, data: dict) -> User:
        self._logger.debug(f'Creating user with data: {data}')
        with Session(self._engine) as session:
            try:
                user = User(**data)
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
            except Exception as e:
                self._logger.warning(e)
                return None

    def put_user(self, user_id: int, data: dict) -> User:
        self._logger.debug(f'Updating user with ID {user_id} with data: {data}')
        with Session(self._engine) as session:
            try:
                user = User(**data)
                user.id = user_id
                session.merge(user)
                session.commit()
                return user
            except Exception as e:
                self._logger.warning(f'User with ID {user_id} not found')
                return None

    def delete_user(self, user_id: int) -> User:
        self._logger.debug(f'Deleting user with ID {user_id}')
        with Session(self._engine) as session:
            try:
                user = session.query(User).where(User.id == user_id).one()
                session.delete(user)
                session.commit()
                return user
            except Exception as e:
                self._logger.warning(f'User with ID {user_id} not found')
                return None
