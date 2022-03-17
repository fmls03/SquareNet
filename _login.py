from sqlalchemy import *
from passlib.hash import sha256_crypt
from flask import session, request, render_template


from _app import bp
from _db_classes import Users
from _logout import logout
from _redirecting import redirecting



@bp.route('/login', methods=["GET", "POST"])
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
                    return redirecting()
                    
            else:
                alert = "* WRONG CREDENTIALS *"
    return render_template('auth/login.html', alert=alert)
