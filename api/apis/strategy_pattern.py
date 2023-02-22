import sys
from http import HTTPStatus
from flask import make_response
from flask_restx import Namespace, Resource, fields

sys.path.insert(0,'../..')
import design_patterns_api.strategy_pattern.duck_classes as ducks

# namespace metadata - title and description
api = Namespace("Strategy Pattern", description="Create ducks using the strategy pattern")

DUCKS = {
    "mallard duck": ducks.MallardDuck(),
    "decoy duck": ducks.DecoyDuck(),
    "model duck": ducks.ModelDuck(),
}


@api.route("/list_ducks")
class DuckList(Resource):
    @api.doc("list_ducks")
    def get(self):
        """List all ducks"""
        return make_response(
            f"Here are all of the different ducks: {', '.join(list(DUCKS.keys()))}",
            HTTPStatus.OK
        )


@api.route("/fetch_duck/<name>")
@api.param("name", "The duck's name")

class Duck(Resource):
    @api.doc("get_duck")
    def get(self, name):
        """Fetch a duck given its name"""
        duck = DUCKS.get(name, None)
        if duck: 
            return make_response(
                {
                    "name": duck.name,
                    "fly": duck.fly(),
                    "quack": duck.quack(),
                    "swim": duck.swim()

                },
                HTTPStatus.OK,
            )
        return make_response(
            "Invalid duck name. check /Strategy Pattern/list_ducks for all valid duck names",
            HTTPStatus.BAD_REQUEST,
        )
