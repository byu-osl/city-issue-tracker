import re

from flask import jsonify
from app import db
from subscriptions import subscriptions
from sqlalchemy.orm import validates
from citmodel import CITModel

class User(CITModel):
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
	subscriptionList: A DB relationship tying the Service Requests to the User ID.

	"""

	__tablename__ = "user"
	_open311Name = "user"
	_open311ListName = "users"

	userId = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(255), unique = True) #This needs to be unique
	firstName = db.Column(db.String(255))
	lastName = db.Column(db.String(255))
	phone = db.Column(db.String(10))
	passwordHash = db.Column(db.Text)
	passwordSalt = db.Column(db.Text)
	role = db.Column(db.Enum('user', 'employee', 'admin'))
	lastLogin = db.Column(db.TIMESTAMP)
	joined = db.Column(db.Date)
	subscriptionList = db.relationship("ServiceRequest", secondary=subscriptions, backref=db.backref('subscribers', lazy='dynamic'))

	def __init__(self):
		self.email = ""
		self.firstname = ""
		self.lastname = ""
		self.phone = None
		self.role = "user"


	def toDict(self):
		return {
			"user_id" : self.userId,
			"email" : self.email,
			"first_name" : self.firstName,
			"last_name" : self.lastName,
			"phone" : self.phone,
			"password_hash" : self.passwordHash,
			"password_salt" : self.passwordSalt,
			"role" : self.role,
			"last_login" : self.lastLogin,
			"joined" : self.joined,
			"subscription_list" : map(lambda x : x.serviceRequestId, self.subscriptionList)
		}


	def toCitDict(self):
		admin = True if self.role == 'admin' else False
		return {
			"user_id" : self.userId,
			"admin" : admin,
			"first_name" : self.firstName,
			"last_name" : self.lastName,
			"email" : self.email
		}


	def fromDict(self, d):
		"""
		This converts a dictionary to a user model
		"""
		self.userId = d.get("user_id", self.userId)
		self.email = d.get("email", self.email)
		self.firstName = d.get("first_name", self.firstName)
		self.lastName = d.get("last_name", self.lastName)
		self.phone = d.get("phone", self.phone)
		self.passwordHash = d.get("password_hash", self.passwordHash)
		self.passwordSalt = d.get("password_salt", self.passwordSalt)
		self.role = d.get("role", self.role)
		self.lastLogin = d.get("last_login", self.lastLogin)
		self.joined = d.get("joined", self.joined)
		self.subscriptionList = d.get("subscription_list", self.subscriptionList)
		return True


	@validates('email')
	def validateEmail(self, key, email):
		validator = re.compile("([\w]+[\.|\_|\-|\+]?)+@(([\w]+[\-]?)+[\.]?)+.[\w]{2,4}")

		if validator.match(email) is None:
			return ''

		if validator.match(email).group():
			return email
		else:
			return ''
	
