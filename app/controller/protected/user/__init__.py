from flask import Blueprint

from .apis import *

user = Blueprint('user', __name__, url_prefix='/user')

user_api = UserAPI.as_view('config_api')
user.add_url_rule('', view_func=user_api, methods=['GET'])
