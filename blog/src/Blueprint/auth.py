import functools

from flask import (Blueprint, flash, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('auth/login.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    """
    Register new user
    """
    if request.method == 'POST':
        username = request.form['username']
        fullname = request.form['fullname']
        password = request.form['password']
        birthday = request.form['birthday']

        print(request.form)
    return render_template('auth/register.html')

# @bp.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('login'))