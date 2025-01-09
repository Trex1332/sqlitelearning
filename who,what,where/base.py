import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite') #sets up db locatin
app.config['SQLALCHEMY_TRACK_MODIFICATONS']= False

db = SQLAlchemy(app)

Migrate(app,db)

class whowhatwhere(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    game = db.Column(db.Text)
    character = db.Column(db.Text)

    def __init__(self,name,game,character):
        self.name = name
        self.game = game
        self.character = character

    def __repr__(self):
        return f"Name is {self.name}, Their Favorite character is from {self.game}, the character is {self.character}"