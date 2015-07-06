import datetime
from app import db

class Meal(db.Model):
    """Entity Meal"""

    __tablename__ = 'meal'

    id = db.Column('id', db.Integer, primary_key=True)
    date = db.Column('date', db.DateTime, nullable=False, default=datetime.date.today(),
                     server_default=db.text('CURRENT_TIMESTAMP'))

    def __str__(self):
        return self.date.format("%d/%m/%Y")
