from app import db
from flask import jsonify, Response
import xmltodict
import json

class CITModel(db.Model):
	"""
	This model is an extention for the db.Model that helps with printing out data.
	Open311 requires XML and we want use JSON so we need a way to easily convert from
	Model->JSON or Model->XML. We also need a way to do XML->Model and JSON->Model.
	This Class is suppose to help with these conversions.

	In order for a Class to inherit from this class it has to implement 2 methods and override
	2 attributes.

	Methods to overwrite:
	1. toDict: This function should convert the model attributes into a dictionary
	2. fromDict: Not created yet
	3. toCitDict: This function converts the Model to a format for the CIT frontend
	4. fromCitDict: This function takes the format from the CIT frontend and converts back to a model


	Attibutes to overwrite:
	1. _open311Name: The name of the class (Used when generating xml)
	2. _open311ListName: The name of an array of the class (Used when generating xml)

	Attributes:
	__abstract__ (Boolean): Will tell SQLAlchemy not to make a table for this 
	"""
	__abstract__ = True
	
	_open311Name = "Implement"

	_open311ListName = "Implements"

	def toDict(self):
		"""
		This converts the model to a dictionary.
		This is an abstract method
		"""
		raise NotImplementedError

	def fromDict(self):
		"""
		This converts a dictionary back into an objects format
		This is an abstract method
		"""
		raise NotImplementedError

	def toCitDict(self):
		"""
		This converts the model to a dictionary.
		This is an abstract method
		"""
		raise NotImplementedError

	def fromCitDict(self):
		"""
		This converts the model to a dictionary.
		This is an abstract method
		"""
		raise NotImplementedError

	def toJSON(self):
		"""
		A simple function that converts this object into json
		"""
		return jsonify(self.toDict())

	def fromJSON(self, jsonStr):
		"""
		A simple function that converts a json string to being placed into the model
		"""
		return self.fromDict(json.loads(jsonStr))

	def toCitJSON(self):
		"""
		A simple function that converts this object into json
		"""
		return jsonify(self.toCitDict())

	def fromCitJSON(self, jsonStr):
		"""
		A simple function that converts a json string to being placed into the model
		"""
		return self.fromCitDict(json.loads(jsonStr))


	def toXML(self):
		"""
		A simple function that converts this obejct into XML
		NOTE: There can be a problem since valid XML needs to be wrapped
		by one tag at the head
		"""
		return xmltodict.unparse({self._open311Name: self.toDict()})



	def toFormat(self, format):
		"""
		This function is called so that a format of either json or xml
		can result in the correct type of model being returned
		"""
		if(format == "json"):
			output = self.toJSON()
			return  Response(output, mimetype='application/json')
		elif(format == "xml"):
			output = self.toXML()
			return Response(output, mimetype='application/xml')
		else:
			#TODO: Should not get here. Throw error?
			return self.toDict()

	@classmethod
	def composeFormatList(cls, format, list):
		"""
		This function takes a format and a list of objects.
		It converts them into either a json or xml string for display
		"""
		if(format == "json"):
			output = cls.composeJSONList(list)
			return Response(output, mimetype='application/json')
		elif(format == "xml"):
			output = cls.composeXMLList(list)
			return Response(output, mimetype='application/xml')

		else:
			#TODO: Should not get here. Throw error?
			return cls.toDict()

	@classmethod
	def composeJSONList(cls, list):
		"""
		Creates a JSON list
		"""
		#TODO: 
		return json.dumps(map(lambda x: x.toDict(), list));

	@classmethod
	def composeCitJSONList(cls, list):
		"""
		Creates a CIT JSON list
		"""
		#TODO: 
		return json.dumps(map(lambda x: x.toCitDict(), list));

	@classmethod
	def composeXMLList(cls, list):
		"""
		Creates a XML list
		"""
		return xmltodict.unparse({cls._open311ListName: {cls._open311Name:  map(lambda x:  x.toDict(), list)}});
