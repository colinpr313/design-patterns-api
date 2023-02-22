import sys
from http import HTTPStatus
from flask import make_response, request
from flask_restx import Namespace, Resource

sys.path.insert(0, "../..")
import design_patterns_api.strategy_pattern.duck_classes as ducks

# namespace metadata - title and description
api = Namespace(
    "Strategy Pattern", description="Create ducks using the strategy pattern"
)

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
            HTTPStatus.OK,
        )


@api.route("/fetch_duck")
@api.param("name", "The duck's name")
class Duck(Resource):
    def get(self):
        """Fetch a duck given its name"""
        name = request.args.get("name", None)
        duck = DUCKS.get(name, None)
        if duck:
            return make_response(
                {
                    "name": duck.name,
                    "fly": duck.fly(),
                    "quack": duck.quack(),
                    "swim": duck.swim(),
                },
                HTTPStatus.OK,
            )
        return make_response(
            (
                "Invalid duck name. check /Strategy Pattern/list_ducks"
                "for all valid duck names"
            ),
            HTTPStatus.BAD_REQUEST,
        )
    
@api.route("/quack")
@api.param("name", "The duck's name")
class Quack(Resource):
    def get(self):
        """Make a duck quack"""
        name = request.args.get("name", None)
        duck = DUCKS.get(name, None)
        if duck:
            return make_response(
                duck.quack(),
                HTTPStatus.OK
            )
        return make_response(
            (
                "Invalid duck name. check /Strategy Pattern/list_ducks"
                "for all valid duck names"
            ),
            HTTPStatus.BAD_REQUEST,
        )
    
@api.route("/fly")
@api.param("name", "The duck's name")
class Fly(Resource):
    def get(self):
        """Make a duck fly"""
        name = request.args.get("name", None)
        duck = DUCKS.get(name, None)
        if duck:
            return make_response(
                duck.fly(),
                HTTPStatus.OK
            )
        return make_response(
            (
                "Invalid duck name. check /Strategy Pattern/list_ducks"
                "for all valid duck names"
            ),
            HTTPStatus.BAD_REQUEST,
        )
    
@api.route("/swim")
@api.param("name", "The duck's name")
class Swim(Resource):
    def get(self):
        """Make a duck swim"""
        name = request.args.get("name", None)
        duck = DUCKS.get(name, None)
        if duck:
            return make_response(
                duck.swim(),
                HTTPStatus.OK
            )
        return make_response(
            (
                "Invalid duck name. check /Strategy Pattern/list_ducks"
                "for all valid duck names"
            ),
            HTTPStatus.BAD_REQUEST,
        )
    

