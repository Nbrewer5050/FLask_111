#!/usr/bin/env python3
"""Routes flie: specifies http routes"""

from flask import g
from app import app #from the app [module] import app [variable] that we created in the __init__.py file
import sqlite3

DATABASE = "my_page.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def return_users():
    cursor = get_db().execute("select * from user", ())
    results = cursor.fetchall()
    cursor.close()
    return results 

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route("/dump/users")
def show_all_user():
    user = get_users()
    return render_template("all_users.html", user=users)

@app.route("/users")
def dump_json():
    out = {"ok": True, "body": ""}
    users = get_all_users()
    body_list = []
    for user in user:
        temp_dictionary ={}
        temp_dictionary["first_name"] = user[0]
        temp_dictionary["last_name"] =user[1]
        temp_dictionary["hobbies"] = user[2]
        body_list.append(temp_dictionary)
    out["body"] = body_list
    return out


@app.route("/")
def index():
    return "Hello, world!"

@app.route("/users")
def get_users():
    return str(return_users())

@app.route("/aboutme")
def about_me():
    me = {"first_name": "Nicholas",
          "last_name": "Brewer",
          "hobbies": "Photography"
         }
    return me
