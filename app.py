from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

from routes import *

if __name__ == "__main__":
    app.run(debug=True,port=5000,host="127.0.0.1")