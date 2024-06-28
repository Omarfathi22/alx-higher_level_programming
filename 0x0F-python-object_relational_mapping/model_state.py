#!/usr/bin/python3
"""
This module defines a State class and an instance Base using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table 'states'.

    Attributes:
        id (int): Auto-generated, unique integer, can't be null, primary key.
        name (str): String with maximum 128 characters, can't be null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)