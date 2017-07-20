
from flask import Flask, render_template, url_for, request, redirect, flash,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
import database_queries as r
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    items = r.get_restaurantmenu(restaurant_id)
    return jsonify(MenuItems=[i.serialize for i in items])

# ADD JSON API ENDPOINT HERE
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    item = r.get_menuitem(menu_id)
    return jsonify(MenuItem=item.serialize)


@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menu = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', items=menu, restaurant = restaurant)


# Task 1: Create route for newMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/new', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        # create new menu item
        r.set_newmenuitem(request.form['name'],restaurant_id)
        flash("new menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# Task 2: Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit',methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        # edit menu item
        name = request.form['name']
        if name != "":
            r.set_editmenuitem(name,menu_id)
        flash("Menu item edit edited!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        menu = r.get_menuitem(menu_id) # return dict
        return render_template('editmenuitem.html', 
                               restaurant_id=restaurant_id, 
                               menu_name = menu.name,
                               menu_id = menu_id)

# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete',methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        # delete menu item
        r.set_deletemenuitem(menu_id)
        flash("Menu item delete!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        menu = r.get_menuitem(menu_id) # return dict
        return render_template('deletemenuitem.html', 
                               restaurant_id=restaurant_id, 
                               menu_name = menu.name,
                               menu_id = menu_id)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
     
    
    
    
    
    
    
    
    
    