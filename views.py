from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import Usuarios, Comentarios, Like

def user():
    if 'user' not in session or session['user'] == None:
        return None
    else:
        return Usuarios.query.filter_by(email=session['user']).first()

@app.route('/')
def index():
    comentarios = Comentarios.query.filter_by(resposta=None).order_by(Comentarios.id.desc())
    return render_template('index.html', comentarios=comentarios, user=user(), like=Like)

@app.route('/@<usuario>')
def perfil(usuario):
    if Usuarios.query.filter_by(usuario=usuario).first():
        usuario = Usuarios.query.filter_by(usuario=usuario).first()
    else:
        flash('Usuário não encontrado!')
        return redirect(url_for('index'))
    comentarios = Comentarios.query.filter_by(resposta=None).order_by(Comentarios.id.desc())
    respostas = Comentarios.query.filter(Comentarios.resposta.isnot(None)).order_by(Comentarios.id.desc()).all()
    action = request.args.get('action')
    return render_template('perfil.html', action=action, respostas=respostas, comentarios=comentarios, user=usuario, like=Like)

@app.route('/!<id>')
def comentario(id):
    comentario = Comentarios.query.filter_by(id=id).first()
    respostas = Comentarios.query.filter_by(resposta=id).order_by(Comentarios.id.desc())
    return render_template('comentario.html', comentario=comentario, respostas=respostas, user=user(), like=Like)

@app.route('/explorar', methods=['GET', 'POST'])
def explorar():
    if 'pesquisa' in request.form:
        pesquisa = request.form['pesquisa']
    else:
        pesquisa = ''
    usuarios = Usuarios.query.filter(Usuarios.usuario.like(f"%{pesquisa}%")).all()
    comentarios = Comentarios.query.filter(Comentarios.comentario.like(f"%{pesquisa}%")).all()
    return render_template('explorar.html', user=user(), pesquisa=pesquisa, usuarios=usuarios, comentarios=comentarios, like=Like)
    