from flask import request, session, render_template
import datetime


from _app import app, db
from _db_classes import Posts
from _logout import logout
from _redirecting import redirecting
from _login import login


@app.route('/createPost', methods=['GET', 'POST'])
def createPost():
    if not session.get('logged_in'):
        return logout()
    else:
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            newPost = Posts(title, description, now, 0, login.id_acc)
            db.session.add(newPost)
            db.session.commit()

            return redirecting()
    return render_template('createPost.html')