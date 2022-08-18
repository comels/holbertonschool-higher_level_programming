#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    session = Session(engine)
    Base.metadata.create_all(engine)

    first = session.query(State).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")

    session.close()
