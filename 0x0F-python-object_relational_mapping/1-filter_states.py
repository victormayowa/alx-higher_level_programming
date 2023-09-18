#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N'
"""

import MySQLdb
import sys

def filter_states():
    """
    Lists all states with names starting with 'N'
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

    # Execute the query to get states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    filter_states()
