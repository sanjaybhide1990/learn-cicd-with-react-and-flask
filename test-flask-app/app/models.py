# Database schemas

from . import db

class TestDB(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120),nullable=False,unique=True)
