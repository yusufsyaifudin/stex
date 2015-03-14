# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db


# Define a User model
class User(db.Model):
    __tablename__ = 'account'

    # User Name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),  nullable=False)
    description = db.Column(db.Unicode(200))

    # New instance instantiation procedure
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % (self.name)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
            }
