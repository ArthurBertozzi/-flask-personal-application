from project import database, app
from datetime import datetime


# relação N:N -> muitos usuarios podem ler um livro enquanto que muitos livros podem ser lidos por um usuário

class User(database.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    date_inserted = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    # N:N
    books = database.relationship('Book', secondary='user_books', backref='users')


class Book(database.Model):
    __tablename__ = 'books'
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String, nullable=False)
    pages_qty = database.Column(database.String, nullable=False)
    date_inserted = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    # se fosse 1:N
    #reader = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    # N:N -> não é ncessario colocar em ambas os models
    #reader = database.relationship('User', secondary='user_books', backref='livros')


class UserBook(database.Model):
    __tablename__ = 'user_books'
    __table_args__ = {'extend_existing': True}
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    book_id = database.Column(database.Integer, database.ForeignKey('books.id'))
    current_page = database.Column(database.Integer, nullable=False)


# To create our databases tables
if __name__ == '__main__':
    with app.app_context():
        database.create_all()
