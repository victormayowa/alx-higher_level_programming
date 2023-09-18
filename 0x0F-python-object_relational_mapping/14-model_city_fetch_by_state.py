#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state():
    """
    Fetches and prints all City objects by state
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

    # Query and print cities
    cities = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()


if __name__ == "__main__":
    fetch_cities_by_state()
