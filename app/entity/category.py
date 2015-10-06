import datetime
from app import db

class Category(db.Model):
    """Entity Category"""

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(),
                     server_default=db.text('CURRENT_TIMESTAMP'))
    name = db.Column(db.String(255), nullable=False, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='categories')

    def __str__(self):
        return self.name
