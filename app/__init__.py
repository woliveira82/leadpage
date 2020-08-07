from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exception import ResponseException
import importlib
from werkzeug.exceptions import HTTPException
from flask_jwt_extended import JWTManager


def handler_error(app):
    

    @app.errorhandler(HTTPException)
    def handler_error(error):
        return ResponseException(error.name, status=error.code).to_dict(), error.code


    @app.errorhandler(ResponseException)
    def handler_error(error):
        response = error.to_dict()
        return response, response['status']


    @app.errorhandler(Exception)
    def handler_error(error):
        data = str(error) if app.config['DEBUG'] else None
        return ResponseException(data, status=500).to_dict(), 500


def handler_jwt_error(app, jwt):


    @jwt.claims_verification_failed_loader
    @jwt.needs_fresh_token_loader
    @jwt.invalid_token_loader
    @jwt.revoked_token_loader
    @jwt.token_in_blacklist_loader
    @jwt.unauthorized_loader
    @jwt.user_loader_error_loader
    def token_callback(error):
        data = str(error) if app.config['DEBUG'] else None
        return ResponseException(data, status=401).to_dict(), 401


    @jwt.expired_token_loader
    def expired_token_callback(error):
        data = str(error) if app.config['DEBUG'] else None
        return ResponseException(data, status=401).to_dict(), 401

app = Flask(__name__, instance_relative_config=True)
handler_error(app)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
handler_jwt_error(app, jwt)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

modules = [
    {'name': 'info', 'path': '/info', 'version': 1, 'package': 'open'},
    {'name': 'login', 'path': '/login', 'version': 1, 'package': 'open'},
    {'name': 'token', 'path': '/token', 'version': 1, 'package': 'protected'},
]

for item in modules:
    module = importlib.import_module(f".{item['package']}", package='app.controller')
    app.register_blueprint(
        getattr(module, f"{item['name']}"),
        url_prefix=f"/api/v{item['version']}{item['path']}"
    )
