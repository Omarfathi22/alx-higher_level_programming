#!/usr/bin/python3
"""
Script to print the State object with the name passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def get_state_id(username, password, database, state_name):
    """
    Retrieves the id of the State object with the given name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to search.

    Returns:
        int: The id of the State object if found, otherwise None.
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

    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Close the session
    session.close()

    # Return the id of the State object if found, otherwise None
    if state:
        return state.id
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get MySQL username, password, database name, and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to get the state id
    state_id = get_state_id(username, password, database, state_name)

    # Print the result
    if state_id is not None:
        print(state_id)
    else:
        print("Not found")
