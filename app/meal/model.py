import datetime as dt

from app import db
from sqlalchemy import Column, Table, Integer, ForeignKey, text, Date
from sqlalchemy.orm import relationship

Cooking = Table(
    'cooking',
    db.metadata,
    Column('recipe_id', Integer, ForeignKey('recipe.id'), primary_key=True),
    Column('meal_id', Integer, ForeignKey('meal.id'), primary_key=True))

Participation = Table(
    'participation',
    db.metadata,
    Column('friend_id', Integer, ForeignKey('friend.id'), primary_key=True),
    Column('meal_id', Integer, ForeignKey('meal.id'), primary_key=True))


class Meal(db.Model):
    """Entity Meal"""

    __tablename__ = 'meal'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, default=dt.date.today(), server_default=text('CURRENT_TIMESTAMP'))
    friends = relationship('Friend', secondary=Participation, backref="meals")
    recipes = relationship('Recipe', secondary=Cooking, backref="meals")

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='meals')

    def __str__(self):
        return "Repas du", self.date.strftime("%d/%m/%Y")

    @property
    def categories(self):
        result = []
        for recipe in self.recipes:
            if recipe.category not in result:
                result.append(recipe.category)
        return result