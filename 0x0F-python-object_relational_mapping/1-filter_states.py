#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N'
"""
import MySQLdb
from sys import argv


def filter_states():
    """
    Lists all states with names starting with 'N'
    """
    script, mysql_user, mysql_password, database_name = argv
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
