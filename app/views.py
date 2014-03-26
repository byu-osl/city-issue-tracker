import json
from app import app, db
from flask import render_template, request, jsonify, Response
from fakeData import service_list, service_def, get_service_reqs, get_service_req, user_data
from models import Service, ServiceAttribute, Keyword, KeywordMapping, ServiceRequest
from os import urandom
from passlib.hash import sha512_crypt

#############
# Main Page #
#############

#TODO: Make sure the html is being served up correctly
@app.route('/index')
@app.route('/')
def home():
	return render_template('index.html')

################
# User Section #
################

#TODO: How to do this securely
@app.route('/users/sign_in', methods=['POST'])
def signIn():
	return "---"

#TODO: Implement
@app.route('/users/sign_out', methods=['POST'])
def signOut():
	return "---"

#TODO: Implement
@app.route('/users', methods=['POST'])
def createUser():
	hash_iterations

	if not request.json:
		abort(400)

	req_json = request.get_json()
	userId = req_json['id']
	email = req_json['email']
	firstName = req_json['name']
	lastName = req_json['name']
	password = req_json['password']

	passwordSalt = urandom(16)	# Generate a Cryptographically Secure Salt of length 16 bytes

	passwordHash = sha512_crypt.encrypt(password, rounds = 10000, salt = passwordSalt)
	

	


	admin = req_json['admin']

	new_user = User(req_json['id'], )

	# userId, email, firstName, lastName, phone = "(555) 555-5555", passwordHash, passwordSalt, role = 'user', 

	new_user = User()
	new_user.fromDict(request.json)



	return "---"

#TODO: Implement
@app.route('/users/<int:user_id>', methods=['GET'])
def getUser(user_id):
	return "---"

#TODO: Implement
@app.route('/users/<int:user_id>', methods=['POST'])
def updateUser(user_id):
	return "---"

#TODO: Implement
@app.route('/users/signed_in_user')
def getOwnAccount():
	return "---"

#TODO: Implement
@app.route('/users', methods=['GET'])
def getAllUsers():
	return "---"
###################
# Service Section #
###################

@app.route('/gen/service', methods=['GET'])
def genServices():
	s = Service()
	s.title = "Title"
	s.description = "Description"
	s.type = "batch"
	s.metaData = False

	db.session.add(s)
	db.session.commit()
	return s.toJSON()

#Create a new service
@app.route('/services', methods=['POST'])
def newService():

	if not request.json:
		abort(400)

	s = Service()
	s.fromDict(request.json)

	db.session.add(s)
	db.session.commit()

	return s.toJSON()

#TODO: Implement
@app.route('/services', methods=['GET'])
def getServices():
	l = Service.query.all()

	return Service.composeFormatList("json", l)

#TODO: Implement
@app.route('/services/<int:serviceId>', methods=['GET'])
def getService(serviceId):
	s = Service.query.get(serviceId)

	return s.toJSON()

#TODO: Implement
#Updates a service
@app.route('/services/<int:serviceId>', methods=['POST'])
def postService(serviceId):

	if not request.json:
		abort(400)

	s = Service.query.get(serviceId)

	s.fromDict(request.json);

	db.session.commit()

	return s.toJSON()

@app.route('/services/<int:serviceId>', methods=['DELETE'])
def deleteService(serviceId):

	s = Service.query.get(serviceId)

	db.session.delete(s)
	db.session.commit()

	#TODO: Some other way of marking success
	return "---"





#TODO: Implement
@app.route('/services/<int:serviceId>/attr', methods=['GET'])
def getServiceAttr(serviceId):
	sa1 = ServiceAttribute()


	sa2 = ServiceAttribute()


	sa3 = ServiceAttribute()

	return "---"



##################
# Issues Section #
##################

@app.route('/issues/<int:issue_id>', methods=['GET'])
def getIssue(issue_id):
	"""
	Return the issue with id = issue_id
	"""

	serviceRequest = ServiceRequest.query.get(issue_id)
	notes = serviceRequest.statusNotes
	notesArray = []

	for i in range(len(notes)):
		notesArray.append(notes[i].toJSON())

	return
	{
		"id" : serviceRequest.serviceRequestId,
		"owner" : serviceRequest.accountId,
		"title" : serviceRequest.title,
		"description" : serviceRequest.description,
		"location" : 
		{
			"lat" : serviceRequest.lat,
			"long" : serviceRequest.longitude,
			"address" : serviceRequest.address
		},
		"open" : (serviceRequest.status == "open"),
		"approved" : serviceRequest.approved,
		"priority" : serviceRequest.priority,
		"image_url" : serviceRequest.mediaUrl,
		"notes" : notesArray,
		"created_at" : serviceRequest.requestedDatetime,
		"updated_at" : serviceRequest.updatedDatetime
	}

#TODO: Implement
@app.route('/issues', methods=['POST'])
def createIssue():
	"""
	Create an issue
	"""

	requestJson = request.get_json()

	if not requestJson:
		abort(400)

	serviceRequest = ServiceRequest()
	serviceRequest.serviceRequestId = requestJson["id"]
	serviceRequest.accountId = requestJson["owner"]
	serviceRequest.title = requestJson["title"]
	serviceRequest.description = requestJson["description"]
	serviceRequest.lat = requestJson["location"]["lat"]
	serviceRequest.longitude = requestJson["location"]["long"]
	serviceRequest.address = requestJson["location"]["address"]
	serviceRequest.status = "open" if requestJson["open"] else "closed"
	serviceRequest.approved = requestJson["approved"]
	serviceRequest.priority = requestJson["priority"]
	serviceRequest.mediaUrl = requestJson["image_url"]
	serviceRequest.requestedDatetime = localtime().strftime("%Y-%m-%d %H:%M:%S")
	serviceRequest.updatedDatetime = localtime().strftime("%Y-%m-%d %H:%M:%S")
	serviceRequest.fromDict(requestJson)
	db.session.add(serviceRequest)
	db.session.commit()

	return serviceRequest.toJSON()

#TODO: Implement
@app.route('/issues/<int:issue_id>', methods=['POST'])
def updateIssue(issue_id):
	"""
	Update the given issue
	"""

	requestJson = request.get_json()

	if not requestJson:
		abort(400)

	serviceRequest = ServiceRequest.query.get(issue_id)
	serviceRequest.accountId = requestJson["owner"]
	serviceRequest.title = requestJson["title"]
	serviceRequest.description = requestJson["description"]
	serviceRequest.lat = requestJson["location"]["lat"]
	serviceRequest.longitude = requestJson["location"]["long"]
	serviceRequest.address = requestJson["location"]["address"]
	serviceRequest.status = "open" if requestJson["open"] else "closed"
	serviceRequest.approved = requestJson["approved"]
	serviceRequest.priority = requestJson["priority"]
	serviceRequest.mediaUrl = requestJson["image_url"]
	serviceRequest.updatedDatetime = localtime().strftime("%Y-%m-%d %H:%M:%S")
	serviceRequest.fromDict(requestJson);
	db.session.commit()

	return s.toJSON()

#TODO: Implement
@app.route('/issues', methods=['GET'])
def viewAllIssues():
	"""
	Return all the issues
	"""

	requestJson = request.get_json()

	if not requestJson:
		abort(400)

	orderBy = requestJson["orderBy"]
	offset = int(requestJson["offset"])
	max = int(requestJson["max"])
	query = requestJson["query"]
	reversed = bool(requestJson["reversed"])
	includeClosed = bool(requestJson["includeClosed"])

	query = ServiceRequest.query.filter(ServiceRequest.title.contains(query) or ServiceRequest.description.contains(query)).filter(True if includeClosed else ServiceRequest.status == "open")

	if orderBy == "created_at":
		allIssues = query.order_by(ServiceRequest.createdAt).all()
	elif orderBy == "priority":
		allIssues = query.order_by(ServiceRequest.priority).all()
	elif orderBy == "open":
		allIssues = query.order_by(ServiceRequest.status).all()

	requestArray = []

	for i in range(len(allIssues)):
		if len(requestArray) < max:
			try:
				if reversed:
					serviceRequest = allIssues[-(i + offset)]
				else:
					serviceRequest = allIssues[i + offset]

				notes = serviceRequest.statusNotes
				notesArray = []

				for i in range(len(notes)):
					notesArray.append(notes[i].toJSON())

				requestArray.append
				(
					{
						"id" : serviceRequest.serviceRequestId,
						"owner" : serviceRequest.accountId,
						"title" : serviceRequest.title,
						"description" : serviceRequest.description,
						"location" : 
						{
							"lat" : serviceRequest.lat,
							"long" : serviceRequest.longitude,
							"address" : serviceRequest.address
						},
						"open" : (serviceRequest.status == "open"),
						"approved" : serviceRequest.approved,
						"priority" : serviceRequest.priority,
						"image_url" : serviceRequest.mediaUrl,
						"notes" : notesArray,
						"created_at" : serviceRequest.requestedDatetime,
						"updated_at" : serviceRequest.updatedDatetime
					}
				)
			except:
				break
		else:
			break

	return
	{
		"total_results": len(allIssues),
		"total_returned": len(requestArray),
		"offset": offset,
		"issues": requestArray
	}

#TODO: Implement
@app.route('/issues/images', methods=['POST'])
def uploadImage():
	"""
	Upload an image
	"""
	return "---"

#TODO: Implement
@app.route('/issues/images/<int:photo_id>', methods=['GET'])
def viewImage(photo_id):
	"""
	Return the photo with id = photo_id
	"""
	return "---"


######################
# Open311 API Routes #
######################

#TODO: Implement
@app.route('/open311/api/services.<form>', methods=['GET'])
def json_view_services(form):
	s1 = Service()
	s1.title = "Title",
	s1.description = "Description"
	s1.type = "batch"
	s1.metaData = True

	s2 = Service()
	s2.title = "Title",
	s2.description = "Description"
	s2.type = "batch"
	s2.metaData = True

	s3 = Service()
	s3.title = "Title",
	s3.description = "Description"
	s3.type = "batch"
	s3.metaData = True

	return Service.composeFormatList(form, [s1, s2, s3])

@app.route('/open311/api/services/<int:serviceCode>.<form>')
def apiViewService(serviceCode, form):
		

	return "---"

#TODO: Implement
@app.route('/open311/api/issue/<int:issue_id>.<form>', methods = ['GET'])
def json_view_issue(issue_id, format):
	return format
#	return jsonify(get_service_req)

#TODO: Implement
@app.route('/open311/api/issues', methods = ['GET'])
def json_view_issues():
	return jsonify(get_service_reqs)

##################
# Error Handlers #
##################

#TODO: Implement
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#TODO: Implement
@app.errorhandler(405)
def page_not_found(e):
	return render_template('405.html'), 405
