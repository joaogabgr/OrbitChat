from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import Usuarios

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/explorar')
def explorar():
    return render_template('explorar.html')

@app.route('/autenticar')
def autenticar():
    action = request.args.get('action')
    return render_template('autenticar.html', action=action)

@app.route('/cadastrar', methods=['POST',])
def cadastrar():
    email = request.form['email']
    nome = request.form['nome']
    senha = request.form['password']
    confSenha = request.form['password1']

    if senha != confSenha:
        flash('As senhas não são iguais!')
        return redirect(url_for('autenticar', action='Cadastrar'))
    
    if Usuarios.query.filter_by(email=email).first():
        flash('O email utilizado já esta em uso!')
        return redirect(url_for('autenticar', action='Cadastrar'))

    user = Usuarios(email=email, nome=nome, senha=senha)
    db.session.add(user)
    db.session.commit()

    flash('Conta criada com sucesso')
    return redirect(url_for('index'))

