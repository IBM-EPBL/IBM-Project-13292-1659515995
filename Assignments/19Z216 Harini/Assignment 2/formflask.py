from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
	return 'WELCOME %s' % name
@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['username']
		return redirect(url_for('success', name=user))
	else:
		user = request.args.get('username')
		return redirect(url_for('success', name=user))

if __name__ == '_main_':
	app.run(debug=True)
