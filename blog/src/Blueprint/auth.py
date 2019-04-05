import functools
from datetime import datetime

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
import mysql.connector


from src import crud_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        cnx = mysql.connector.connect(user='cuong', password='1', host='127.0.0.1', port='3306', database='blog')
        cursor = cnx.cursor(dictionary=True, buffered=True)
        cursor.execute("""SELECT * FROM `users` WHERE id=%(user_id)s""", {'user_id': user_id})
        g.user = cursor.fetchone()
        cursor.close()
        cnx.close()

@bp.route('/register', methods=('GET', 'POST'))
def register():
    """
    Register new user
    """
    error = 'Success'
    if request.method == 'POST':
        username = request.form['username']
        fullname = request.form['fullname']
        password = request.form['password']

        data_user = {
            'username': username,
            'fullname': fullname,
            'password': generate_password_hash(password)
        }
        err = crud_db.add_user(data_user)
        if err != None:
            error = 'Error'
        print(error)
    return render_template('auth/register.html', error = error)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    """
    Login
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = None
        try:
            cnx = mysql.connector.connect(user='cuong', password='1', host='127.0.0.1', port='3306', database='blog')
            cursor = cnx.cursor(dictionary=True, buffered=True)
            cursor.execute("""SELECT * FROM `users` where username=%(username)s""", {'username': username})
            user = cursor.fetchone()
            print(user)
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(err)
            error = err

        if not check_password_hash(user['password'], password):
            error = 'error'

        print(error)
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html', error = 'error')        
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))