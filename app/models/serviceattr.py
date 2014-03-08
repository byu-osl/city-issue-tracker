from app import db
from sqlalchemy.orm import validates


DATATYPE_STR = "string"
DATATYPE_NUM = "number"
DATATYPE_DT = "datetime"
DATATYPE_TXT = "text"
DATATYPE_SVL = "singlevaluelist"
DATATYPE_MVL = "multivaluelist"


datatype_list = [
	DATATYPE_STR,
	DATATYPE_NUM,
	DATATYPE_DT,
	DATATYPE_TXT,
	DATATYPE_SVL,
	DATATYPE_MVL
]

class ServiceAttribute(db.Model):
	"""
	A model to deal with the additional metadata that the Service might require

	Attributes
	id (int): The primary key of the object
	variable (boolean): See documentations for open311 spec
	required (boolean): Is this attribute a required field?
	code (string): unique id for attribute NOTE: Should this just be the id?
	datatype (string): The datatype of the field (see datatype_list)
	datatype_description (text): A description of the datatype
	order (int): The order of the attributes to be displayed
	description (text): A description of this attribute
	service_id (int): The foreign key for the Service this Attribute points too
	values (ServiceAttributeValue): An array of ServiceAttributeValues
	service (Service): The parent of this service
	"""
	serviceAttrId = db.Column(db.Integer, primary_key=True)
	variable = db.Column(db.Boolean)
	required = db.Column(db.Boolean)
	datatype = db.Column(db.Enum(DATATYPE_STR, DATATYPE_NUM, DATATYPE_DT, DATATYPE_TXT, DATATYPE_SVL, DATATYPE_MVL))
	datatype_description = db.Column(db.String(255))#TODO: What is a good example of this?
	description = db.Column(db.Text)#TODO: Should there be a limit on the description?
	order = db.Column(db.Integer)
	serviceId = db.Column(db.Integer, db.ForeignKey('service.serviceId'))
	values = db.relationship('ServiceAttributeValue', backref='attribute', lazy='joined')

	def get_datatype_list(): #TODO: Maybe not needed
		"""

		"""
		return datatype_list

	@validates('order')
	def validate_order(self, key, order):
		"""
		A validator that asserts order is above 0 (starts at 1)
		"""
		assert order > 0
		return order
