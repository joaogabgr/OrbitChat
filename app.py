from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *
from autenticar import *
from publicar import *
from perfil import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)