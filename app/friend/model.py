import datetime as dt

from app import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, text
from sqlalchemy.orm import relationship


class Friend(db.Model):
    """Entity Friend"""

    __tablename__ = 'friend'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=dt.datetime.now(), server_default=text('CURRENT_TIMESTAMP'))
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='friends')

    def __unicode__(self):
        return u"{:s} {:s}".format(self.name, self.surname)

    @property
    def recipes(self):
        array = []
        for meal in self.meals:
            for recipe in meal.recipes:
                if recipe not in array:
                    array.append(recipe)
        return array
