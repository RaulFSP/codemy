from flask import render_template, redirect, url_for, flash
from app import app, db
from forms import UserForm, PassowordForm, PostForm
from models import UserModel, PostModel
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

@app.route('/add_post', methods=['POST','GET'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = PostModel(
            title=form.title.data,
            content=form.content.data,
            author=form.author.data,
            slug = form.slug.data
        )
        form = PostForm(formdata=None)
        db.session.add(post)
        db.session.commit()
        flash('Postagem criada!')
        return redirect(url_for('add_post'))
    else:
        return render_template('add_post.html',form=form)

@app.route('/posts')
def posts():
    posts = PostModel.query.order_by(PostModel.id).all()
    return render_template('posts.html',posts=posts)

@app.route('/vizualizar_postagem/<int:id>')
def vizualizar_postagem(id):
    post = PostModel.query.get_or_404(id)
    return render_template('postagem.html',post=post)



#Rota de erro
#==============================================================
@app.errorhandler(404)
def error_404(e):
    return "Página não encontrada"
