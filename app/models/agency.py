from app import db
from citmodel import CITModel

class Agency(CITModel):
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


	def toDict(self):
		"""
		This converts the model to a dionary
		"""
		
		return
		{
			"agency_id" : self.agencyId,
			"name" : self.name,
			"service_requests" : self.serviceRequests
		}

	def fromDict(self, d):
		"""
		This converts the dictionary to a model
		"""

		self.agencyId = d.get("agency_id", self.agencyId)
		self.name = d.get("name", self.name)
		self.serviceRequests = d.get("service_requests", self.serviceRequests)
		return True