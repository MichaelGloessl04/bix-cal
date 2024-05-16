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


class Entry(Base):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, index=True)
    author_id = Column(Integer, index=True)
    hot = Column(Float, index=True)
    crazy = Column(Float, index=True)
    nice = Column(Float, index=True)
    comment = Column(String(50), index=True, nullable=True)

    __table_args__ = tuple(UniqueConstraint('person_id', 'author_id', name='unique_person_author'))


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)

    __table_args__ = tuple(UniqueConstraint('username', name='unique_username'),
                           UniqueConstraint('email', name='unique_email'))
