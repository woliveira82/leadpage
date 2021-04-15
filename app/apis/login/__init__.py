from flask import Blueprint

login = Blueprint('login', __name__)

from app.apis.login.login_apis import *