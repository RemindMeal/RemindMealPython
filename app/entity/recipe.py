import datetime
from app import db

class Recipe(db.Model):
    """Entity Recipe"""

    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(),
                     server_default=db.text('CURRENT_TIMESTAMP'))
    name = db.Column(db.String(255), nullable=False, unique=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='recipes')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='recipes')

    def __str__(self):
        return self.name
