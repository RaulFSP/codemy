from app import db
from sqlalchemy import Integer, String, Date, Text, Boolean, DateTime
from sqlalchemy.orm import mapped_column
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class UserModel(db.Model):
    id = mapped_column(Integer,autoincrement=True,primary_key=True)
    nome = mapped_column(String(60), nullable=False)
    email = mapped_column(Text,nullable=False)
    color = mapped_column(String(30), nullable=False)
    data = mapped_column(Date,default=datetime.now())
    status = mapped_column(Boolean, default=True)
    password_hash = mapped_column(String(128), nullable=False)
    @property
    def password(self):
        raise AttributeError("Password not readable!")
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)
    
class PostModel(db.Model):
    id = mapped_column(Integer, primary_key=True,autoincrement=True)
    title = mapped_column(String(255))
    content = mapped_column(Text)
    author = mapped_column(String(255))
    date_posted = mapped_column(DateTime, default=datetime.now(timezone.utc))
    slug = mapped_column(String(255))
    