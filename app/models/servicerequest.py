from app import db

#TODO: Maybe this should be moved to somewhere else like defs.py
status_list = ['open', 'closed']

class ServiceRequest(db.Model):
	"""
	A class for storing a service request and getting details about that

	Attributes:
	service_request_id (int): An autoincrement id stored in the database, starts at 1
	status (enum): A statement of what the status of the request is in, open or closed
	status_notes (string): A set of notes describing why the status has changed
	service_name (string): A human readable string of the service type
	service_code (int): A foreign key pointing to service.id
	description (string): This may contain line breaks, but not html or code; free form text limited to 4,000 characters
	agency_responsible (int): Probably a foreign key pointing to an agency table
	service_notice (unsure): This is probably going to be a many to one table type thing
	requested_datetime (timestamp): This is when the request was submitted
	updated_datetime (timestamp): This is when the request was last updated
	expected_datetime (timestamp): This is when the request is expected to be completed
	address (string): Human readable address or description of location
	address_id (int): The internal address ID used by a jurisdictions master address repository or other addressing system
	zipcode (int): The postal code for the location of the service request
	lat (float): Latitude
	longitude (float): Longitude
	media_url (string): A URL to media associated with the request
	email (string): The email of the person submitting the request
	device_id (string): The unique id of the device submitting the request, only makes sense for mobile devices
	account_id (int): The id of the person submitting the request
	first_name (string): The first name of the person submitting the request
	last_name (string): The last name of the person submitting the request
	phone (string): The phone number of the person submitting the request
	"""

	service_request_id = db.Column(db.Integer, primary_key=True)
	status = db.Column(db.Enum('open', 'closed'))
	status_notes = db.Column(db.Text)
	service_name = db.Column(db.Text, db.ForeignKey('service.service_name'))
	service_code = db.Column(db.Integer, db.ForeignKey('service.id'))
	description = db.Column(db.Text)
	agency_responsible = db.Column(db.Integer)
	service_notice = db.Column(db.Text)
	requested_datetime = db.Column(db.TIMESTAMP)
	updated_datetime = db.Column(db.TIMESTAMP)
	expected_datetime = db.Column(db.TIMESTAMP)
	address = db.Column(db.Text)
	address_id = db.Column(db.Integer)
	zipcode = db.Column(db.Integer)
	lat = db.Column(db.Float)
	longitude = db.Column(db.Float)
	media_url = db.Column(db.Text)
	email = db.Column(db.Text)
	device_id = db.Column(db.Text)
	account_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	phone = db.Column(db.Text)

	@validates('status')
	def validate_type(self, key, status):
		assert status in status_list
		return status
