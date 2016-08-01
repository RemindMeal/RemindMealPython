from app import db
from flask_security import UserMixin, RoleMixin
from sqlalchemy import Table, Column, Integer, ForeignKey, String, Boolean, DateTime
from sqlalchemy.orm import relationship, backref

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
    password = Column(String(255))
    active = Column(Boolean)
    confirmed_at = Column(DateTime)

    roles = relationship('Role', secondary=roles_users, backref=backref('users', lazy='dynamic'))

    def __str__(self):
        return "{:s} {:s}".format(self.name, self.surname)
