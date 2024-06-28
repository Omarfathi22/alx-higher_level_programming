#!/usr/bin/python3
"""Module defining City class"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base, State  # Import State here

Base = declarative_base()

class City(Base):
    """City class representing cities table in the database"""

    __tablename__ = 'cities'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    state_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('states.id'))
    state = relationship("State")  # Use the State class here