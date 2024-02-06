from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'  # Ajuste o nome do banco aqui
db = SQLAlchemy(app)

# As classes do modelo devem ser importadas depois da instanciação do db
from models import *

if __name__ == '__main__':
    app.run(debug=True)

