#!/usr/bin/python3
"""
Script to add the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, database, state_name):
    """
    Adds a new State object to the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to add.

    Returns:
        int: The id of the newly added State object.
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

    # Create a new State object
    new_state = State(name=state_name)

    # Add the new State object to the session and commit it to the database
    session.add(new_state)
    session.commit()

    # Get the id of the newly added State object
    state_id = new_state.id

    # Close the session
    session.close()

    return state_id

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <username> <password> <database>")
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to add the state "Louisiana" and get the new state id
    new_state_id = add_state(username, password, database, "Louisiana")

    # Print the new state id
    print(new_state_id)
