from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import Usuarios, Seguidor

def user():
    if 'user' not in session or session['user'] == None:
        return None
    else:
        return Usuarios.query.filter_by(email=session['user']).first()

@app.route('/seguir/<usuario>', methods=['POST', 'GET'])
def seguir(usuario):
    seguir = Usuarios.query.filter_by(usuario=usuario).first()
    usuario = user()
    if seguir == None:
        flash('Usuário não encontrado!')
        return redirect(url_for('index'))
    if usuario == None:
        flash('Você precisa estar logado para seguir!')
        return redirect(url_for('index'))
    if usuario.id == seguir.id:
        flash('Você não pode seguir a si mesmo!')
        return redirect(url_for('index'))
    if Seguidor.query.filter_by(user_email=usuario.email, fk_id=seguir.id).first():
        flash('Você já segue esse usuário!')
        return redirect(url_for('index'))
    else:
        seguidor = Seguidor(user_email=usuario.email, fk_id=seguir.id)
        seguir.qtd_seguidores += 1
        usuario.qtd_seguindo += 1
    db.session.add(usuario)
    db.session.add(seguidor)
    db.session.commit()
    return 'None'

@app.route('/deseguir/<usuario>', methods=['POST', 'GET'])
def deseguir(usuario):
    deseguir = Usuarios.query.filter_by(usuario=usuario).first()
    usuario = user()
    if usuario == None:
        flash('Usuário não encontrado!')
        return redirect(url_for('index'))
    if usuario == None:
        flash('Você precisa estar logado para deseguir!')
        return redirect(url_for('index'))
    if usuario.id == deseguir.id:
        flash('Você não pode deseguir a si mesmo!')
        return redirect(url_for('index'))
    if Seguidor.query.filter_by(user_email=usuario.email, fk_id=deseguir.id).first():
        seguidor = Seguidor.query.filter_by(user_email=usuario.email, fk_id=deseguir.id).first()
        deseguir.qtd_seguidores -= 1
        usuario.qtd_seguindo -= 1
        db.session.delete(seguidor)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        flash('Você não segue esse usuário!')
        return redirect(url_for('index'))
    
# EDITAR PERFIL

@app.route('/atualizarPerfil', methods=['POST'])
def atualizarPerfil():
    usuario = user()
    
    idUsuario = request.form['idUsuario']
    if request.files['banner'].filename != '':
        banner = request.files['banner']
        banner.save(f'static/uploads/banner{idUsuario}.jpg')
        usuario.banner = f'static/uploads/banner{idUsuario}.jpg'
    
    if request.files['perfil'].filename != '':
        perfil = request.files['perfil']
        perfil.save(f'static/uploads/perfil{idUsuario}.jpg')
        usuario.perfil = f'static/uploads/perfil{idUsuario}.jpg'

    usuario.nome = request.form['name']
    usuario.descricao = request.form['descricao']
    db.session.commit()
    return redirect(url_for('perfil', usuario=usuario.usuario))