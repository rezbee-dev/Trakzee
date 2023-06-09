import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


# application factory pattern
# see: https://flask.palletsprojects.com/en/2.3.x/patterns/appfactories/
def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    migrate.init_app = Migrate(app, db)
    bcrypt.init_app(app)

    # Setup API
    from server.account.controller import AccountRouter
    from server.ping.router import ping_ns
    from server.profile.controller import ProfileRouter

    api = Api(version="1.0", title="Habit Tracker API", doc="/api/docs")
    api.add_namespace(ping_ns, path="/api/ping")
    api.add_namespace(AccountRouter, path="/api/account")
    api.add_namespace(ProfileRouter, path="/api/profile")

    api.init_app(app)

    # shell context for flask cli
    # enables app and db to be present in flask shell session
    # allows you to work with these entities without having to import them
    # Ex: running `flask shell` will start shell session where you can invoke app and db
    # see: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database/page/0
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
