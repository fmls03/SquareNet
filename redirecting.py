from flask import session, redirect


from app import app


@app.route('/redirecting')
def redirecting():
    if not session.get('logged_in'):
        return redirect('/signup')
    else:
        return redirect('/Home')