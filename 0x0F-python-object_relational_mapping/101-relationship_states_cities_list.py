#!/usr/bin/python3
"""
Script to list all State objects and corresponding City objects.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Create connection to database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for all State objects and their associated City objects
    states = session.query(State).order_by(State.id).all()

    # Iterate over each state and print its corresponding cities
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close session
    session.close()
