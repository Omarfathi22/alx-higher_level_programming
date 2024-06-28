#!/usr/bin/python3
"""
Script to list all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a connection to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query State objects that contain the letter 'a' and order by id
    states_with_a = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()

    # Display the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
