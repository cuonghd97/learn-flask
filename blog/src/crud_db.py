from datetime import datetime

import mysql.connector
from mysql.connector import errorcode

OK = 'OK'
EXISTED = 'EXISTED'
NOW = datetime.now()

# SQL
SELECT_USER = """SELECT id FROM users WHERE username = %(username)s"""
ADD_USER = """INSERT INTO users (fullname, username, password, created_at) VALUES (%(fullname)s, %(username)s, %(password)s, %(created_at)s)"""

# Function execute
def add_user(data_user):
    cnx = mysql.connector.connect(
        user='cuong', password='1', host='localhost', port='3306', database='blog')
    cursor = cnx.cursor(buffered=True, dictionary=True)
    error = None
    data_user.update({'created_at': NOW})
    
    try:
        cursor.execute(ADD_USER, data_user)
        cnx.commit()
    except mysql.connector.Error as err:
        error = err

    cursor.close()
    cnx.close()

    return error
