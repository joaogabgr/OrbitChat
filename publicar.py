from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import Usuarios, Comentarios

def user():
    if 'user' not in session or session['user'] == None:
        return None
    else:
        return Usuarios.query.filter_by(email=session['user']).first()

@app.route('/publicar', methods=['POST',])
def publicar():
    usuario = user()
    if usuario == None:
        flash('Você precisa estar logado para publicar!')
        return redirect(url_for('index'))
    publicacao = request.form['publicacao']
    comentario = Comentarios(comentario=publicacao, fk_id=usuario.id, fk_nome=usuario.nome)
    db.session.add(comentario)
    db.session.commit()
    flash('Publicação realizada com sucesso!')
    return redirect(url_for('index'))


# EDITAR PERFIL

@app.route('/atualizarPerfil', methods=['POST'])
def atualizarPerfil():
    usuario = user()
    usuario.nome = request.form['name']
    usuario.descricao = request.form['descricao']
    db.session.commit()
    return redirect(url_for('perfil', usuario=usuario.usuario))