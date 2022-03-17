from crypt import methods
import os 
from flask import Flask, render_template, redirect, request, session, flash, url_for
from passlib.hash import sha256_crypt
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *


from logout import logout


key = os.urandom(32)
key = str(key)

app = Flask(__name__) # Modulo flask
app.config['SECRET_KEY'] = key
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://fmls03:Schipilliti03!@localhost/SquareNet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    email = db.Column(db.String(255), unique = True)
    username = db.Column(db.String(255), unique = True)
    passw = db.Column(db.String(255))
    id_acc = db.Column(db.Integer, primary_key = True) 

    def __init__(self, email, username, passw):
        self.email = email
        self.username = username
        self.passw = passw


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    insertTime = db.Column(db.DateTime)
    likes = db.Column(db.Integer)
    id_acc = db.Column(db.Integer)

    def __init__(self, title, description, insertTime, likes):
        self.title = title
        self.description = description
        self.insertTime = insertTime
        self.likes = likes


if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
    logout()
