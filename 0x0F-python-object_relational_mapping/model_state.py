#!/usr/bin/python3
# Contains the class definition of a State and an instance
# Base = declarative_base()

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_city import City

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto",
                unique=True)
    name = Column(String(128),
                  nullable=False)
