# Statement for enabling the development environment
import os

DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLALCHEMY_DATABASE_URI = 'mysql://root:mydb_pwd@localhost:3306/mydb'
SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/flask'
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_ECHO = True

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
