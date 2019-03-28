import os
import datetime

from flask import Flask
import mysql.connector
from . import db
import bcrypt


def create_app():
    app = Flask(__name__)

    cnx = mysql.connector.connect(
        user='cuong', password='1', host='localhost', port='3306', database='blog')
    cursor = cnx.cursor()

    @app.route('/add-user')
    def add_user():
        now = datetime.datetime.now()
        password = b'cuong'
        print(bcrypt.hashpw(password, bcrypt.gensalt()))
        data_user = {
            'fullname': 'cuongqweqwe1',
            'username': 'cu',
            'password': password,
            'age': 22,
            'created_at': now
        }
        # add_user = ("INSERT INTO users "
        #     "(fullname, username, password, age, created_at) "
        #     "VALUES (%(fullname)s, %(username)s, %(password)s, %(age)s, %(created_at)s)")
        # cursor.execute(add_user, data_user)
        # cnx.commit()
        # cursor.close()
        # cnx.close()
        return db.add_user(data_user)

    return app