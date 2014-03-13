from app import db

# TODO: Do we even need this class?
class Agency(db.Model):
	"""
	A class for storing an agency

	Attributes:
	agencyId (int): An autoincrement id stored in the database, starts at 1
	name (string): A human readable string of the agency's name
	"""

	__tablename__ = "agency"
	agencyId = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	serviceRequests = db.relationship("ServiceRequest", backref = "agency")
