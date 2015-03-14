from flask import Flask, render_template # Import flask and template operators
from flask.ext.script import Manager, Command # Import flask script
from flask.ext.sqlalchemy import SQLAlchemy # Import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand # Import flask migrate
from app.commands import hellocommand  # Import commands module


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define command
Command = Command()

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
manager.add_command('hello', hellocommand.hellocommand)



# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable
import app.modules

