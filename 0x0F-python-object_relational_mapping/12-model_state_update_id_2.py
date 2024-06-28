#!/usr/bin/python3
"""
Script to change the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def update_state(username, password, database):
    """
    Updates the name of a State object with id=2 to "New Mexico".

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

    # Query the State object with id=2
    state = session.query(State).filter(State.id == 2).first()
    
    # Update the name if the state exists
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <username> <password> <database>")
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to update the state with id=2 to "New Mexico"
    update_state(username, password, database)
