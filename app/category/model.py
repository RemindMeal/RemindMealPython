import datetime as dt

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, text, UniqueConstraint
from sqlalchemy.orm import relationship

from app import db


class Category(db.Model):
    """Entity Category"""

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=dt.datetime.now(), server_default=text('CURRENT_TIMESTAMP'))
    name = Column(String(255), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', backref='categories')

    __table_args__ = (
        UniqueConstraint('name', 'user_id'),
    )

    def __str__(self):
        return self.name
