from app.apis.login import login
from app.inc import Parser, Response, ResponseException, Valid
from app.model import User
from flask import request
from flask_jwt_extended import create_access_token


@login.route('/', methods=['POST'])
def post_login():
        data = Parser(request).parse({
            'email': Valid(required=True),
            'password': Valid(required=True)
        })
        users = User.read(query=data)
        
        if len(users) == 0:
            raise ResponseException('Email or password is wrong', status=401)

        access_token = create_access_token(identity=data['email'])
        return Response({'access_token': access_token}).to_dict()


@login.route('/', methods=['POST'])
def post_logout():
    return 'ok'

