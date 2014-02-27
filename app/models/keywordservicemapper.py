from app import db


class KeywordMapping(db.Model):
	"""
	This model maps keywords with services and because of this is many-to-many

	Attributes
	id (int): The primary key for this object
	service_id (int): The foreign key for a service
	keyword_id (int): The foreign key for a keyword
	"""
	id = db.Column(db.Integer, primary_key=True)#TODO: I don't think this is needed
	service_id = db.Column(db.Integer, db.ForeignKey('service.id'))#TODO: Check that foreign key works
	keyword_id = db.Column(db.Integer, db.ForeignKey('keyword.id'))#TODO: Check that foreign key works


