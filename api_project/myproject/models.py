from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)

    characters = relationship('Person', back_populates='film')
    starships = relationship('Starship', back_populates='film')

class Person(Base):
    __tablename__ = 'personages'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    film_id = Column(Integer, ForeignKey('films.id'))

    film = relationship('Film', back_populates='characters')

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String)

    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship('Film', back_populates='starships')