#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa that match the given name."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Create the query
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    
    # Execute the query
    cur.execute(query)
    
    # Fetch and print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Close cursor and database connection
    cur.close()
    db.close()
