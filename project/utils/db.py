from project import app, database
from project.models import User, Book, UserBook
from flask import jsonify

"""
Funções do banco de dados (usuário e livros)
Usadas nas rotas de api e nos testes
"""


class User_db_functions:

    def inserir_usuario_db(self, username, email, senha):
        with app.app_context():
            usuario = User(username=username, email=email, senha=senha)
            try:
                database.session.add(usuario)
                database.session.commit()
                print(f'Usuario {username} cadastrado com sucesso.')
                user = User.query.order_by(User.id.desc()).first()
                response = jsonify({f'Sucesso na inserção do usuário {user.username}': {'ID': user.id, 'email': user.senha, "Date": user.date_inserted}})
                return response
            except Exception as e:
                database.session.rollback()
                print(f'Erro: {e}')
                response = jsonify({'erro': 'Falha na inserção do usuário'})
                return response

    def get_users(self):
        with app.app_context():
            response_json = {}
            for usuario in User.query.all():
                print(f"Id: {usuario.id} Nome: {usuario.username} Email: {usuario.email}")
                response_json[f'ID: {usuario.id}'] = {
                    "Nome": usuario.username,
                    "Email": usuario.email,
                    "Date": usuario.date_inserted.strftime('%m/%d/%Y')
                }
            return response_json

    def get_user_by_id(self, id):
        with app.app_context():
            try:
                # query do id no banco de dados
                user = User.query.filter_by(id=id).first()
                return jsonify({f"Usuário com ID: {user.id}": {"User": user.username, "Email": user.email}})
            except IndexError:
                return jsonify({'error': 'Id não existe no banco de dados'})
            except AttributeError:
                return jsonify({'error': 'Id não existe no banco de dados'})
            except Exception as e:
                print(e)
                return jsonify({'error': 'erro desconhecido'})

    def delete_user_by_id(self, id):
        with app.app_context():
            try:
                print(id)
                user = User.query.filter_by(id=id).first()
                mensagem = jsonify({f"Usuário deletado com ID: {user.id}": {"User": user.username, "Email": user.email}})
                # para deletar
                database.session.delete(user)
                database.session.commit()
                return mensagem
            except IndexError:
                return jsonify({'error': 'Id não existe no banco de dados'})
            except AttributeError:
                return jsonify({'error': 'Id não existe no banco de dados'})
            except Exception as e:
                print(e)
                return jsonify({'error': 'erro desconhecido'})


class Book_db_functions:

    def book_insert(self, title, pages_qty):
        with app.app_context():
            livro = Book(title=title, pages_qty=pages_qty)
            try:
                database.session.add(livro)
                database.session.commit()
                print(f'Livro {title} cadastrado com sucesso.')
                livro = Book.query.order_by(Book.id.desc()).first()
                response = jsonify({f'Sucesso na inserção do usuário {livro.title}': {'ID': livro.id, 'email': livro.pages_qty, "Date": livro.date_inserted}})
                return response
            except Exception as e:
                database.session.rollback()
                print(f'Erro: {e}')
                response = jsonify({'erro': 'Falha na inserção do usuário'})
                return response

    def get_books(self):
        with app.app_context():
            response_json = {}
            for book in Book.query.all():
                print(f"Id: {book.id} Titulo: {book.title} Pages_qty: {book.pages_qty}")
                response_json[f'ID: {book.id}'] = {
                    "Titulo": book.title,
                    "Quantidade de paginas": book.pages_qty,
                    "Date": book.date_inserted.strftime('%m/%d/%Y')
                }
            return response_json

# todo quando tiver front-end vamos ter que dar uma query no nome do livro para obter o id
class User_book_db_functions:
    def reader_insert(self, book_id, user_id, current_page):
        with app.app_context():
            user = User.query.get(user_id)
            book = Book.query.get(book_id)

            total_pages = book.pages_qty

            if user is None or book is None:
                return jsonify({'erro': 'user or book not found'})

            if int(current_page) > int(total_pages):
                return jsonify({'erro': 'Pagina atual não pode ser maior que o total de paginas do livro em questao'})

            user_book = UserBook(user_id=user_id, book_id=book_id, current_page=current_page)
            try:
                database.session.add(user_book)
                database.session.commit()
                leitor = UserBook.query.order_by(UserBook.id.desc()).first()
                response = jsonify({f'Sucesso na inserção do leitor': leitor.id})
                return response
            except Exception as e:
                database.session.rollback()
                print(f'Erro: {e}')
                response = jsonify({'erro': 'Falha do leitor'})
                return response

