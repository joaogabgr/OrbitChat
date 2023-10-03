from app import db

class Usuarios(db.Model):
    email = db.Column(db.String, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
