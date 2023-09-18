#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_cities_states():
    """
    Lists all City objects with corresponding State objects
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for City objects and their associated states
    cities = session.query(City).order_by(City.id).all()

    # Loop through cities and print details
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close session
    session.close()


if __name__ == "__main__":
    list_cities_states()
