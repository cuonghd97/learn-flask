import os

from flask import Flask, app

from api.database import db
from api.conf.config import (SQLALCHEMY_DATABASE_URI, SECRET_KEY)
from api.conf.routes import generate_routes
import api.models as models

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = SECRET_KEY

    db.init_app(app)

    if not os.path.exists(SQLALCHEMY_DATABASE_URI):
        db.app = app
        db.create_all()

    return app

if __name__ == '__main__':
    app =create_app()
    db.create_all()
    generate_routes(app)

    app.run()