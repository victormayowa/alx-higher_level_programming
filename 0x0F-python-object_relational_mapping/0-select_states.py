#!/usr/bin/python3
"""script to select all entries from the states table from a db
passed as an argument"""
from sys import argv as sysargv
import MySQLdb as sqldb


def get_states():
    """selects all states from the database"""
    script, user, passwd, db_name = sysargv
    db = sqldb.connect(host='localhost', port=3306,
                       user=user, passwd=passwd, db=db_name)
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id""")
    states = c.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    get_states()
