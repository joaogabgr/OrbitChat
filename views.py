from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import Usuarios, Comentarios, Likes, Seguidor

def user():
    if 'user' not in session or session['user'] == None:
        return None
    else:
        return Usuarios.query.filter_by(email=session['user']).first()

@app.route('/')
def index():
    comentarios = Comentarios.query.filter_by(resposta=None).order_by(Comentarios.id.desc())
    return render_template('index.html', comentarios=comentarios, user=user(), like=Likes)

@app.route('/@<usuario>')
def perfil(usuario):
    if Usuarios.query.filter_by(usuario=usuario).first():
        usuario = Usuarios.query.filter_by(usuario=usuario).first()
    else:
        flash('Usuário não encontrado!')
        return redirect(url_for('index'))
    comentarios = Comentarios.query.filter_by(resposta=None, fk_usuario=usuario.usuario).order_by(Comentarios.id.desc())
    respostas = Comentarios.query.filter(
    Comentarios.resposta.isnot(None),
    Comentarios.fk_usuario == usuario.usuario
    ).order_by(Comentarios.id.desc()).all()
    action = request.args.get('action')
    return render_template('perfil.html', action=action, respostas=respostas, comentarios=comentarios, user=user(), usuario=usuario, like=Likes, seguidor=Seguidor)

@app.route('/!<id>')
def comentario(id):
    comentario = Comentarios.query.filter_by(id=id).first()
    respostas = Comentarios.query.filter_by(resposta=id).order_by(Comentarios.id.desc())
    return render_template('comentario.html', comentario=comentario, respostas=respostas, user=user(), like=Likes)

@app.route('/explorar', methods=['GET', 'POST'])
def explorar():
    if 'pesquisa' in request.form:
        session['pesquisa'] = request.form['pesquisa']
    else:
        session['pesquisa'] = ''
    usuarios = Usuarios.query.filter(Usuarios.usuario.like(f"%{session['pesquisa']}%")).all()
    comentarios = Comentarios.query.filter(Comentarios.comentario.like(f"%{session['pesquisa']}%")).all()
    return render_template('explorar.html', user=user(), pesquisa=session['pesquisa'], usuarios=usuarios, comentarios=comentarios, like=Likes)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', user=user()), 404
    