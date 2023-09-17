#!/usr/bin/python3
""" scripting of select statement"""

if __name__ == "__main__"

    import MySQLdb
    import sys

    # Take command line arguments
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

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the query to get all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()

