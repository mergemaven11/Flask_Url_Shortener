import os 

# os.environ.get('DATABASE_URL')
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_USERNAME = os.environ.get('ADMIN_UNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PWD')
