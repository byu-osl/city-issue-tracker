from app import app, db
from flask import render_template, request, jsonify
from fakeData import service_list, service_def, get_service_reqs, get_service_req, user_data
from models import Service, ServiceAttribute, Keyword, KeywordMapping

@app.route('/hello_world')
def hello_world():
	return render_template('hello_world.html')

#TODO: Make sure the html is being served up correctly
@app.route('/index')
@app.route('/')
def home():
	return render_template('index.html')

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
def newUsers():
	return "---"


#TODO: Implements
@app.route('/users/<int:user_id>')
def getUser(user_id):
	return "---"

#TODO: Implements
@app.route('/users', methods=['GET'])
def getAllUsers():
	return "---"

#TODO: 
@app.route('/issues/<int:issue_id>', methods=['GET'])
def getIssue():
	return "---"

#TODO: 
@app.route('/issues/<int:issue_id>', methods=['POST'])
def updateIssue():
	return "---"





#TODO: 
@app.route('/issues', methods=['GET'])
def newIssue():
	return "---"








@app.route('/api/services', methods=['GET'])
def json_view_services():
	return jsonify(service_list)


@app.route('/api/issue/<int:issue_id>', methods = ['GET'])
def json_view_issue(issue_id):
	return jsonify(get_service_req)

@app.route('/api/issues', methods = ['GET'])
def json_view_issues():
	return jsonify(get_service_reqs)

@app.route('/issue/<int:issue_num>', methods = ['GET', 'POST'])
def view_issue(issue_num):
	if request.method == 'GET':
		return render_template('view_issue.html', issue_num = issue_num, issue = get_service_req)
	elif request.method == 'POST':
		return render_template('post_issue.html', issue_num = issue_num, issue = get_service_req)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/logout')
def logout():
	return render_template('logout.html')

@app.route('/issues')
def issues():
	return render_template('issues.html', issues = get_service_reqs)

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/profile')
def profile():
	return render_template('profile.html', user_data = user_data)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(405)
def page_not_found(e):
	return render_template('405.html'), 405
