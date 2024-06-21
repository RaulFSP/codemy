from flask import render_template, redirect, url_for
from app import app, db

@app.route('/')
def index():
    return "depois"

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def error_404(e):
    return "Página não encontrada"
