#!/usr/bin/python3
# Write a Python file similar to model_state.py named model_city.py
# that contains the class definition of a City.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto",
                unique=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
