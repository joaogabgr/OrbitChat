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

@app.route('/explorar', methods=['GET', 'POST'])
def explorar():
    if 'pesquisa' in request.form:
        pesquisa = request.form['pesquisa']
    else:
        pesquisa = ''
    usuarios = Usuarios.query.filter(Usuarios.usuario.like(f"%{pesquisa}%")).all()
    comentarios = Comentarios.query.filter(Comentarios.comentario.like(f"%{pesquisa}%")).all()
    print(comentarios)
    return render_template('explorar.html', user=user(), pesquisa=pesquisa, usuarios=usuarios, comentarios=comentarios)
    