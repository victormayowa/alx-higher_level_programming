#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter 'a'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a():
    """
    Deletes all State objects with a name containing the letter 'a'
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

    # Query and delete states
    states_to_delete = session.query(State).filter(
            State.name.like('%a%')
            ).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    delete_states_with_a()
