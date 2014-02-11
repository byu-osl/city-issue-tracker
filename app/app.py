from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
	return render_template('hello_world.html')

@app.route('/index')
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/issue/<int:issue_num>', methods = ['GET', 'POST'])
def view_issue(issue_num):
	if request.method == 'GET':
		return render_template('view_issue.html', issue_num = issue_num)
	elif request.method == 'POST':
		return render_template('post_issue.html', issue_num = issue_num)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/logout')
def logout():
	return render_template('logout.html')

@app.route('/issues')
def issues():
	return render_template('issues.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/profile')
def profile():
	return render_template('profile.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(405)
def page_not_found(e):
	return render_template('405.html'), 405

if __name__ == '__main__':
	app.run(debug = True)