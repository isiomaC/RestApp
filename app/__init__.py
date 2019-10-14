import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
import platform
import extraction
import requests
from PIL import Image
from io import BytesIO
from urllib.request import urlopen
import ssl

app = Flask(__name__)
api = Api(app)

url = "https://www.pond5.com/photo/"

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

class mediaInfo(Resource):
	def get(self, id):

		# Append imageid to url to get image 
		imageurl = url + str(id)

		# Getting html text from the url
		html =  requests.get(imageurl).text

		# Using extractor to get the title and image size
		extracted = extraction.Extractor().extract(html, source_url=imageurl)

		gcontext = ssl.SSLContext()

		# Create request object
		response = urlopen(extracted.image, context=gcontext)

		# Getting the reponse code from the request
		responseCode = response.getcode()

		# Getting the image response in bytes
		responseBytes = response.read()

		# Getting an Image instance object from the extracted Image bytes data
		img = Image.open(BytesIO(responseBytes))

		# splicing the image name from the image url 
		# and assigning it to the img filename property
		img.filename = extracted.image[25:]

		print(extracted.titles)
		# Constructing the json response to be served 
		res = jsonify({
			"message": "success",
			"data": {
				"title": extracted.titles[1],
				"filename": img.filename,
				"size":{
					"bytes": str(len(img.fp.read()))
				},
				"dimension":{
					"width": img.size[0],
					"height": img.size[1]
				}
			}
		})
		res.status_code = responseCode
		return res

api.add_resource(ping, '/ping')
api.add_resource(systemInfo, '/system')
api.add_resource(mediaInfo, '/mediainfo/<int:id>')