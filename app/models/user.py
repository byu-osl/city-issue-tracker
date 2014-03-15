import re

from flask import jsonify
from app import db
from subscriptions import subscriptions
from sqlalchemy.orm import validates

class User(db.Model):
	"""
	A Model to define Users and their information

	Attributes
	userId (int): The primary key of the User
	email (string): The User's email address
	firstName (string): The User's first name
	lastName (string): The User's last name
	passwordHash (text): The User's salted and hashed password
	passwordSalt (text): The Salt that goes with the user's password
	role (string): The type of user, ie 'user', 'employee', or 'admin'
	lastLogin (date): The last time the user logged in
	joined (data): The date the user registered
	subscriptions: A DB relationship tying the Service Requests to the User ID.

	"""

	__tablename__ = "user"
	userId = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(255)) #This needs to be unique
	firstName = db.Column(db.String(255))
	lastName = db.Column(db.String(255))
	phone = db.Column(db.String(10))
	passwordHash = db.Column(db.Text)
	passwordSalt = db.Column(db.Text)
	role = db.Column(db.Enum('user', 'employee', 'admin'))
	lastLogin = db.Column(db.TIMESTAMP)
	joined = db.Column(db.Date)
	subscriptionList = db.relationship("ServiceRequest", secondary=subscriptions, backref=db.backref('subscribers', lazy='dynamic'))

	def toDict(self):
		return {"userId" : self.userId,
				"email" : self.email,
				"firstName" : self.firstName,
				"lastName" : self.lastName,
				"phone" : self.phone,
				"passwordHash" : self.passwordHash,
				"passwordSalt" : self.passwordSalt,
				"role" : self.role,
				"lastLogin" : self.lastLogin,
				"joined" : self.joined,
				"subscriptionList" : map(lambda x : x.serviceRequestId, self.subscriptionList)}

	def toJSON(self):
		return jsonify(self.toDict())	

	@validates('email')
	def validateEmail(self, email):
		validator = re.compile("([\w]+[\.|\_|\-|\+]?)+@(([\w]+[\-]?)+[\.]?)+.[\w]{2,4}")

		if validator.match(email).group():
			return True
		else:
			return False
		