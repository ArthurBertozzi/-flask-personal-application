from project import database, app
from flask_login import UserMixin
from datetime import datetime


class Usuario(database.Model):
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    date_inserted = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)


# To create our databases tables
if __name__ == '__main__':
    with app.app_context():
        database.create_all()
