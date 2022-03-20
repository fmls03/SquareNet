from flask import Blueprint, redirect, session

redirecting_bp = Blueprint('redirecting_bp', __name__)

@redirecting_bp.route('/')
def redirecting():
    if not session.get('logged_in'):
        return redirect('/signup')
    else:
        return redirect('/Home')

