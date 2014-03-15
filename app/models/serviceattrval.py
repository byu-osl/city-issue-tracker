from app import db

class ServiceAttributeValue(db.Model):
	"""
	This model helps Service Attributes deal with the `singlevaluelist` and `multivaluelist` datatypes

	Attributes
	serviceAttrValId (int): The primary key of the object
	serviceAttrId (string): The foreign key of the service to point too
	name (string): The name of the key
	
	"""
	__tablename__ = "serviceAttributeValue"
	serviceAttrValId = db.Column(db.Integer, primary_key=True)
	#TODO: should the key be the same as the ID?
	serviceAttrId = db.Column(db.Integer, db.ForeignKey('serviceAttribute.serviceAttrId'))
	name = db.Column(db.String(100))

