from flask import Blueprint

from .apis import *

info = Blueprint('info', __name__, url_prefix='/info')

info_api = InfoAPI.as_view('config_api')
info.add_url_rule('', view_func=info_api, methods=['GET'])
