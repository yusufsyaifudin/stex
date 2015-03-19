# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db


# Define a User model
class User(db.Model):
    __tablename__ = 'account'
    # __table_args__ = {'mysql_engine': 'InnoDB'}

    # User Name
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(60),  nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'name': self.name
            }

db.create_all()
