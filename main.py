import os 
from flask import Flask, render_template, redirect, request, session
from passlib.hash import sha256_crypt
from datetime import date
import sqlite3
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

key = os.urandom(32)
key = str(key)

app = Flask(__name__) # Modulo flask
app.config['SECRET_KEY'] = key

email = ""
id_acc = ""
username = ""
passw = ""


@app.route('/')
def session_clear():
    logout()
    return Home()


@app.route('/Redirect')
def Home():
    if not session.get('logged_in'):
        return redirect('/signup')
    else:
        return redirect('/Home')


@app.route('/signup', methods=('GET', 'POST'))
def signin():


@app.route('/login', methods=('GET', 'POST'))
def login():
   

     
@app.route('/Home') # Home page della web app
def index():


@app.route('/<int:idx>/delete', methods=('POST',))
def delete(idx): #usiamo 'idx' perchè 'id' darebbe problemi
    if session.get('logged_in'):
        connection = sqlite3.connect('database.db')
        connection.row_factory = sqlite3.Row
        connection.execute('DELETE FROM posts WHERE id=?', (idx, ))
        connection.execute('UPDATE posts SET id = id - 1 WHERE id > ?', (idx, ))
        connection.commit()
        connection.close()
    else:
        return Home()
    return redirect('/Promemoria')


def logout():
    global username
    global email
    global passw
    global id_acc
    username = ""
    email = ""
    passw = ""
    id_acc = "" 
    session['logged_in'] = False  
    session.clear()
    return Home()


@app.route('/create', methods=('GET', 'POST'))
def create():
    if session.get('logged_in'):
        if request.method == 'POST':
            today = date.today()
            title = request.form['title']
            info = request.form['info']
            connection = sqlite3.connect('database.db')
            connection.row_factory = sqlite3.Row
            connection.execute('INSERT INTO posts (title, info, today, id_acc) VALUES (?, ?, ?, ?)', (title, info, today, id_acc))
            connection.commit()
            connection.close()
            return redirect('/Promemoria')
    else:
        return Home()
    return render_template('create.html')

if __name__ == "__main__":
    app.run("localhost", 5000, debug=True)
    session_clear()