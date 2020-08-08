from flask import request
from flask.views import MethodView
from app.inc import Response, Parser, Valid, ResponseException
from flask_jwt_extended import create_access_token
from app.model import User


class LoginAPI(MethodView):


    def post(self):
        data = Parser(request).parse({
            'email': Valid(required=True),
            'password': Valid(required=True)
        })
        users = User.read(query=data)
        
        if len(users) == 0:
            raise ResponseException('Email or password is wrong', status=401)

        access_token = create_access_token(identity=data['email'])
        return Response({'access_token': access_token}).to_dict()
