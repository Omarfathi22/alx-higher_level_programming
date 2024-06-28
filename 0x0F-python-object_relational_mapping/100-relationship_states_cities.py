#!/usr/bin/python3
"""
Script to create State 'California' with City 'San Francisco'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Create connection to database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create tables if they do not exist
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State 'California' with City 'San Francisco'
    california = State(name='California', cities=[City(name='San Francisco')])
    session.add(california)
    session.commit()

    # Close session
    session.close()
