from flask import Blueprint, redirect, session, render_template, request
from sqlalchemy import *
from passlib.hash import sha256_crypt

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
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
                
            return redirect("/")
                
                
    return render_template("signup.html", alert=alert, session=session)
    

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    logout()
    if request.method == 'POST':
        username = str(request.form['username'])
        passw = str(request.form['passw'])    
        users = Users.query.all()
        for user in users:
            if username == user.username:
                if sha256_crypt.verify(passw, user.passw):
                    session['logged_in'] = True
                    session['user_id'] = user.id_acc
                    session['user_username'] = user.username
                    return redirect("/")
                    
            else:
                alert = "* WRONG CREDENTIALS *"
    return render_template('auth/login.html', alert=alert)


@auth_bp.route('/logout')
def logout():
    session['logged_in'] = False  
    session.clear()
    return redirect("/")