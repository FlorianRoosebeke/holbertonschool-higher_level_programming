#!/usr/bin/python3
"""Print the states.id of a State object matching the given name."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == search).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
