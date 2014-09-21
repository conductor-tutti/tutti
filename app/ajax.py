from flask import jsonify, request, render_template
from app import app

@app.route('/')
def test():
	return render_template('ajax_test.html')


@app.route('/ajax', methods=['GET','POST'])
def ajax():
	
	data = {}

	if request.method == 'GET':
		pass

	elif request.method == 'POST':
		resp = request.form
		data['hahaha'] = int(resp["one"]) + int(resp["two"])
		
	return jsonify(data)

	
	