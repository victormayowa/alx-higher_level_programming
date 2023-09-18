#!/usr/bin/python3
"""
Script to list all cities of a specific state
"""

import MySQLdb
import sys


def filter_cities():
    """
    Lists all cities of a specific state
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    cursor = conn.cursor()

    # Execute the query to get cities of the specific state
    cursor.execute("""SELECT cities.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name=%s
                    ORDER BY cities.id ASC""", (state_name,))

    # Fetch and print the results
    cities = cursor.fetchall()
    if cities:
        print(", ".join(city[0] for city in cities))
    else:
        print("No cities found for the specified state")

    # Close cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    filter_cities()

