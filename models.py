from app import db
from sqlalchemy.sql import func

class Usuarios(db.Model):
    email = db.Column(db.String, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    usuario = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), default='Sem descrição')

class Comentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_id = db.Column(db.Integer, nullable=False)
    fk_nome = db.Column(db.String(255), nullable=False)
    comentario = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=func.now())