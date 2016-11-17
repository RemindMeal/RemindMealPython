from datetime import datetime, date

from flask_security import RoleMixin, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, SMALLINT, String, Table, Text, text
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()


class Friend(db.Model):
    """Entity Friend"""

    __tablename__ = 'friend'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now(), server_default=text('CURRENT_TIMESTAMP'))
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
    date = Column(Date, nullable=False, default=date.today(), server_default=text('CURRENT_DATE'))
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


class Mark(db.Model):
    """Entity Mark"""

    __tablename__ = 'mark'

    id = Column(Integer, primary_key=True)
    value = Column(SMALLINT, unique=True)
    description = Column(String(255))


class Category(db.Model):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    def __str__(self):
        return self.name


class Recipe(db.Model):
    """Entity Recipe"""

    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now(), server_default=text('CURRENT_TIMESTAMP'))
    name = Column(String(255), nullable=False, unique=True)
    reference = Column(String(255))
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    mark_id = Column(Integer, ForeignKey('mark.id'))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    category = relationship('Category')
    mark = relationship('Mark')
    user = relationship('User', backref='recipes')

    def __str__(self):
        return self.name

    @property
    def friends(self):
        return set(friend for meal in self.meals for friend in meal)


roles_users = Table(
    'role_user',
    db.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('role_id', Integer, ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(255))

    def __str__(self):
        return str(self.name)


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False)
    confirmed_at = Column(DateTime)

    roles = relationship('Role', secondary=roles_users, backref=backref('users', lazy='dynamic'))

    def __str__(self):
        return u"{:s} {:s}".format(self.name, self.surname)
