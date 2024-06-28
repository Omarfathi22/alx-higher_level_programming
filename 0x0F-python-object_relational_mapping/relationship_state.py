#!/usr/bin/python3
"""
Defines the State class and its relationship with the City class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    State class linked to the MySQL table 'states'.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")
