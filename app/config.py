import os
basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

SQLALCHEMY_DATABASE_URI = 'postgresql:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
