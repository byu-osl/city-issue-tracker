from app import db
from sqlalchemy.orm import validates
from defs import status_list
from citmodel import CITModel

class ServiceRequest(CITModel):
	"""
	A class for storing a service request

	Attributes:
	serviceRequestId (int): An autoincrement id stored in the database, starts at 1
	status (enum): A statement of what the status of the request is in, open or closed
	statusNotes (string): A note describing why the status has changed
	description (string): This may contain line breaks, but not html or code; free form text limited to 4,000 characters
	serviceNotice (unsure): This is probably going to be a many to one table type thing
	requestedDatetime (timestamp): This is when the request was submitted
	updatedDatetime (timestamp): This is when the request was last updated
	expectedDatetime (timestamp): This is when the request is expected to be completed
	address (string): Human readable address or description of location
	addressId (int): The internal address ID used by a jurisdions master address repository or other addressing system
	zipcode (int): The postal code for the location of the service request
	lat (float): Latitude
	longitude (float): Longitude
	mediaUrl (string): A URL to media associated with the request
	deviceId (string): The unique id of the device submitting the request, only makes sense for mobile devices
	agencyResponsible (int): A foreign key pointing to agency.agencyId
	serviceCode (int): A foreign key pointing to service.serviceId
	accountId (int): A foreign key pointing to user.userId
	agency (Agency): A backref that is created in Agency
	subscribers (User): A backref that is created in User
	"""

	__tablename__ = "serviceRequest"
	serviceRequestId = db.Column(db.Integer, primary_key=True)
	status = db.Column(db.Enum("open", "closed"))
	# TODO: If we're going to do stuff with service notices this should have a table created and so on
	statusNotes = db.Column(db.Text)
	description = db.Column(db.Text)
	serviceNotice = db.Column(db.Text)
	requestedDatetime = db.Column(db.TIMESTAMP)
	updatedDatetime = db.Column(db.TIMESTAMP)
	expectedDatetime = db.Column(db.TIMESTAMP)
	address = db.Column(db.Text)
	# TODO: Determine if we actually want or need this
	addressId = db.Column(db.Integer)
	zipcode = db.Column(db.Integer)
	lat = db.Column(db.Float)
	longitude = db.Column(db.Float)
	mediaUrl = db.Column(db.Text)
	deviceId = db.Column(db.Text)
	agencyResponsible = db.Column(db.Integer, db.ForeignKey("agency.agencyId"))
	serviceCode = db.Column(db.Integer, db.ForeignKey("service.serviceId"))
	accountId = db.Column(db.Integer, db.ForeignKey("user.userId"))

	@validates("status")
	def validate_type(self, key, status):
		"""
		Validates that the status is in a list of valid statuses
		"""

		assert status in status_list
		return status

	def toDict(self):
		"""
		This converts the model to a dionary
		"""
		
		return
		{
			"service_request_id" : self.serviceRequestId,
			"status" : self.status,
			"status_notes" : self.statusNotes,
			"description" : self.description,
			"service_notice" : self.serviceNotice,
			"requested_datetime" : self.requestedDatetime,
			"updated_datetime" : self.updatedDatetime,
			"expected_datetime" : self.expectedDatetime,
			"address" : self.address,
			"address_id" : self.addressId,
			"zipcode" : self.zipcode,
			"lat" : self.lat,
			"longitude" : self.longitude,
			"media_url" : self.mediaUrl,
			"device_id" : self.deviceId,
			"agency_responsible" : self.agencyResponsible,
			"service_code" : self.serviceCode,
			"account_id" : self.accountId
		}

	def fromDict(self, d):
		"""
		This converts the dictionary to a model
		"""

		self.serviceRequestId = d.get("service_request_id", self.serviceRequestId)
		self.status = d.get("status", self.status)
		self.statusNotes = d.get("status_notes", self.statusNotes)
		self.description = d.get("description", self.description)
		self.serviceNotice = d.get("service_notice", self.serviceNotice)
		self.requestedDatetime = d.get("requested_datetime", self.requestedDatetime)
		self.updatedDatetime = d.get("updated_datetime", self.updatedDatetime)
		self.expectedDatetime = d.get("expected_datetime", self.expectedDatetime)
		self.address = d.get("address", self.address)
		self.addressId = d.get("address_id", self.addressId)
		self.zipcode = d.get("zipcode", self.zipcode)
		self.lat = d.get("lat", self.lat)
		self.longitude = d.get("longitude", self.longitude)
		self.mediaUrl = d.get("media_url", self.mediaUrl)
		self.deviceId = d.get("device_id", self.deviceId)
		self.agencyResponsible = d.get("agency_responsible", self.agencyResponsible)
		self.serviceCode = d.get("service_code", self.serviceCode)
		self.accountId = d.get("account_id", self.accountId)
		return True
