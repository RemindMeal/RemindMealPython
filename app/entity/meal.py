import datetime
from app import db
from .cooking import Cooking
from .participation import Participation


class Meal(db.Model):
    """Entity Meal"""

    __tablename__ = 'meal'

    id = db.Column('id', db.Integer, primary_key=True)
    date = db.Column('date', db.Date, nullable=False, default=datetime.date.today(),
                     server_default=db.text('CURRENT_TIMESTAMP'))

    friends = db.relationship('Friend', secondary=Participation, backref="meals")
    recipes = db.relationship('Recipe', secondary=Cooking, backref="meals")

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")
