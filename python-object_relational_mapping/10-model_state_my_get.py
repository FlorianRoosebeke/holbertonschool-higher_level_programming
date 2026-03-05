#!/usr/bin/python3
"""Print a State object from the database hbtn_0e_6_usa."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """Define the main function"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}'
                           '@localhost:3306/{}'.format(username, password,
                                                       database))
    session = sessionmaker(bind=engine)
    session = session()
    states = session.query(State).filter(State.name == search).first()
    if states:
        print("{}".format(states.name))
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    main()
