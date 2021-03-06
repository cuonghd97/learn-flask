import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import bcrypt

DB_NAME = 'blog'

TABLES = {}

# User table
TABLES['users'] = (
    "CREATE TABLE `users`("
    "   `id` INT NOT NULL AUTO_INCREMENT,"
    "   `fullname` VARCHAR(255) NOT NULL,"
    "   `username` VARCHAR(30) NOT NULL,"
    "   `password` CHAR(255) NOT NULL,"
    "   `created_at` TIMESTAMP,"
    "   PRIMARY KEY (`id`),"
    "   UNIQUE KEY `username` (`username`)"
    "   ) ENGINE=InnoDB"
)

# Blog table
TABLES['blogs'] = (
    "CREATE TABLE `blog`("
    "   `id` INT NOT NULL AUTO_INCREMENT,"
    "   `title` VARCHAR(255) NOT NULL,"
    "   `category` VARCHAR(255) NOT NULL,"
    "   `content` LONGTEXT,"
    "   `created_at` TIMESTAMP,"
    "   `user_id` INT NOT NULL,"
    "   PRIMARY KEY(`id`),"
    "   CONSTRAINT `user_blog` FOREIGN KEY (`user_id`)"
    "       REFERENCES `users`(`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

IS_EXIST = False

cnx = mysql.connector.connect(user='cuong', password='1', host='localhost', port='3306')
cursor = cnx.cursor()
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} CHARACTER SET utf8 COLLATE utf8_general_ci".format(DB_NAME)
        )
    except mysql.connector.Error as err:
        print(err)
        exit(1)

try:
    IS_EXIST = True
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print('Create success')
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# is_created = cursor.execute(SELECT_DATABASE, {'db_name': DB_NAME})
# print(is_created)
if IS_EXIST == False:
    for table in TABLES:
        table_desc = TABLES[table]
        try:
            print('Creating {} '.format(table), end='')
            cursor.execute(table_desc)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table already exist")
            else:
                print(err.msg)
        else:
            print("ok")

cursor.close()
cnx.close()