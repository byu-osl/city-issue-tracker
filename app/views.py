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
