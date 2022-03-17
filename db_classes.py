from app import db

class Users(db.Model):
    email = db.Column(db.String(255), unique = True)
    username = db.Column(db.String(255), unique = True)
    passw = db.Column(db.String(255))
    id_acc = db.Column(db.Integer, primary_key = True) 

    def __init__(self, email, username, passw):
        self.email = email
        self.username = username
        self.passw = passw


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    insertTime = db.Column(db.DateTime)
    likes = db.Column(db.Integer)
    id_acc = db.Column(db.Integer)

    def __init__(self, title, description, insertTime, likes):
        self.title = title
        self.description = description
        self.insertTime = insertTime
        self.likes = likes
