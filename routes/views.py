from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from models import Usuarios, Comentarios, Likes, Seguidor
from sqlalchemy import union


def user():
    if 'user' not in session or session['user'] == None:
        return None
    else:
        return Usuarios.query.filter_by(email=session['user']).first()

@app.route('/')
def index():
    action = request.args.get('action')
    usuario = user()
    comentarios = Comentarios.query.filter_by(resposta=None).order_by(Comentarios.id.desc())
    if usuario != None:
        # Consulta 1: Comentarios dos seguidores
        # Obter todos os seguidores do usuário
        seguidores = Seguidor.query.filter_by(fk_seguidor=usuario.id).all()

        # Extrair os IDs dos seguidores
        follower_ids = [seguidor.fk_seguindo for seguidor in seguidores]

        # Filtrar os comentários
        filtro = Comentarios.query.filter(
            Comentarios.fk_id.in_(follower_ids),
            Comentarios.resposta.is_(None)
        )

        # Consulta 2: Comentarios do usuário
        filtroADD = Comentarios.query.filter_by(fk_id=usuario.id, resposta=None)

        # Combinação de resultados, remoção de duplicatas e ordenação por id
        seguidoresComentarios = sorted(set(filtro.union(filtroADD)), key=lambda x: x.id, reverse=True)

        return render_template('index.html', comentarios=comentarios, seguidoresComentarios=seguidoresComentarios, user=user(), like=Likes, comentar=Comentarios, action=action)
    return render_template('index.html', comentarios=comentarios, user=user(), like=Likes, action=action, comentar=Comentarios)

@app.route('/@<usuario>')
def perfil(usuario):
    if Usuarios.query.filter_by(usuario=usuario).first():
        usuario = Usuarios.query.filter_by(usuario=usuario).first()
    else:
        flash('Usuário não encontrado!')
        return redirect(url_for('index'))
    seguidores = len(Seguidor.query.filter_by(fk_seguindo=usuario.id).all())
    seguindo = len(Seguidor.query.filter_by(fk_seguidor=usuario.id).all())

    comentarios = Comentarios.query.filter_by(resposta=None, fk_id=usuario.id).order_by(Comentarios.id.desc())
    respostas = Comentarios.query.filter(
    Comentarios.resposta.isnot(None),
    Comentarios.fk_usuario == usuario.usuario
    ).order_by(Comentarios.id.desc()).all()

    midias = Comentarios.query.filter(
        Comentarios.imagem.isnot(None),
        Comentarios.fk_usuario == usuario.usuario
    ).order_by(Comentarios.id.desc()).all()

    action = request.args.get('action')
    return render_template('perfil.html', action=action, midias=midias, respostas=respostas, comentarios=comentarios, user=user(), usuario=usuario, like=Likes, seguidor=Seguidor, comentar=Comentarios,seguidores=seguidores, seguindo=seguindo)

@app.route('/!<id>')
def comentario(id):
    comentario = Comentarios.query.filter_by(id=id).first()
    respostas = Comentarios.query.filter_by(resposta=id).order_by(Comentarios.id.desc())
    return render_template('comentario.html', comentario=comentario, respostas=respostas, user=user(), like=Likes, comentar=Comentarios)

@app.route('/explorar', methods=['GET', 'POST'])
def explorar():
    if 'user' not in session or session['user'] == None:
        return redirect(url_for('autenticar'))
    
    session['pesquisa'] = request.args.get('pesquisa')

    usuarios = Usuarios.query.filter(Usuarios.usuario.like(f"%{session['pesquisa']}%")).all()
    comentarios = Comentarios.query.filter(Comentarios.comentario.like(f"%{session['pesquisa']}%")).order_by(Comentarios.id.desc()).all()
    return render_template('explorar.html', user=user(), pesquisa=session['pesquisa'], usuarios=usuarios, comentarios=comentarios, like=Likes, comentar=Comentarios)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', user=user()), 404
    