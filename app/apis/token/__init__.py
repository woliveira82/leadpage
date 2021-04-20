from flask import Blueprint

token = Blueprint('token', __name__)

from app.apis.token.token_apis import *
