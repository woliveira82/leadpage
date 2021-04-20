from app.apis.login import login
from app.inc import Response, ResponseException
from app.model import User
from flask import request
from flask_jwt_extended import create_access_token
from webargs import fields
from webargs.flaskparser import parser


@login.route('/', methods=['POST'])
def post_login():
    json = parser.parse({
        'email': fields.Email(required=True),
        'password': fields.Str(required=True)
    }, request)
    user = User.query.filter_by(**json).first()
    if not user:
        raise ResponseException('Email or password is wrong', status=401)

    access_token = create_access_token(identity=user.email)
    return Response({'access_token': access_token}).to_dict()


@login.route('/logout', methods=['POST'])
def post_logout():
    return 'ok'

