from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import Usuarios, Comentarios

def user():
    if 'user' not in session or session['user'] == None:
        return None
    else:
        return Usuarios.query.filter_by(email=session['user']).first()

@app.route('/')
def index():
    comentarios = Comentarios.query.order_by(Comentarios.id.desc())
    return render_template('index.html', comentarios=comentarios, user=user())

@app.route('/perfil')
def perfil():
    usuario = request.args.get('q')
    if Usuarios.query.filter_by(usuario=usuario).first():
        usuario = Usuarios.query.filter_by(usuario=usuario).first()
    else:
        flash('Usuário não encontrado!')
        return redirect(url_for('index'))
    comentarios = Comentarios.query.filter_by(fk_id=usuario.id).order_by(Comentarios.id.desc())
    return render_template('perfil.html', comentarios=comentarios, user=usuario)

@app.route('/explorar')
def explorar():
    usuarios = Usuarios.query.order_by(Usuarios.id).all()
    comentarios = Comentarios.query.order_by(Comentarios.id).all()
    return render_template('explorar.html', user=user(), usuarios=usuarios, comentarios=comentarios)
    