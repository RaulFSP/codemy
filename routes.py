from flask import render_template, redirect, url_for
from app import app, db
from forms import UserForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:name>')
def name(name):
    return f"{name} vc clicou no form"

@app.route('/name', methods=['POST','GET'])
def user():
    form = UserForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
        return redirect(url_for('name', name=name))
    else:
        return render_template('user.html', form=form)


@app.errorhandler(404)
def error_404(e):
    return "Página não encontrada"
