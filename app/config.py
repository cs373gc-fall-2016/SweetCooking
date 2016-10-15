import os
basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#app.config['SQLALCHEMY_DATABASE_URI'] = ''
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
