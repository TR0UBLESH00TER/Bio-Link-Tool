# Importing required modules and functions.
from flask import Flask, render_template, request, redirect
import datetime
import sqlite3
import os


# Created App
Tree = Flask(__name__)


# Main page where all links are displayed.
@Tree.route('/')
def tree():

    # Fetching all data for buttons.
    db = sqlite3.connect('links.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM links;")
    linkList = cursor.fetchall()[::-1]
    db.close()

    # All required variables used in the webpage.
    CurrentYear = datetime.datetime.now().year
    tab_title = os.getenv("tab_title")
    organisation_name = os.getenv("organisation_name")
    title = os.getenv("title")
    avatar = os.getenv("avatar_link")
    page_icon = os.getenv("page_icon")

    return render_template('tree.html', CurrentYear=CurrentYear, title=title, avatar=avatar, \
        linkList=linkList, organisation_name=organisation_name, tab_title=tab_title, page_icon=page_icon)


# Login page for admin login.
@Tree.route('/login')
def login():

    # All required variables used in the webpage.
    CurrentYear = datetime.datetime.now().year
    tab_title = "Login"
    organisation_name = os.getenv("organisation_name")
    page_icon = os.getenv("page_icon")

    # Creating database if not existing.
    try:
        db = sqlite3.connect('links.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE links (DisplayName VARCHAR(265) PRIMARY KEY, Link VARCHAR(256))")
        db.commit()
        db.close()
    except Exception: pass 

    return render_template('login.html', CurrentYear=CurrentYear, organisation_name=organisation_name, \
        tab_title=tab_title, page_icon=page_icon)


# To verify fetch data entered in login page and redirect to /admin where checking/ verifying of 
# username and passwrd is done and a page is displayed accordingly.
@Tree.route('/verify',methods=["POST"])
def verify():

    global user_name, _password
    user_name = request.form.get("user_name")
    _password = request.form.get("_password")
    
    return redirect('/admin')


# Admin page where adding and removing of links from the page can be done.
@Tree.route('/admin')
def admin():

    global user_name, _password

    # All required variables used in the webpage.
    CurrentYear = datetime.datetime.now().year
    tab_title = "Admin"
    organisation_name = os.getenv("organisation_name")
    title = os.getenv("title")
    avatar = os.getenv("avatar_link")
    page_icon = os.getenv("page_icon")

    # Fetching all data for buttons.
    db = sqlite3.connect('links.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM links;")
    linkList = cursor.fetchall()[::-1]
    db.close()

    try:
        # Checking password and username entered in login page.
        if user_name == os.getenv("user_name") and _password == os.getenv("_password"):
            print(user_name,_password)
            user_name = _password = ""
            
            return render_template('admin.html', CurrentYear=CurrentYear, title=title, avatar=avatar, \
                linkList=linkList, organisation_name=organisation_name, tab_title=tab_title, page_icon=page_icon)
        
        else:

            return render_template('invalid.html', CurrentYear=CurrentYear, tab_title=tab_title, \
                organisation_name=organisation_name, page_icon=page_icon)
    
    except Exception:

        return render_template('invalid.html', CurrentYear=CurrentYear, tab_title=tab_title, \
            organisation_name=organisation_name, page_icon=page_icon)


# To add the display name and link passed in admin and redirect back to admin (in a way refreshes the page).
@Tree.route('/add',methods=["POST"])
def add():

    try:
        global user_name, _password
        display_name = request.form.get("display_name")
        link = request.form.get("link")

        if display_name != None and link != None:
            # Adding Links to Database.
            db = sqlite3.connect('links.db')
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO links VALUES(\"{display_name}\",\"{link}\");")
            db.commit()
            db.close()

        user_name=os.getenv("user_name")
        _password=os.getenv("_password")

        return redirect('/admin')

    except Exception: pass


# To delete the display name passed in admin and redirect back to admin (in a way refreshes the page).
@Tree.route('/delete',methods=["POST"])
def delete():

    try:
        global user_name, _password
        del_display_name = request.form.get("del_display_name")

        if del_display_name != None:
            # Deleting Links to Database.
            db = sqlite3.connect('links.db')
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM links WHERE DisplayName=\"{del_display_name}\";")
            db.commit()
            db.close()

        user_name=os.getenv("user_name")
        _password=os.getenv("_password")

        return redirect('/admin')

    except Exception: pass


# Page for Error 404
@Tree.errorhandler(404)
def error404(e):

    # All required variables used in the webpage.
    CurrentYear = datetime.datetime.now().year
    tab_title = "ERROR 404"
    page_icon = os.getenv("page_icon")
    organisation_name = os.getenv("organisation_name")

    return render_template("error404.html", CurrentYear=CurrentYear, tab_title=tab_title, \
        organisation_name=organisation_name, page_icon=page_icon ), 404


# Page for Error 405
@Tree.errorhandler(405)
def error405(e):

    # All required variables used in the webpage.
    CurrentYear = datetime.datetime.now().year
    tab_title = "ERROR 405"
    page_icon = os.getenv("page_icon")
    organisation_name = os.getenv("organisation_name")

    return render_template('error405.html', CurrentYear=CurrentYear, tab_title=tab_title, \
        organisation_name=organisation_name, page_icon=page_icon ), 405