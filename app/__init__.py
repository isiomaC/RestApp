
from flask import Flask, jsonify
from flask_restful import Resource, Api
import platform
import extraction
import os
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
	"""home page"""
	return 'HOME PAGE'

# @app.route("/ping")
# def ping():
# 	response = jsonify({'data': 'pong',
# 						'message': 'success'})
# 	return response, 200

# @app.route('/system')
# def systeminfo():
# 	return jsonify({

# 		})

class ping(Resource):
	def get(self):
		response = jsonify({
			"data": "pong",
			"message": "success"
			})
		response.status_code = 200
		return response


class systemInfo(Resource):
	def get(self):
		response = jsonify({
			"message": "success",
			"data": {
				"service_version": 1.0,
				"system_information": {
					"system": platform.system(),
					"version": platform.version(),
					"machine": platform.machine(),
					"platform": platform.platform(),
					"processor": platform.processor()
				}
			}
		})
		response.status_code = 200
		return response


api.add_resource(ping, '/ping')
api.add_resource(systemInfo, '/system')