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
	subscriptions = db.relationship("ServiceRequest", secondary=subscriptions, backref = "subscribers")

	@validates('email')
	def validate_type(self, email):
		#TODO: Check using regEx that this is a valid email
		assert email;
		return email;