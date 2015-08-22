import datetime
from app import db

class Category(db.Model):
    """Entity Category"""

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(),
                     server_default=db.text('CURRENT_TIMESTAMP'))
    name = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return u"".format(self.name)
