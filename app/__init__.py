from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exception import ResponseException


def handler_error(app):

    @app.errorhandler(ResponseException)
    def handler_error(error):
        response = error.to_dict()
        return response, response['status']

app = Flask(__name__, instance_relative_config=True)
handler_error(app)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# modules = [ {'name': 'info', 'path': '/info', 'version': 1}, ]
# for line in modules:
#     module = importlib.import_module('os.path')
# for service in lists:
#     module = importlib.import_module('.views', pachage='app')
#     app.register_blueprint(
#         getattr(module, f'{service['db']}'),
#         url_prefix=f'/{service['db']}'
#     )

from app.controller import *

app.register_blueprint(info)
