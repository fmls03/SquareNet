from flask import request, session, render_template
from sqlalchemy import *
from passlib.hash import sha256_crypt


from _app import app, db
from _db_classes import Users
from _logout import logout
from _redirecting import redirecting


@app.route('/signup', methods=["GET", "POST"])
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
                
            return redirecting()
                
                
    return render_template("signup.html", alert=alert, session=session)