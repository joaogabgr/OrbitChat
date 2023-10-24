from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import Usuarios

def user():
    if 'user' not in session or session['user'] == None:
        return None
    else:
        return Usuarios.query.filter_by(email=session['user']).first()

@app.route('/autenticar')
def autenticar():
    action = request.args.get('action')
    return render_template('autenticar.html', action=action, user=user())

@app.route('/logar', methods=['POST',])
def logar():
    email = request.form['email']
    senha = request.form['password']

    if '@' in email:
        if not Usuarios.query.filter_by(email=email).first():
            flash('Email não cadastrado!')
            return redirect(url_for('autenticar', action='Cadastrar'))
        elif Usuarios.query.filter_by(email=email).first().senha != senha:
            flash('Senha incorreta!')
            return redirect(url_for('autenticar', action='Login'))
        else:
            session['user'] = email
            return redirect(url_for('index'))
    else:
        if not Usuarios.query.filter_by(usuario=email).first():
            flash('Email não cadastrado!')
            return redirect(url_for('autenticar', action='Cadastrar'))
        elif Usuarios.query.filter_by(usuario=email).first().senha != senha:
            flash('Senha incorreta!')
            return redirect(url_for('autenticar', action='Login'))
        else:
            session['user'] = Usuarios.query.filter_by(usuario=email).first().email
            return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session['user'] = None
    return redirect(url_for('index'))

@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    email = request.form['email']
    nome = request.form['nome']
    usuario = request.form['usuario']
    senha = request.form['password']
    confSenha = request.form['password1']

    if senha != confSenha:
        flash('As senhas não são iguais!')
        return redirect(url_for('autenticar', action='Cadastrar'))
    
    if Usuarios.query.filter_by(email=email).first():
        flash('O email utilizado já esta em uso!')
        return redirect(url_for('autenticar', action='Cadastrar'))
    
    if Usuarios.query.filter_by(usuario=usuario).first():
        flash('O nome de usuário já esta em uso!')
        return redirect(url_for('autenticar', action='Cadastrar'))

    user = Usuarios(email=email, nome=nome, usuario=usuario, senha=senha)
    db.session.add(user)
    db.session.commit()

    session['user'] = email
    flash('Conta criada com sucesso')
    return redirect(url_for('index'))