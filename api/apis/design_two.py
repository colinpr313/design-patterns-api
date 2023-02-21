from flask_restx import Namespace, Resource, fields

# namespace metadata - title and description
api = Namespace('dogs', description='dogs related operations')

dog = api.model('Dog', {
    'id': fields.String(required=True, description='The dog identifier'),
    'name': fields.String(required=True, description='The dog name'),
})

DOGS = [
    {'id': 'felix', 'name': 'Felix'},
]

@api.route('/')
class DogList(Resource):
    @api.doc('list_dogs')
    @api.marshal_list_with(dog)
    def get(self):
        '''List all dogs'''
        return DOGS

@api.route('/<id>')
@api.param('id', 'The dog identifier')
@api.response(404, 'Dog not found')
class Cat(Resource):
    @api.doc('get_dog')
    @api.marshal_with(dog)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for dog in DOGS:
            if dog['id'] == id:
                return dog
        api.abort(404)
