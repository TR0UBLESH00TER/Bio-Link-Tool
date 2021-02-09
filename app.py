from flask import Flask, render_template, request, redirect
import datetime
import sqlite3
import os

Tree = Flask(__name__)

@Tree.route('/')
def tree():
    # Fetching all data for buttons
    db = sqlite3.connect('links.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM links;")
    linkList = cursor.fetchall()[::-1]
    db.close()

    CurrentYear = datetime.datetime.now().year
    tab_title = os.getenv("tab_title")
    organisation_name = os.getenv("organisation_name")
    title = os.getenv("title")
    avatar = os.getenv("avatar_link")
    page_icon = os.getenv("page_icon")

    return render_template('tree.html', CurrentYear=CurrentYear, title=title, avatar=avatar, \
        linkList=linkList, organisation_name=organisation_name, tab_title=tab_title, page_icon=page_icon)

@Tree.route('/login')
def login():
    CurrentYear = datetime.datetime.now().year
    tab_title = "Login"
    organisation_name = os.getenv("organisation_name")
    page_icon = os.getenv("page_icon")

    return render_template('login.html', CurrentYear=CurrentYear, organisation_name=organisation_name, \
        tab_title=tab_title, page_icon=page_icon)

@Tree.route('/verify',methods=["POST"])
def verify():
    global user_name, _password
    user_name = request.form.get("user_name")
    _password = request.form.get("_password")
    return redirect('/admin')

@Tree.route('/admin')
def admin():
    global user_name, _password

    CurrentYear = datetime.datetime.now().year
    tab_title = "Admin"
    organisation_name = os.getenv("organisation_name")
    title = os.getenv("title")
    avatar = os.getenv("avatar_link")
    page_icon = os.getenv("page_icon")

    # Fetching all data for buttons
    db = sqlite3.connect('links.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM links;")
    linkList = cursor.fetchall()[::-1]
    db.close()

    # Creating database if not existing
    try:
        db = sqlite3.connect('links.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE links (DisplayName VARCHAR(265) PRIMARY KEY, Link VARCHAR(256))")
        db.commit()
        db.close()
    except Exception: pass 

    a,b=os.getenv("user_name"),os.getenv("_password")
    print(a,b)
    print(user_name,_password)

    try:
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

@Tree.route('/add',methods=["POST"])
def add():
    # Adding Links to Database
    try:
        global user_name, _password
        display_name = request.form.get("display_name")
        link = request.form.get("link")
        if display_name != None and link != None:
            db = sqlite3.connect('links.db')
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO links VALUES(\"{display_name}\",\"{link}\");")
            db.commit()
            db.close()
        user_name=os.getenv("user_name")
        _password=os.getenv("_password")
        return redirect('/admin')
    except Exception: pass

@Tree.route('/delete',methods=["POST"])
def delete():
    # Deleting Links to Database
    try:
        global user_name, _password
        del_display_name = request.form.get("del_display_name")
        if del_display_name != None:
            db = sqlite3.connect('links.db')
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM links WHERE DisplayName=\"{del_display_name}\";")
            db.commit()
            db.close()
        user_name=os.getenv("user_name")
        _password=os.getenv("_password")
        return redirect('/admin')
    except Exception: pass

@Tree.errorhandler(404)
def error404(e):
    CurrentYear = datetime.datetime.now().year
    tab_title = "ERROR 404"
    page_icon = os.getenv("page_icon")
    organisation_name = os.getenv("organisation_name")
    return render_template("error404.html", CurrentYear=CurrentYear, tab_title=tab_title, \
        organisation_name=organisation_name, page_icon=page_icon ), 404

@Tree.errorhandler(405)
def error405(e):
    CurrentYear = datetime.datetime.now().year
    tab_title = "ERROR 405"
    page_icon = os.getenv("page_icon")
    organisation_name = os.getenv("organisation_name")
    return render_template('error405.html', CurrentYear=CurrentYear, tab_title=tab_title, \
        organisation_name=organisation_name, page_icon=page_icon ), 405