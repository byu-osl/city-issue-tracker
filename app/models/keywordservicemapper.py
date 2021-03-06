from app import db
#http://docs.sqlalchemy.org/en/rel_0_9/orm/relationships.html
#http://docs.sqlalchemy.org/en/rel_0_9/orm/extensions/associationproxy.html

keywordMapping = db.Table('keywordMapping', db.metadata, 
	db.Column('service_id', db.Integer, db.ForeignKey('service.serviceId')),
	db.Column('keyword_id', db.Integer, db.ForeignKey('keyword.keywordId'))
)

'''
class KeywordMapping(db.Model):
	"""
	This model maps keywords with services and because of this is many-to-many

	Attributes
	id (int): The primary key for this object
	service_id (int): The foreign key for a service
	keyword_id (int): The foreign key for a keyword
	"""
	service_id = db.Column(db.Integer, db.ForeignKey('service.id'))#TODO: Check that foreign key works
	keyword_id = db.Column(db.Integer, db.ForeignKey('keyword.id'))#TODO: Check that foreign key works
'''

