from flask import redirect, url_for, flash, request, abort, jsonify
from project import app
from project.utils.db import User_db_functions
from project.models import User, Book


user_db_functions = User_db_functions()


@app.route('/api/v1/allusers', methods=['GET'])
def get_all_users():
    if request.method == 'GET':
        return user_db_functions.get_users()
    else:
        return abort(404)


@app.route('/api/v1/insertuser', methods=['POST'])
def post_user():
    if request.method == 'POST':
        # obtenção do body como um objeto Json
        data = request.get_json()

        # todo colocar lógica de encriptação da senha
        # extração dos dados do json
        nome = data['username']
        senha = data['senha']
        email = data['email']

        # instanciar a classe Db_functions e inserir o usuário
        response = user_db_functions.inserir_usuario_db(username=nome, senha=senha, email=email)
        return response
    else:
        abort(404)


@app.route('/api/v1/userid', methods=['GET'])
def get_user_by_id():
    if request.method == 'GET':
        # obtenção do id passado como argumento na request
        userid = request.args.get('id')
        response = user_db_functions.get_user_by_id(userid)
        return response
    else:
        return abort(404)


@app.route('/api/v1/deleteuserid', methods=['DELETE'])
def delete_user_by_id():
    if request.method == 'DELETE':
        userid = request.args.get('id')
        response = user_db_functions.delete_user_by_id(int(userid))
        return response
    else:
        return abort(404)