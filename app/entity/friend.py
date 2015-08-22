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

    def __str__(self):
        return u"{:s} {:s}".format(self.name, self.surname)
