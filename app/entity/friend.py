import datetime
from app import db

class Friend(db.Model):
    """Entity Friend"""

    __tablename__ = 'friend'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(),
                     server_default=db.text('CURRENT_TIMESTAMP'))
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='friends')

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
