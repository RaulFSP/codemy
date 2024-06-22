from flask import render_template, redirect, url_for, flash
from app import app, db
from forms import UserForm
from models import UserModel

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/<string:name>')
def name(name):
    return f"{name} vc clicou no form"

@app.route('/name', methods=['POST','GET'])
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


@app.errorhandler(404)
def error_404(e):
    return "Página não encontrada"
