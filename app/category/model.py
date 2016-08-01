import datetime as dt

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, text
from sqlalchemy.orm import relationship

from app import db


class Category(db.Model):
    """Entity Category"""

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=dt.datetime.now(), server_default=text('CURRENT_TIMESTAMP'))
    name = Column(String(255), nullable=False, unique=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='categories')

    def __str__(self):
        return self.name
