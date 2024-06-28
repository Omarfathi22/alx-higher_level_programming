#!/usr/bin/python3
"""
Script to print all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_cities(username, password, database):
    """
    Fetches and prints all City objects from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
    """
    # Create a connection to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()

    # Query and print all City objects with associated State names
    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <username> <password> <database>")
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to fetch and print cities
    fetch_cities(username, password, database)
