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
        data = str(error)
        return ResponseException(data, status=500).to_dict(), 500

app = Flask(__name__, instance_relative_config=True)
handler_error(app)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

modules = [
    {'name': 'info', 'path': '/info', 'version': 1, 'package': 'open'},
    {'name': 'login', 'path': '/login', 'version': 1, 'package': 'open'},
]

for item in modules:
    module = importlib.import_module(f".{item['package']}", package='app.controller')
    app.register_blueprint(
        getattr(module, f"{item['name']}"),
        url_prefix=f"/api/v{item['version']}{item['path']}"
    )
