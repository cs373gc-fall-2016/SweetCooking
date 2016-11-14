import os
basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

SQLALCHEMY_DATABASE_URI = 'postgresql:///app'
SQLALCHEMY_TRACK_MODIFICATIONS = False
WHOOSH_BASE = 'whoosh'
