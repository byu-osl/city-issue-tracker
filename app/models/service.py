from app import db
from keywordservicemapper import keywordMapping
from sqlalchemy.orm import validates

#TODO: Maybe this should be moved to somewhere else. Maybe a defs.py ???
type_list = ['realtime', 'batch', 'blackbox']

class Service(db.Model):
	"""
	A Model to deal with Service types and information about them


	Attributes
	id (int): The primary key of the object
	service_name (string): The name of the service
	description (string): A description of what the service is
	meta_data (boolean): Says whether metadata is enabled or not
	type (realtime/batch/blackbox): See docs for explaination

	"""
	id = db.Column(db.Integer, primary_key=True)
	service_name = db.Column(db.String(255))#TODO: Make unique
	description = db.Column(db.Text)
	meta_data = db.Column(db.Boolean)
	type = db.Column(db.String(10))#Note: I think the maxium number of character ever needed is 8 but just making it a round 10
	attributes = db.relationship('ServiceAttribute', backref="service", lazy="joined")
	keywords = db.relationship("Keyword", secondary=keywordMapping, backref="services")


	def get_type_list(): #TODO: Maybe this is not needed
		"""
		Returns a list of valid types
		"""
	#TODO: Make a function to store meta data
		return type_list;

	def prep_for_send(self):
		"""
		Returns a simple data structure that can be turned into JSON or XML
		NOTE: I am doing this because `metadata` is reserved so I used `meta_data`
		The Open311 spec says it should be `metadata` so I have to translate it
		"""
		return {
			'id': self.id,
			'service_name': self.service_name,
			'description': self.description,
			'metadata': self.meta_data,
			'type': self.type
		}

	@validates('type')
	def validate_type(self, key, type):
		#TODO:Check that it is valid
		assert type in type_list;
		return type;


