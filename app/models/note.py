from app import db
from citmodel import CITModel
import datetime

class Note(CITModel):
	"""
	A class for representing notes for a request

	noteId (int): An autoincrement id stored in the database, starts at 1
	createdAt (timestamp): A timestamp of when the note was created
	note (string): A human readable string of the note contents
	requestId (int): A foreign key pointing to serviceRequest.serviceRequestId
	"""

	__tablename__ = "note"
	noteId = db.Column(db.Integer, primary_key=True)
	createdAt = db.Column(db.TIMESTAMP, default=datetime.datetime.utcnow)
	note = db.Column(db.Text)
	requestId = db.Column(db.Integer, db.ForeignKey("serviceRequest.serviceRequestId"))

	def toDict(self):
		"""
		This converts the model to a dictionary
		"""

		return {
			"note_id" : self.noteId,
			"created_at" : self.createdAt.__repr__(),
			"note" : self.note,
			"request_id" : self.requestId
		}

	def toCitDict(self):
		"""
		This converts the model to a dictionary for the CIT front-end
		"""

		return {
			"note_id" : self.noteId,
			"created_at" : self.createdAt.__str__(),
			"note" : self.note,
			"request_id" : self.requestId
		}

	def fromDict(self, d):
		"""
		This converts the dictionary to a model
		"""

		self.noteId = d.get("note_id", self.noteId)
		self.createdAt = d.get("created_at", self.createdAt)
		self.note = d.get("note", self.note)
		self.requestId = d.get("request_id", self.requestId)
		return True

	def fromCitDict(self, d):
		"""
		This converts a CIT dictionary into a model
		"""

		#self.noteId = d.get("note_id", self.noteId)
		#self.createdAt = d.get("created_at", self.createdAt)
		self.note = d.get("note", self.note)
		self.requestId = d.get("request_id", self.requestId)

		return True
