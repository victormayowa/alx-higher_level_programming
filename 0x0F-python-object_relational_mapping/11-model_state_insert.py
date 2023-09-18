#!/usr/bin/python3
"""
Script to add the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana():
    """
    Adds the State object "Louisiana" to the database hbtn_0e_6_usa
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and bind session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_user, mysql_password, database_name
        ), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create and add new state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's ID
    print(new_state.id)

    # Close session
    session.close()


if __name__ == "__main__":
    add_louisiana()
