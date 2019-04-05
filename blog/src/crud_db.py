from datetime import datetime

import mysql.connector

OK = 'OK'
NOW = datetime.now()

def add_user(data_user):
    cnx = mysql.connector.connect(user='cuong', password='1', host='localhost', port='3306', database='blog')
    cursor = cnx.cursor()
    add_user = ("INSERT INTO users "
                "(fullname, username, password, age, created_at "
                "VALUES (%(fullname)s, %(username)s, %(password)s, %(age)s, %(NOW)s)")
    cursor.execute(add_user, data_user)
    cnx.commit()
    cursor.close()
    cnx.close()
    
    return OK