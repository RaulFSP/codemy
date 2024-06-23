from flask import render_template, redirect, url_for, flash
from app import app, db
from forms import UserForm, PassowordForm
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash
#==============================================================


#para o hash da senha
#==============================================================
@property
def password(self):
    raise AttributeError("Password not readable!")
@password.setter
def password(self,password):
    self.password_hash = generate_password_hash(password)
def verify_password(self, password):
    return check_password_hash(self.password_hash,password)
#==============================================================



@app.route('/')
def index():
    
    return render_template('index.html')




# Rotas do Usuário
#==============================================================
@app.route('/user', methods=['POST','GET'])
def user():
    form = UserForm()
    nome = None
    email = None
    color = None
    password_hash = None
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        color = form.color.data
        password_hash = generate_password_hash(form.password_hash.data, method='pbkdf2:sha256')
        user = UserModel(nome=nome,email=email, color=color, password_hash=password_hash)
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
    color = user.color
    if form.validate_on_submit():
        user.nome = form.nome.data
        user.email = form.email.data
        user.color = form.color.data
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
#==============================================================





#Rota de Login
#==============================================================
@app.route('/testeSenha', methods=['POST','GET'])
def teste_senha():
    form = PassowordForm()
    email = None
    password = None
    pw_check = None
    passed = None
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        form = PassowordForm(formdata=None)
        pw_check = UserModel.query.filter_by(email=email).first_or_404()
        passed=check_password_hash(pw_check.password_hash,password)
    
    return render_template('teste_pw.html',form=form, email=email,password=password, pw_check=pw_check, passed=passed)


#==============================================================








#Rota de erro
#==============================================================
@app.errorhandler(404)
def error_404(e):
    return "Página não encontrada"
