from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length

class UserForm(FlaskForm):
    name = StringField(label="Enter your name", validators=[DataRequired(),Length(min=3,max=60)])
    submit = SubmitField(label="Submit")