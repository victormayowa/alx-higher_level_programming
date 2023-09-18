#!/usr/bin/python3
"""
Script to print the State object with the name passed as argument
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_by_name():
    """
    Prints the State object with the name passed as argument
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    search_name = sys.argv[4]

    # Create engine and bind session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_user, mysql_password, database_name
        ), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for state
    state = session.query(State).filter(State.name == search_name).first()

    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()


if __name__ == "__main__":
    get_state_by_name()
