import os 
from flask import Flask, session, redirect
from flask_sqlalchemy import SQLAlchemy

from _auth import *
from _create_post import *
from _home import *
from _redirecting import *


key = os.urandom(256)
key = str(key)

app = Flask(__name__) # Modulo flask
app.config['SECRET_KEY'] = key
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://fmlspi:Schipilliti03!@192.168.1.57/SquareNet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(auth_bp)
app.register_blueprint(createPost_bp)
app.register_blueprint(redirecting_bp)
app.register_blueprint(home_bp)

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
