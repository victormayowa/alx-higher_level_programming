#!/usr/bin/python3
"""
Script to list all State objects that contain the letter 'a' from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_states_with_a():
    """
    Lists all State objects that contain the letter 'a'
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and bind sessioni
    conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(mysql_user,
                                                       mysql_password,
                                                       database_name)
    engine = create_engine(conn, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch states with 'a'
    states_with_a = session.query(State).filter(State.name.like("%a%"))
    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()


if __name__ == "__main__":
    filter_states_with_a()
