#!/usr/bin/python3
"""
Prints all State objects along with their related City objects from the database.

This script connects to a MySQL database using SQLAlchemy, retrieves all State 
objects, and for each State, it retrieves and prints the associated City objects.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a new SQLAlchemy engine instance, connecting to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    
    # Create all tables in the database (based on the Base class metadata)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class and an instance of a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and order them by their id
    for instance in session.query(State).order_by(State.id):
        # Print the State id and name
        print(instance.id, instance.name, sep=": ")

        # For each State, query and print the associated City objects
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")

