from app import db, ValidationError
from sqlalchemy.orm import validates
from defs import status_list, priority_list
from citmodel import CITModel
import datetime

class ServiceRequest(CITModel):
	"""
	A class for storing a service request

	Attributes:
	serviceRequestId (int): An autoincrement id stored in the database, starts at 1
	status (enum): A statement of what the status of the request is in, open or closed
	statusNotes (relationship): A relationship that points to the notes table
	description (string): This may contain line breaks, but not html or code; free form text limited to 4,000 characters
	title (string): This contains a readable string for the title of the request
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
	approved (boolean): A boolean stating if the request has been approved by an admin
	priority (enum): A statement of the priority of the request, low, medium, or high
	agencyResponsible (int): A foreign key pointing to agency.agencyId
	serviceCode (int): A foreign key pointing to service.serviceId
	accountId (int): A foreign key pointing to user.userId
	agency (Agency): A backref that is created in Agency
	subscribers (User): A backref that is created in User
	"""

	__tablename__ = "serviceRequest"
	serviceRequestId = db.Column(db.Integer, primary_key=True)
	status = db.Column(db.Enum("open", "closed"))
	statusNotes = db.relationship("Note")
	title = db.Column(db.Text)
	description = db.Column(db.Text)
	serviceNotice = db.Column(db.Text)
	requestedDatetime = db.Column(db.TIMESTAMP, default=datetime.datetime.utcnow)#TODO: Default
	updatedDatetime = db.Column(db.TIMESTAMP)# TODO: Default
	expectedDatetime = db.Column(db.TIMESTAMP) #TODO: Default
	address = db.Column(db.Text)
	addressId = db.Column(db.Integer)
	zipcode = db.Column(db.Integer)
	lat = db.Column(db.Float)
	longitude = db.Column(db.Float)
	mediaUrl = db.Column(db.Text)
	deviceId = db.Column(db.Text)
	approved = db.Column(db.Boolean)
	priority = db.Column(db.Enum("low", "medium", "high"))
	agencyResponsible = db.Column(db.Integer, db.ForeignKey("agency.agencyId"))
	serviceCode = db.Column(db.Integer, db.ForeignKey("service.serviceId"))
	accountId = db.Column(db.Integer, db.ForeignKey("user.userId"))

	def __init__(self):
		"""
		Setups default values
		"""
		self.accountId = 0
		self.title = "A basic issue"
		self.description = "A basic issue description"
		self.lat = 0
		self.longitude = 0
		self.address = "Unknown"
		self.status = "open"
		self.approved = 0
		self.priority = "low"
		self.mediaUrl = None;


	@validates("status")
	def validate_status(self, key, status):
		"""
		Validates that the status is in a list of valid statuses
		"""

		if not status in status_list:
			raise ValidationError("'"+status+"' is not a valid status")
		return status

	@validates("priority")
	def validate_priority(self, key, priority):
		"""
		Validates that the status is in a list of valid statuses
		"""

		if not priority in priority_list:
			raise ValidationError("'"+priority+"' is not a valid priority")
		return priority

	def toDict(self):
		"""
		This converts the model to a dionary
		"""
		
		return
		{
			"service_request_id" : self.serviceRequestId,
			"status" : self.status,
			"status_notes" : self.statusNotes,
			"title" : self.title,
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
			"approved" : self.approved,
			"priority" : self.priority,
			"agency_responsible" : self.agencyResponsible,
			"service_code" : self.serviceCode,
			"account_id" : self.accountId
		}

	def toCitDict(self):
		"""
		This converts a model to a dictionary for the CIT front-end
		"""

		#TODO: Fill out notes
		notesArray = map(lambda x: x.toCitDict(), self.statusNotes)

		return {
			"id" : self.serviceRequestId,
			"owner" : self.accountId,
			"title" : self.title,
			"description" : self.description,
			"location" :
			{
				"lat" : self.lat,
				"long" : self.longitude,
				"address" : self.address
			},
			"open" : (self.status == "open"),
			"approved" : self.approved,
			"priority" : self.priority,
			"image_url" : self.mediaUrl,
			"notes" : notesArray,
			"created_at" : self.requestedDatetime,
			"updated_at" : self.updatedDatetime
		}

	def fromDict(self, d):
		"""
		This converts the dictionary to a model
		"""

		self.serviceRequestId = d.get("service_request_id", self.serviceRequestId)
		self.status = d.get("status", self.status)
		self.statusNotes = d.get("status_notes", self.statusNotes)
		self.title = d.get("title", self.title)
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
		self.approved = d.get("approved", self.approved)
		self.priority = d.get("priority", self.priority)
		self.agencyResponsible = d.get("agency_responsible", self.agencyResponsible)
		self.serviceCode = d.get("service_code", self.serviceCode)
		self.accountId = d.get("account_id", self.accountId)

		return True

	def fromCitDict(self, d):
		"""
		This converts the dictionary to a model
		"""

		self.serviceRequestId = d.get("service_request_id", self.serviceRequestId)
		self.status = d.get("status", self.status)
		self.statusNotes = d.get("status_notes", self.statusNotes)
		self.title = d.get("title", self.title)
		self.description = d.get("description", self.description)
		self.serviceNotice = d.get("service_notice", self.serviceNotice)
		self.requestedDatetime = d.get("requested_datetime", self.requestedDatetime)
		self.updatedDatetime = d.get("updated_datetime", self.updatedDatetime)
		self.expectedDatetime = d.get("expected_datetime", self.expectedDatetime)
		self.address = d.get("address", self.address)
		self.addressId = d.get("address_id", self.addressId)
		self.zipcode = d.get("zipcode", self.zipcode)
		#TODO: This has to be changed
		self.lat = d.get("location", {}).get("lat", self.lat)
		self.longitude = d.get("location", {}).get("long", self.longitude)
		self.address = d.get("location", {}).get("address", self.address)

		self.mediaUrl = d.get("media_url", self.mediaUrl)
		self.deviceId = d.get("device_id", self.deviceId)
		self.approved = d.get("approved", self.approved)
		self.priority = d.get("priority", self.priority)
		self.agencyResponsible = d.get("agency_responsible", self.agencyResponsible)
		self.serviceCode = d.get("service_code", self.serviceCode)
		self.accountId = d.get("account_id", self.accountId)
		self.updatedDatetime = datetime.datetime.utcnow();

		return True

