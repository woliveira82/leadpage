from flask import Blueprint
from .LoginAPI import LoginAPI

login = Blueprint('login', __name__)

login_api = LoginAPI.as_view('login_api')
login.add_url_rule(None, view_func=login_api, methods=['POST'])
