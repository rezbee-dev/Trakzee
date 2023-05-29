from flask_restx import Namespace, Resource

# Blueprints are like express router
# they represent collection of routes for some model that can be registered with flask app
# ping_blueprint = Blueprint("ping", __name__)
# Registering blueprints with flask_restx api allows for more routing functionalities (url prefixes) and other uses
# see: https://flask-restx.readthedocs.io/en/latest/scaling.html?highlight=blueprint#use-with-blueprints
# api = Api(ping_blueprint)

ping_ns = Namespace("ping")


class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


ping_ns.add_resource(Ping, "")
