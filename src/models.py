import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(10), nullable=False)
    gender = Column(String(20), nullable=False)
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    homeworld = Column(String(100), nullable=False)
    url = Column(String(100), nullable=False)
    description = Column(String(150), nullable=False)
    img = Column(String(150), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(String(50), nullable=False)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)
    description = Column(String(150), nullable=False)
    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    userName = Column(String(50),nullable=False)
    userPassword = Column(String(250),nullable=False)
    created = Column(DateTime, nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    typeFavorite = Column(String(20),nullable=False)
    idCharPlan = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

 



        

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')