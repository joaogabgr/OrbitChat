from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import Usuarios, Comentarios, Likes, Retweet

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
    comentario = Comentarios(comentario=publicacao, fk_id=usuario.id, fk_nome=usuario.nome, fk_usuario=usuario.usuario, fk_perfil=f'/static/uploads/perfil{usuario.id}.jpg')
    db.session.add(comentario)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/responder', methods=['POST',])
def responder():
    usuario = user()
    if usuario == None:
        flash('Você precisa estar logado para responder!')
        return redirect(url_for('index'))
    comentario = Comentarios(fk_id=usuario.id, fk_nome=usuario.nome, comentario=request.form['publicacao'], resposta=request.form['resposta'], fk_usuario=usuario.usuario, fk_perfil=f'/static/uploads/perfil{usuario.id}.jpg')
    publicacao = Comentarios.query.filter_by(id=request.form['resposta']).first()
    if publicacao.qtd_respostas is not None:
        publicacao.qtd_respostas += 1
    else:
        publicacao.qtd_respostas = 1
    db.session.add(publicacao)
    db.session.add(comentario)
    db.session.commit()
    return redirect(url_for('comentario', id=request.form['resposta']))


# CURTIR COMENTARIO

@app.route('/curtir/<id>', methods=['POST', 'GET'])
def curtir(id):
    usuario = user()
    if usuario == None:
        return redirect(url_for('index'))
    publicacao = Comentarios.query.filter_by(id=id).first()
    if Likes.query.filter_by(user_id=usuario.id, tweet_id=id).first():
        Likes.query.filter_by(user_id=usuario.id, tweet_id=id).delete()
        if publicacao.qtd_likes is not None:
            publicacao.qtd_likes -= 1
        else:
            publicacao.qtd_likes = 0
    else:
        likes = Likes(user_id=usuario.id, tweet_id=id)
        if publicacao.qtd_likes is not None:
            publicacao.qtd_likes += 1
        else:
            publicacao.qtd_likes = 1
        db.session.add(likes)
    db.session.commit()
    return 'None'

# RETWEETAR COMENTARIO

@app.route('/retweetar/<id>', methods=['POST', 'GET'])
def retweetar(id):
    usuario = user()
    if usuario == None:
        return redirect(url_for('index'))
    publicacao = Comentarios.query.filter_by(id=id).first()
    if Retweet.query.filter_by(fk_retweet=usuario.id, fk_comentarioID=id).first():
        Retweet.query.filter_by(fk_retweet=usuario.id, fk_comentarioID=id).delete()
        publicacao.qtd_retweets -= 1
    else:
        retweet = Retweet(fk_retweet=usuario.id, fk_comentarioID=id, fk_usuarioID=publicacao.fk_id)
        publicacao.qtd_retweets += 1
        db.session.add(retweet)
    db.session.commit()
    return 'None'