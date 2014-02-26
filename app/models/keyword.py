from app import db

#http://stackoverflow.com/questions/5729500/how-does-sqlalchemy-handle-unique-constraint-in-table-definition


class Keyword(db.Model):
	"""
	A model for the Service models.

	According to the specifications of the Open311 standard...
	'A comma separated list of tags or keywords to help users identify the request type. 
	This can provide synonyms of the service_name and group.'

	Attributes
	id (int): The primary key for this object
	keyword (string): A string that represents the keyword

	"""
	id = db.Column(db.Integer, primary_key=True)
	keyword = db.Column(db.String(255), unique=True)#I think that should be long enough TODO: Make unique

