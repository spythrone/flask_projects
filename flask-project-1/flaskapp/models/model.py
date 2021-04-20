import datetime
from flaskapp import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    data = db.Column(db.String(20), nullable=False)