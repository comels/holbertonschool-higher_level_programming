#!/usr/bin/python3
"""Write a python file that contains the class
definition of a State and an instance Base = declarative_base():"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """the class State"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
