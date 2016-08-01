import datetime as dt
from app import db
from sqlalchemy import Column, Integer, text, DateTime, String, Text, ForeignKey, SMALLINT
from sqlalchemy.orm import relationship


class Mark(db.Model):
    """Entity Mark"""

    __tablename__ = 'mark'

    id = Column(Integer, primary_key=True)

    value = Column(SMALLINT, unique=True)
    description = Column(String(255))


class Recipe(db.Model):
    """Entity Recipe"""

    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=dt.datetime.now(), server_default=text('CURRENT_TIMESTAMP'))
    name = Column(String(255), nullable=False, unique=True)
    reference = Column(String(255))
    description = Column(Text)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', backref='recipes')

    mark_id = Column(Integer, ForeignKey('mark.id'))
    mark = relationship('Mark')

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='recipes')

    def __str__(self):
        return self.name

    @property
    def friends(self):
        return set(friend for meal in self.meals for friend in meal)
