from app import db

class ServiceAttributeValue(db.Model):
	"""
	This model helps Service Attributes deal with the `singlevaluelist` and `multivaluelist` datatypes

	Attributes
	id (int): The primary key of the object
	service_attr_id (string): The foreign key of the service to point too
	name (string): The name of the key
	
	"""
	id = db.Column(db.Integer, primary_key=True)
	#TODO: should the key be the same as the ID?
	service_attr_id = db.Column(db.Integer, db.ForeignKey('service_attribute.id'))
	name = db.Column(db.String(100))

