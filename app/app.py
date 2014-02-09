from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('hello_world.html')

@app.route('/issue/<int:issue_num>', methods = ['GET', 'POST'])
def view_issue(issue_num):
	if request.method == 'GET':
		return 'Stub for viewing issue %d' % issue_num
	else:
		return 'Trying to post to issue %d' % issue_num

if __name__ == '__main__':
	app.run()