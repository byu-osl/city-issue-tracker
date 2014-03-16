from app import db
from flask import jsonify
import json
import xmltodict
from keywordservicemapper import keywordMapping
from sqlalchemy.orm import validates
from citmodel import CITModel

TYPE_REALTIME = "realtime"
TYPE_BATCH = "batch"
TYPE_BLACKBOX = "blacbox"

#TODO: Maybe this should be moved to somewhere else. Maybe a defs.py ???
type_list = [TYPE_REALTIME, TYPE_BATCH, TYPE_BLACKBOX]

class Service(CITModel):
	"""
	A Model to deal with Service types and information about them


	Attributes
	serviceId (int): The primary key of the object
	serviceName (string): The name of the service
	description (string): A description of what the service is
	metaData (boolean): Says whether metadata is enabled or not
	type (realtime/batch/blackbox): See docs for explaination
	attributes (ServiceAttributes): An array of ServiceAttribute models
	keywords (Keyword): An array of keywords models
	"""
	__tablename__ = "service"
	_open311Name = "service"
	_open311ListName = "services"

	serviceId = db.Column(db.Integer, primary_key=True)
	serviceName = db.Column(db.String(255), unique=True)#TODO: Make unique
	description = db.Column(db.Text)
	metaData = db.Column(db.Boolean)
	type = db.Column(db.Enum(TYPE_REALTIME, TYPE_BATCH, TYPE_BLACKBOX))
	attributes = db.relationship('ServiceAttribute', backref="service", lazy="joined")
	keywords = db.relationship("Keyword", secondary=keywordMapping, backref="services")

	def __repr__(self):
		return self.toJSON();

	def toDict(self):
		return {
			"serviceId": self.serviceId,
			"serviceName": self.serviceName,
			"description": self.description,
			"metadata": self.metaData,
			"type": self.type,
			"keywords": ["ok","kk"]
		}

	@validates('type')
	def validate_type(self, key, type):
		"""
		Validates that the typebeing set
		"""
		#TODO:Check that it is valid
		assert type in type_list;
		return type;



