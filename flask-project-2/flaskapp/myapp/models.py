import datetime

from flaskapp import db

class Myuser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    content = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"User(Username -> {self.username} , Content -> {self.content})"