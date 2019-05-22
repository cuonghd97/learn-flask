import os

import bcrypt
from run import db
from sqlalchemy import exc

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    avatar = db.Column(db.String(300), nullable=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @staticmethod
    def generate_hash(password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    @staticmethod
    def verify_hash(password, hashed):
        return bcrypt.checkpw(password.encode('utf8'), hashed)

    @classmethod
    def upload_avatar(cls, path, username):
        user = cls.query.filter_by(username=username).first()
        print(user)
        if user.avatar:
            if os.path.exists(user.avatar):
                os.remove(user.avatar)
            else:
                print("The file does not exist")
        try:
            user.avatar = path
            db.session.commit()
            return True
        except exc.SQLAlchemyError as er:
            print(er)
            return False


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
