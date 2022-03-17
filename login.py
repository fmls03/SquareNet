from sqlalchemy import *
from passlib.hash import sha256_crypt
from flask import session, request, render_template


from app import app, Users
from logout import logout
from redirecting import redirecting



@app.route('/login', methods=["GET", "POST"])
def login():
    logout()
    alert = ""
    if request.method == 'POST':
        username = str(request.form['username'])
        passw = str(request.form['passw'])    
        users = Users.query.all()
        for user in users:
            if username == user.username:
                if sha256_crypt.verify(passw, user.passw):
                    session['logged_in'] = True
                    id_acc = user.id_acc
                    return redirecting()
                    
            else:
                alert = "* WRONG CREDENTIALS *"

    return render_template("login.html", alert=alert, session=session), id_acc