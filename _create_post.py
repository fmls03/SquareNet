from flask import request, session, render_template, Blueprint
import datetime

createPost_bp = Blueprint('createPost', __name__)



@createPost_bp.route('/createPost', methods=['GET', 'POST'])
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