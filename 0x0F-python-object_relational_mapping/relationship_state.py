#!/usr/bin/python3
"""Module defining State class"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class representing states table in the database"""

    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    