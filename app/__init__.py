from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#import os
#basedir = os.path.abspath(os.path.dirname(__file__))
#For local testing reasons
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

#db.create_all()

from app import views
