from app import db
from flask import jsonify
import json
import xmltodict
from keywordservicemapper import keywordMapping
from sqlalchemy.orm import validates


TYPE_REALTIME = "realtime"
TYPE_BATCH = "batch"
TYPE_BLACKBOX = "blacbox"

#TODO: Maybe this should be moved to somewhere else. Maybe a defs.py ???
type_list = [TYPE_REALTIME, TYPE_BATCH, TYPE_BLACKBOX]

class Service(db.Model):
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
	serviceId = db.Column(db.Integer, primary_key=True)
	serviceName = db.Column(db.String(255), unique=True)#TODO: Make unique
	description = db.Column(db.Text)
	metaData = db.Column(db.Boolean)
	type = db.Column(db.Enum(TYPE_REALTIME, TYPE_BATCH, TYPE_BLACKBOX))
	attributes = db.relationship('ServiceAttribute', backref="service", lazy="joined")
	keywords = db.relationship("Keyword", secondary=keywordMapping, backref="services")

	def __repr__(self):
		return self.toJSON(self.toDict);

	def toDict(self):
		return {
			"serviceId": self.serviceId,
			"serviceName": self.serviceName,
			"description": self.description,
			"metadata": self.metaData,
			"type": self.type,
			"keywords": ["ok","kk"]
		}

	def toJSON(self):
		return jsonify(self.toDict())

	def toXML(self):
		print(self.toDict())
		return xmltodict.unparse({"Test": None})

	def toFormat(self, format):
		if(format == "json"):
			return self.toJSON()
		elif(format == "xml"):
			return self.toXML()
		else:
			#TODO: Should not get here
			assert False

	def prep_for_send(self):
		"""
		Returns a simple data structure that can be turned into JSON or XML
		NOTE: I am doing this because `metadata` is reserved so I used `meta_data`
		The Open311 spec says it should be `metadata` so I have to translate it
		"""
		return {}

	@validates('type')
	def validate_type(self, key, type):
		"""
		Validates that the typebeing set
		"""
		#TODO:Check that it is valid
		assert type in type_list;
		return type;



