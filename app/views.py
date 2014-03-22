import json
from app import app, db
from flask import render_template, request, jsonify, Response
from fakeData import service_list, service_def, get_service_reqs, get_service_req, user_data
from models import Service, ServiceAttribute, Keyword, KeywordMapping, ServiceRequest


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

	print(request.json)
#	print(json.loads(request.json))

	s.fromDict(request.json);

	db.session.commit()

	return s.toJSON()





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

#TODO: Implement
@app.route('/issues/<int:issue_id>', methods=['GET'])
def getIssue(issue_id):
	"""
	Return the issue with id = issue_id
	"""

	serviceRequest = ServiceRequest.query.get(issue_id)

	return
	{
		"id" : serviceRequest.serviceRequestId,
		"owner" : serviceRequest.accountId,
		"title" : serviceRequest.description, #TODO: title? what is that?
		"description" : serviceRequest.description,
		"location" : 
		{
			"lat" : serviceRequest.lat,
			"long" : serviceRequest.longitude,
			"address" : serviceRequest.address
		},
		"open" : (serviceRequest.status == "open"),
		"approved" : True, #TODO: we don't currently have this
		"priority" : "Medium", #TODO: we don't currently have this
		"image_url" : serviceRequest.mediaUrl,
		"notes" : 
		[
			{"created_at" : 1200, "note" : "Test note"}
		], #TODO: we don't currently have this, kind of...
		"created_at" : 1200, #TODO: we don't currently have this
		"updated_at" : 1200 #TODO: we don't currently have this
	}

#TODO: Implement
@app.route('/issues', methods=['POST'])
def createIssue():
	"""
	Create an issue
	"""
	return "---"

#TODO: Implement
@app.route('/issues/<int:issue_id>', methods=['POST'])
def updateIssue(issue_id):
	"""
	Update the given issue
	"""
	return "---"

#TODO: Implement
@app.route('/issues', methods=['GET'])
def viewAllIssues():
	"""
	Return all the issues
	"""
	return "---"

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
