import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()


# application factory pattern
# see: https://flask.palletsprojects.com/en/2.3.x/patterns/appfactories/
def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from server.ping.router import ping_blueprint

    app.register_blueprint(ping_blueprint)

    from server.user.router import user_blueprint

    app.register_blueprint(user_blueprint)

    # shell context for flask cli
    # enables app and db to be present in flask shell session
    # allows you to work with these entities without having to import them
    # Ex: running `flask shell` will start shell session where you can invoke app and db
    # see: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database/page/0
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
