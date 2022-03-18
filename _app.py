import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import _db_classes
import routes

key = os.urandom(256)
key = str(key)

app = Flask(__name__) # Modulo flask
app.config['SECRET_KEY'] = key
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://fmlspi:Schipilliti03!@192.168.1.57/SquareNet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(auth_bp)

db = SQLAlchemy(app)

@app.route('/')
def func():
    return "hey"


if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
