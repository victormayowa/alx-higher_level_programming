#!/usr/bin/python3
"""script to select all entries from the states table"""
import MySQLdb as sqldb
from sys import argv


def get_states():
    """selects all states"""
    script, user, passwd, db_name = argv
    db = sqldb.connect(host='localhost', port=3306,
                       user=user, passwd=passwd, db=db_name)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states ORDER BY states.id""")
    states = cursor.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    get_states()
