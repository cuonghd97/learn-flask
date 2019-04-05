import os
import datetime

from flask import Flask, render_template, request, url_for
import mysql.connector
import bcrypt


def create_app():
    app = Flask(__name__)

    from src.Blueprint import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def base():
        return render_template('base.html')

    return app