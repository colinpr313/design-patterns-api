from flask import Flask
from flask_restx import Api, Resource


flask_app = Flask(__name__)
app = Api(
	app = flask_app,
	version="1.0",
	title="Design Patterns",
	description="API to utilize different design patterns",
)

name_space = app.namespace('main', description='Main APIs')

@name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}
