from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
database = SQLAlchemy(app)

# importação das rotas
from routes import routes, userapiroute, bookapiroutes, userbookapiroutes

