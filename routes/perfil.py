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
        return redirect(url_for('index'))
    if usuario == None:
        return redirect(url_for('index'))
    if usuario.id == seguir.id:
        return redirect(url_for('index'))
    if Seguidor.query.filter_by(fk_seguidor=usuario.id, fk_seguindo=seguir.id).first():
        return redirect(url_for('index'))
    else:
        seguidor = Seguidor(fk_seguidor=usuario.id, fk_seguindo=seguir.id)
    db.session.add(usuario)
    db.session.add(seguidor)
    db.session.commit()
    return 'None'

@app.route('/deseguir/<usuario>', methods=['POST', 'GET'])
def deseguir(usuario):
    deseguir = Usuarios.query.filter_by(usuario=usuario).first()
    usuario = user()
    if usuario == None:
        return redirect(url_for('index'))
    if usuario == None:
        return redirect(url_for('index'))
    if usuario.id == deseguir.id:
        return redirect(url_for('index'))
    if Seguidor.query.filter_by(fk_seguidor=usuario.id, fk_seguindo=deseguir.id).first():
        seguidor = Seguidor.query.filter_by(fk_seguidor=usuario.id, fk_seguindo=deseguir.id).first()
        db.session.delete(seguidor)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('index'))
    else:
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
    usuario.profissao = request.form['profissao']
    db.session.commit()
    return redirect(url_for('perfil', usuario=usuario.usuario))