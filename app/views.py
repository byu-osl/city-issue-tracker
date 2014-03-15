import json
from app import app, db
from flask import render_template, request, jsonify
from fakeData import service_list, service_def, get_service_reqs, get_service_req, user_data
from models import Service, ServiceAttribute, Keyword, KeywordMapping



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

#TODO: Implement
@app.route('/services', methods=['GET'])
def getServices():
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

	return json.dumps([s3.toDict(), s2.toDict(), s1.toDict()]);


#TODO: Implement
@app.route('/services/<int:serviceId>', methods=['GET'])
def getService(serviceId):
	s = Service()
	s.title = "Title",
	s.description = "Description"
	s.type = "batch"
	s.metaData = True
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
def getIssue():
	return "---"

#TODO: Implement
@app.route('/issues', methods=['POST'])
def createIssue():
	return "---"

#TODO: Implement
@app.route('/issues/<int:issue_id>', methods=['POST'])
def updateIssue():
	return "---"

#TODO: Implement
@app.route('/issues', methods=['GET'])
def viewAllIssues():
	return "---"

#TODO: Implement
@app.route('/issues/images', methods=['POST'])
def uploadImage():
	return "---"

#TODO: Implement
@app.route('/issues/images/<int:photo_id>', methods=['GET'])
def viewImage(photo_id):
	return "---"

##############
# API Routes #
##############

#TODO: Implement
@app.route('/api/services', methods=['GET'])
def json_view_services():
	return jsonify(service_list)

#TODO: Implement
@app.route('/api/issue/<int:issue_id>', methods = ['GET'])
def json_view_issue(issue_id):
	return jsonify(get_service_req)

#TODO: Implement
@app.route('/api/issues', methods = ['GET'])
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
