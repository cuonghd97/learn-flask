import os
import datetime

from flask import Flask, render_template, request, url_for
import mysql.connector
from flask_wtf.csrf import CsrfProtect
from werkzeug.utils import secure_filename

CsrfProtect(app)
UPLOAD_FOLDER = '/uploads'

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config.from_mapping(SECRET_KEY='dev')
    

    from src.Blueprint import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    app.add_url_rule('/', endpoint='index')
    
    # @app.route('/')
    # def base():
    #     return render_template('base.html')

    return app