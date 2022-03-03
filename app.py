from crypt import methods
import os 
from flask import Flask, render_template, redirect, request, session, flash, url_for
from passlib.hash import sha256_crypt
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

key = os.urandom(32)
key = str(key)

app = Flask(__name__) # Modulo flask
app.config['SECRET_KEY'] = key
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://fmls03:Schipilliti03!@93.45.81.217/SquareNet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

id_acc = ""

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




app.route('/')
def logout():
    session['logged_in'] = False  
    session.clear()
    return redirecting()



@app.route('/redirecting')
def redirecting():
    if not session.get('logged_in'):
        return redirect('/signup')
    else:
        return redirect('/Home')



@app.route('/signup', methods=["GET", "POST"])
def signup():
    global id_acc
    logout()
    alert = ""
    if request.method == 'POST':
        email = str(request.form['email'])
        username = str(request.form['username'])  
        passw= str(request.form['passw'])
        confirm_passw = str(request.form['confirm_passw'])
        users = Users.query.all()
        err = 0
        for user in users:
            if (username == user.username):
                alert = ("*USERNAME ALREADY USED*")   
                err += 1           
            elif (email == user.email):
                alert = ("*ACCOUNT ALREADY EXISTS*")
                err += 1
            elif (len(passw) < 8 or any(map(str.isdigit, passw)) == False):
                alert = ("* USE AT LEAST 8 CHARACTERS AND 1 NUMBER *")
                err += 1
            elif (passw != confirm_passw):
                alert = ("*CONFIRM THE RIGHT PASSWORD*")
                err += 1

        if err == 0:
            session['logged_in'] = True 
            passw = sha256_crypt.hash(passw)
            u = Users(email, username, passw)
            db.session.add(u)
            db.session.commit()
                
            return redirecting()
                
                
    return render_template("signup.html", alert=alert, session=session)



@app.route('/login', methods=["GET", "POST"])
def login():
    logout()
    global id_acc
    alert = ""
    if request.method == 'POST':
        username = str(request.form['username'])
        passw = str(request.form['passw'])    
        users = Users.query.all()
        for user in users:
            if username == user.username:
                if sha256_crypt.verify(passw, user.passw):
                    session['logged_in'] = True
                    return redirecting()
            else:
                alert = "* WRONG CREDENTIALS *"

    return render_template("login.html", alert=alert, session=session)



@app.route('/Home')
def Home():
    if not session.get('logged_in'):
        return logout()
    else:
        posts = db.engine.execute("SELECT * FROM posts")
        for post in posts:
            username = db.engine.execute("SELECT username FROM users WHERE id_acc = :val", {'val' : post.id_acc})

    return render_template('home.html', post = post, username = username)    



@app.route('/createPost', methods=['GET', 'POST'])
def createPost():
    if not session.get('logged_in'):
        return logout()
    else:
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            newPost = Posts(title, description, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 0, id_acc)
            db.session.add(newPost)
            db.session.commit()

            return redirecting()
    return render_template('createPost.html')

if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
    logout()
