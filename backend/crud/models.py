from sqlalchemy import Column, Float, Integer, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)

    __table_args__ = tuple(UniqueConstraint('name', 'surname', name='unique_name_surname'))


class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    score = Column(Float, index=True)
    hot = Column(Float, index=True)
    crazy = Column(Float, index=True)
    nice = Column(Float, index=True)
    comment = Column(String(20), index=True, nullable=True)

    __table_args__ = (
        UniqueConstraint('person_id', 'user_id', name='uq_person_user'),
    )


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)

    __table_args__ = tuple(UniqueConstraint('username', 'email', name='unique_username_email'))
