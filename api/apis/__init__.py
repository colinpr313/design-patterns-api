from flask_restx import Api

# import seperate api namespces
from .desgin_one import api as ns1
from .design_two import api as ns2

# api metadata
api = Api(
	version="1.0",
	title="Design Patterns",
	description="API to utilize different design patterns",
)

# add namespaces to app
api.add_namespace(ns1)
api.add_namespace(ns2)
