import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TACK_MIDIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class books(db.Model):
    
    __tabelname__ = "books"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    #one to many
    sources = db.relationship('source',backref = 'books',lazy='dynamic')
    #one to one
    owner = db.relationship('person',backref='books',uselist=False)

    def __init__(self,name)
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"book is {self.name}, the person with it is {self.owner.name}"
        else:
            return f"book is {self.name}. Has not been checked out."
        
    def report_source(self):
        print("the sources: ")
        for source in self.sources:
            print(source.name)

class source(db.Model):
    __tabelname__ = "source"

    id = db.Column(db.Integer,primary_key = True)
    sourcename = db.Column(db.Text)
    bookid = db.Column(db.Integer,db.Foreignkey('books.id'))

    def __init__(self,sourename,bookid):
        self.sourcename = sourename
        self.bookid = bookid
        

class person(db.Model):
    
    __tabelname__ = 'person'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    book_id = db.Colum(db.Integrt,db.Foreignkey('books.id'))

    def __init__(self,name,book_id):
        self.name = name
        self.book_id = book_id

