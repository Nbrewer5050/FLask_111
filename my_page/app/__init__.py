#!/usr/bin/env python3
"""A simple flask app"""

from flask import Flask

app = Flask(__name__)


def create_user(user):
    sql = """INSERT INTO user (
                    first_name,
                    last_name,
                    hobbies)
                VALUES (?, ?, ?)"""
    cursor = get_db()
    cursor.execute(sql, user)
    cursor.commit()
    return True                

from app import routes