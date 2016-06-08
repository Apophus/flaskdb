#!usr/bin/python

from flask import Flask
from flask_sqlalcchemy import SQLAlchemy

#instantiate the app
app = Flask(__name__)
#the uri just shows where the database is and the string has username and password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/mydatabase'

#instantiate a db object with  SQLAlchemy and pass the app as it's argument
db = SQLAlchemy(app)

#create the db model aka how you want it to look like
class Example(db.model):
    __tablename__ = 'example' #name of table
#define the columns
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)
