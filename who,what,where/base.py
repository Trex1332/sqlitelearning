import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite') #sets up db locatin
app.config['SQLALCHEMY_TRACK_MODIFICATONS']= False

db = SQLAlchemy(app)

class whowhatwhere(db.Model):
    