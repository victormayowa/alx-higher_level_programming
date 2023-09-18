#!/usr/bin/python3
"""
Script to list all State objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_all_states():
    """
    Lists all State objects from the database
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

    # Fetch all states
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()


if __name__ == "__main__":
    fetch_all_states()
