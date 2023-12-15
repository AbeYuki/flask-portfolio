from portfolio.app import db
from datetime import datetime


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255))
    user_email = db.Column(db.String(255))
    user_pass = db.Column(db.String(255))
    user_created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)