#!/usr/bin/python3
"""
Script to list all states with a specific name
"""

import MySQLdb
from sys import argv


def filter_states():
    """
    Lists all states with a specific name
    """
    script, mysql_user, mysql_password, database_name, state_name = argv

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    cursor = conn.cursor()
    # Execute the query to get states with the specified name
    quare = "SELECT * FROM states\
             WHERE states.name LIKE BINARY '{}'\
             ORDER BY states.id".format(state_name)
    cursor.execute(quare)
    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    filter_states()
