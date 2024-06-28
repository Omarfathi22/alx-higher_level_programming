#!/usr/bin/python3
"""
Script to list all City objects and their associated State objects.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py <mysql username> <mysql password> <database name>")
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

    # Query the database for all City objects and their associated State objects
    cities = session.query(City).order_by(City.id).all()

    # Iterate over each city and print its associated state
    for city in cities:
        state_name = city.state.name if city.state else "No associated state"
        print(f"{city.id}: {city.name} -> {state_name}")

    # Close session
    session.close()
