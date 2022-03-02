import os 
from flask import Flask, render_template, redirect, request, session, flash, url_for
from forms import LoginForm
from passlib.hash import sha256_crypt
from datetime import date
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


key = os.urandom(32)
key = str(key)

app = Flask(__name__) # Modulo flask
app.config['SECRET_KEY'] = key
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://fmls03:Schipilliti03!@localhost/squarenetProva'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#modello
class User(db.model):
    email = db.Column(db.String(255), unique = True)
    username = db.Column(db.String(255), unique = True)
    passw = db.Column(db.String(255))
    id_acc = db.Column(db.Integer, primary_key = True) 

    def __init__(self, email, username, passw):
        self.email = email
        self.username = username
        self.passw = passw
    

@app.route('/')
def index():
    return render_template('index.html')    


@app.route('/login' , methods = ['GET', 'POST'])
def Login():
    form = LoginForm()
 
    if form.validate_on_submit():
        if request.form['username'] != 'codeloop' or request.form['password'] != '12345':
            flash("Invalid Credentials, Please Try Again")

        else:
            return redirect(url_for('index'))
 
    return render_template('login.html', form = form)
 

if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
