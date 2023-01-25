from flask import redirect, url_for, flash, request, abort, jsonify
from project import app
from project.utils.db import Book_db_functions
from project.models import User, Book

book_db_functions = Book_db_functions()


@app.route('/api/v1/insertbook', methods=['POST'])
def post_book():
    if request.method == 'POST':
        # obtenção do body como um objeto Json
        data = request.get_json()

        # todo colocar lógica de encriptação da senha
        # extração dos dados do json
        title = data['title']
        pages_qty = data['pages_qty']

        # instanciar a classe Db_functions e inserir o usuário
        response = book_db_functions.book_insert(title=title, pages_qty=pages_qty)
        return response
    else:
        abort(404)

@app.route('/api/v1/getbooks', methods=['GET'])
def get_all_boooks():
    if request.method == 'GET':
        return book_db_functions.get_books()
    else:
        return abort(404)