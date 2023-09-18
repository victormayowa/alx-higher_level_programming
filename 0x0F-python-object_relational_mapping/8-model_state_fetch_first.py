#!/usr/bin/python3
"""
Script to print the first State object from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state():
    """
    Prints the first State object from the database
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and bind session
    conn = 'mysql+mysqldb://{}:{}@localhost/{}'.format(mysql_user,
                                                       mysql_password,
                                                       database_name)
    engine = create_engine(conn, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first state
    first_state = session.query(State).order_by(State.id).first()

    # Print the result
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close session
    session.close()


if __name__ == "__main__":
    fetch_first_state()
