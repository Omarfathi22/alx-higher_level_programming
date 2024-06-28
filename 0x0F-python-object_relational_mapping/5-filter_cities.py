#!/usr/bin/python3
"""
Script to list all cities of a given state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def filter_cities_by_state(username, password, database, state_name):
    """
    Lists all cities of a given state from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): State name to filter cities by.

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

    # Execute SQL query using parameterized query to prevent SQL injection
    query = """SELECT cities.name
               FROM cities
               INNER JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id"""
    cursor.execute(query, (state_name,))

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Extract city names from rows
    cities = [row[0] for row in rows]

    # Display results as comma-separated list
    print(", ".join(cities))

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL username, password, database name, and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function with provided arguments
    filter_cities_by_state(username, password, database, state_name)
