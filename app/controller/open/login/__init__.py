from flask import Blueprint

from .apis import *

login = Blueprint('login', __name__, url_prefix='/login')

login_api = LoginAPI.as_view('login_api')
login.add_url_rule('', view_func=login_api, methods=['POST'])
