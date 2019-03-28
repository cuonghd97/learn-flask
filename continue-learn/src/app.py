import os

from flask import Flask
import mysql.connector

def create_app():
    app = Flask(__name__)
    
    cnx = mysql.connector.connect(user='cuong', password='1', host='localhost',  database='cuong')
    cursor = cnx.cursor()
    
    @app.route('/hello')
    def hello():
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchall()
        for i in data:
            print(i)
        cursor.close()
        cnx.close()
        return 'hi'

    return app

