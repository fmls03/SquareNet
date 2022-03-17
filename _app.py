import os 
from flask import Flask, Blueprint, g, redirect, session
from flask_sqlalchemy import SQLAlchemy


import _routes

key = os.urandom(256)
key = str(key)

app = Flask(__name__) # Modulo flask
app.config['SECRET_KEY'] = key
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://fmlspi:Schipilliti03!@192.168.1.57/SquareNet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')



if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
