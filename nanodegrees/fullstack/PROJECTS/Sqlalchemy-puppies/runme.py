#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Using SQLAlchemy perform the following queries on your database:
"""

import datetime
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from puppies import Base,Shelter,Puppy


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
old_180days = (datetime.datetime.now() - datetime.timedelta(days=180)).\
              date().isoformat()

def print_poppies(puppies):
    for p in puppies:
        print p.name," DOB:",p.dateOfBirth," weight:",round(p.weight,2),"location:",p.shelter.name

def get_q1():
    """
    Query all of the puppies and return the results
    in ascending alphabetical order
    """
    puppies = session.query(Puppy).order_by(Puppy.name.asc()).all()
    print_poppies(puppies)

def get_q2():
    """
    Query all of the puppies that are less than 6 months old
    organized by the youngest first
    """
    puppies = session.query(Puppy).filter(Puppy.dateOfBirth >= old_180days ).\
                           order_by(Puppy.dateOfBirth.desc())
    print_poppies(puppies)

def get_q3():
    """
    Query all puppies by ascending weight
    """
    puppies = session.query(Puppy).order_by(Puppy.weight.asc()).all()
    print_poppies(puppies)

def get_q4():
    """
    Query all puppies grouped by the shelter in which they are staying
    """
    shelter = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
    for item in shelter:
        print item[0].id, item[0].name, item[0].state ,'Total:' ,  item[1]


if __name__ == '__main__':
    get_q1()
    get_q2()
    get_q3()
    get_q4()






























