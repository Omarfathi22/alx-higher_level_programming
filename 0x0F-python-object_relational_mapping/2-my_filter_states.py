#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


def filter_states(username, password, db_name, state_name):
    """
    Connects to MySQL database and filters states by user input.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to filter.

    Returns:
        None
    """
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create cursor object
    cur = db.cursor()

    # Execute query to select state by name provided as argument
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(state_name))

    # Fetch all rows
    rows = cur.fetchall()

    # Print all rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
