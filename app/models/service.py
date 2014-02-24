from app import db

class Service(db.Model):
	"""
	A Model to deal with Service types and information about them

	TODO: Make setter for type

	Attributes
	id (int): The primary key of the object
	service_name (string): The name of the service
	description (string): A description of what the service is
	metadata (boolean): Says whether metadata is enabled or not
	type (realtime/batch/blackbox): See docs for explaination

	"""
	id = db.Column(db.Integer, primary_key=True)
	service_name = db.Column(db.String(255))#TODO: Make unique
	description = db.Column(db.Text)
	meta_data = db.Column(db.Boolean)
	type = db.Column(db.String(10))#Note: I think the maxium number of character ever needed is 8 but just making it a round 10

#	def get_type_list(): #TODO: Maybe this is not needed
#		"""
#		Returns a list of valid types
#		"""
#	#TODO: Make a function to store meta data

