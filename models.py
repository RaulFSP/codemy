from app import db
from sqlalchemy import Integer, String, Date, Text, Boolean
from sqlalchemy.orm import mapped_column
from datetime import datetime

class UserModel(db.Model):
    id = mapped_column(Integer,autoincrement=True,primary_key=True)
    nome = mapped_column(String(60), nullable=False)
    email = mapped_column(Text,nullable=False)
    data = mapped_column(Date,default=datetime.now())
    status = mapped_column(Boolean, default=True)