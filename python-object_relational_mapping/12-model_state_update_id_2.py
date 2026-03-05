#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """Define the main function"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}'
                           '@localhost:3306/{}'.format(username, password,
                                                       database))
    session = sessionmaker(bind=engine)
    session = session()
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
