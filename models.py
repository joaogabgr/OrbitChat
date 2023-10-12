from app import db
from sqlalchemy.sql import func

class Usuarios(db.Model):
    email = db.Column(db.String(255), primary_key=True)
    id = db.Column(db.INTEGER, nullable=False, index=True)
    nome = db.Column(db.String(255), nullable=False)
    usuario = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), default='Sem descrição')
    qtd_seguidores = db.Column(db.Integer, default=0)
    qtd_seguindo = db.Column(db.Integer, default=0)

class Comentarios(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, index=True)
    fk_id = db.Column(db.Integer, nullable=False)
    fk_nome = db.Column(db.String(255), nullable=False)
    fk_usuario = db.Column(db.String(15), nullable=False)
    resposta = db.Column(db.Integer, nullable=True)
    qtd_respostas = db.Column(db.Integer, default=0)
    qtd_likes = db.Column(db.Integer, default=0)
    comentario = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=func.now())

class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    tweet_id = db.Column(db.Integer, db.ForeignKey('comentarios.id'), nullable=False)

class Seguidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(255), db.ForeignKey('usuarios.email'), nullable=False)
    fk_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
