import os
basedir = os.path.abspath(os.path.dirname(__file__))
# Define the database - we are working with
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mydb_pwd@localhost:3306/mydb'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/flask?charset=utf8'
# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost:5432/flask'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_ECHO = True
