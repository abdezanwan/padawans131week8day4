from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)
jwt = JWTManager(app)

from app import routes
