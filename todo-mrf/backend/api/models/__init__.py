from datetime import datetime

from sqlalchemy import exc

from api.database import db
import api.error as error

class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    work = db.Column(db.String(120), nullable=False)
    is_done = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def to_json(item):
        return {
            'id': item.id,
            'work': item.work,
            'is_done': item.is_done,
            'created_at': str(item.created_at.strftime("%m/%d/%Y, %H:%M:%S"))
        }

    @classmethod
    def get_all(cls):
        return {'todo_list': list(
            map(lambda item: cls.to_json(item), cls.query.all())
        )}

    @classmethod
    def change_done(cls, id):
        try:
            todo_item = cls.query.get(id)
            todo_item.is_done = 1
            db.session.commit()

            return {'message': 'Update success'}
        except exc.SQLAlchemyError as ex:
            print(ex)
            return error.SERVER_ERROR_500

    @classmethod
    def delete_one(cls, id):
        try:
            todo_item = db.session.query(cls).get(id)
            db.session.delete(todo_item)
            db.session.commit()

            return {'message': 'Delete success'}
        except exc.SQLAlchemyError as ex:
            print(ex)

            return error.SERVER_ERROR_500

    @classmethod
    def delete_done(cls):
        # todo_done = cls.query.filter_by(is_done=1).all()
        # print(todo_done)
        try:
            todo_done = db.session.query(cls).filter(cls.is_done == 1)
            todo_done.delete(synchronize_session=False)
            db.session.commit()
            # todo_done = cls.query.filter_by(is_done=1).all()
            # db.session.delete(todo_done)
            # db.session.commit()

            return {'message': 'Deleted all done'}
        except exc.SQLAlchemyError as ex:
            print(ex)
            return error.SERVER_ERROR_500