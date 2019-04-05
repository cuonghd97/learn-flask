import functools

from flask import (Blueprint, flash, redirect, render_template, request, session, url_for, jsonify)
import mysql.connector

from src.Blueprint.auth import login_required

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    return render_template('blog/index.html')

@bp.route('/write', methods=('GET', 'POST'))
@login_required
def write():
    return render_template('blog/create.html')

@bp.route('/post-write', methods=('GET', 'POST'))
@login_required
def post_write():
    if request.method == 'POST':
        print("request")
    return jsonify({})