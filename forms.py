from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length
from datetime import datetime

class UserForm(FlaskForm):
    nome = StringField(label="Enter your name", validators=[DataRequired(),Length(min=3,max=60)])
    email = StringField(label="Enter your email",validators=[DataRequired(),Length(min=7)])
    submit = SubmitField(label="Submit")