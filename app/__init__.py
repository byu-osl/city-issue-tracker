from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

class ValidationError(Exception):
	def __init__(self, str):
		self.str = str
	def __str__(self):
		return repr(self.str)

def genError(code, desc):
	jsonResp = jsonify({
		"code": code,
		"description": desc
	})

	jsonResp.status_code = code

	return jsonResp;


app = Flask(__name__)

import os
basedir = os.path.abspath(os.path.dirname(__file__))
#For local testing reasons
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

#db.create_all()


from app import views



