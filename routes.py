from flask import render_template, redirect, url_for, flash
from app import app, db
from forms import UserForm
from models import UserModel

@app.route('/')
def index():
    
    return render_template('index.html')



@app.route('/user', methods=['POST','GET'])
def user():
    form = UserForm()
    nome = None
    email = None
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data 
        user = UserModel(nome=nome,email=email)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f"Usuário {user.nome} preencheu o formulario!")
            return redirect(url_for('user'))
        except Exception as e:
            return str(e)
    else:
        users = UserModel.query.order_by(UserModel.id).all()
        return render_template('user.html', form=form, users=users)


@app.route('/alterar/<int:id>', methods=['POST','GET'])
def alterar_usuario(id):
    form = UserForm()
    user = UserModel.query.get_or_404(id)
    nome = user.nome
    email = user.email
    if form.validate_on_submit():
        user.nome = form.nome.data
        user.email = form.email.data
        db.session.commit()
        flash(f"Usuário {user.nome} alterado!")
        return redirect(url_for('user'))
    else:
        return render_template('alterar_usuario.html',form=form, user=user)

@app.route('/desativar/<int:id>')
def desativar_usuario(id):
    user = UserModel.query.get_or_404(id)
    user.status = False
    db.session.commit()
    flash(f"Usuário {user.nome} foi desativado!")
    return redirect(url_for('user'))


@app.errorhandler(404)
def error_404(e):
    return "Página não encontrada"
