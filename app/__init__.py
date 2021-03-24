from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object(Config)
#app.config['SECRET_KEY']= 'MY$50@s!xpm'
#app.config['SQLALCHEMY_DATABASE_URL']='postgreql://username:password@localhost/database'
#app.config['SQLALCHEMY_TRACK_MODIFICATTIONS']=True

db=SQLAlchemy(app)

app.config.from_object(Config)
from app import views