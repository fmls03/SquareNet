from flask import session, redirect


from _app import app


@app.route('/redirecting')
def redirecting():
    if not session.get('logged_in'):
        return redirect('/signup')
    else:
        return redirect('/Home')