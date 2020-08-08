from flask import Blueprint
from .TokenAPI import TokenAPI

token = Blueprint('token', __name__, url_prefix='/token')

token_api = TokenAPI.as_view('config_api')
token.add_url_rule('', view_func=token_api, methods=['GET'])
