from flask import redirect, url_for, flash, request, abort, jsonify
from project import app
from project.utils.db import User_book_db_functions
from project.models import User, Book

user_book_db_functions = User_book_db_functions()


@app.route('/api/v1/insertreader', methods=['POST'])
def post_reader():
    if request.method == 'POST':
        # obtenção do body como um objeto Json
        data = request.get_json()

        # todo colocar lógica de encriptação da senha
        # extração dos dados do json
        user_id = data['user_id']
        book_id = data['book_id']

        # instanciar a classe Db_functions e inserir o usuário
        response = user_book_db_functions.reader_insert(book_id=book_id, user_id=user_id)
        return response
    else:
        abort(404)