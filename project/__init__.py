from flask import Flask
from flask_sqlalchemy import SQLAlchemy


"""
O Arquivo inicial do projeto __init__.py é onde instanciamos o Flask, o endereço do banco de dados
Outras funcionalidades como login manager 
E Iniciamos as rotas do aplicativo
"""

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

database = SQLAlchemy(app)



from project import routes

