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

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='meals')

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")

    def __unicode__(self):
        return str(self)

    @property
    def categories(self):
        result = []
        for recipe in self.recipes:
            if recipe.category not in result:
                result.append(recipe.category)
        return result