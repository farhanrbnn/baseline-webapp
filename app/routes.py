from app import app
from flask import render_template, jsonify


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/greet', methods = ['GET'])
def new():
	return render_template('greetings.html')

@app.route('/employees', methods = ['GET'])
def list_employee():
	return render_template('employees.html')
