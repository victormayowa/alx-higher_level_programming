#!/usr/bin/python3
"""
Script to list all cities with their respective states
"""

import MySQLdb
import sys


def cities_by_state():
    """
    Lists all cities with their respective states
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    cursor = conn.cursor()

    # Execute the query to get cities with their respective states
    cursor.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    ORDER BY cities.id ASC""")

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    cities_by_state()
