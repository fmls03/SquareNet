import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from logout import logout


key = os.urandom(32)
key = str(key)

app = Flask(__name__) # Modulo flask
app.config['SECRET_KEY'] = key
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://fmls03:Schipilliti03!@localhost/SquareNet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
    logout()
