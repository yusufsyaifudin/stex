from flask import Flask  # Import flask and template operators
from flask.ext.script import Manager  # Import flask script
from flask.ext.sqlalchemy import SQLAlchemy  # Import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand  # Import flask migrate


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
# db.init_app(app)

# Define migrate object
migrate = Migrate(app, db)


# Define manager application object
manager = Manager(app)

# Register command(s)
manager.add_command('db', MigrateCommand)
import app.console as command  # Import commands module


# Import a module / component using its blueprint handler variable
import app.modules as modules
