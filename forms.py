from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo
from datetime import datetime

class UserForm(FlaskForm):
    nome = StringField(label="Enter your name", validators=[DataRequired(),Length(min=3,max=60)])
    email = StringField(label="Enter your email",validators=[DataRequired(),Length(min=7)])
    color = StringField(label="Enter your favorite color",validators=[DataRequired(),Length(min=3,max=30)])
    password_hash = PasswordField(label="Password", validators=[DataRequired(),EqualTo('password_hash2',message="As senhas devem ser as mesmas!")])
    password_hash2 = PasswordField(label="Confirm password", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

class PassowordForm(FlaskForm):
    email = StringField(label="Enter your email",validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Submit")