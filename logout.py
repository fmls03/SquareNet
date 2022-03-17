from redirecting import redirecting
from flask import session


def logout():
    session['logged_in'] = False  
    session.clear()
    return redirecting()
