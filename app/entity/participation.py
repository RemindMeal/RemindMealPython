from app import db

Participation = db.Table(
    'participation',
    db.Column('friend_id', db.Integer, db.ForeignKey('friend.id'), primary_key=True),
    db.Column('meal_id', db.Integer, db.ForeignKey('meal.id'), primary_key=True)
)
