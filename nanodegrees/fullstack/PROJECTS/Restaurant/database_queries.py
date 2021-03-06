#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Using SQLAlchemy perform the following queries on your database:
"""

import datetime
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


html_li = """
          <li>
            {name}
           <div> <a href="/restaurants/{id}/delete">delete</a> </div>
           <div> <a href="/restaurants/{id}/edit">edit</a> </div>
          </li>
          """

def get_restaurants(id = None):
    """
    Query all of the restaurants and return the results
    in ascending alphabetical order
    """
    restaurants = session.query(Restaurant).order_by(Restaurant.name.asc()).all()
    output = ""
    
    if id:
        for rest in restaurants:
            if rest.id == int(id):
                return (rest.name,rest.id)
    else:    
        for rest in restaurants:
            output += html_li.format(id=rest.id, name=rest.name)
        return(output) 

def get_restaurant(id = None):
    if id:
        return session.query(Restaurant).order_by(Restaurant.name.asc()).all()

def set_newmenuitem(name,restaurant_id):
        newItem = MenuItem(name=name, restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()  
        
def set_editmenuitem(name,menu_id):
        menu = session.query(MenuItem).filter_by(id = menu_id).one()
        menu.name = name
        session.commit()

def set_deletemenuitem(menu_id):
        menu = session.query(MenuItem).filter_by(id = menu_id).one()
        session.delete(menu)
        session.commit()
    
def get_menuitem(menu_id):
    if menu_id:
        return session.query(MenuItem).filter_by(id = menu_id).one()

def get_restaurantmenu(restaurant_id):
    if restaurant_id:
        return session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()

def set_restaurant(restaurant):
    # New restaurant 
    if restaurant:
        try:
            new_rest = Restaurant(name=restaurant)
            session.add(new_rest)
            session.commit()
            print 'restaurant added'
            return 0
        except:
            pass
            return 1
        
def delete_restaurant(restName):
    # New restaurant and all its menus
    if restName:
        try:
            del_rest = session.query(Restaurant).filter_by(name = restName).one()
            menus = session.query(MenuItem).filter_by(restaurant_id = del_rest.id).all()
            session.delete(del_rest)
            for m in menus:
                session.delete(m)
            session.commit()
            print 'restaurant deleted'
            return 0
        except:
            pass
            return 1

def update_restaurant(data = None):
    # New restaurant 
    if data:
        try:
            update_rest = session.query(Restaurant).filter_by(id = data[1]).one()
            update_rest.name = data[0]
            session.commit()
            print 'restaurant updated'
            return 0
        except:
            pass
            return 1