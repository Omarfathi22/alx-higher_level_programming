#!/usr/bin/python3
"""
Script to safely filter states from a MySQL database.
"""

import sys
import MySQLdb


def safe_filter_states(username, password, database, state_name):
    """
    Safely filters states from the database based on the given state_name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): State name to search for.

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Display each row
    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))

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
    safe_filter_states(username, password, database, state_name)
