from flask import session, render_template,Blueprint

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/Home')
def Home():
    if not session.get('logged_in'):
        return logout()
    else:
        posts = db.engine.execute("SELECT * FROM posts")
        for post in posts:
            username = db.engine.execute("SELECT username FROM users WHERE id_acc = :val", {'val' : post.id_acc})

    return render_template('home.html', post = post, username = username) 