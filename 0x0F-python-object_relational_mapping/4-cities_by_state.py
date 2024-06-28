#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def cities_by_state(username, password, database):
    """
    List all cities from the given database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to list all cities
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               INNER JOIN states ON cities.state_id = states.id
               ORDER BY cities.id"""
    cursor.execute(query)

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        city_id, city_name, state_name = row
        print("({}, '{}', '{}')".format(city_id, city_name, state_name))

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function with provided arguments
    cities_by_state(username, password, database)
