import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir =os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite') #sets up db locatin
app.config['SQLALCHEMY_TRACK_MODIFICATONS']= False

db = SQLAlchemy(app)

class character(db.Model):
    __tablename__ = 'character'


    id = db.Column(db.Interger,primary_key = True)
    name = db.Column(db.Text)
    characters = db.Column(db.Text)

    def __init__(self,name,characters):
        self.name = name
        self.characters = characters

    def __repr__(self):
        return f"name is {self.name}, character chosen is {self.characters} as there character"