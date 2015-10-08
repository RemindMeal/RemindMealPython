from app import db

class Mark(db.Model):
    """Entity Mark"""

    __tablename__ = 'mark'

    id = db.Column(db.Integer, primary_key=True)

    value = db.Column(db.SMALLINT, unique=True)
    description = db.Column(db.String(255))

    def __unicode__(self):
        return self.description
