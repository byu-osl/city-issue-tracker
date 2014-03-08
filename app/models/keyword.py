from app import db
from sqlalchemy.orm import validates

#http://stackoverflow.com/questions/5729500/how-does-sqlalchemy-handle-unique-constraint-in-table-definition


class Keyword(db.Model):
	"""
	A model for the Service models.

	According to the specifications of the Open311 standard...
	'A comma separated list of tags or keywords to help users identify the request type. 
	This can provide synonyms of the service_name and group.'

	Attributes
	keywordId (int): The primary key for this object
	keyword (string): A string that represents the keyword

	"""
	keywordId = db.Column(db.Integer, primary_key=True)
	keyword = db.Column(db.String(255), unique=True)#I think that should be long enough TODO: Make unique


	@validates('keyword')
	def validate_type(self, key, keyword):
		"""
		A validator that check that the keyword is not the empty string
		"""
		assert keyword #TODO: Check this works. It should work based on the fact that empty strings are fasley
		return keyword
